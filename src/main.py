import sys
sys.path.insert(0, "../src/")

from fastapi import FastAPI

from elasticsearch import Elasticsearch
from es_search import ElasticsearchSearch
from es_index import ElasticsearchIndex
from es_result import ask_es
from entities import esSearchResult, Query, Item
from es_gpt import GPTSummary

api_key_file = '../config/openaikey.txt'

# Elasticsearch 클라이언트 생성
es = Elasticsearch(hosts='http://localhost:9200', http_compress=True)

# ElasticsearchSearch 인스턴스 생성
elasticsearch_search = ElasticsearchSearch(es)

# JSON 데이터 파일 경로
data_file = '../data/json_data.json'

# Elasticsearch 인덱스 생성
elasticsearch_index = ElasticsearchIndex()
elasticsearch_index.data_file = data_file
elasticsearch_index.create_elasticsearch_index()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "ES is running"}


@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/summarize")
async def summarize_text(query: Query):
    gpt_summary = GPTSummary(api_key_file, 'gpt-3.5-turbo', elasticsearch_search)
    summary_text = query.text
    result = gpt_summary.summarize(summary_text)
    return {"result": result}


if __name__ == "__main__":
    user_question = input("검색어를 입력하세요: ")

    search_text = ask_es(user_question)
    search_text = [str(value) for value in search_text]
    search_text = ' '.join(search_text)

    es_query = elasticsearch_search.search_in_elasticsearch(search_text)

    gpt_summary = GPTSummary(api_key_file, 'gpt-3.5-turbo', elasticsearch_search)

    result = gpt_summary.summarize(es_query)
    
    print(result)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
