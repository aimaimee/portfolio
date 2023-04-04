<center><img src="https://user-images.githubusercontent.com/115875669/228904040-4aba838e-0da6-47e8-bac0-eb80a46e6c92.png" width="500" height="650"></center>


# 브라질 이커머스 데이터셋(Olist), 판매 물품 선정 가이드라인 분석

## 1. 프로젝트 개요
프로젝트 기간 : 23.01.09- 23.01.13 (5일)

활용 데이터 : [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

대회 주제 : Olist 온라인 쇼핑몰 데이터를 활용하여 비즈니스적 가치 창출하기

## 2. EDA

브라질 E-Commerce 회사인 Olist에 판매자로서 입점하고자 하는 타겟에게,
**‘판매할 품목, 대상 장소, 판매 방법’**
에 대한 분석 결과를 제공하고자 합니다.

### 2.1 매출 상위 품목 분석
🔸 최종 결론 : 매출 상위 품목들로 범위를 제한하여 분석을 진행합니다.📍📌💡🔎

품목별 매출과 해당 매출이 전체 매출에서 차지하는 비율 누적 그래프입니다. 빨간선은 누적 비율 80% 기준선입니다. **전체 거래 금액의 약 80%가 매출 상위 15개 품목에서 발생**하고 있습니다. 
 > 그래프에서 보여지는 상위 품목은 health_beauty, watches_gifts, bed_bth_table, sports_leisure, computers_accessories 등입니다.

![image](https://user-images.githubusercontent.com/115875669/228911832-f8f9e115-16b0-497e-be8c-334e52d6bbc4.png)

### 2.2 지역 분석

🔸 결론 1 : 브라질 남동부와 상파울루 지역의 주문이 많다.

🔸 결론 2 : 빠른 배송(23일 기준)을 제공할 수 있도록 지역을 선택해야 한다.

🔸 최종 결론 : 배송과 주문건수를 모두 만족할 수 있는 곳은 **상파울루 지역**이다.

#### 2.2.1 지역 주문 건수 비교


총 주문건수는 110,475이며 총 판매자와 구매자의 지역의 수(distinct)는 588입니다. 브라질 남동부 지역과 특히 상파울루 주변에서 대부분의 주문이 발생합니다.

![image](https://user-images.githubusercontent.com/115875669/228913738-d8b1266b-f05f-4619-94c2-f91eee4b436a.png)

하단의 이미지는 브라질의 남동부 지역에 집중된 주문 건수의 시각화입니다.
<center><img src="https://user-images.githubusercontent.com/115875669/228914916-5b4f6570-cad9-4980-8989-02352b15fc4f.png" width="400" height="250"></center>
<center><img src="https://user-images.githubusercontent.com/115875669/228915016-e6021571-838c-4576-a9dc-5725a6721463.png" width="400" height="250"></center>

#### 2.2.2 거리, 배송이 주문 건수에 미치는 영향

가로축인 거리가 멀어질 수록, 세로축인 주문 건수가 감소하는 것을 확인할 수 있습니다.

![image](https://user-images.githubusercontent.com/115875669/228916465-088248a0-81ca-4a0a-9690-c7f91fa66c94.png)
> 해당 분석에 사용한 수식 참고
>
> (x1, y1)과 (x2, y2)의 거리를 구할 때, 일반적인 좌표평면 두 점 사이의 거리 공식을 사용하면 지구가 구 모양이기 정확하지 않습니다. 따라서 이미지의 수식을 활용하여 구 모양이 반영된 소비자-판매자 거리 차이를 구할 수 있습니다.(위, 경도 x, y 대입)
> ![image](https://user-images.githubusercontent.com/115875669/228916245-70571eeb-ef87-4dde-ba20-eb214d638904.png)

<br/><br/>
예상 배송 소요일 23일을 기점으로 주문량이 감소합니다.

![image](https://user-images.githubusercontent.com/115875669/228919310-a5927e9b-77ff-4c24-8f4b-25c4338615ec.png)

<br/>

### 2.4 판매자 분석

🔸 결론 1 : 매출 상위 판매자는 평균 4개의 품목을 취급한다.

🔸 최종결론 : 판매자가 1개 품목이 아닌 여러 품목을 구성하여 판매를 시작하고 싶다면, 장바구니 분석을 고려하면 된다.

Olist의 판매자 데이터(olist_sellers_dataset)은 판매건수가 없는 경우는 기록되지 않기 때문에 실제 Olist를 사용하는 총 판매자의 수는 알 수 없습니다. 단지, 성공한 판매자의 특징을 알아보기 위해, 총 3,056명의 판매자 중, 판매건수를 기준으로 상위 500명을 샘플링하여 분석을 진행하였습니다.

> **olist_sellers_dataset**
>
> This dataset includes data about the sellers that **fulfilled orders made at Olist.** Use it to find the seller location and to identify which seller fulfilled each product.
> 

| 총 매출 | 평균 매출 | 총 주문건수 | 평균 주문건수 | 평균 품목 수 |
| --- | --- | --- | --- | --- |
| 1위 : 244627,55 | 20028.25 | 1위 : 2153건 | 188.106건 | 4.198 품목 |
| 500위 : 873.36 |  | 500위 : 247건 |  |  |

#### 2.4.1 판매 품목 구성 분석

판매자 분석에서 상위 500명의 판매자가 평균 4개의 품목을 취급하고 있고, 하위 500명의 판매자는 평균 1개의 품목을 취급하고 있습니다. 어떤 품목을 함께 구성하여 판매하면 좋을지 알아보기 위해 ‘장바구니 분석’을 통해 상품 간 연관성을 분석하였습니다.

#### 2.4.2 장바구니 분석

원의 크기는 판매 상품 조합의 연결 중심성의 크기입니다. 이는 해당 상품이 얼마나 많이 출현했는지를 의미합니다. 예를 들어, housewares 품목의 상품을 판매하는 판매자는 health_beauty, auto, sports_leisure 등의 품목의 상품도 함께 판매하는 경우가 많습니다.

<center><img src="https://user-images.githubusercontent.com/115875669/228920929-8fd8d681-14c0-4b74-8f9a-ed96e717b5c9.png" width="600" height="400"></center>

<br/>

## 3. 평가 지표 구성

### 3.1 평가지표 1 : 군집화(시장 규모와 상위 품목)

2018-08 기준, 품목별 주문량과 총 매출을 기반으로 등급(S~C)을 나눕니다. 해당 등급 작성에는 K-Means Clustering을 사용하였습니다.

<center><img src="https://user-images.githubusercontent.com/115875669/228921112-1b614120-f2b6-4f1a-8e6b-45ca766abb13.png" width="400" height="300"></center>

전체 기간(2016-10~2018-08) 동안 한 번이라도 S, A 등급을 받은 품목들의 등급입니다.(21개 품목) S등급에 2점, A등급에 1점, 이외 등급에 0점을 부여하였습니다.

![image](https://user-images.githubusercontent.com/115875669/228921217-daf793dd-7a92-4b3a-a7ce-07fb5678ea14.png)

2018년의 cluster 점수를 품목별로 더하고(18개 품목 산출), 너무 작은 값(0, 1, 2)을 제거하여 상위 8개 품목을 선정하였습니다.

<center><img src="https://user-images.githubusercontent.com/115875669/228921329-e7864f19-7a4d-4533-bf3a-fb4779d25d85.png" width="300" height="300"></center>

### 3.2 평가지표2 : Z-score(판매자 기준 상위 품목)

**3.2.1 평균과 표준편차 계산**

상위 등급인 S, A 등급을 대상으로 **1. 판매자 1인당 평균 매출액, 주문건수**와 **2. 판매자별 매출과 주문건수의 표준편차**를 구했습니다. 1번에서 평균값이 클수록 해당 품목의 물건을 판매할 때 잠재력이 크다는 것을 의미합니다. 2번에서 표준편차가 클수록 소수가 장악하는 시장임을 의미합니다.

**3.2.2 Z-score로 평균과 표준편차 비교**

평균과 표준편차의 단위가 달라 비교가 어렵기 때문에, 각 평균과 표준편차마다 표준정규분포를 도입하여 비교를 가능하게 합니다. 주문 건수와 매출의 평균은 클수록 좋기 때문에 Z-score 공식을 따르고, 표준편차는 작을수록 좋기 때문에 Z-score 공식에 -1을 곱하여 비교합니다.

<center><img src="https://user-images.githubusercontent.com/115875669/228921447-85123e88-02fc-4470-981e-57fe25c21717.png" width="250" height="100"></center>

- 주문 건수가 많을수록 해당 품목이 유리하다고 판단한다면, 주문 건수의 평균과 표준편차 z_score를 더한 값(z_order)에 더 가중치를 둡니다.
- 매출액이 클수록 해당 품목이 유리하다고 판단한다면, 매출액의 평균과 표준편차 z_score를 더한 값(z_price)에 더 가중치를 둡니다.
- 두 개 모두 비슷하게 중요하다고 판단한다면, 모든 z_score를 더한 값(z_total)을 사용합니다.

**3.2.3 Z-total**

주문 건수와 매출액 모두 중요하다고 판단했기 때문에 전체 기간 동안 한 번이라도 S, A 등급을 받은 품목들의 Z_total로 계산을 하였습니다.

![image](https://user-images.githubusercontent.com/115875669/228921958-8af0d757-1962-4709-b701-bb334d956105.png)

<center><img src="https://user-images.githubusercontent.com/115875669/228922110-60bb2612-456d-4053-88d1-e49dbf9fa873.png" width="300" height="300"></center>

<br/><br/>

### 3.3 평가지표3 : RFM(구매자 기준 상위 품목)

상위 8개 품목을 비교할 때, 해당 품목별 구매 가능성이 높은 고객 비율이 높을수록 유리합니다.

![image](https://user-images.githubusercontent.com/115875669/228922604-61c05e98-f44a-4743-ba0e-7405cd7ee5c9.png)

<center><img src="https://user-images.githubusercontent.com/115875669/228922804-eb88a3a0-bba4-4f60-8653-8c588fc70cff.png" width="350" height="300"></center>

분류된 고객군에 Lost-0부터 Champions-6의 값을 할당합니다. 분류된 고객군의 비율에 할당된 점수(0~6점)를 곱하여 고객군별 점수를 구합니다. 해당 품목의 고객군별 점수를 모두 더해 RFM 점수를 구합니다. RFM 점수는 높을수록 좋습니다.

<center><img src="https://user-images.githubusercontent.com/115875669/228923119-45bb3641-7eea-4ab5-9fe9-010f155105d4.png" width="300" height="300"></center>

<br/><br/>

### 3.4 평가지표 결론

1. 시장 규모를 중점으로 보는 판매자라면, 군집화(cluster) 기준으로 품목을 고릅니다.
    - 1등 : ‘health_beauty’
    - 2등 : ‘bed_bath_table’
    - 3등 : ‘computers_accessories’
    - 이외 : 'sports_leisure', 'watches_gifts', 'furniture_decor', 'housewares', 'auto’
2. 경쟁자(타 판매자)를 중점으로 보는 판매자라면, Z_total 기준으로 품목을 고릅니다.
    - 1등: 'bed_bath_table'
    - 2등:  'computers_accessories'
    - 3등: 'health_beauty'
    - 이외: 'watches_gifts', 'auto', 'sports_leisure', 'housewares', 'furniture_decor’
3. 구매자 충성도를 중점으로 보는 판매자라면, RFM 기준으로 품목을 고릅니다.
    - 1등: 'bed_bath_table'
    - 2등: 'furniture_decor'
    - 3등: 'sports_leisure'
    - 이외: 'watches_gifts', 'computers_accessories', 'auto', 'housewares', 'health_beauty’

<br/>

## 4. 종합 결론

- 입점 할 지역 : 상파울루
- 판매할 품목
    - 평가지표들을 종합적으로 고려해서, 단 하나의 품목으로 판매를 시작하고 싶다면, bed_bath_table 품목입니다.
    - 상위 판매자들이 평균 4개 품목을 함께 구성해서 판매한 것을 참고하여 여러 품목으로 판매를 시작하고 싶다면, housewares 품목입니다.
        - bed_bath_table이 장바구니 분석에서 출현하지 않는 것은, 한 개 품목만으로 잘 팔리기 때문입니다.
        - 장바구니 분석의 cool_stuff 품목은 평가 지표 순위에는 없습니다. 이유는 하나의 품목만으로는 좋은 평가를 받을 수 없지만, 단점을 상쇄하기 위해 여러 품목을 함께 판매하는 전략을 사용했을 것이라고 유추합니다.

## 5. 개인 회고
- 매출 상위 품목을 나누는 기준의 통일성 부족
  - 품목 분석 EDA를 진행 시에는 매출의 80%를 담당하는 15개 품목으로 제한(Top15 품목)
  - 지역 분석 EDA를 진행 시에는 매출 합계 상위 5개 품목(Top5 품목), 매출 합계 상위 10개 도시(Top10 도시)
  - 평가 지표 생성 시에는 군집화를 진행 할 때, 점수가 낮은 품목은 제거하면서 8개 품목으로 변경(Top8 품목)
- 시각화 양식의 통일성 부족