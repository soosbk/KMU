# 소켓을 사용하기 위해서는 socket을 import해야 한다.
import socket
import random
import time
from multiprocessing import Process, Pipe

#user-defined module
import function_zip as f

HOST = '127.0.0.1'
	# port는 위 서버에서 설정한 9990로 접속을 한다.
PORT = 9999



def Application_layer(conn):
	print("(S1)<Start: Application_layer>")
	stream=conn.recv()
    #conn.close()
    #checking
	print("input_stream: ",stream)

    #Application -> Transport
	App_conn, Trans_conn = Pipe()
	print("Application -> Transport")

	print("Sending Stream [{}] to Transport_layer".format(stream))
	App_conn.send(stream)
	p2 = Process(target=Transport_layer, args=(Trans_conn,))
	p2.start()
	#p2.join()
	print("(S1)<End: Application_layer>\n\n")

	inv_stream=App_conn.recv()
	print("(S2)<Start: Application_layer>")
	
	if(inv_stream=="1111000011110000"): last_stream="SUCCESS"
	print("Receiving Stream [{}] from Transport_layer".format(last_stream))
	print("Application -> user")
	conn.send(last_stream)
	print("(S2)<End: Application_layer>\n\n")

	conn.close()


def Transport_layer(conn):
	NOW_STATE=True
	#print("Application -> Transport")
	print("(S1)<Start: Transport_layer>")
	stream=conn.recv()

	#checking
	print("Transport - stream: ",stream)

	#Transport -> Network
	Trans_conn,Net_conn=Pipe()

	print("Transport -> Network")
	print("Sending Stream [{}] to Network_layer by Stop and Wait".format(stream))
	
	#stop and wait
	#try:
	while True:
		try:
			if(random.randint(1,10))>8: 
				print("LOST from SENDER")
				time.sleep(2)
				raise socket.timeout
				continue

		except socket.timeout:
			print("timeout! \n Resending a MSG")
		
		Trans_conn.send(stream)
		NOW_ACK='ACK'
		p3 = Process(target=Network_layer, args=(Net_conn,))
		p3.start()
		print("SENDING SUCCESS")
		print("WAITING ACK....")
		NOW_STATE=False  #waiting 상태
		print("(S1)<End: Transport_layer>\n\n")


		inv_stream=Trans_conn.recv()
		if inv_stream=='1111000011110000': NOW_STATE=True

		print("(S2)<Start: Transport_layer>")
		print("Receiving Stream [{}] from Network_layer".format(inv_stream))
		if NOW_STATE: #ACK라는 것을 받았으면 성공한 것
			print("SUCCESS TO RECEIVE ACK MSG")
			print("Transport -> Application")
			conn.send(inv_stream)
			print("(S2)<End: Transport_layer>\n\n")
			conn.close()
			break
		

	
	
	


	
def Network_layer(conn):
#bypass
	

	print("(S1)<Start: Network_layer>")
	stream=conn.recv()
	#checking
	print("Network - stream: ",stream)

	#Network -> Datalink
	Net_conn, Data_conn = Pipe()
	print("Network -> Datalink")

	print("Sending Stream [{}] to Datalink_layer".format(stream))
	Net_conn.send(stream)

	p4 = Process(target=Datalink_layer, args=(Data_conn,))
	p4.start()
	#p4.join()
	#conn.close()
	print("(S1)<End: Network_layer>\n\n")


	inv_stream=Net_conn.recv()

	print("(S2)<Start: Network_layer>")
	print("Receiving Stream [{}] from Datalink_layer".format(inv_stream))
	print("Network -> Transport")
	conn.send(inv_stream)
	print("(S2)<End: Network_layer>\n\n")

	conn.close()


def Datalink_layer(conn):
	#print("Network -> Datalink")
	print("(S1)<Start: Datalink_layer>")
	stream=conn.recv()

	#checking
	print("Datalink - stream: ",stream)

	#bitstuffing
	aft_bitstuff_stream=f.bit_stuffing_fun(stream)
	print("Aft Bit stuffing:[{}]".format(aft_bitstuff_stream))
	
	print("Sending to MAC sub layer using simple protocol")
	#Datalink(DLC-> MAC)
	print("DLC sub layer -> MAC sub layer")
	mac_stream=aft_bitstuff_stream

	#Datalink -> Physical
	Data_conn, Phy_conn = Pipe()
	print("Datalink -> Physical")


	print("Sending Stream [{}] to Physical_layer".format(mac_stream))
	Data_conn.send(f.CSMA_CD(mac_stream))
    

	p5 = Process(target=Physical_layer, args=(Phy_conn,))
	p5.start()
	print("(S1)<End: Datalink_layer>\n\n")

	inv_stream=Data_conn.recv()

	print("(S2)<Start: Datalink_layer>")
	print("Receiving Stream [{}] from Physical_layer".format(inv_stream))
	#bitunstuffing
	aft_bitunstuff_stream=f.bit_unstuffing_fun(stream)
	print("Aft Bit unstuffing:[{}]".format(aft_bitunstuff_stream))
	
	print("Datalink -> Network by simple protocol")
	conn.send(aft_bitunstuff_stream)
	print("(S2)<End: Datalink_layer>\n\n")

	conn.close()


def Physical_layer(conn):
	#print("Datalink -> Physical")

	print("(S1)<Start: Physical_layer>")
	stream=conn.recv()

	#checking
	print("Physical - stream: ",stream)

	#MLT-3
	sending_stream=f.EN_MLT_3(stream)
	print("After MLT-3: [{}]".format(sending_stream))
	#Physical -> aft
	Phy_conn, send_conn = Pipe()
	print("Physical -> binder")

	print("Sending Stream [{}] to  binder".format(sending_stream))
	Phy_conn.send(sending_stream)

	p6 = Process(target=binder, args=(send_conn,))
	p6.start()


	print("(S1)<End: Physical_layer>\n\n")


	inv_stream=Phy_conn.recv()

	print("(S2)<Start: Physical_layer>")
	print("Receiving Stream [{}] from binder".format(inv_stream))
	
	#Re-MLT-3
	sending_stream=f.DE_MLT_3(inv_stream)
	print("Aft Reverse MLT-3:[{}]".format(sending_stream))
	print("Physical -> Datalink")
	conn.send(sending_stream)
	print("(S2)<End: Physical_layer>\n\n")
	conn.close()


def binder(conn):
	#print("Physical -> binder")
	print("(S1)<Start: binder>")
	stream=conn.recv()
	#checking
	print("binder - stream: ",stream)
	
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# connect함수로 접속을 한다.
	client_socket.connect((HOST, PORT))
	print("\nStart Socket\n")
	data = stream.encode();
	# 메시지 길이를 구한다.
	length = len(data)

	# server로 리틀 엔디언 형식으로 데이터 길이를 전송한다.
	client_socket.sendall(length.to_bytes(4, byteorder="little"))
	# 데이터를 전송한다.
	client_socket.sendall(data)

	print("\n\n========= start Scenario 2=========\n\n")

	data = client_socket.recv(4)
	# 데이터 길이는 리틀 엔디언 형식으로 int를 변환한다.
	length = int.from_bytes(data, "little")
	# 데이터 길이를 받는다.
	data = client_socket.recv(length)
	# 데이터를 수신한다.
	inv_stream = data.decode()
	print("(S2)<SENDING TO RECEIVER>")

	#inv_stream='010000010100001101001011'
	print("Receive from RECEIVER: ",inv_stream)
	conn.send(inv_stream)
	print("(S2)<End: binder>\n\n")

	conn.close()




if __name__ == '__main__':
	
	print("I'm Sender\n Let's Go Communication")
	input_stream='1111000011110000'
	Sender_conn, App_conn = Pipe()
	print("\n\nuser -> Application")
	
	
	Sender_conn.send(input_stream)
	p1 = Process(target=Application_layer, args=(App_conn,))
	p1.start()
	out_stream=Sender_conn.recv()
	print("[최종적으로 Sender가 받은 msg: {}]".format(out_stream))


