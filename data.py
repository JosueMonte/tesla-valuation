import yfinance as yf

# Descargar datos de Tesla
tsla = yf.Ticker("TSLA")

# Datos históricos (últimos 5 años)
hist = tsla.history(period="5y")
print(hist.head())  # Muestra las primeras filas: Open, High, Low, Close, Volume
