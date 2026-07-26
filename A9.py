import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
    df = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df.select_dtypes(include=np.number))
    print("Normalized data sample:\n", df_scaled[:5])

if __name__ == "__main__":
    main()
