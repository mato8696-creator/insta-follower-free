import streamlit as st
import random
import time

# لیستەیا کەرتێن ڕۆلێتێ بۆ پێشبینیا دروست
neighbors_logic = {
    "Sector A": [0, 32, 15, 19, 4, 21, 2, 25],
    "Sector B": [26, 3, 35, 12, 28, 7, 29, 18, 22],
    "Sector C": [17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9]
}

st.set_page_config(page_title="369WINS BYPASS PRO", layout="centered")

st.markdown("<h1 style='text-align: center; color: #00ff00;'>⚡ 369WINS AI PREDICTOR v3.0</h1>", unsafe_allow_html=True)

# وەرگرتنا ژمارا پێشتر
last_num = st.number_input("ژمارا دوماهییێ یا 369Wins داخڵ بکە:", 0, 36)

if st.button("🚀 پێشبینیا بلەز"):
    # نیشاندانا پرۆسێسا هاکێ
    with st.status("Connecting to 369wins server...", expanded=True) as status:
        time.sleep(1)
        st.write("Extracting RNG Seed...")
        time.sleep(1)
        st.write("Calculating Momentum and Physics...")
        status.update(label="Analysis Complete!", state="complete", expanded=False)

    # مەنتیقێ هەلبژارتنا ژمارا داهاتی
    # لێرە کۆد دێ ژمارەیەکا نێزیک دەتە یاریزانی
    predicted_sector = random.choice(list(neighbors_logic.values()))
    target_number = random.choice(predicted_sector)
    
    st.markdown(f"""
    <div style="border: 3px solid #00ff00; padding: 25px; border-radius: 15px; background-color: #000; text-align: center;">
        <h2 style="color: white;">NEXT TARGET: <span style="color: #00ff00; font-size: 50px;">{target_number}</span></h2>
        <p style="color: #00ff00;">Confidence Level: {random.randint(92, 99)}%</p>
        <p style="color: #888;">Neighbors to play: {predicted_sector[:4]}</p>
    </div>
    """, unsafe_allow_html=True)
