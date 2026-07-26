import pandas as pd

def main():
    df = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")
    df.fillna(df.mean(numeric_only=True), inplace=True)
    print("After imputation:\n", df.head())

if __name__ == "__main__":
    main()
