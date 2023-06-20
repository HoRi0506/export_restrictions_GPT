# final_project_es_gpt

## Title: 수출 규제 관련 데이터로부터 유저 QA 가능한 검색 챗봇 시스템 개발
<br>


team_name: 2게 되조?

Member: HoRi0506, kwanggyu99, Kate Lee

Duration: 23/4/28 - 23/6/22

Mentor: dane ahn
<br>


### Step

- [ ] 1. ES 구동
  
- [ ] 2. ES 인덱싱
  
- [ ] 3. ES Query
  
- [ ] 4. GPT API wraping
  
- [ ] 5. Fast API로 API 생성
  
- [ ] 6. 위 과정 자동화
  
- [ ] 7. wrap up
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


-------------------------------------------------------------------------------
