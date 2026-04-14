import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_temp(temp):
    temps = [temp + np.random.randint(-3, 3) for _ in range(7)]

    df = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Temp": temps
    })

    plt.figure()
    plt.plot(df["Day"], df["Temp"], marker="o")
    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.title("Weekly Trend")

    return plt
