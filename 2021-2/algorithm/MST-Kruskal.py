def find(a,parent):
	while parent[a]>0:
		if a==parent[a]: break
		else: a=parent[a]
	root=a
	return root 


case_num=int(input())

for _ in range(case_num):
	return_val=0
	node=int(input())
	parent={v:v for v in range(node+1)}
	rank={v:0 for v in range(node+1)}
	edge=[]
	for n in range(1,node+1):
		s=list(map(int,input().split()))
		for t in range(1,s[1]+1):
			edge.append((s[t*2+1],n,s[t*2]))
	edge.sort()

	for e in edge:
		w,s,e=e

		root_s=find(s,parent)
		root_e=find(e,parent)
		if root_s!=root_e:
			if rank[root_s]>rank[root_e]: parent[root_e]=root_s
			else:
				parent[root_s]=root_e
				if rank[root_s]==rank[root_e]: rank[root_e]+=1
			return_val+=w

	print(return_val)
    
