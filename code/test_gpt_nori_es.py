import json
from elasticsearch import Elasticsearch
import openai

# OpenAI API 키 설정
openai.api_key = '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'

# Elasticsearch 설정
es = Elasticsearch(hosts='http://localhost:9200', http_compress=True, headers={'Content-Type': 'application/json'})
index_name = 'test_json'

# 데이터 로드 및 인덱스 생성
data_file = 'json_data.json'
with open(data_file, 'r') as file:
    json_data = json.load(file)

if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

settings = {
    "settings": {
        "number_of_shards": 5,
        "number_of_replicas": 1,
        "analysis": {
            "analyzer": {
                "custom_analyzer": {
                    "type": "custom",
                    "tokenizer": "nori_tokenizer",
                    "filter": ["lowercase"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "품목(가공식품)": {"type": "text", "analyzer": "custom_analyzer", "fielddata": True},
            "대상국가": {"type": "keyword"},
            "대상국가 수입요건(trade navi)": {
                "type": "text",
                "analyzer": "custom_analyzer",
                "fielddata": True
            }
        }
    }
}

es.indices.create(index=index_name, body=settings)

for document in json_data:
    es.index(index=index_name, body=document)

# 사용자 질문 입력
user_question = input("질문을 입력하세요: ")

# Elasticsearch로부터 검색 쿼리 수행
tokens = es.indices.analyze(index=index_name, body={'tokenizer': 'nori_tokenizer', 'text': user_question})
tokens = [token['token'] for token in tokens['tokens']]

query = {
    "query": {
        "bool": {
            "should": [
                {"multi_match": {"query": " ".join(tokens), "fields": ["품목(가공식품)^2", "대상국가^3"]}},
                {"match": {"대상국가 수입요건(trade navi)": " ".join(tokens)}}
            ],
            "minimum_should_match": 1
        }
    },
    "size": 3,
    "sort": [
        {"_score": {"order": "desc"}},
        {"품목(가공식품)": {"order": "asc"}},
        {"대상국가 수입요건(trade navi)": {"order": "asc"}},
        {"대상국가": {"order": "asc"}}
    ]
}

response = es.search(index=index_name, body=query)

if response['hits']['hits']:
    for hit in response['hits']['hits']:
        document = hit['_source']
        #print("품목(가공식품):", document['품목(가공식품)'])
        #print("대상국가:", document['대상국가'])
        #print("대상국가 수입요건(trade navi):", document['대상국가 수입요건(trade navi)'])
        #print()

        # GPT를 사용하여 대화형 답변 생성
        gpt_response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_question,
            max_tokens=100
        )
        print(gpt_response.choices[0].text.strip())
else:
    print("검색 결과가 없습니다.")
