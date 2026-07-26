import pandas as pd

def main():
    df = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")
    print("Data types:\n", df.dtypes)
    print("Missing values:\n", df.isnull().sum())
    print("Mean values:\n", df.mean(numeric_only=True))
    print("Variance:\n", df.var(numeric_only=True))

if __name__ == "__main__":
    main()
