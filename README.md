# portfolio
## 목차
- 1️⃣ 데이터 분석
  - [이커머스 데이터셋(Olist), 판매 물품 선정 가이드라인 분석](https://github.com/aimaimee/portfolio#%EC%9D%B4%EC%BB%A4%EB%A8%B8%EC%8A%A4-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8Bolist-%ED%8C%90%EB%A7%A4-%EB%AC%BC%ED%92%88-%EC%84%A0%EC%A0%95-%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8-%EB%B6%84%EC%84%9D)
  - [예비 창업자들을 위한 서울 상권 분석 보고서](https://github.com/aimaimee/portfolio#%EC%98%88%EB%B9%84-%EC%B0%BD%EC%97%85%EC%9E%90%EB%93%A4%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%84%9C%EC%9A%B8-%EC%83%81%EA%B6%8C-%EB%B6%84%EC%84%9D-%EB%B3%B4%EA%B3%A0%EC%84%9C)
  - [(미니 프로젝트) 식도염의 원인 분석](https://github.com/aimaimee/portfolio#%EA%B0%9C%EC%9D%B8%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%8B%9D%EB%8F%84%EC%97%BC%EC%9D%98-%EC%9B%90%EC%9D%B8-%EB%B6%84%EC%84%9D)
- 2️⃣ ML
  - [온라인 수강생의 자리비움 여부 탐지 모델링](https://github.com/aimaimee/portfolio#%EC%98%A8%EB%9D%BC%EC%9D%B8-%EC%88%98%EA%B0%95%EC%83%9D%EC%9D%98-%EC%9E%90%EB%A6%AC%EB%B9%84%EC%9B%80-%EC%97%AC%EB%B6%80-%ED%83%90%EC%A7%80-%EB%AA%A8%EB%8D%B8%EB%A7%81)
- [3️⃣ 미니 프로젝트](https://github.com/aimaimee/portfolio#3%EF%B8%8F%E2%83%A3-%EB%AF%B8%EB%8B%88-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-2%EA%B0%9C10%EA%B0%9C-%EC%A7%84%ED%96%89-%EC%A4%91)

</br>

## 1️⃣ 데이터 분석
### 이커머스 데이터셋(Olist), 판매 물품 선정 가이드라인 분석

__보고서 :__ [Olist_ecommerce_md](https://github.com/aimaimee/portfolio/blob/main/olist_ecommerce/README.md)

__개요 :__ 

브라질 이커머스 회사인 Olist에 입점하려는 판매자를 가정하였습니다. 해당 판매자가 어떤 지역에서, 어떤 품목을, 어떻게 구성하여 판매할 지를 추천하기 위하여 분석을 진행합니다.

- EDA를 통해 Olist의 매출 상위 품목, 지역, 판매자를 분석
- 군집화, z-score, RFM을 활용하여 평가 지표를 생성
- 대상인 판매자가 시장 규모, 경쟁자, 구매자 충성도 중 중점으로 보는 것을 기준으로 품목을 고를 수 있도록 분석 결과를 제공

__담당역할 :__

- Olist의 매출과 품목을 중심으로 EDA를 진행(seaborn, plotly 활용)

- RFM 분석을 진행(고객 분류에 점수를 부여하여 RFM 결과를 점수화, 해당 점수를 군집화와 z_score 점수와 비교할 수 있도록 데이터프레임화)

### 예비 창업자들을 위한 서울 상권 분석 보고서

__보고서 :__ [Seoul_Commercial_Area_md](https://github.com/aimaimee/portfolio/tree/main/Seoul_Commercial_Area)

__개요 :__

창업자가 제일 주목하는 요인은 '매출'일 것이라고 가정, 매출에 영향을 가장 많이 끼치는 변수를 EDA 분석합니다. 그 외 인구, 업종 등 데이터셋에 따른 EDA 결과를 Streamlit을 사용해 제공합니다.

__담당역할 :__

- 유동인구와 매출 데이터셋 전처리, EDA 분석
- 팀리더, 분담된 업무 진행과정 체크

### (개인프로젝트) 식도염의 원인 분석

__보고서 :__ 진행 중

__개요 :__

2022년 1월 이후 잠잠했던 역류성 식도염 증상이 2023년 3월 다시 시작되었습니다. 나의 역류성 식도염에는 어떤 요인이 원인이 될까 분석합니다. 식도염의 각종 원인을 식사습관과 생활습관으로 나누고, 제일 큰 요인이 되는 것을 찾아봅니다.

__담당역할 :__

데이터 수집, 분석


## 2️⃣ ML
### 온라인 수강생의 자리비움 여부 탐지 모델링

__보고서 :__ [Zoom_Detection_md](https://github.com/aimaimee/portfolio/tree/main/Zoom_Detection)

__개요 :__

온라인 화상 수업(Zoom)에서 수강생이 자리를 비울 경우를 탐지하는 모델을 구현합니다. 자리에 있는지 여부를 파악하여 메세지를 출력하고, 기록합니다.
- 얼굴 탐지 모델 비교 및 선정(MediaPipe, OpenCV, Face Recognition, YOLOv3-5-7)
- YOLOv7 모델 후처리(사람만 인식하도록, 한 개의 탐지 박스만 출력하도록)
- 탐지된 인물이 탐지되지 않았을 경우, '자리비움' 시간 출력
- Edge Case

__담당역할 :__
- colab과 로컬환경에서 웹캠이 구현되는지 테스트를 진행
- YOLOv7 모델 연구(기본 코드 실행, YOLOv7 논문)
- 발표

## 3️⃣ 미니 프로젝트 (2개/10개 진행 중)
### 뉴스 기사 스크래핑
수집한 데이터 안에서, 원하는 키워드가 속한 기사를 스크래핑합니다. 키워드는 이슈 중 하나인 '환율'로 선정하였고, 환율 관련 기사를 찾을 수 있는 네이버 뉴스 경제 탭을 스크래핑하였습니다.

### 제주특별자치도 BC카드 사용 데이터 EDA 분석 연습
2014~2016년도 제주도 내 내국인 관광객의 BC카드 사용 데이터입니다. 상관관계 비교, 연령별 지역별 업종별 시각화를 진행하였습니다. 결제 건수가 가장 많은 지역, 소비가 높은 업종이 제주공항과 가깝다는 공통점을 가지고 있다는 것을 발견했습니다.
