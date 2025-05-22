import streamlit as st
import pandas as pd
import numpy as np
st.title("Streamlit 자동 배포 테스트")

name = st.text_input("이름을 입력하세요")



age=st.number_input("나이를 입력하세요",min_value=0,max_value=100)

st.image("./img/1.jpg", caption="로고 이미지")

if st.button("확인"):
    st.success(f"{name}님 반가워요!")
    

video=st.video('./img/2.mp4')


data= pd.DataFrame(np.random.randn(10,2),columns=["A","B"])


st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)

col1,col2=st.columns(2)

col1.write("left")
col2.write("right")

with st.sidebar:
    st.write("여기는 사이드바입니다")
    st.selectbox("옵션 선택", ["A", "B", "C"])


tab1, tab2 = st.tabs(["탭 1", "탭 2"])
with tab1:
    st.write("첫 번째 탭 내용입니다.")
with tab2:
    st.write("두 번째 탭 내용입니다.")

    st.success("성공 메시지입니다!")
st.info("정보 메시지입니다.")
st.warning("경고 메시지입니다.")
st.error("에러 메시지입니다.")