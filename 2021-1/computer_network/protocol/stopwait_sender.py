# 소켓을 사용하기 위해서는 socket을 import해야 한다.
import socket
import random
import time
# 로컬은 127.0.0.1의 ip로 접속한다.
HOST = '127.0.0.1'
# port는 위 서버에서 설정한 9999로 접속을 한다.
PORT = 9999
SEQ_NUM=2
# 소켓을 만든다.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)

# connect함수로 접속을 한다.
client_socket.connect((HOST, PORT))


#send SEQUENCE NUMBER
NOW_ACK=0
msg=str(SEQ_NUM)
data=msg.encode()
length=len(data)
# server로 리틀 엔디언 형식으로 데이터 길이를 전송한다.
client_socket.sendall(length.to_bytes(4, byteorder="little"))
# 데이터를 전송한다.
client_socket.sendall(data)
np=0
while True:
	try:
			# 메시지는 hello로 보낸다.
			if np==0: msg = input(">>> input your msg: ")
			# 메시지를 바이너리(byte)형식으로 변환한다.
			if msg=="Quit": 
				client_socket.close()
				break

			while True:
				if(random.randint(1,10))>8: 
					print("LOST from SENDER")
					time.sleep(4)
					raise socket.timeout
					continue
				data = msg.encode();
				# 메시지 길이를 구한다.
				length = len(data)
				# server로 리틀 엔디언 형식으로 데이터 길이를 전송한다.
				client_socket.sendall(length.to_bytes(4, byteorder="little"))
				# 데이터를 전송한다.
				client_socket.sendall(NOW_ACK.to_bytes(4, byteorder="little"))
				client_socket.sendall(data)
				print("SENDING SUCCESS")
				break

			# server로 부터 전송받을 데이터 길이를 받는다.
			data = client_socket.recv(4)
			# 데이터 길이는 리틀 엔디언 형식으로 int를 변환한다.
			length = int.from_bytes(data, "little")
			# 데이터 길이를 받는다.
			data = client_socket.recv(length)
			# 데이터를 수신한다.
			msg = data.decode()
			# 데이터를 출력한다.
			if ((NOW_ACK+1)%2)==(int(msg[4:])%2): 
				print(msg[4:],"and NOW_ACK",NOW_ACK)
				print("Receive SUCCESS!")
				NOW_ACK+=1
			np=0

	
	except socket.timeout:
		print("timeout! \n Resending a MSG")
		np=1
client_socket.close();

