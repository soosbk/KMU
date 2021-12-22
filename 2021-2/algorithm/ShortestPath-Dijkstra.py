import sys


def dijstra(edge,n):
	touch=[1 for _ in range(n+1)]
	length=[edge[1][i] for i in range(n+1)]
	return_val=0
	for t in range(n-1):
		vnear=1
		min_num=sys.maxsize
		for i in range(2,n+1):
			if 0<=length[i]<min_num:
				min_num=length[i]
				vnear=i

		return_val+=edge[touch[vnear]][vnear]

		for i in range(2,n+1):
			if(length[vnear]+edge[vnear][i])<length[i]: 
				length[i]=length[vnear]+edge[vnear][i]
				touch[i]=vnear
		length[vnear]=-1

	return return_val







case_num=int(input())

for _ in range(case_num):
	return_val=0
	node=int(input())
	edge=[[sys.maxsize for _ in range(node+1)]for _ in range(node+1)]
	for n in range(1,node+1):
		s=list(map(int,input().split()))
		for t in range(1,s[1]+1):
			edge[n][s[t*2]]=s[t*2+1]
	

		
	print(dijstra(edge,node))

