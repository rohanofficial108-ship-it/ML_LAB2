import pandas as pd
import numpy as np

def main():
    df = pd.read_excel("Lab Session Data.xlsx", sheet_name="Purchase Data")
    X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].values
    y = df["Payment (Rs)"].values

    print("Rank of matrix:", np.linalg.matrix_rank(X))
    pinv = np.linalg.pinv(X)
    costs = pinv.dot(y)
    print("Estimated product costs:", costs)

if __name__ == "__main__":
    main()
