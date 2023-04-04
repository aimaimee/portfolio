# portfolio
# 목차
- [프로젝트](https://github.com/aimaimee/portfolio.git)
  - [이커머스 데이터셋(Olist), 판매 물품 선정 가이드라인 분석](https://github.com/aimaimee/portfolio.git)


## 프로젝트(데이터 분석)
### 이커머스 데이터셋(Olist), 판매 물품 선정 가이드라인 분석
__코드 :__ [Olist_ecommerce ipynb](https://github.com/aimaimee/portfolio/tree/main/olist_ecommerce/olist_code)

__보고서 :__ [Olist_ecommerce_md](https://github.com/aimaimee/portfolio/blob/main/olist_ecommerce/README.md)

__개요 :__ 

브라질 이커머스 회사인 Olist에 입점하려는 판매자를 가정하였습니다. 해당 판매자가 어떤 지역에서, 어떤 품목을, 어떻게 구성하여 판매할 지를 추천하기 위하여 분석을 진행합니다.

- EDA를 통해 Olist의 매출 상위 품목, 지역, 판매자를 분석합니다.
- 군집화, z-score, RFM을 활용하여 평가 지표를 생성합니다.
- 대상인 판매자가 시장 규모, 경쟁자, 구매자 충성도 중 중점으로 보는 것을 기준으로 품목을 고를 수 있도록 분석 결과를 제공합니다.

__담당역할 :__

Olist의 매출과 품목을 중심으로 EDA를 진행했습니다.(seaborn, plotly 활용)

RFM 분석을 진행하였습니다.(고객 분류에 점수를 부여하여 RFM 결과를 점수화하였고, 해당 점수를 군집화와 z_score 점수와 비교할 수 있도록 데이터프레임화하였습니다.)

## 프로젝트(ML)
### 온라인 수강생의 자리비움 여부 탐지 모델링
__코드 :__ 

__보고서 :__ 

__개요 :__

온라인 화상 수업(Zoom)에서 수강생이 자리를 비울 경우를 탐지하는 모델을 구현합니다. 자리에 있는지 여부를 파악하여 메세지를 출력하고, 기록합니다.
- 얼굴 탐지 모델 비교 및 선정(MediaPipe, OpenCV, Face Recognition, YOLOv3-5-7)
- YOLOv7 모델 후처리(사람만 인식하도록, 한 개의 탐지 박스만 출력하도록)
- 탐지된 인물이 탐지되지 않았을 경우, '자리비움' 시간 출력
- Edge Case

__담당역할 :__