import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def main():
    df = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")
    data = df.iloc[:20].select_dtypes(include=np.number).values
    sim_matrix = np.zeros((20,20))
    for i in range(20):
        for j in range(20):
            sim_matrix[i,j] = cosine_similarity(data[i], data[j])
    sns.heatmap(sim_matrix, annot=False)
    plt.show()

if __name__ == "__main__":
    main()
