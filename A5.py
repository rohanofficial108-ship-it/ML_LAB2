import numpy as np

def jaccard_smc(v1, v2):
    f11 = np.sum((v1 == 1) & (v2 == 1))
    f00 = np.sum((v1 == 0) & (v2 == 0))
    f01 = np.sum((v1 == 0) & (v2 == 1))
    f10 = np.sum((v1 == 1) & (v2 == 0))
    jc = f11 / (f01 + f10 + f11)
    smc = (f11 + f00) / (f00 + f01 + f10 + f11)
    return jc, smc

def main():
    v1 = np.array([1,0,1,1,0])
    v2 = np.array([1,1,0,1,0])
    jc, smc = jaccard_smc(v1,v2)
    print("Jaccard:", jc, "SMC:", smc)

if __name__ == "__main__":
    main()
