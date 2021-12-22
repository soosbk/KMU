time=int(input())

for i in range(time):
	s1,s2=map(str,input().split())
	l1=len(s1)+1
	l2=len(s2)+1
	L=[[0]*l2 for j in range(l1)]

	for j in range(1,l1):
		for k in range(1,l2):
			if s1[j-1]==s2[k-1]:
				L[j][k]=L[j-1][k-1]+1

			else:
				if L[j][k-1]<L[j-1][k]: L[j][k]=L[j-1][k]
				else: L[j][k]=L[j][k-1]

	print(L[l1-1][l2-1])
