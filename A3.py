import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")
    prices = df["Price"].values
    print("Mean:", np.mean(prices))
    print("Variance:", np.var(prices))

    loss_prob = (df["Chg%"] < 0).mean()
    print("Probability of loss:", loss_prob)

    wed_data = df[df["Day"] == "Wed"]
    profit_prob = (wed_data["Chg%"] > 0).mean()
    print("Profit probability on Wednesday:", profit_prob)

    sns.scatterplot(x=df["Day"], y=df["Chg%"])
    plt.show()

if __name__ == "__main__":
    main()
