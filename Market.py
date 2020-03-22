
from OrderManeger import Orders

class Market:
	def __init__(self,marketName,marketData):
		self.activeOrders=list()
		self.marketName=marketName
		self.marketTick=0
		self.simulationEnded=False
		self.data = marketData
		self.dataLen=len(marketData)-1

	def orderCreate(self,action,lot,stopLoss,takeProfit):
		orderID=self.marketTick
		order=Orders(self.getCurrentMarketData(),action,lot,stopLoss,takeProfit,orderID)
		self.activeOrders.append(order)
		return orderID

	def getCurrentMarketData(self):	
		return self.data[self.marketTick]

	def getTotalMarketData(self):
		return self.data
	
	def closeOrder(self,orderID):
		moneyDiff=0
		currentValue=self.getCurrentMarketData()
		for order in self.activeOrders:
			if orderID==order.orderID:
				moneyDiff=moneyDiff + order.closeOrder(currentValue)
				self.deleteClosedOrder(order)
		return moneyDiff

	def closeAllOrders(self):
		moneyDiff=0
		currentValue=self.getCurrentMarketData()
		for order in self.activeOrders:
			moneyDiff=moneyDiff + order.closeOrder(currentValue)
			self.deleteClosedOrder(order)
		return moneyDiff
	
	def inceraseSelfTick(self):
		if self.marketTick<self.dataLen:
			self.marketTick=self.marketTick+1
		else:
			self.endSimulation()

	def marketTickReturnResult(self):
		totalMoneyDiff=0
		currentValue=self.getCurrentMarketData()
		for order in self.activeOrders:
			moneyDiff=order.checkIfReadyToClose(currentValue) 	
			if moneyDiff is not None:
				self.deleteClosedOrder(order)
				totalMoneyDiff=totalMoneyDiff+moneyDiff
		self.inceraseSelfTick()
		if self.simulationEnded==False:
			return totalMoneyDiff
		else:
			return 0

	def endSimulation(self):
		self.simulationEnded=True

	def deleteClosedOrder(self,order):
		self.activeOrders.remove(order)
		
