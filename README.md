# portfolio
# 목차
- [프로젝트](https://github.com/aimaimee/portfolio.git)
  - [이커머스 데이터셋(Olist), 판매 물품 선정 가이드라인 분석](https://github.com/aimaimee/portfolio.git)


## 프로젝트
### 이커머스 데이터셋(Olist), 판매 물품 선정 가이드라인 분석
__코드:__ [Olist_ecommerce ipynb](https://github.com/aimaimee/portfolio/tree/main/olist_ecommerce/olist_code)

__보고서:__ [Olist_ecommerce_md](https://github.com/aimaimee/portfolio/blob/main/olist_ecommerce/README.md)

__개요:__ 

브라질 이커머스 회사인 Olist에 입점하려는 판매자를 가정하였습니다. 해당 판매자가 어떤 지역에서, 어떤 품목을, 어떻게 구성하여 판매할 지를 추천하기 위하여 분석을 진행합니다.

- EDA를 통해 Olist의 매출 상위 품목, 지역, 판매자를 분석합니다.
- 군집화, z-score, RFM을 활용하여 평가 지표를 생성합니다.
- 대상인 판매자가 시장 규모, 경쟁자, 구매자 충성도 중 중점으로 보는 것을 기준으로 품목을 고를 수 있도록 분석 결과를 제공합니다.

__담당역할:__

Olist의 매출과 품목을 중심으로 EDA를 진행했습니다.(seaborn, plotly 활용)

RFM 분석을 진행하였습니다.(고객 분류에 점수를 부여하여 RFM 결과를 점수화하였고, 해당 점수를 군집화와 z_score 점수와 비교할 수 있도록 데이터프레임화하였습니다.)