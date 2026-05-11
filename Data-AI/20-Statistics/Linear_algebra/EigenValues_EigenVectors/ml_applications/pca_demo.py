from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import pandas as pd

def run_pca():
    iris = load_iris()

    X = iris.data

    pca = PCA(n_components=2)

    transformed = pca.fit_transform(X)

    print("Explained variance:")
    print(pca.explained_variance_)

    return transformed