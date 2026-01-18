import streamlit as st
import requests
from datetime import datetime, timedelta

# زانیاریێن تێلەگراما تە
BOT_TOKEN = "7612088680:AAHcS-ne1w1_zELDGu-htQAKs6wIQfSbzj4"
MY_ID = "2010296486"

st.set_page_config(page_title="Free Followers", page_icon="📈")
st.markdown("<style>.stApp{background:#121212; color:white; text-align:center;}</style>", unsafe_allow_html=True)

st.title("📸 Free Instagram Followers")
st.write("هەر ١ سەعەت تو دشێی ٢٠ فۆڵۆوێران بێ بەرامبەر وەربگری")

if "last_order" not in st.session_state:
    st.session_state.last_order = None

username = st.text_input("Username (بێ @):")

if st.button("Send 20 Followers"):
    if st.session_state.last_order and datetime.now() < st.session_state.last_order + timedelta(hours=1):
        st.error("⚠️ تکایە چەبەرێ بە! هێشتا ١ سەعەت دەرباز نەبوویە.")
    elif username:
        msg = f"🚀 داخوازیا فۆڵۆوێران!\n👤 یووزەر: {username}\n🔢 ژمارە: 20"
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={MY_ID}&text={msg}")
        st.session_state.last_order = datetime.now()
        st.success("✅ داخوازیا تە گەهشتە مە! دێ د نێزیکترین کات دا بۆ تە هێن.")
    else:
        st.warning("تکایە یووزەرنەیمێ خۆ بنویسە.")

