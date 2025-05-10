
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('outputs/tables/cleaned_data.csv')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Snapshot date for Recency calculation
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Compute RFM metrics
rfm = df.groupby('Customer ID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'Invoice': 'nunique',
    'TotalPrice': 'sum'
}).reset_index()

rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# Normalize RFM values
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

# KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Save full RFM with cluster labels
os.makedirs('../outputs/tables', exist_ok=True)
rfm.to_csv('../outputs/tables/rfm_segmented.csv', index=False)

# Save cluster-level averages
cluster_summary = rfm.groupby('Cluster')[['Recency', 'Frequency', 'Monetary']].mean().round(1)
cluster_summary.to_csv('../outputs/tables/cluster_summary.csv')

# Plot average monetary value per cluster
os.makedirs('../outputs/charts', exist_ok=True)
plt.figure(figsize=(8, 5))
sns.barplot(data=rfm, x='Cluster', y='Monetary', estimator='mean', ci=None)
plt.title('Average Monetary Value per Cluster')
plt.xlabel('Customer Cluster')
plt.ylabel('Avg Spend ($)')
plt.tight_layout()
plt.savefig('../outputs/charts/monetary_by_cluster.png')
