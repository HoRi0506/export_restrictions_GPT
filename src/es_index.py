import json

from elasticsearch import Elasticsearch


class ElasticsearchIndex:

    def __init__(self):
        # Elasticsearch 클라이언트 생성
        self.es = Elasticsearch(hosts='http://localhost:9200', http_compress=True)
        # JSON 데이터 파일 경로
        self.data_file = '../data/json_total.json'

    def create_elasticsearch_index(self):
        # JSON 파일 열기
        with open(self.data_file, 'r') as file:
            json_data = json.load(file)
        # 인덱스 삭제
        index_name = "my_index"
        if self.es.indices.exists(index=index_name):
            self.es.indices.delete(index=index_name)
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
        self.es.indices.create(index='my_index', body=settings)  # 인덱스 생성
        for document in json_data:
            self.es.index(index='my_index', body=document)

if __name__ == "__main__":
    print(1)