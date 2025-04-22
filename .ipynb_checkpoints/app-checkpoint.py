import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# Load dataset
file_path = "DatasetSIH1647.csv"
df = pd.read_csv(file_path)
df.set_index('Commodities', inplace=True)
df = df.T
df.index = pd.date_range(start='2014', periods=len(df), freq='Y')  
df = df.ffill()

# List available commodities
commodities = df.columns.tolist()

@app.route("/", methods=["GET", "POST"])
def index():
    forecast_df = None
    selected_commodity = None
    forecast_path = None
    train_rmse = None

    if request.method == "POST":
        selected_commodity = request.form["commodity"]
        data = df[selected_commodity]

        # Train SARIMA model
        model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 0, 12))
        sarimax_model = model.fit(disp=False)

        # Forecast for next 5 years
        forecast = sarimax_model.get_forecast(steps=5)
        forecasted_values = forecast.predicted_mean
        forecast_years = pd.date_range(start='2025', periods=5, freq='Y')

        forecast_df = pd.DataFrame({
            "Year": forecast_years.strftime("%Y"),
            "Forecasted Price": forecasted_values
        })

        # Save forecast plot
        plt.figure(figsize=(10, 6))
        plt.plot(data, label=f'Actual {selected_commodity} Prices')
        plt.plot(forecast_years, forecasted_values, label='Forecasted Prices', color='orange')
        plt.xlabel('Year')
        plt.ylabel('Price')
        plt.title(f'{selected_commodity} Price Forecast (2025-2029)')
        plt.legend()
        plot_path = "static/forecast.png"
        plt.savefig(plot_path)
        plt.close()

        # Calculate RMSE for evaluation
        train_rmse = np.sqrt(((data - sarimax_model.fittedvalues) ** 2).mean())

    return render_template("index.html", commodities=commodities, forecast_df=forecast_df,
                           selected_commodity=selected_commodity, train_rmse=train_rmse, plot_path="forecast.png")


if __name__ == "__main__":
    app.run(debug=True)
