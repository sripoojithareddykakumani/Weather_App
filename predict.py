# WEATHER PREDICTION LOGIC
def predict_rain(temp, humidity, pressure, description):
    """
    Predicts whether it will rain based on:
    - Weather description (most accurate)
    - Humidity levels
    """

    # If API already says rain → most reliable
    if "rain" in description.lower():
        return "Rain 🌧️"

    # High humidity → possible rain
    elif humidity > 85:
        return "Possible Rain 🌦️"

    # Otherwise no rain
    else:
        return "No Rain ☀️"


# RAIN PROBABILITY CALCULATION
def rain_probability(temp, humidity, pressure):
    """
    Calculates approximate probability of rain (0–100%)
    based on simple weather conditions.
    """

    prob = 0

    # Humidity impact
    if humidity > 70:
        prob += 40
    if humidity > 85:
        prob += 30

    # Pressure impact (low pressure → rain)
    if pressure < 1005:
        prob += 20

    # Temperature impact (cooler → more chance)
    if temp < 25:
        prob += 10

    return min(prob, 100)  # limit to 100%
