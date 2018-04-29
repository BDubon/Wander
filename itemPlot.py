import pandas as pd
import matplotlib.pyplot as plt

prices = []

# gets average of ONLY price column
'''with open("B007TY6MK2.csv") as file:
    for line in file:
        prices.append(line[21:26])

prices.pop(0)
prices = list(map(float, prices))
# print(prices)

# max, min, and avg
max_value = max(prices)
min_value = min(prices)
avg_value = sum(prices)/len(prices)
print(max_value)
print(min_value)
print(avg_value)'''
# read file
df = pd.read_csv("B007TY6MK2.csv")
avgscore = df['Price'].mean()
hscore = df['Price'].max()
lscore = df['Price'].min()

print(avgscore)
print(hscore)
print(lscore)


# ------------- plot section ---------------


# set axis
x = df["Date"]
y = df["Price"]

# displays graph
plt.title('Item price over time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.plot(x, y)
plt.show()
# ------------- plot section ---------------
