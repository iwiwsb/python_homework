import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

with open("hw-10\\events.json") as events:
    data = json.load(events)
    dataframe = pd.DataFrame(data["events"])

    plt.figure()
    plt.title("Распределение типов событий безопасности")
    plt.grid()
    plt.xlabel("Число срабатываний")
    sns.countplot(dataframe, y="signature")
    plt.show()
