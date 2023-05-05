import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Aqila Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_1jibotah.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Aqila :wave:")
    st.title("A Junior Highschool Student from Indonesia")
    st.write("I am passionate about sports and games")
    st. write("[Know more about me >](https://instagram.com/_qiljak_?igshid=YmMyMTA2M2Y=)")

# --- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            Saya seorang siswa kelas 9 yang sedang:
            - belajar pemrograman sederhana menggunakan Python dan Streamlit
            - menambah dan muroja'ah hafalan Al-Qur'an & Hadits
            - belajar untuk menghadapi US bulan depan 💪
            
            Doa'kan saya sukses!"""
        )
        st.write("[My Channel >](https://youtube.com/QiljakNiboss)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")