coinsUsed=[0]*1001
lastCoin=[0]*1001


def coinExchange(coins,numDiffCoins,change):
	#coinsUsed=C, lastCoin=L
	global coinsUsed
	global lastCoin
	coinsUsed[0]=0
	lastCoin[0]=0

	for cents in range(1,change+1):
		minCoins=cents
		newCoin=1

		for j in range(0,numDiffCoins):
			
			if coins[j]>cents: continue
			if coinsUsed[cents-coins[j]]+1<minCoins:
				minCoins=coinsUsed[cents-coins[j]]+1
				newCoin=coins[j]
				
		coinsUsed[cents]=minCoins
		lastCoin[cents]=newCoin

t=int(input())
for i in range(t):
	money=int(input())
	in_p=list(map(int, input().split()))
	diff_num=in_p[0]
	coin=in_p[1:diff_num+1]
	coinExchange(coin,diff_num,money)
	print(coinsUsed[money])


