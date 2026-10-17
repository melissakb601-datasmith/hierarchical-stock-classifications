import os
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import MinMaxScaler

# Gets the folder where StockGroup_HC.py lives
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "StockData.csv")

# Ensure .csv file is located in the same directory
print("--- Files found in this folder: ---")
print(os.listdir(current_dir))
print("----------------------------------")

# Dynamically read the stock labels from the first column
stock_labels = []
with open(file_path, "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        if row:  # Ensure the row isn't empty
            stock_labels.append(row[0])
pass    

# Load the numeric data (skipping the first column since it has strings)
# 'usecols' loads everything except column 0.
ccdata = np.loadtxt("StockData.csv", delimiter=",", skiprows=1, usecols=range(1, 5))

# Normalize data
mms = MinMaxScaler()
ccdata = mms.fit_transform(ccdata)

# Perform hierarchical clustering using the Ward method
linkage_matrix_stocks = linkage(ccdata, method="ward")

# Plot the dendrogram
plt.figure(figsize=(12, 6))  # Widened slightly to fit many labels cleanly

dendrogram(
    linkage_matrix_stocks,
    labels=stock_labels,  # Uses the dynamically generated list
    leaf_rotation=90,
    leaf_font_size=10,  # Helps with readability when you have 50+ stocks
)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Stocks")
plt.ylabel("Distance")
plt.tight_layout()  # Prevents labels from getting cut off at the bottom
plt.show()
