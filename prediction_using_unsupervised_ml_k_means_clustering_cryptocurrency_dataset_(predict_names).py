# -*- coding: utf-8 -*-
"""Prediction Using Unsupervised ML K Means Clustering Cryptocurrency Dataset (Predict Names).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fGuFg49AUInfQWEnzG_iRseKsubxMM5v

# **Prediction Using Unsupervised ML K Means Clustering Cryptocurrency Dataset (Predict Names)**

The provided Jupyter Notebook applies K-Means clustering, an unsupervised machine learning algorithm, to a cryptocurrency dataset to identify patterns and group similar cryptocurrencies. This technique helps in categorizing assets based on performance and other attributes without prior labeling.
"""

# importing some lib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snes

data = pd.read_csv("/content/bitcoin.csv")

df = pd.DataFrame(data)

df.head()

df.isnull().sum()

df.info()

df.describe()

df.nunique()

# dropping unnessary columns

df = df.drop(columns=['Currency'])

df

#convertion of time

df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_numeric(df['Date'])

df

"""# Unsuppervised Machine Learning
here we will be using Algorithm of K-Mean
K-Means Clustering is an unsupervised machine learning algorithm used to group similar data points into K clusters based on feature similarity. It is widely used in pattern recognition, segmentation, and anomaly detection.


"""

# importing some important files
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


wcss = []
for k in range(1, 11):  # Testing K from 1 to 10
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)

plt.scatter(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('# of Clusters')
plt.ylabel('Sum of Square')
plt.grid()
plt.show()

plt.figure(figsize=(8,5))
plt.plot(range(1, 11), wcss,marker='o', linestyle='--')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal K')
plt.show()

"""The best K value to decide is where it stops to decrease rapidly and the best walue here is K = 3

# Prediction
"""

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
clusters = kmeans.fit_predict(df)

x = df.values
x

plt.scatter(x[clusters==0,0], x[clusters==0,1], s=12, c='red', label='USD')
plt.scatter(x[clusters==1,0], x[clusters==1,1], s=12, c='green', label='BTC')
plt.scatter(x[clusters==2,0], x[clusters==2,1], s=12, c='blue', label='1INCH')

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=20, c='black', label='Centroids')
plt.legend()
plt.grid()
plt.show()

"""# Accuracy

Silhouette Score	Interpretation

0.7 - 1.0	Excellent clustering ✅

0.5 - 0.7	Good clustering 👍

0.3 - 0.5	Moderate, needs improvement ⚠

0.0 - 0.3	Weak clustering, poor separation ❌

Negative	Completely wrong clustering ❌

✔ If silhouette_avg > 0.5, your clustering is good!
❌ If silhouette_avg < 0.3, you might need to adjust K or preprocess the data better.
"""

from sklearn.metrics import silhouette_score

silhouette_avg = silhouette_score(x, clusters)
print(f"Silhouette Score: {silhouette_avg:.4f}")



