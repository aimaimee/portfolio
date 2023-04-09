import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="줌인줌아웃",
    page_icon="📸",
    layout="wide"
)

# sidebar
with st.sidebar:
    st.markdown("## 📸줌인줌아웃📸")
    st.markdown("#### 실시간 웹캠 자리비움 탐지 보고서")

   
img1 = Image.open('data/logo.png')
st.image(img1)

def main() :
    
    tab1, tab2, tab3 = st.tabs(["Topic", "Model", "Output"])
    with tab1:
        st.subheader("코로나19와 비대면 원격 수업")
        st.write("신종 코로나바이러스 감염증(코로나19)으로 비대면 원격 서비스 활용이 늘어나면서, <멋쟁이사자처럼 AIS> 7기 수업 역시 줌(Zoom)을 통한 온라인 수업으로 진행되고 있습니다.")
        st.write("이런 온라인 강의는 대부분 관리 효율성을 위해 어느 정도 모니터링이 필요하며, 7기 수강생들 역시 모니터링 매니저님 덕분에 수업 집중도를 높일 수 있었습니다.")
        st.write("하지만 모니터링 매니저님 혼자서 다수의 줌 화면을 확인하는 데는 피로도가 높을 것으로 판단하였고, 저희 팀은 모니터링 매니저님의 업무 효율성을 높일 수 있는, <온라인 화상 수업 서포팅 프로그램> 을 프로젝트 주제로 선정했습니다.")
        st.image("data/topic.png")

    with tab2:
        selected_item = st.radio("", ("Mediapipe", "OpenCV", "Face Recognition", "Yolo"), horizontal=True, label_visibility="collapsed")

        if selected_item == "Mediapipe":
            st.write("")
            st.image("data/mediapipe.png")
            st.write(f"""
                - 구글에서 주로 인체를 대상으로 하는 비전인식기능들을 AI모델 개발과 기계 학습까지 마친 상태로 제공하는 서비스
                - 다양한 프로그램 언어에서 사용하기 편하게 라이브러리 형태로 모듈화되어 제공되며 사용 방법 또한 풍부하게 제공되기 때문에 몇 가지 간단한 단계로 Mediapipe에서 제공하는 AI기능을 활용한 응용 프로그램 개발이 가능
            """)
            st.header("MediaPipe의 Face Detection")
            st.write(f"""
                - 6개의 랜드마크(오른쪽 눈, 왼쪽 눈, 코 끝, 입 중심, 오른쪽 귀 윗 가장자리 위의 점 및 왼쪽 귀 윗 가장자리 위의 점) 및 다중 얼굴 지원과 함께 제공되는 초고속 얼굴 감지 솔루션
            """)
        elif selected_item == "OpenCV":
            st.write("")
            st.image("data/s_opencv.png", width=400)
            st.write(f"""
                - Open Source Computer Vision의 약자로, 영상 처리에 사용할 수 있는 오픈 소스 라이브러리
                - 컴퓨터가 사람의 눈처럼 인식할 수 있게 처리해주는 역할을 하기도 하며, 카메라 어플에서도 OpenCV가 사용됨
                - 추가로 사용되는 예시 : 공장에서 제품 검사, 의료 영상 처리 및 보정 그리고 판단, CCTV영상, 로보틱스
             """)
        elif selected_item == "Face Recognition":
            st.header("Face Recognition")
            st.write(f"""
                - 해당 라이브러리는 딥러닝 기반으로 제작된 [dlib](http://dlib.net/)의 얼굴 인식 기능을 사용하여 구축
                - 핵심은 DB에 보유한 Class의 대표 이미지와 입력된 Input 이미지간의 distance를 구하고 이 distance를 가지고 어떤 사람인지를 판단
                - 일반적인 전처리 과정
                  1) face detection, 얼굴 검출: 시스템에 입력된 이미지에서 얼굴 영역을 찾음(face detection, 얼굴 검출)
                  2) face alignment, 얼굴 정렬: 눈과 코 등 얼굴의 특징을 나타내는 점을 찾음
                  3) 이 특징점을 이용해 얼굴 영역을 동일한 형태와 크기로 변경
                - 이 모델은 [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) 기반으로 99.38%의 정확도를 가짐([https://github.com/ageitgey/face_recognition](https://github.com/ageitgey/face_recognition))
             """)
        else:
            st.header("What is the best YOLO?")
            st.image("data/yolo.png")
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.image("data/yolov3.png", width=420, caption="사진1️⃣ : YOLOv3, 4, 5를 비교(4와 5 버전의 우위가 정확하지 않음)")
#             with col2:
#                 st.image("data/yolov5.png", caption="사진2️⃣ : 4, 5를 따로 비교한 자료")
            
#             e1, e2, e3 = st.columns([0.3, 1.0, 0.3])
#             with e1:
#                 st.write(' ')
#             with e2:
#                 st.image("data/yolov7.png", width=650)
#             with e3:
#                 st.write(' ')
                
            st.subheader("📝 결론")
            st.write(f"""
                - YOLOv4는 v5에 비해 느리게 동작하지만 FPS성능의 최적화 가능
                - YOLOv5는 v4에 비해 더 쉽게 환경을 구성하고, 구현 가능
                - YOLOv7은 real-time object detection 분야에서 SOTA로 인정받고 있으며, 그 전 모델들보다 훨씬 더 좋은 성능과 속도를 가짐
            """)

    with tab3:
        selected_item = st.radio("", ("1️⃣st", "2️⃣nd", "3️⃣rd", "4️⃣th"), horizontal=True, label_visibility="collapsed")
        if selected_item == "1️⃣st":
            st.subheader("📹 웹캠 시작")
            a1, b1 = st.columns(2)
            with a1:
                st.image("data/o1.png", width=420)
            with b1:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("- 웹캠이 실행되고, 인물 탐지를 시작")
                
        if selected_item == "2️⃣nd":
            st.subheader("📹 웹캠 화면 이탈")
            st.image("data/o24.png")
            st.write(f"""
                - while 문을 일정 횟수 동안 반복했을 때, 지속해서 자리에 없다면 ‘자리 비움’ 로그를 생성
                - 해당 횟수는 사용자가 지정 가능
                - 자리를 비웠을 때, 루프문이 돌면서 존재 여부를 탐색
                - 인물이 인식되지 않을 경우 계속해서 자리 비움 로그 생성
            """)
                
        if selected_item == "3️⃣rd":
            st.subheader("📹 자리 복귀")
            a3, b3 = st.columns(2)
            with a3:
                st.image("data/o5.png", width=400)
            with b3:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("- 인공지능이 인물을 다시 탐지")
                
        if selected_item == "4️⃣th":
            st.subheader("📹 화면 재이탈")
            st.image("data/o67.png", width=820)
            st.write("- 다시 화면 상에서 사라지면, 그 기준으로 다시 자리 비움 여부를 체크")
    
    
if __name__ == "__main__" :
    main()