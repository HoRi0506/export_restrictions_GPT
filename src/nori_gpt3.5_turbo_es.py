import json
from elasticsearch import Elasticsearch
import openai


# OpenAI API Key 설정
openai_key_file = '../config/openaikey.txt'

with open(openai_key_file, 'r') as file:
    openai_key = file.read().strip()

openai.api_key = openai_key  # API Key 설정

# Elasticsearch 클라이언트 생성
es = Elasticsearch(hosts='http://localhost:9200', http_compress=True)

# JSON 데이터 파일 경로
data_file = '/Users/kimkiwan/es/kiwan_fp/final_project_es_gpt/code/jsondata/json_data.json'

# JSON 파일 열기
with open(data_file, 'r') as file:
    json_data = json.load(file)

# 인덱스 삭제
index_name = "my_index"
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

# 인덱스 생성 설정
index_name = "my_index"
settings = {
    "settings": {
        "number_of_shards": 5,
        "number_of_replicas": 1,
        "analysis": {
            "tokenizer": {
                "nori_tokenizer": {
                    "type": "nori_tokenizer",
                    "decompound_mode": "mixed"
                }
            },
            "analyzer": {
                "nori_analyzer": {
                    "type": "custom",
                    "tokenizer": "nori_tokenizer"
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "대상국가": {
                "type": "text",
                "analyzer": "nori_analyzer"
            },
            "품목(가공식품)": {
                "type": "text",
                "analyzer": "nori_analyzer"
            },
            "HS CODE (대표)": {
                "type": "keyword"
            },
            "대상국가 수입요건(trade navi)": {
                "type": "text",
                "analyzer": "nori_analyzer"
            }
        }
    }
}

# Elasticsearch에 색인하기
es.indices.create(index='my_index', body=settings)  # 인덱스 생성
for document in json_data:
    es.index(index='my_index', body=document)

# 사용자 질문 입력 받기
user_question = input("질문을 입력하세요: ")

# 질문을 분석하여 대상국가와 품목 추출
tokens = user_question.split()

# Elasticsearch에서 관련 정보 검색
# 1. 대상국가 + 품목 + 대상국가 수입요건
query = {
    "query": {
        "bool": {
            "must": [
                {"match": {"대상국가": {"query": user_question, "boost": 3}}},
                {"match": {"품목(가공식품)": {"query": user_question, "boost": 2}}},
                {"match": {"대상국가 수입요건(trade navi)": {"query": user_question, "boost": 1}}}
            ]
        }
    }
}
response = es.search(index='my_index', body=query,  size=3)
if not response['hits']['hits']:  # 결과가 없는 경우
    # 2. 대상국가 + 대상국가 수입요건
    query = {
            "query": {
            "bool": {
                "must": [
                    {"match": {"대상국가": {"query": user_question, "boost": 3}}},
                    {"match": {"대상국가 수입요건(trade navi)": {"query": user_question, "boost":2}}}
                ]
            }
        }
    }
    response = es.search(index='my_index', body=query,  size=3)
if not response['hits']['hits']:  # 결과가 없는 경우
    # 3. 대상국가 + 품목
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"대상국가": {"query": user_question, "boost": 3}}},
                    {"match": {"품목(가공식품)": {"query": user_question, "boost": 2}}}
                ]
            }
        }
    }
    response = es.search(index='my_index', body=query, size=3)

# 검색 결과 저장
search_results = []

# 검색 결과 출력
for hit in response['hits']['hits']:
    result = {
        'Score': hit['_score'],
        '대상국가': hit['_source']['대상국가'],
        '품목(가공식품)': hit['_source']['품목(가공식품)'],
        '대상국가 수입요건(trade navi)': hit['_source']['대상국가 수입요건(trade navi)']
    }
    search_results.append(result)

# 검색 결과를 요약할 텍스트 생성
summary_text = ""
for result in search_results:
    summary_text += f"대상국가: {result['대상국가']}\n"
    summary_text += f"품목(가공식품): {result['품목(가공식품)']}\n"
    summary_text += f"대상국가 수입요건(trade navi): {result['대상국가 수입요건(trade navi)']}\n\n"

# 이제 이 검색 결과를 요약하도록 GPT-3.5-turbo에 요청합니다.
# GPT-3.5-turbo는 입력을 'messages' 형태로 받습니다. 각 메시지는 'role'과 'content'를 가지는데,
# 'role'은 'system', 'user', 'assistant' 중 하나가 될 수 있고, 'content'는 해당 메시지의 내용입니다.
response_gpt = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
        {"role": "user", "content": summary_text},
        {"role": "user", "content": "해당 내용을 요약해줘."}
    ]
)

# 응답 결과 확인
generated_text = response_gpt['choices'][0]['message']['content'].strip()
print("GPT 요약:")
print(generated_text)
