import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def creating_clusters_products(data: pd.DataFrame):
    n_clusters = 5
    silhouette_avg = -1
    while silhouette_avg < 0.145:
        kmeans = KMeans(init='k-means++', n_clusters = n_clusters, n_init=30)
        kmeans.fit(data)
        clusters = kmeans.predict(data)
        silhouette_avg = silhouette_score(data, clusters)
        clusters = pd.DataFrame(clusters)
    return clusters
