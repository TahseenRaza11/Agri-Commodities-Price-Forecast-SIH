# 🌾 Agri Price Predictor using SARIMAX

This project is built for the Smart India Hackathon (SIH) and predicts future prices of key agricultural commodities in India using historical data from 2014 to 2024. The model uses the **SARIMAX** (Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors) approach for time series forecasting.

## 📊 Problem Statement

Price fluctuations of essential agri-commodities affect both farmers and consumers. The aim of this project is to forecast the prices of essential food grains and oils like:
- Rice
- Wheat & Atta
- Pulses (Tur, Urad, Moong, Masoor, Gram Dal)
- Edible Oils (Groundnut, Mustard, Vanaspati)

Forecasting helps:
- Policymakers in regulating Minimum Support Prices (MSP)
- Farmers in planning crop cycles
- Consumers in managing monthly expenditure

---

## 🧠 Technologies Used

- Python 🐍
- **SARIMAX** (from `statsmodels`)
- Pandas & Numpy for data preprocessing
- Matplotlib & Seaborn for visualization
- **Streamlit** for web interface
- **Render** for cloud deployment
- GitHub for version control

---

## 🗃️ Dataset

The dataset contains average yearly retail prices (in ₹/kg or ₹/litre) of key commodities from **2014 to 2024**. It includes:

| Year | Rice | Wheat | Gram Dal | Tur Dal | Urad Dal | Moong Dal | Mustard Oil | Groundnut Oil | Vanaspati |
|------|------|-------|----------|---------|----------|-----------|--------------|----------------|------------|
| 2014 | 27.91| 21.64 | 47.26    | 71.79   | 72.20    | 87.80     | 97.47        | 120.38         | 76.71      |
| ...  | ...  | ...   | ...      | ...     | ...      | ...       | ...          | ...            | ...        |

---

## 📈 Forecasting Approach

- Data cleaned and structured in time series format
- Each commodity trained separately using **SARIMAX**
- Model parameters selected based on AIC and residual analysis
- Forecasts for **upcoming years** displayed with interactive graphs

---

## 🚀 Deployment

- Built using **Streamlit** and deployed using **Render**
- Accessible via web interface with drop-down to select commodity
- Real-time forecasting with confidence intervals

---

## 🔗 Live Demo

[🔗 Click here to try the app (Hosted on Render)]([https://your-render-app-link](https://pblproject-9mga.onrender.com/))

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/your-username/Agri-Price-Predictor-SIH.git
cd Agri-Price-Predictor-SIH
pip install -r requirements.txt
streamlit run app.py
