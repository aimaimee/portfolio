# 온라인 수강생의 자리비움 여부 탐지 모델링
## 1. 프로젝트 개요

프로젝트 기간 : 22.12.22- 22.01.05 (2주)

팀 구성 : AI 부트캠프 파이널프로젝트 팀 5인

프로젝트 목표 : 온라인 화상 수업에서 수강생이 자리를 비울 경우를 탐지하는 모델을 구현합니다. 자리에 있는지 여부를 파악하여 메세지를 출력하고, 기록합니다.

## 2. 모델 선정 과정(MediaPipe, OpenCV, Face Recognition, YOLOv3-5-7)

### 2-1. MediaPipe

🔸 결론 : 최소 감지 신뢰값 변경에도 불구하고, 탐지 결과가 동일합니다. 마스크 쓴 경우 탐지 하지 못합니다.

CASE 1) model_selection(모델 선택)=0 일 때, 최소 감지 신뢰값(min_detection_confidence)을 0.2, 0.5, 0.8로 조정하였으나 얼굴 탐지 결과가 동일하며, 마스크 쓴 경우는 탐지하지 못합니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/377b137f-0d5e-4a82-9278-0ff461eca16e/Untitled.png)

## 3. 결과물(자리 비움 탐지)

1. 웹캠 실행, 인물 탐지 시작

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f30207d-2ab4-4b86-83c2-561d55798030/Untitled.jpeg)

1. 인물이 웹캠 화면을 이탈, 지속해서 자리에 없다면 ‘자리 비움’ 로그를 생성

![1회 자리비움 출력](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/655ac122-8953-45a3-88fb-710bddc29bcc/Untitled.png)

1회 자리비움 출력

![2회 자리비움 출력](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d40f7074-ddfa-4a76-8102-0782f4338771/Untitled.png)

2회 자리비움 출력

![3회 자리비움 출력](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d0c793bf-a179-4d4a-ba93-db2e5333907b/Untitled.png)

3회 자리비움 출력

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cfe19c5c-e1da-43f2-800f-f13af2ca297c/Untitled.png)

1. 인물이 다시 웹캠 화면 상에 탐지(25초경)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/58766b94-1b5d-4487-b9d6-220e1ac49b7b/Untitled.jpeg)

1. 잠시 등장했다가 화면 상에서 사라지면(31초), 그 기준으로 다시 자리 비움 여부를 체크
(44초경 1회 자리 비움 메시지 출력)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4df28d7-4fae-4f66-a4da-4987e06c7562/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f29cebe4-fb98-481d-96c8-f2d08a5c626c/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7fd54d85-0f4f-47aa-ae50-a7ab0d15d02c/Untitled.png)

## 4. Edge Case

### 4-1. 거울에 비친 사람 인식

거울에 비친 경우는 실체보다 낮은 점수지만 사람이라고 판단하여 탐지

![Untitled (16)_censored.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b2a91997-d5c1-4722-874a-191c468138c2/Untitled_(16)_censored.jpg)

![Untitled (17)_censored.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/94a4c0f8-5594-4155-824e-d3140edbfbea/Untitled_(17)_censored.jpg)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04da872a-f041-4ea6-9a2f-af060c512712/Untitled.png)

### 4-2. 인형, 그림, 사진을 사람으로 인식

![사람을 닮은 인형](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/977529be-87ff-491e-b8ca-565520877cf6/Untitled.png)

사람을 닮은 인형

![사진](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c8fc996f-2324-4bf4-a8d5-079f6db7400e/Untitled.png)

사진

![그림](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d0e42e7-77de-4911-b338-63afc6940880/Untitled.png)

그림

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/29d8155a-4c34-4870-a627-2cdf8b0b46aa/Untitled.png)

## 5. 모델 선정 과정(MediaPipe, OpenCV, Face Recognition, YOLOv3-5-7 비교)

### 5-1. YOLOv7 선택 이유

➡ 결론 : YOLOv7의 COCO 데이터셋과 파스칼 데이터셋을 비교해 본 결과, YOLOv7의 순수한 가중치와 COCO 데이터셋이 더 나은 성능을 보여줌

➡ 결론 : 0.80 이상의 confidence로 YOLOv5보다 성능이 좋기 때문에 YOLOv7을 선택

YOLOv3도 인물 탐지를 5명 모두 잘 하고 있지만 YOLO 모델 별 성능 비교를 확인하면 최근 버전이 더 나은 성능을 보여주는 것을 확인하고, YOLOv5와 YOLOv7 테스트 진행

![YOLOv3](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ffef6ba9-ced7-4669-bae7-8061166179f9/Untitled.png)

YOLOv3

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c454c35c-6f6e-4fb9-9b95-3cb7f43ded33/Untitled.jpeg)

![[출처](https://yong0810.tistory.com/30) YOLOv3, 5 비교시 YOLOv5가 나은 성능](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1590e381-53b0-4889-a3ee-64083423b345/Untitled.png)

[출처](https://yong0810.tistory.com/30) YOLOv3, 5 비교시 YOLOv5가 나은 성능

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9bd026dd-17ba-48f1-a0ef-b9f261799ca7/Untitled.png)

YOLOv5에 비해 YOLOv7은 하나의 0.50점을 제외하고 모두 0.80 이상의 confidence를 확인할 수 있으므로 **YOLOv7을 선택**. 또한, YOLOv7에서 파스칼 데이터셋을 활용해 사람만 예측하도록 후처리를 해준 경우, 사람을 인지하지 못한 경우가 존재하고 가장 높은 confidence 점수가 0.67점임을 확인하여 **YOLOv7의 코코 데이터셋을 활용하기로 결정**.하나만 점수가 지나치게 낮은것
vs 0.80 후반대와 0.90 점수는 안나오지만 점수 분포가 고른 것

![YOLOv5
0.66, 0.68, 0.77, 0.81, 0.76 confidence 점수](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ddfdbcd2-f573-4992-8ed4-29cf0e65868d/Untitled.png)

YOLOv5
0.66, 0.68, 0.77, 0.81, 0.76 confidence 점수

![YOLOv7-순수한 가중치, 파스칼 후처리 데이터셋
0.88, 0.94, 0.83, 0.89, 0.50 confidence 점수](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/28f978fe-d2bd-4753-b9a6-1bb0257e58cc/Untitled.png)

YOLOv7-순수한 가중치, 파스칼 후처리 데이터셋
0.88, 0.94, 0.83, 0.89, 0.50 confidence 점수

![YOLOv7-파스칼 사람만 예측하도록 후처리 데이터셋
사람 인지 불가, 0.67, 0.44, 0.43, 0.46 confidence 점수](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1d731418-dd87-4737-a182-721387cbfb7e/Untitled.png)

YOLOv7-파스칼 사람만 예측하도록 후처리 데이터셋
사람 인지 불가, 0.67, 0.44, 0.43, 0.46 confidence 점수

![YOLOv5
0.66, 0.68, 0.77, 0.81, 0.76 confidence 점수](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52063992-c08f-4236-af02-3ab12eb3fac8/Untitled.jpeg)

YOLOv5
0.66, 0.68, 0.77, 0.81, 0.76 confidence 점수

![YOLOv7
0.88, 0.94, 0.83, 0.89, 0.50 confidence 점수](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/865ac378-ed6b-4475-8713-d9dc9e791b9f/Untitled.jpeg)

YOLOv7
0.88, 0.94, 0.83, 0.89, 0.50 confidence 점수

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7ece49af-d366-4b32-af7f-997c71ee8626/Untitled.png)

### 5-1. MediaPipe

`MediaPipe`는 6개의 랜드마크(오른쪽 눈, 왼쪽 눈, 코 끝, 입 중심, 오른쪽 귀, 왼쪽 귀) 및 다중 얼굴 지원과 함께 제공되는 초고속 얼굴 감지 솔루션. `min_detection_confidence`의 기본값은 0.5이며, 0.0~1.0 사이의 값으로 모델의 최소 신뢰값. `model_selection`의 기본값은 0. 카메라에서 2m 이내의 얼굴에 적합한 근거리 모델일 때는 0, 5m 이내의 얼굴에 적합한 전체 범위 모델일 때는 1을 선택.

CASE 1) model_selection(모델 선택) = 0 일 때,

최소 감지 신뢰값(min_detection_confidence)을 0.2, 0.5, 0.8로 조정하였으나 얼굴 탐지 결과가 동일하며, 마스크 쓴 경우는 탐지 불가.

![Untitled_censored.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/225a116a-e6d4-4b8e-95b3-4ea8c0b637b1/Untitled_censored.jpg)

![Untitled (1)_censored.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7c0fb945-b4c8-4d57-ae21-9726c22d5612/Untitled_(1)_censored.jpg)

![Untitled (2)_censored.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eeb205f5-c4c5-401c-99d4-425fcbb10737/Untitled_(2)_censored.jpg)

CASE 2) model_selection(모델 선택)  = 1 일 때,

model_selection = 0 인 경우에 비해 얼굴 측면을 잘 탐지하지만, 여전히 마스크 쓴 사람은 탐지 불가.

![min_detection_confidence(최소 감지 신뢰값) = 0.2](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4fce9149-9e86-4b3f-91b6-01325837acec/Untitled.jpeg)

min_detection_confidence(최소 감지 신뢰값) = 0.2

![min_detection_confidence(최소 감지 신뢰값) = 0.8](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/59d1d7ea-a567-4c8c-aa47-340dbde8f58f/Untitled.jpeg)

min_detection_confidence(최소 감지 신뢰값) = 0.8

![min_detection_confidence(최소 감지 신뢰값) = 0.8](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/73068ef5-4cc3-4b9d-ba56-d8fd590798ac/Untitled.jpeg)

min_detection_confidence(최소 감지 신뢰값) = 0.8

### 2-2. OpenCV

`OpenCV`는 영상 처리에 사용할 수 있는 오픈 소스 라이브러리. Face detection의 결과물은 **파란색 박스**, **Eye detection**의 결과물은 연두색 박스로 출력

CASE 1) 5명 중 2명 탐지

- Face detection : 마스크를 쓴 사람과 얼굴 측면이 보이는 사람은 탐지 불가
- Eye detection : 얼굴 탐지한 2명 중 1명만 탐지, 입을 눈으로 잘못 탐지

CASE 2) 4명 중 1명 탐지

- Face detection : 이목구비가 다 보이는 1명만 탐지
- Eye detection : 입(술)이 가려진 상태에서는 정상적으로 탐지

CASE 3) 5명 중 3명 탐지

- Face detection : 마스크를 쓴 사람이 없는 경우, 5명 중 3명의 얼굴을 탐지
- Eye detection : 얼굴을 탐지한 3명 중, 눈을 제대로 탐지한 경우가 1건, 입을 눈으로 잘못 탐지한 경우가 1건, 눈을 아예 탐지하지 못한 경우가 1건

![CASE 1) 5명 중 2명 얼굴 탐지](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7bb4071f-9deb-4321-9e13-28b1628a1a7d/Untitled.png)

CASE 1) 5명 중 2명 얼굴 탐지

![CASE 2) 4명 중 1명 얼굴 탐지](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2b03ab75-0364-4250-abfe-6d2da006121c/Untitled.png)

CASE 2) 4명 중 1명 얼굴 탐지

![CASE 3) 5명 중 3명 얼굴 탐지](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75371fb8-6057-4d42-8fac-de2dc56e0fc6/Untitled.png)

CASE 3) 5명 중 3명 얼굴 탐지

![CASE 1) 5명 중 2명 얼굴 탐지](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/88aa86aa-9f0e-4c3c-8372-c7452c0c954a/Untitled.jpeg)

CASE 1) 5명 중 2명 얼굴 탐지

![CASE 2) 4명 중 1명 얼굴 탐지](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/326fdcea-eee1-458f-a3f8-d8aa183b2558/Untitled.jpeg)

CASE 2) 4명 중 1명 얼굴 탐지

![CASE 3) 5명 중 3명 얼굴 탐지](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d727c6d5-d0b3-4775-8549-e805472f0065/Untitled.jpeg)

CASE 3) 5명 중 3명 얼굴 탐지

### 2-3. Face Recognition

`Face Recognition`은 딥러닝 기반으로 제작된 dlib의 얼굴 인식 기능을 사용하여 구축. 수강생 정면 얼굴 사진과 이름을 사전 학습 시켜야 한다는 전제 조건이 발생. 조건을 만족하더라도 얼굴 탐지가 잘 되려면 각도가 잘 맞아야 하는 제한 사항.

CASE 1) 팀원 사진을 모두 사전 학습

이목구비가 잘 나온 팀원 2명은 얼굴과 라벨이 잘 맞게 탐지하는 것을 확인

마스크를 쓴 사람과 얼굴 측면이 보이는 경우에는 얼굴을 탐지하지 못함

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b8c3beaf-59a8-47de-8301-71ee8fc58d0f/Untitled.jpeg)
