import random
import time

def bit_stuffing_fun(bit_stream):
	print("Start bit_stuffing")
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


def bit_unstuffing_fun(bit_stream):
	print("Start bit_unstuffing")
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


def EN_MLT_3(bit_stream):
	print("Start MLT-3 scheme")
	default=1  # save last nonzero level
	now='0' # save current level
	output="" # save output string

	# At the beginning
	if bit_stream[0]=='0': #no transition
		output+='0'
		default=-1

	else: 
		output+='+'
		now='+'
	#=============================


	# On-running	
	for i in range(1,len(bit_stream)): 
		if bit_stream[i]=='0': pass
		else: # next bit is 1
			if now!='0': now='0'
			else: #now=0
				if  default>0: now='-'
				else: 
					now='+'
				default*=-1
		output+=now

	return output

#=============================
#MLT-3 DEcoding

def DE_MLT_3(bit_stream):
	print("Start Reverse MLT-3 scheme")
	aft_bitstream=""
	
	# At the beginning
	if bit_stream[0]=='+': aft_bitstream+='1'
	else: aft_bitstream+='0'

	#=============================


	# On-running
	for i in range(1,len(bit_stream)):
		if(bit_stream[i-1]=='0'):
			if bit_stream[i]=='0': aft_bitstream+='0'
			else: aft_bitstream+='1'
		else:
			if bit_stream[i]=='0': aft_bitstream+='1'
			else: aft_bitstream+='0'

		

	return aft_bitstream
#============================



#bit-stuffing -> MLT-3 (sender)->MLT-3 (receiver)-> bit-unstuffing
#test bit stream: 0001111111001111101000
#=============================




Limit=100 #이상적인 상황 가정
K=0 #시도 횟수
def CSMA_CD(input_stream):
	print("Start CSMA_CD")
	busy=False #persistence 함수에서 busy 저장
	Success=False #Transmission done 저장
	Abort=False #limit 횟수까지 성공하지 못했을 때
	Collision=True #Collision detected 저장		
	global Limit
	global K



	#one-persistence
	while True:
		busy=random.choice([True, False])
		if busy==False: 
			print("Data packet was sent, waiting for acknowlegement ...")
			break #idle

	#collision
	while True:	
		counter=random.randint(1,10) #홀수: transmission done
		if counter%2!=0: #transmission done
			Collision=False 
			break


	while((Abort==False) and K<Limit):
		
		
	  #Abort=False일때 while loop
		print("Attemp " , (K + 1) , ":")
		if not(busy): #idle check
			if not(Collision): #transmission done 
				Success=True
				jam=False #False면 다른 기기는 전송금지!
		if (K<Limit) and (Success==True): 
			print("Transmission done...")
			print("The attemp was successful.")
			return input_stream

		else:
			print("Collision detected...")
			print("Send a Jamming signal!")
			K+=1
			print("K:", K)
			if K>Limit: #Abort
				Abort=True
				print("The whole process was aborted. We need to try another time.")

			print("Choose a random number R")
			R=random.randint(0,pow(2, K)-1)
			random.seed(time.time())
			n=random.choice([True, False]) 
			
			#0이면 RxTp
			if n: Tb=R*Tfr
			else: Tb=R*Tp
			
			print("Waiting the TB timer to expire and to start a new attemp ...")
			time.sleep(n)

		print("\n\n")



def making_bitstream(ascii_str):
	out_stream=""
	for i in range(0,len(ascii_str)):
		n=ord(ascii_str[i])
		s=""
		while True:
			if n==0: break
			s=str(n&0x01)+s
			n=n>>1
		#if len(s)<8: s="0"*(8-len(s))+s
		out_stream+=s

	return out_stream



