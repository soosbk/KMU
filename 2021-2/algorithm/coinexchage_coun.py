MAX_COINS=11
MAX_CHANGE=1001
N=[[0]*(MAX_CHANGE+1) for i in range(MAX_COINS+1)]


def CountcoinExchange(coins,numDiffCoins,change):
	global N
	N[MAX_COINS][MAX_CHANGE]=0

	#base case
	for i in range(0,numDiffCoins+1): N[i][0]=1
	for i in range(1,change+1): N[0][i]=0
	
	for i in range(0,numDiffCoins):
		for j in range(1,change+1):
			#base case
			if j-coins[i]<0: numComb=0
			#recursive case
			else: numComb=N[i][j-coins[i]]
			N[i][j]=N[i-1][j]+numComb
			 
	return N[numDiffCoins-1][change]

t=int(input())
for i in range(t):
	money=int(input())
	in_p=list(map(int, input().split()))
	diff_num=in_p[0]

	coin=in_p[1:diff_num+1]
	ans=CountcoinExchange(coin,diff_num,money)
	print(ans)

