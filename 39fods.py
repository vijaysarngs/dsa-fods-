import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/vijay/OneDrive/Documents/transaction_data.csv")

n_init=5
features = ['total_spent', 'number_of_items']


model = KMeans(n_clusters=3)


model.fit(data[features])
labels = model.predict(data[features])

# Visualize the clusters using a scatter plot
plt.scatter(data['total_spent'], data['number_of_items'], c=labels)
plt.xlabel('Total spent')
plt.ylabel('Number of items')
plt.title('Customer segmentation using K-Means')
plt.show()
print(len(labels))