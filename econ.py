import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from fredapi import Fred 

fred = Fred(api_key="e58d7eba2519edf715a1a1ab12fca02f")

unemploy = fred.get_series("UNRATE")
infl = fred.get_series("CPILFESL")

cpi_infl = infl.pct_change(periods=12) * 100

data = pd.DataFrame ( {
    "Unemployment": unemploy,
    "Inflation" : cpi_infl
}).dropna()

data = data.loc[data.index >= pd.Timestamp.today() - pd.DateOffset(years=20)]

x = data["Unemployment"].values
y = data["Inflation"].values

mask = ~np.isnan(x) & ~np.isnan(y)
x, y = x[mask], y[mask]

plt.scatter(x,y)
plt.title("Phillips Curve - USA")
plt.xlabel("Unemployment rate (%)")
plt.ylabel("Inflation rate (YoY %)")
plt.grid()
plt.show()

