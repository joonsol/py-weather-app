import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
import os
from weather_util import fetch_weather

# ✅ 폰트 설정 (NanumGothic 직접 지정)
font_path = os.path.join("font", "NanumGothic.ttf")
font_prop = fm.FontProperties(fname=font_path)

matplotlib.rcParams['font.family'] = font_prop.get_name()
matplotlib.rcParams['axes.unicode_minus'] = False

api_key = st.secrets["api_key"]
city = st.text_input("도시 이름 입력(ex: Seoul,New York)")

if st.button("날씨 조회"):
    data = fetch_weather(city, api_key)

    if data.get("cod") != 200:
        st.error(f"오류 : {data.get('message','조회 실패')}")
    else:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]

        st.subheader(f"{city}의 현재의 날씨 : {desc}")
        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        st.write(f"🌡️ 온도: {temp} °C")
        st.write(f"💧 습도: {humidity} %")

        fig, ax = plt.subplots()

        # ✅ 폰트를 x축 라벨에도 수동 적용
        bars = ax.bar(["온도", "습도"], [temp, humidity])
        ax.set_ylim(0, max(temp, humidity) + 20)
        ax.set_xticklabels(["온도", "습도"], fontproperties=font_prop)

        # (선택) 그래프 제목 등도 수동 지정
        ax.set_title("날씨 정보 시각화", fontproperties=font_prop)

        st.pyplot(fig)
