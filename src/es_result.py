from elasticsearch import Elasticsearch
from es_index import ElasticsearchIndex
from es_search import ElasticsearchSearch
# Elasticsearch 클라이언트 생성
es = Elasticsearch(hosts='http://localhost:9200', http_compress=True)
# JSON 데이터 파일 경로
data_file = 'json_total.json'
elasticsearch_index = ElasticsearchIndex()
elasticsearch_index.data_file = data_file
elasticsearch_index.create_elasticsearch_index()
elasticsearch_search = ElasticsearchSearch(es)
# 사용자 질문 입력 받기
user_question = input("질문을 입력하세요: ")
# Elasticsearch에서 검색
results = elasticsearch_search.search_in_elasticsearch(user_question)
# 검색 결과 출력
for result in results:
    print('Score:', result['Score'])
    print("대상국가:", result['대상국가'])
    print("품목(가공식품):", result['품목(가공식품)'])
    print("대상국가 수입요건(trade navi):", result['대상국가 수입요건(trade navi)'])
    print()
