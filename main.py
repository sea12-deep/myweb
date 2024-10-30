import streamlit as st



# 버튼 = st.button("버튼")
# if 버튼 :
#     st.write("버튼을 눌렀습니다.")

# check = st.checkbox("선택")
# if check :
#     st.write("체크")

# st.write("hello world!!")
# st.write("스트림릿")

# import streamlit as st

# st.title("Title")
# st.header("Header")
# st.subheader("Subheader")
# st.markdown("우리 함께 **스트림릿**을 :red[배워]봅시다!!!")
# st.write("우리 함께 **스트림릿**을 :red[배워]봅시다!!!")

# 과목 = st.selectbox("과목을 선택하세요",
#                     ["확률과 통계",
#                      "미분과 적분",
#                      "기하와 벡터"])
# st.subheader(f"당신이 선택한 과목은 {과목}입니다.")
# id=st.text_input("아이디")

# id=st.text_inplit as stut("아이디")  
import streamlit as st
db_id = "test"
db_pw = "123"
if menu == "로그인":
  st.title("로그인")
id = st.text_input("아이디",placeholder="아이디를 입력하세요")
pw = st.text_input("비밀번호",type = "password")
login = st.button("로그인")
if login:
    if db_id == id and db_pw == pw :
        st.success("로그인 성공")
        st.balloons(  )
    else
        st.error("로그인 실패")
        st.snow( )
elif menu == "회원가입":
    st.title("회원가입")
    st.vedio(https://www.youtube.com/watch?v=pZ9sgHCrJZw )