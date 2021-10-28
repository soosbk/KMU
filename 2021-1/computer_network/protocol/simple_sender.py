# 소켓을 사용하기 위해서는 socket을 import해야 한다.
import socket
# 로컬은 127.0.0.1의 ip로 접속한다.
HOST = '127.0.0.1'
# port는 위 서버에서 설정한 9999로 접속을 한다.
PORT = 9999
# 소켓을 만든다.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect함수로 접속을 한다.
client_socket.connect((HOST, PORT))
# 10번의 루프로 send receive를 한다.
while True:
	# 메시지는 hello로 보낸다.
	msg = input(">>> input your message: 	");
	#Quit 이 입력되면 통신 종료

	data = msg.encode();
	# 메시지 길이를 구한다.
	length = len(data);
	# server로 리틀 엔디언 형식으로 데이터 길이를 전송한다.
	client_socket.sendall(length.to_bytes(4, byteorder="little"));
	# 데이터를 전송한다.
	client_socket.sendall(data);
	if msg=="Quit": 
		
		client_socket.close();
		break
	


