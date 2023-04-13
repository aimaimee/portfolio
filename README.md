# portfolio
## 목차
- [프로젝트(데이터 분석)](https://github.com/aimaimee/portfolio#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D)
  - [이커머스 데이터셋(Olist), 판매 물품 선정 가이드라인 분석](https://github.com/aimaimee/portfolio#%EC%9D%B4%EC%BB%A4%EB%A8%B8%EC%8A%A4-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8Bolist-%ED%8C%90%EB%A7%A4-%EB%AC%BC%ED%92%88-%EC%84%A0%EC%A0%95-%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8-%EB%B6%84%EC%84%9D)
  - [(미니 프로젝트) 식도염의 원인 분석](https://github.com/aimaimee/portfolio#%EA%B0%9C%EC%9D%B8%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%8B%9D%EB%8F%84%EC%97%BC%EC%9D%98-%EC%9B%90%EC%9D%B8-%EB%B6%84%EC%84%9D)
- [프로젝트(ML)](https://github.com/aimaimee/portfolio#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8ml)
  - [온라인 수강생의 자리비움 여부 탐지 모델링](https://github.com/aimaimee/portfolio#%EC%98%A8%EB%9D%BC%EC%9D%B8-%EC%88%98%EA%B0%95%EC%83%9D%EC%9D%98-%EC%9E%90%EB%A6%AC%EB%B9%84%EC%9B%80-%EC%97%AC%EB%B6%80-%ED%83%90%EC%A7%80-%EB%AA%A8%EB%8D%B8%EB%A7%81)


## 데이터 분석
### 이커머스 데이터셋(Olist), 판매 물품 선정 가이드라인 분석
__코드 :__ [Olist_ecommerce_code](https://github.com/aimaimee/portfolio/tree/main/olist_ecommerce/olist_code)

__보고서 :__ [Olist_ecommerce_md](https://github.com/aimaimee/portfolio/blob/main/olist_ecommerce/README.md)

__개요 :__ 

브라질 이커머스 회사인 Olist에 입점하려는 판매자를 가정하였습니다. 해당 판매자가 어떤 지역에서, 어떤 품목을, 어떻게 구성하여 판매할 지를 추천하기 위하여 분석을 진행합니다.

- EDA를 통해 Olist의 매출 상위 품목, 지역, 판매자를 분석
- 군집화, z-score, RFM을 활용하여 평가 지표를 생성
- 대상인 판매자가 시장 규모, 경쟁자, 구매자 충성도 중 중점으로 보는 것을 기준으로 품목을 고를 수 있도록 분석 결과를 제공

__담당역할 :__

- Olist의 매출과 품목을 중심으로 EDA를 진행(seaborn, plotly 활용)

- RFM 분석을 진행(고객 분류에 점수를 부여하여 RFM 결과를 점수화, 해당 점수를 군집화와 z_score 점수와 비교할 수 있도록 데이터프레임화)

### (개인프로젝트) 식도염의 원인 분석
__코드 :__ []

__보고서 :__

__개요 :__



## ML
### 온라인 수강생의 자리비움 여부 탐지 모델링
__코드 :__ [Zoom_Detection_code](https://github.com/aimaimee/portfolio/tree/main/Zoom_Detection/Zoom_Detection_code)

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

## 미니 프로젝트
### 뉴스 기사 스크래핑
수집한 데이터 안에서, 원하는 키워드가 속한 기사를 스크래핑합니다. 키워드는 이슈 중 하나인 '환율'로 선정하였고, 환율 관련 기사를 찾을 수 있는 네이버 뉴스 경제 탭을 스크래핑하였습니다.

### 제주특별자치도 BC카드 사용 데이터 EDA 분석 연습
2014~2016년도 제주도 내 내국인 관광객의 BC카드 사용 데이터입니다. 상관관계 비교, 연령별 지역별 업종별 시각화를 진행하였습니다. 결제 건수가 가장 많은 지역, 소비가 높은 업종이 제주공항과 가깝다는 공통점을 가지고 있다는 것을 발견했습니다.