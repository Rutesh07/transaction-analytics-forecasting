
import pandas as pd
from prophet import Prophet
import os
import matplotlib.pyplot as plt

# Load cleaned transaction data
df = pd.read_csv('outputs/tables/cleaned_data.csv')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Aggregate daily sales
daily_sales = df.groupby('InvoiceDate')['TotalPrice'].sum().reset_index()
daily_sales.columns = ['ds', 'y']

# Fit Prophet model
model = Prophet()
model.fit(daily_sales)

# Create future dataframe and forecast
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# Save forecast table
os.makedirs('outputs/tables', exist_ok=True)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('outputs/tables/forecast_90_days.csv', index=False)

# Save forecast plot
fig = model.plot(forecast)
os.makedirs('outputs/charts', exist_ok=True)
fig.savefig('outputs/charts/sales_forecast.png')

# Save seasonality/trend components
fig2 = model.plot_components(forecast)
fig2.savefig('outputs/charts/forecast_components.png')
