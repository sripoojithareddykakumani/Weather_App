import streamlit as st
from fetch import get_weather
from predict import predict_rain, rain_probability
from alerts import get_alert
from visualize import plot_temp

from streamlit_lottie import st_lottie
import requests
import time
import datetime
from streamlit_autorefresh import st_autorefresh

# SESSION STATE (for auto refresh)
if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

if "city" not in st.session_state:
    st.session_state.city = ""

# LOTTIE FUNCTION
def load_lottie(url):
    r = requests.get(url)
    return r.json()

# CSS DESIGN
st.markdown("""
<style>
.card {
    background-color: #1e1e2f;
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    color: white;
}

.title {
    text-align: center;
    font-size: 35px;
    color: #4CAF50;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #ccc;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# HEADER + ANIMATION
st.markdown('<div class="title">🌦️ Smart Weather System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Real-time weather + smart predictions</div>', unsafe_allow_html=True)

lottie_weather = load_lottie("https://assets2.lottiefiles.com/packages/lf20_jmBauI.json")
st_lottie(lottie_weather, height=200)

# Auto refresh every 10 seconds (10000 ms)
st_autorefresh(interval=10000, key="datarefresh")

# INPUT
city_input = st.text_input("📍 Enter City Name")

if st.button("Get Weather"):
    st.session_state.city = city_input

# MAIN LOGIC
if st.session_state.city:

    data = get_weather(st.session_state.city)

    if data is None:
        st.error("❌ City not found!")
    else:
        temp = data["temp"]
        humidity = data["humidity"]
        pressure = data["pressure"]
        description = data["description"]

        prediction = predict_rain(temp, humidity, pressure, description)
        prob = rain_probability(temp, humidity, pressure)
        alert = get_alert(temp, humidity, prediction)

        # WEATHER CARD
        st.markdown(f"""
        <div class="card">
            <h3>📍 Weather in {st.session_state.city}</h3>
            <p>🌡️ Temperature: {temp} °C</p>
            <p>💧 Humidity: {humidity}%</p>
            <p>📉 Pressure: {pressure}</p>
            <p>☁️ Condition: {description}</p>
        </div>
        """, unsafe_allow_html=True)

        # PREDICTION CARD
        st.markdown(f"""
        <div class="card">
            <h3>🤖 Prediction</h3>
            <p>{prediction}</p>
        </div>
        """, unsafe_allow_html=True)

        # PROBABILITY CARD
        st.markdown(f"""
        <div class="card">
            <h3>🌧️ Rain Probability</h3>
            <p>{prob}% chance of rain</p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(prob)

        # ALERT CARD
        st.markdown(f"""
        <div class="card">
            <h3>⚠️ Smart Alert</h3>
            <p>{alert}</p>
        </div>
        """, unsafe_allow_html=True)

        # GRAPH
        fig = plot_temp(temp)
        st.pyplot(fig)

        # LAST UPDATED TIME
        st.caption(f"Last updated: {datetime.datetime.now().strftime('%H:%M:%S')}")

