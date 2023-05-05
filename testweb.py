from PIL import Image
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
lottie_learning = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_9ungcrzx.json")
img_steps = Image.open("C:\Users\ADMIN\images\steps.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Aqila :wave:")
    st.title("A Junior Highschool Student from Indonesia")
    st.write("I am passionate about sports and games")
    st.write("[Know more about me >](https://instagram.com/_qiljak_?igshid=YmMyMTA2M2Y=)")

# --- WHO AM I ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who Am I")
        st.write("##")
        st.write(
            """
            Saya seorang siswa kelas 9 yang sedang:
            - belajar pemrograman sederhana menggunakan Python dan Streamlit
            - menambah dan muroja'ah hafalan Al-Qur'an & Hadits
            - belajar untuk menghadapi US bulan depan 💪
            
            Doa'kan saya sukses!"""
        )
        st.write("[I Learn to Make Web from Here >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
    with right_column:
        st_lottie(lottie_learning, height=300, key="learning")

# --- WHAT I'VE DONE ----
with st.container():
    st.write("---")
    st.header("What I've Done")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_steps)
    with text_column:
        st.write(
            """
            1. Install Anaconda Navigator [Get File Here >](https://www.anaconda.com/)
            2. Create Environment baru di Anaconda Navigator
            3. Open Terminal di Environment baru
            4. Ketik python (jika belum ada install dari Microsoft Store, jika sudah ada..lanjut)
            5. Ikuti langkah-langkah di video [I Learn to Make Web from Here](https://www.youtube.com/watch?v=VqgUkExPvLY)
            6. Sebelum deploy ke web, ikuti langkah [ini](https://www.youtube.com/watch?v=nJHrSvYxzjE) hanya sampai file requirements.txt terbuat
            7. Deploy web, ikuti cara [ini](https://www.youtube.com/watch?v=HKoOBiAaHGg)
            
            Selamat mencoba!!!"""
        )
