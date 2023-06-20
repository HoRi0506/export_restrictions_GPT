class ElasticsearchSearch:
    def __init__(self, es):
        # Elasticsearch 클라이언트 생성
        self.es = es
    def search_in_elasticsearch(self, user_question):
        # 질문을 분석하여 대상국가와 품목 추출
        tokens = user_question.split()
        # target_country = tokens[0]  # 첫 번째 토큰을 대상국가로
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
        response = self.es.search(index='my_index', body=query, size=3)
        if not response['hits']['hits']:  # 결과가 없는 경우
            # 2. 대상국가 + 대상국가 수입요건
            query = {
                "query": {
                    "bool": {
                        "must": [
                            {"match": {"대상국가": {"query": user_question, "boost": 3}}},
                            {"match": {"대상국가 수입요건(trade navi)": {"query": user_question, "boost": 2}}}
                        ]
                    }
                }
            }
            response = self.es.search(index='my_index', body=query, size=3)
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
            response = self.es.search(index='my_index', body=query, size=3)
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
        return search_results
