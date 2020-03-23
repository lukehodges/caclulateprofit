items = {
'toiletroll' : {
   'cost_price' : 0.50,
   'sell_price' : 5.00, 
   'inventory' : 500
},
'apple' : {
  'cost_price' : 0.10,
  'sell_price' : 0.50,
  'inventory' : 100
 },
'banana' : {
  'cost_price' : 0.50,
  'sell_price' : 0.70,
  'inventory' : 120
 }
}

def finditem(A,Dic):
	if A in Dic:
		return True
	else:
		return False
def calculate_profit(A,Dic):
	item = Dic[A]
	cost = item['cost_price']
	sell = item['sell_price']
	inventory = item['inventory']
	profit = sell - cost
	profit = profit * inventory
	profit = round(profit,3)
	return profit
while 1:
	item = input('enter the item to calculate the total profit\n> ')
	if finditem(item,items):
		print('item found')
		print(item + ' : ' + str(calculate_profit(item,items)))
		repeat = input('do you want another item?\n> ').upper()
		if repeat == 'NO' or repeat == 'N':
			break 
