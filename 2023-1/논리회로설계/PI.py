from collections import defaultdict

def make_length(binary,cnt):
	return ''.join(['0'*(cnt-len(binary)),str(binary)])



def one_different(a,b):
	count_lst=[0,-1]
	for i in range(0,len(a)):
		if a[i]!=b[i]: 
			count_lst[0]+=1
			count_lst[1]=i

	return count_lst



def solution(minterm):
	answer = []
	minterms_str=[make_length(str(bin(term))[2:],int(minterm[0])) for term in minterm[2:]]
	
	while len(minterms_str)>0:
		new_minterms=[]
		group=defaultdict(list)
		for i in range(len(minterms_str)):
			number_of_one=minterms_str[i].count("1")
			group[number_of_one].append(minterms_str[i])
		
		keylist=list(group.keys())
		if len(keylist)<=1: 
			for minterm_str in minterms_str:
				if minterm_str not in answer: answer.append(minterm_str)
			break

		for key in keylist:
			try:
				lists = [(left,right) for left in group[key] for right in group[key+1]]
			except:
				continue
			for left, right in lists:
				cnt,idx=one_different(left, right)
				if cnt!=1: continue
				else: 
					if left in minterms_str: 
						minterms_str.remove(left)
					if right in minterms_str:
						minterms_str.remove(right)

					tmp_n="".join([left[:idx],"2",left[idx+1:]])
					if tmp_n not in new_minterms: new_minterms.append(tmp_n)
					

		for minterm_str in minterms_str:
				if minterm_str not in answer: answer.append(minterm_str)
		
		minterms_str=new_minterms
	answer=list(set(answer))
	answer=[term.replace("2","-") for term in sorted(answer)]
	return answer

