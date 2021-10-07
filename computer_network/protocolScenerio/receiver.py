# 소켓을 사용하기 위해서는 socket을 import해야 한다.
import socket
import random
import time
from multiprocessing import Process, Pipe
#user-defined module
import function_zip as f
right_stream='1111000011110000'
PORT=9999
def Application_layer(conn):
	
	print("(S1)<Start: Application_layer>")
	stream=conn.recv()
	#conn.close()
	#checking
	print("Received_stream: ",stream)

	print("Check stream !=====")

	if stream==right_stream:
		print("SUCCESS")
		conn.send("SUCCESS")
	else: pass
	print("(S1)<End: Application_layer>\n\n")
	conn.close()


def Transport_layer(conn):
	NOW_STATE=True
	#print("Network -> Transport")
	print("(S1)<Start: Transport_layer>")
	#try:
	while True:
		stream=conn.recv()

		#checking
		print("Transport - stream: ",stream)
		print("MAke ACK MSG")
		ACK_MSG='ACK'
		NOW_STATE=False
		#Transport -> App
		Trans_conn,App_conn=Pipe()
		print("Transport -> Application")
		print("Sending Stream [{}] to Application_layer".format(stream))
		Trans_conn.send(stream)
		R5 = Process(target=Application_layer, args=(App_conn,))
		R5.start()
		print("(S1)<End: Transport_layer>\n\n")
		
		inv_stream=Trans_conn.recv()
		print("===== start Scenario 2 =====")
		print("(S2)<Start: Transport_layer>")

		#통신 성공하면 Application은  'ACK' msg를 보내기로 함
		if inv_stream=="SUCCESS":
			NOW_STATE=False
		if (NOW_STATE==False) and (ACK_MSG=='ACK'):
			sending_stream=f.making_bitstream('ACK')
			print("Sending Stream [{}] to Network_layer".format(sending_stream))
			print("Transport -> Network")
			conn.send(sending_stream)
			print("(S2)<END: Transport_layer>\n\n")
			NOW_STATE=True
			conn.close()
			break


	


def Network_layer(conn):
#bypass
	#print("Datalink -> Network")

	print("(S1)<Start: Network_layer>")
	stream=conn.recv()
	#checking
	print("Network - stream: ",stream)

	#Network -> Datalink
	Net_conn, Trans_conn = Pipe()
	print("Network -> Transport")

	print("Sending Stream [{}] to Trasport_layer".format(stream))
	Net_conn.send(stream)

	R4 = Process(target=Transport_layer, args=(Trans_conn,))
	R4.start()
	
	print("(S1)<End: Network_layer>\n\n")


	inv_stream=Net_conn.recv()

	print("(S2)<Start: Network_layer>")
	print("Receiving Stream [{}] from Transport_layer".format(inv_stream))
	print("Network -> Datelink")
	conn.send(inv_stream)
	print("(S2)<End: Network_layer>\n\n")

	conn.close()


def Datalink_layer(conn):
	#print("Physical -> Datalink")
	print("(S1)<Start: Datalink_layer>")
	stream=conn.recv()

	#checking
	print("Datalink - stream: ",stream)

	#bitunstuffing
	aft_bitunstuff_stream=f.bit_unstuffing_fun(stream)
	print("Aft Bit unstuffing:[{}]".format(aft_bitunstuff_stream))
	
	#Datalink(DLC-> MAC)
	mac_stream=aft_bitunstuff_stream

	#Datalink -> Network
	Data_conn, Net_conn = Pipe()
	print("Network -> Datalink using simple protocol")


	print("Sending Stream [{}] to Network_layer".format(mac_stream))
	Data_conn.send(mac_stream)

	R3 = Process(target=Network_layer, args=(Net_conn,))
	R3.start()
	print("(S1)<End: Datalink_layer>\n\n")


	inv_stream=Data_conn.recv()

	print("(S2)<Start: Datalink_layer>")
	print("Receiving Stream [{}] from Network_layer".format(inv_stream))
	#bitstuffing
	aft_bitstuff_stream=f.bit_stuffing_fun(inv_stream)
	print("Aft Bit stuffing:[{}]".format(aft_bitstuff_stream))
	
	print("Sending to MAC sub layer using simple protocol")
	#Datalink(DLC-> MAC)
	print("DLC sub layer -> MAC sub layer")
	mac_stream=aft_bitstuff_stream

	print("Datalink -> Physical")
	print("Sending Stream [{}] to Physical_layer".format(mac_stream))
	conn.send(f.CSMA_CD(mac_stream))
	print("(S2)<End: Datalink_layer>\n\n")

	conn.close()


def Physical_layer(conn):
	#print("Receiver(main) -> Physical")

	print("(S1)<Start: Physical_layer>")
	stream=conn.recv()

	#checking
	print("Physical - stream: ",stream)

	#Re-MLT-3
	sending_stream=f.DE_MLT_3(stream)
	print("Aft Reverse MLT-3:[{}]".format(sending_stream))
	#Physical -> aft
	Phy_conn, Data_conn = Pipe()
	print("Physical -> Network")

	print("Sending Stream [{}] to  Datalink_layer".format(sending_stream))
	

	Phy_conn.send(sending_stream)

	R2 = Process(target=Datalink_layer, args=(Data_conn,))
	R2.start()
	#p4.join()
	#conn.close()
	print("(S1)<End: Physical_layer>\n\n")


	inv_stream=Phy_conn.recv()

	print("(S2)<Start: Physical_layer>")
	print("Receiving Stream [{}] from Datalink_layer".format(inv_stream))
	print("Physical -> Receiver")

	#MLT-3
	sending_stream=f.EN_MLT_3(inv_stream)
	print("Aft MLT-3:[{}]".format(sending_stream))
	
	conn.send(sending_stream)
	print("(S2)<End: Physical_layer>\n\n")
	conn.close()



if __name__ == '__main__':
	
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 소켓 레벨과 데이터 형태를 설정한다.
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# 서버는 복수 ip를 사용하는 pc의 경우는 ip를 지정하고 그렇지 않으면 None이 아닌 ''로 설정한다.
	# 포트는 pc내에서 비어있는 포트를 사용한다. cmd에서 netstat -an | find "LISTEN"으로 확인할 수 있다.


	server_socket.bind(('', PORT))
	# server 설정이 완료되면 listen를 시작한다.
	server_socket.listen()
	try:
		client_socket, addr = server_socket.accept();
		print("I'm RECEIVER! LETs GO!\n\n")
		# socket의 recv함수는 연결된 소켓으로부터 데이터를 받을 대기하는 함수입니다. 최초 4바이트를 대기합니다.
		data = client_socket.recv(4);
		# 최초 4바이트는 전송할 데이터의 크기이다. 그 크기는 little 엔디언으로 byte에서 int형식으로 변환한다.
		length = int.from_bytes(data, "little");
		# 다시 데이터를 수신한다.
		data = client_socket.recv(length);
		# 수신된 데이터를 str형식으로 decode한다.
		input_stream = data.decode();
		# 수신된 메시지를 콘솔에 출력한다.


		
		
		print("Received stream: ",input_stream)

		# Receiver -> Physical
		Rec_conn, Phy_conn = Pipe()
		print("\n\n(S1) Receiver Start!")
		print("Receiver -> Physical")

		print("Sending Stream [{}] to  Physical".format(input_stream))
		Rec_conn.send(input_stream)

		R1 = Process(target=Physical_layer, args=(Phy_conn,))
		R1.start()



		#========
		inv_stream=Rec_conn.recv()
		print("\n\n<SENDING TO SENDER>")
		print("{} stream을 sender에게 전송합니다.".format(inv_stream))
		data = inv_stream.encode();
		# 메시지 길이를 구한다.
		length = len(data)
		# server로 리틀 엔디언 형식으로 데이터 길이를 전송한다.
		client_socket.sendall(length.to_bytes(4, byteorder="little"))
		# 데이터를 전송한다.
		client_socket.sendall(data)
		print("(S2) Receiver End\n\n")

		


	
	except:
		print("server")
	finally:
		# 에러가 발생하면 서버 소켓을 닫는다.
		server_socket.close()
