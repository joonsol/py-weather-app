import matplotlib
import streamlit as st
import matplotlib.pyplot as plt
from weather_util import fetch_weather

import matplotlib.font_manager as fm
import os

font_path = os.path.join("font", "NanumGothic.ttf")
font_name = fm.FontProperties(fname=font_path).get_name()
matplotlib.rcParams['font.family'] = font_name
matplotlib.rcParams['axes.unicode_minus'] = False


api_key =st.secrets["api_key"]

city=st.text_input("도시 이름 입력(ex: Seoul,New York)")

if st.button("날씨 조회"):
  data=fetch_weather(city, api_key)


  if data.get("cod")!=200:
    st.error(f"오류 : {data.get('message','조회 실패')}")
  else:
    temp=data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc=data["weather"][0]["description"]
    icon=data["weather"][0]["icon"]


    st.subheader(f"{city}의 현재의 날씨 : {desc}")
    st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
    st.write(f"🌡️ 온도: {temp} °C")
    st.write(f"💧 습도: {humidity} %")

    fig, ax =plt.subplots()
    ax.bar(["온도","습도"],[temp,humidity])
    ax.set_ylim(0,max(temp, humidity)+20)

    st.pyplot(fig)