import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

all_data_sample = all_data_sample.sample(2500)
X = all_data_sample[features]
pca = PCA(n_components=3)
pca.fit(X)
X_pca = pca.transform(X)


def plot_pca_3(X, c=all_data_sample['period']):
    fig, ax = plt.subplots(2, 2, figsize=(12, 12))
    ax[0,0] = fig.add_subplot(2, 2, 1, projection='3d')
    ax[0,0].scatter(X[:, 0], X[:, 1], X[:, 2], c=c, 
              edgecolor='k')

    ax[0,1].scatter(X[:, 0], X[:, 1],  c=c, s = 8)
    ax[1,0].scatter(X[:, 1], X[:, 2],  c=c, s = 8)
    ax[1,1].scatter(X[:, 2], X[:, 0], c=c, s = 8)
    plt.show()

plot_pca_3(X_pca)
