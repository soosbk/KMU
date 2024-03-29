# -*- coding: utf-8 -*-


#20192218 김수빈 컴퓨터네트워크  bit-stuffing / bit-unstuffing 통합파일 

#=============================

#bit - stuffing

'''
	1. output list 생성 (aft_bit_stuffing_list)
	2. 1이 나올 때 마다 count를 1씩 증가시킨다.
 	3. count가 5가 될 때마다 list에 0을 추가해준다.
 	4. list to str (aft_bit_stuffing_str)
 

'''


def bit_stuffing_fun(bit_stream):
	count=0 #count 1's num
	aft_bit_stuffing_list=[]
	for i in range(0,len(bit_stream)):
		aft_bit_stuffing_list.append(bit_stream[i])
		if bit_stream[i]=='0': count=0
		if bit_stream[i]=='1': count+=1
		if count==5:
			aft_bit_stuffing_list.append("0")
			count=0


		

	aft_bit_stuffing_str="".join(aft_bit_stuffing_list)
	
	return aft_bit_stuffing_str

#=============================

#bit - unstuffing



'''
	1. output list 생성 (aft_bit_unstuffing_list)
	2. 1이 나올 때 마다 count를 	1씩 증가 (0을 만나면 count는 0으로 초기화)
	3. count가 5가 될 때마다 list의 index 내장함수를 이용해 0을 삭제
	4. list to str (aft_bit_unstuffing_str)
	'''


def bit_unstuffing_fun(bit_stream):
	count=0 #count 1's num
	aft_bit_unstuffing_list=[]
	for i in range(0,len(bit_stream)):
		if count==5 and bit_stream[i]=='0': 
			count=0
			continue
		elif bit_stream[i]=='0': count=0
		elif bit_stream[i]=='1': count+=1
		aft_bit_unstuffing_list.append(bit_stream[i])
		

	aft_bit_unstuffing_str="".join(aft_bit_unstuffing_list)

	return aft_bit_unstuffing_str

def main():
	input_stream=input(">>> bit stream을 입력하세요: ") # input bit string (type: str)

 
	print("\n>> 입력한 Frame: ",input_stream)  #echo checking
	print("\n>> bit-stuffing을 실행합니다.")
	aft_bit_stuffing=bit_stuffing_fun(input_stream)
	print(">> after bit-stuffing: ", aft_bit_stuffing) #echo checking
	print("\n>> bit-unstuffing을 실행합니다.")
	aft_bit_unstuffing=bit_unstuffing_fun(aft_bit_stuffing) 
	print("\n>> after bit-unstuffing: ", aft_bit_unstuffing) #echo checking


	#성공 check!
	if(aft_bit_unstuffing==input_stream): print("\n>> Success!\n")
	else: print("\nFailed.. T.T\n")

if __name__ == "__main__":
	main()
