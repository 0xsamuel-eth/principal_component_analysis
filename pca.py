import numpy as np
from sklearn.decomposition import PCA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2)

pca.fit(X)
#output

print(pca.explained_variance_ratio_)
#output

print(pca.singular_values_)
#output
