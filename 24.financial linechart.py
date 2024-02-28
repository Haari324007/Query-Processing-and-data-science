import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2016-10-03', end='2016-10-07'),
    'Open': np.random.rand(5) * 100,
    'High': np.random.rand(5) * 100,
    'Low': np.random.rand(5) * 100,
    'Close': np.random.rand(5) * 100
}

df = pd.DataFrame(data)

df.set_index('Date', inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Open'], label='Open', color='blue', marker='o')
plt.plot(df.index, df['High'], label='High', color='green', marker='o')
plt.plot(df.index, df['Low'], label='Low', color='red', marker='o')
plt.plot(df.index, df['Close'], label='Close', color='purple', marker='o')
plt.title('Sample Stock Prices (Oct 3, 2016 - Oct 7, 2016)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

