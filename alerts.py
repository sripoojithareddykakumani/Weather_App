def get_alert(temp, humidity, prediction):
    if prediction == "Rain 🌧️":
        return "🌧️ Carry umbrella and avoid travel"
    elif temp > 35:
        return "🔥 Heat alert! Stay hydrated"
    elif temp < 15:
        return "🧥 Cold weather! Wear warm clothes"
    elif humidity > 85:
        return "💧 High humidity!"
    else:
        return "✅ Pleasant weather"
  
