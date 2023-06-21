from elasticsearch import Elasticsearch
from es_index import ElasticsearchIndex
from es_search import ElasticsearchSearch

def ask_es(query):
    # Elasticsearch 클라이언트 생성
    es = Elasticsearch(hosts='http://localhost:9200', http_compress=True)
    
    # JSON 데이터 파일 경로
    data_file = '../data/json_data.json'
    elasticsearch_index = ElasticsearchIndex()
    elasticsearch_index.data_file = data_file
    elasticsearch_index.create_elasticsearch_index()
    elasticsearch_search = ElasticsearchSearch(es)

    # Elasticsearch에서 검색
    response = elasticsearch_search.search_in_elasticsearch(query)
    
    # 검색 결과 저장
    search_results = []
    # 검색 결과 출력
    for result in response:
        results = {
            'Score': result['Score'],
            '대상국가': result['대상국가'],
            '품목(가공식품)': result['품목(가공식품)'],
            '대상국가 수입요건(trade navi)': result['대상국가 수입요건(trade navi)']
        }
        search_results.append(result)

    return search_results

if __name__ == "__main__":
    print(1)