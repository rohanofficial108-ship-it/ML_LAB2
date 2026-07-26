import numpy as np

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def main():
    v1 = np.array([1,2,3])
    v2 = np.array([2,3,4])
    print("Cosine similarity:", cosine_similarity(v1,v2))

if __name__ == "__main__":
    main()
