# final_project

## Main Title: 수출규제 GPT
<br>

### Subject: 수출 규제 관련 데이터로부터 유저 QA 가능한 검색 챗봇 시스템 개발
<br>


Team_name: 2게 되조?

Member: HoRi0506(김기완), kwanggyu99(남광규), Kate Lee(이성현)

Duration: 23/4/28 - 23/6/22

Mentor: dane ahn
<br>


### Step

- [x] 1. ES 구동
  
- [x] 2. ES 인덱싱
  
- [x] 3. ES Query
  
- [x] 4. GPT API wraping
  
- [x] 5. Fast API로 API 생성
  
- [x] 6. 위 과정 자동화
  
- [x] 7. wrap up
<br>


### Data

- 주어진 문서의 내용을 토대로 유저가 원하는 정보를 찾을 수 있기 위한 Data Pre-Processing과 Data Normalization 등을 시도
  
- 사용자의 요청에서 elastic search에 필요한 쿼리문 생성
<br><br>
### Analysis Goal

- 주어진 문서의 내용을 토대로 유저가 원하는 정보를 찾을 수 있는 대화형 검색 시스템 개발
  
- 데이터베이스 검색 시 활용되는 쿼리문을 따로 배우지 않고도 사용자가 원하는 결과값 추출
  
- 유저들이 해당 기능을 이해하고 사용할 수 있도록 개발
  
- QA구축 시스템으로, 지속 가능한 서비스를 구현하고 이에 맞는 환경을 구축
<br>  


### Story Line

1. 필요한 라이브러리와 docker 환경 세팅
 
2. 수출 규제 데이터를 ElasticSearch를 통해 빅데이터에서 원하는 부분 추출을 빠르게 할 수 있음
  
3. 위의 방식의 결과물을 Emb 기능을 활용하여 ChatGPT에 적합한 질문으로 바꿔주도록 함
  
4. GPT3의 기능을 활용하여 위의 질문에 적합한 대답을 해주도록 제작
  
5. 결과를 분석 및 해석
  
6. 데모 제작(영상 등)

<br>

----------

<br>

- ~~[세팅 과정 1](https://www.notion.so/1-1f2ed564bf26403c9dd403921c6d8847?pvs=4)~~

- [세팅 과정 2](https://www.notion.so/2-3216d6e915d346af9bc0eacbaad17aa6?pvs=4)

- [세팅 과정 3(git)](https://www.notion.so/Git-setting-de10ad3355394983800bcd2651e7da64?pvs=4)

- [Elasticsearch_nori 1](https://www.notion.so/nori_plugin-33463ceddafa453792b75c6c6a6b45fd?pvs=4)

- [Elasticsearch nori 2](https://www.notion.so/nori-indexing-ecebfb5e4c364d26a385ca59569c3447?pvs=4)

- [test code](https://www.notion.so/cb741a9ac6ca4abfa3f81c70a6bbe6fd?pvs=4)

- [FastAPI 세팅](https://www.notion.so/FastAPI-e2548f334f79482cbf1a5c490aa6b993?pvs=4)

- [PPT](https://www.notion.so/PPT-FastAPI-540dcf0913d04eddb9b20ee2fa04154d?pvs=4)

<br>

------

<br>

- 데모 영상

<img src="https://github.com/team-fc-fp2/final_project_es_gpt/assets/123163133/2ff7715d-3000-4706-a069-da1f57846cd1">
