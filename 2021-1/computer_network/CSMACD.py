
'''
 20192218 김수빈 CSMA/CD python 구현
 이용 persistence: one-persistence 
 
 '''

from tabulate import tabulate
import random
import time

#전역변수로 선언
busy=False #persistence 함수에서 busy 저장
Success=False #Transmission done 저장
Abort=False #limit 횟수까지 성공하지 못했을 때
Collision=True #Collision detected 저장		
table=[]
K=0
''' <table>
	# one-persistence
	# one-persistence의 sence 저장
	# Frame 전송여부
	# Collision
	# Jamming signal
	# R
	'''


#one-persistent 함수 -> busy or idle 인 상태를 random하게 받음
def one_p():
	global count
	global table
	table[K].append("one-persistence")
	global busy 
	i=1 # 몇번 sence했는지 저장
	while True:
		i+=1
		random.seed(time.time()) #seed값을 다르게 주어 랜덤한 상태 유지
		busy=random.choice([True, False])
		if busy==False: break #idle
	table[K].append(i)



#Collision함수 (throughput=50%)
def Collision_f():
	global Collision
	counter=random.randint(1,10) #홀수: transmission done
	if counter%2!=0: Collision=False #transmission done




'''
	abort=false이면 계속 진행 -> 시도횟수가 초과되면 true로 변환
	Success: busy=False -> Collision=False and K<Limit
	'''
#시뮬레이션 함수
def simulate(Limit):
	global Success
	global Abort
	global Collision
	global table
	jam=True
	global K
	R=0
	Tb=0
	Tp=5  #fix
	Tfr=6 #fix
	while((Abort==False) and K<Limit):
		table.append([K+1])
		
	  #Abort=False일때 while loop
		print("Attemp " , (K + 1) , ":")
		random.seed(time.time())
		one_p()
		if not(busy): #idle check
			"Data packet was sent, waiting for acknowlegement ..."
			table[K].append("Sent")
			Collision_f()
			table[K].append(Collision)
			if not(Collision): #transmission done 
				Success=True
				jam=False #False면 다른 기기는 전송금지!
		table[K].append(jam)
		if (K<Limit) and (Success==True): 
			print("Transmission done...")
			table[K].append("NA")
			return 1

		else:
			print("Collision detected...")
			print("Send a Jamming signal!")
			K+=1
			print("K:", K)
			if K>Limit: #Abort
				Abort=True
				return 0

			print("Choose a random number R")
			random.seed(time.time())
			R=random.randint(0,pow(2, K)-1)
			table[K-1].append(R)
			random.seed(time.time())
			n=random.choice([True, False]) 
			
			#0이면 RxTp
			if n: Tb=R*Tfr
			else: Tb=R*Tp
			
			print("Waiting the TB timer to expire and to start a new attemp ...")
			time.sleep(n)

		print("\n\n")


#main 함수
def main():
	print("Enter the maximum number of attemps, between 5 and 15")
	Limit=int(input("Enter: "))
		
	#simulate 함수 호출
	counter=simulate(Limit)
	if counter: print("The attemp was successful.")
	else: print("The whole process was aborted. We need to try another time.")
	

	#table 출력
	print("\n")
	print(tabulate(table, headers=["Attemp", "Persistence", "Sence","Frame","Collision","Jamming","R"]))
	print("\n")



if __name__ == '__main__': main()
	
				
			



