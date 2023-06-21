from elasticsearch import Elasticsearch
from es_index import ElasticsearchIndex
from es_search import ElasticsearchSearch
from es_result import ask_es
import openai

openai_key_file = '../config/openaikey.txt'
file_path = openai_key_file


def read_api_key(file_path):
    with open(file_path, 'r') as file:
        api_key = file.read().replace('\n', '')
    return api_key

class GPTSummary:
    def __init__(self, api_key_file, model_name, es):
        api_key = read_api_key(api_key_file)
        openai.api_key = api_key
        self.model_name = model_name
        self.elasticsearch_search = ElasticsearchSearch(es)
        self.ask_es = ask_es

    def summarize(self, query):
            # search_results = self.elasticsearch_search.search_in_elasticsearch(query)
            search_results = self.ask_es(query)
            summary_text = ""
            for result in search_results:
                summary_text += f"대상국가: {result['대상국가']}\n"
                summary_text += f"품목(가공식품): {result['품목(가공식품)']}\n"
                summary_text += f"대상국가 수입요건(trade navi): {result['대상국가 수입요건(trade navi)']}\n\n"
                
            response = openai.ChatCompletion.create(
                # model=self.model_name,
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes text in detail."},
                    {"role": "user", "content": summary_text},
                    {"role": "user", "content": "해당 내용을 요약해줘."},
                ],
            )
            # generated_text = response['choices'][0]['message']
            generated_text = response['choices'][0]['message']['content'].strip()
            return generated_text


if __name__ == "__main__":
    print(1)