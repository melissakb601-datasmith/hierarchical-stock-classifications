# Portfolio Diversification using Hierarchical Clustering

Unsupervised machine learning pipeline utilizing hierarchical clustering to classify equities based on financial metrics and price dynamics.

## 📌 Overview
This project applies unsupervised machine learning to stock market data to group visually and statistically similar assets. By implementing **Hierarchical Clustering**, the system analyzes patterns in price movements, volatility, and sector behavior to generate diversified portfolio recommendations **without relying on pre-labeled outcomes**.


**Key Project Stages**

* **Automated Data Extraction:** Leverages Google Sheets and the `GOOGLEFINANCE` function to continuously collect real-time stock information and performance metrics.
* **Hierarchical Clustering:** Applies unsupervised learning to construct a dendrogram matrix, mapping out performance patterns and earnings profiles to calculate asset similarity.
* **Portfolio Diversification:** Identifies structural cuts in the dendrogram to isolate unique asset clusters, allowing users to select uncorrelated stocks and minimize risk.

---

## 🎯 Objectives
- **Unsupervised Asset Grouping:** Implements hierarchical clustering to discover relationships between stocks based on historical market behavior.
- **Analyze behavioral and financial indicators** to understand drivers of default.
- **Demonstrate a full machine‑learning workflow** from preprocessing to evaluation.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Numpy, Scikit-Learn, SciPy, Matplotlib
- **Tools:** GitHub for version control and documentation  

---

## 📂 Repository Structure
```text
Credit-Default-SVM
│── /code        # Python scripts for unsupervised machine learning
│── /data        # Google Sheets
│── /visuals     # Dendogram, screenshots
│── README.md
```

---

# 📸 Dashboard Preview

## Google Sheets Screenshot
![Visual Screenshot](visuals/CCdatasample.png)

## Dendogram Output
![Visual Screenshot](visuals/SVMcode.png)



---

# 📥 How to Use
1. **Clone** or download this repository.
2. **Open** the project files in your Python environment.
3. **Edit** the ccdefault_SVM.py file to include the path to the ccdata file on your local machine.
3. **Run** the Python program to generate predictions and view outputs.
