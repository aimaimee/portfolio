# 온라인 수강생의 자리비움 여부 탐지 모델링

![ezgif com-resize](https://user-images.githubusercontent.com/115875669/230790831-14510ebd-d9d9-4d9c-8491-0f7492a4ca5f.gif)
## 1. 프로젝트 개요

프로젝트 기간 : 22.12.22- 22.01.05 (2주)

팀 구성 : AI 부트캠프 파이널프로젝트 팀 5인

## 2. 프로젝트 목표
__온라인 화상 수업에서 수강생이 자리를 비울 경우를 탐지하는 모델을 구현합니다. 자리에 있는지 여부를 파악하여 메세지를 출력하고, 기록합니다.__

## 3. YOLOv7 모델 후처리

### 3-1. 1차 후처리(사람 외 이동수단 인식 제거)

가중치를 높여 보았을 때 해결이 되지 않아서, 라벨을 읽어볼 때부터 사람만 한정하는 코드를 추가해서 이동수단을 인식하는 경우를 제거
![image](https://user-images.githubusercontent.com/115875669/230786156-a93f6088-847a-48ae-9bfb-013937c72d7f.png)

### 3-2. 2차 후처리(사람을 인식하는 여러 개의 box 문제)
사람은 한 명인데 너무 많이 인식하는 경우, 일정 confidence 값 이하로는 시각화하지 않도록 설정하여 해결
![image](https://user-images.githubusercontent.com/115875669/230786286-c5aa3486-8a2d-4014-9166-6077b1a0db9f.png)


## 4. 결과물

1. 웹캠 실행, 인물 탐지 시작
![image](https://user-images.githubusercontent.com/115875669/230788329-4c4ae5e4-5447-49a4-a91d-5fd0e654711e.png)

<br/>

2. 인물이 웹캠 화면을 이탈, 지속해서 자리에 없다면 '자리 비움' 로그 생성
   ![image](https://user-images.githubusercontent.com/115875669/230788394-0ea6075d-adfe-4a7b-a79d-5872b2692b3d.png)

<br/>

3. 인물이 다시 웹캠 화면 상에 탐지(25초경)
   ![Untitled (16)_censored](https://user-images.githubusercontent.com/115875669/230788457-47572cd5-1abc-4df6-8395-d117c531974a.jpg)

<br/>

4. 잠시 등장 후 화면 상에서 사라지면(31초), 그 기준으로 다시 자리 비움 여부를 체크(44초경 1회 자리 비움 메시지 출력)
   ![image](https://user-images.githubusercontent.com/115875669/230788502-14351d43-ea22-42c6-8b16-688f8cb6e8db.png)

<br/>

## 5. Edge Case
### 5-1. 거울에 비친 사람 인식
거울에 비친 경우는 실체보다 낮은 점수지만, 사람이라고 판단하여 탐지
![image](https://user-images.githubusercontent.com/115875669/230788617-8ba44fe0-42e6-446c-a9a5-48737c40bb3c.png)

### 5-2. 인형, 그림, 사진을 사람으로 인식
![image](https://user-images.githubusercontent.com/115875669/230788640-1853cee1-6845-424d-8936-2fb45976989b.png)

<br/>

## 6. 모델 선정 과정(MediaPipe, OpenCV, Face Recognition, YOLOv3-5-7)

### 6-1. YOLOv7 선택 이유
🔸 모델 성능 비교 그래프 상, YOLOv3 < YOLOv5 ➡ YOLOv5 선택

🔸 confidence 점수 비교 상, YOLOv5 < YOLOv7 ➡ YOLOv7 선택

🔸 confidence 점수 비교 상, 파스칼 데이터셋 < 코코 데이터셋 ➡ YOLOv7의 기본 데이터셋인 코코 데이터셋 선택

#### 6-1-1. YOLOv3과 YOLOv5
YOLOv3도 인물 탐지를 5명 모두 잘 하고 있지만 YOLO 모델 별 성능 비교 그래프를 확인하면 최근 버전이 더 나은 성능을 보여주는 것을 확인하고, YOLOv5와 YOLOv7 테스트 진행
![image](https://user-images.githubusercontent.com/115875669/230788931-4e3a540e-115e-464c-a253-17eac3849845.png)

<br/>

#### 6-1-2. YOLOv5와 YOLOv7
YOLOv5에 비해 YOLOv7은 하나의 0.50점을 제외하고 모두 0.80 이상의 confidence를 확인할 수 있으므로 **YOLOv7을 선택**

(❓ 해결 후 삭제 예정 : 하나만 점수가 지나치게 낮은것 vs 0.80 후반대와 0.90 점수는 안나오지만 점수 분포가 고른 것 중 YOLOv7이 설득력 있는 이유가 있는가?)
![image](https://user-images.githubusercontent.com/115875669/230788984-c199d897-0519-449c-8848-c91851a79f56.png)

<br/>

#### 6-1-3. YOLOv7 코코 데이터셋과 파스칼 데이터셋
YOLOv7에서 파스칼 데이터셋을 활용해 사람만 예측하도록 후처리를 해준 경우, 사람을 인지하지 못한 경우가 존재하고 가장 높은 confidence 점수가 0.67점임을 확인하여 **YOLOv7의 코코 데이터셋을 활용하기로 결정**.

(❓ 해결 후 삭제 예정 : YOLOv7 코코 데이터셋 vs YOLOv7 파스칼 데이터셋 비교가 있어야 함.

(❓ 해결 후 삭제 예정 : 보고서 상 예시들은 순수한 가중치+파스칼 파인튜닝 데이터 & 사람만 예측하도록 파인튜닝 한 파스칼 데이터. 그렇다면, 첫 번째 예시의 파스칼 파인튜닝은 무엇을 파인튜닝 한 것인가)

<br/>

### 6-2. MediaPipe
> **MediaPipe는** 6개의 랜드마크(오른쪽 눈, 왼쪽 눈, 코 끝, 입 중심, 오른쪽 귀, 왼쪽 귀) 및 다중 얼굴 지원과 함께 제공되는 초고속 얼굴 감지 솔루션.
> 
> **min_detection_confidence**의 기본값은 0.5이며, 0.0~1.0 사이의 값으로 모델의 최소 신뢰값.
> 
> **model_selection**의 기본값은 0. 카메라에서 2m 이내의 얼굴에 적합한 근거리 모델일 때는 0, 5m 이내의 얼굴에 적합한 전체 범위 모델일 때는 1을 선택.
  
CASE 1) model_selection(모델 선택) = 0 일 때,

- 최소 감지 신뢰값(min_detection_confidence)을 0.2, 0.5, 0.8로 조정하였으나 얼굴 탐지 결과가 동일하며, 마스크 쓴 경우는 탐지 불가.

![image](https://user-images.githubusercontent.com/115875669/230789574-203bbeb1-2f03-4ac4-ac1d-bbd8d4e40640.png)

<br/>

CASE 2) model_selection(모델 선택)  = 1 일 때,

- model_selection = 0 인 경우에 비해 얼굴 측면을 잘 탐지하지만, 여전히 마스크 쓴 사람은 탐지 불가.

![image](https://user-images.githubusercontent.com/115875669/230789643-b9f0ec88-45f6-4b33-96e4-dc09823c6a09.png)

<br/>

### 6-3. OpenCV
> **OpenCV**는 영상 처리에 사용할 수 있는 오픈 소스 라이브러리.
>
> <span style = "color: #0000FF">Face detection</span>의 결과물은 파란색 박스
> 
> Face detection의 결과물은 <span style = "background-color: #0000FF">파란색 박스</span>
> 
> Eye detection의 결과물은 <span style = "background-color : #008000">연두색 박스</span>로 출력

CASE 1) 5명 중 2명 탐지

- Face detection : 마스크를 쓴 사람과 얼굴 측면이 보이는 사람은 탐지 불가

- Eye detection : 얼굴 탐지한 2명 중 1명만 탐지, 입을 눈으로 잘못 탐지

CASE 2) 4명 중 1명 탐지

- Face detection : 이목구비가 다 보이는 1명만 탐지

- Eye detection : 입(술)이 가려진 상태에서는 정상적으로 탐지

CASE 3) 5명 중 3명 탐지

- Face detection : 마스크를 쓴 사람이 없는 경우, 5명 중 3명의 얼굴을 탐지
- Eye detection : 얼굴을 탐지한 3명 중, 눈을 제대로 탐지한 경우가 1건, 입을 눈으로 잘못 탐지한 경우가 1건, 눈을 아예 탐지하지 못한 경우가 1건

![image](https://user-images.githubusercontent.com/115875669/230789721-534a4eb6-f1d1-4a7e-a37c-d0315db00c5e.png)

<br/>

### 6-4. Face Recognition
> Face Recognition은 딥러닝 기반으로 제작된 dlib의 얼굴 인식 기능을 사용하여 구축.
> 
> 수강생 정면 얼굴 사진과 이름을 사전 학습 시켜야 한다는 전제 조건이 발생.
> 
> 조건을 만족하더라도 얼굴 탐지가 잘 되려면 각도가 잘 맞아야 하는 제한 사항.

CASE 1) 팀원 사진을 모두 사전 학습

- 이목구비가 잘 나온 팀원 2명은 얼굴과 라벨이 잘 맞게 탐지하는 것을 확인

- 마스크를 쓴 사람과 얼굴 측면이 보이는 경우에는 얼굴을 탐지하지 못함

CASE 1) model_selection(모델 선택)=0 일 때, 최소 감지 신뢰값(min_detection_confidence)을 0.2, 0.5, 0.8로 조정하였으나 얼굴 탐지 결과가 동일하며, 마스크 쓴 경우는 탐지하지 못합니다.