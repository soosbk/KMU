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

def list_to_dictionary(minterms):
	return_dict={}
	for minterm in minterms[2:]:
		return_dict[make_length(str(bin(minterm))[2:],int(minterms[0]))]=[minterm]

	return return_dict
 

def find_epi(pis): #pi={정수:[--1,-10]}
	value_to_key={}
	for key, pi in pis.items():
		for pi_value in pi:
			if pi_value not in value_to_key:
				value_to_key[pi_value] = [key]
			else:
				value_to_key[pi_value].append(key)
	epi_list=[]
	for new_key in value_to_key:
		if len(value_to_key[new_key])<=1: epi_list=epi_list+value_to_key[new_key]

	return epi_list


def solution(minterm):
	answer = []
	save_cnt_lastm=list_to_dictionary(minterm)  #{pi: [사용된 정수]}
	minterms_str=[make_length(str(bin(term))[2:],int(minterm[0])) for term in minterm[2:]] # 정수를 저장안하고 last pi 만 저장 (binary만)
	
	while len(minterms_str)>0:
		new_minterms=[]

		group=defaultdict(list)
		for i in range(len(minterms_str)):
			number_of_one=minterms_str[i].count("1")
			group[number_of_one].append(minterms_str[i]) #1의 개수:[리스트~]
		keylist=list(group.keys())
		
		if len(keylist)<=1: #이 경우엔, 따로 추가할 필요가 없어짐(epi에)-> 한 번도 활용 못하기 때문!
			for minterm_str in minterms_str:
				if minterm_str not in answer: answer.append(minterm_str)
			break
		check_cnts=set()
		for key in keylist:
			
			try:
				lists = [(left,right) for left in group[key] for right in group[key+1]]
			except:
				continue
			for left, right in lists:
				cnt,idx=one_different(left, right)
				if cnt!=1: continue
				else: 

					tmp_n="".join([left[:idx],"2",left[idx+1:]])
					save_cnt_lastm[tmp_n]=save_cnt_lastm[left]+save_cnt_lastm[right]
					check_cnts.add(left)
					check_cnts.add(right)
				if tmp_n not in new_minterms: new_minterms.append(tmp_n)
		for check_cnt in check_cnts:
			del save_cnt_lastm[check_cnt]

			minterms_str.remove(check_cnt)
				

		for minterm_str in minterms_str:
				if minterm_str not in answer: answer.append(minterm_str)
		
		minterms_str=new_minterms
	

	epi=find_epi(save_cnt_lastm)
	
	epi=list(set(epi))
	answer=list(set(answer))
	epi=[term.replace("2","-") for term in sorted(epi)]
	epi.insert(0,"EPI")
	answer=[term.replace("2","-") for term in sorted(answer)]+epi
	return answer

