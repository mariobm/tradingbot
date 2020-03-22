import pandas as pd
from Account import Account
import matplotlib.pyplot as plt 

data2=pd.read_csv("EURUSD.csv")
data2=data2['Close'].values[:]
a1=Account(1000,100)
a1.createMarket("EURUSD",data2)
tick=0
datalen=len(data2)
while True:
	currentVal1=a1.getCurrentMarketData("EURUSD")

	analyse()

	ended=a1.MarketTick()
	tick=tick+1
	if ended==True:
		a1.closeAllOrders(marketName="EURUSD")
		break	

print(str(a1.getBalance()))

plt.plot(range(len(data2)),data2)
plt.show()

plt.plot(range(len(data)),data)
plt.show()

def analyse:
	pass