import pandas as pd
import matplotlib.pyplot as plt

# gets average of ONLY price column
# read file
df = pd.read_csv("CSVs/B0769MFR7L.csv")
avgPrice = round(df['Price'].mean(), 2)
hPrice = round(df['Price'].max(), 2)
lPrice = round(df['Price'].min(), 2)

print(avgPrice)
print(hPrice)
print(lPrice)

# ------------- plot section ---------------

# set axis
x = df["Date"]
y = df["Price"]

# displays graph
plt.title('Item Price Over Time')
plt.xlabel('Date')
plt.xticks(rotation=90, fontsize=8)
plt.ylabel('Price')
plt.plot(x, y)
plt.show()
# ------------- plot section ---------------
