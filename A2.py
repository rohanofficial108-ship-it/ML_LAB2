import pandas as pd

def main():
    df = pd.read_excel("Lab Session Data.xlsx", sheet_name="Purchase Data")
    df["Class"] = df["Payment (Rs)"].apply(lambda x: "RICH" if x > 200 else "POOR")
    print(df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)", "Payment (Rs)", "Class"]])

if __name__ == "__main__":
    main()
