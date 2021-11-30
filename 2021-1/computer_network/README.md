# computernetwork
<list>
 
- MLT-3.py / un-MLT-3.py
 
- bitstuffing/unstuffing.py
 
- CSMA-CD.py
 
- simple protocol.py
 
- stop and wait .py
 
- Protocol Scenario- final exam
Scenario coding using socket, processing for layer and receiver/sender

#===== final exam =====
Scenario 1)

Application -> Transport: 11110000 11110000 전송

Transport -> Network: "stop and wait" 프로토콜 사용

Network -> Datalink: bypass

Datalink -> Physical: 

 the Logical Link Control (LLC) -> the Media Access Control (MAC) sublayer: bit-stuffing and "Simple Protocol" 
 
 Mac -> Physical: MLT-3 scheme


<socket>
  
 
Physical -> Datalink: Reverse MLT-3 scheme

 Datalink -> Network: bit-unstuffing, "simple Protocol"

 Network -> Transport: bypass

 Transport -> Application: "stop and wait" Protocol and Ack 생성

 Application layer는 최종 수신 확인

----------------------


Scenarion 2)

Application -> Transport

Transport -> Network

 Network -> Datalink

 Datalink -> Physical


 <socket>
  

  Physical -> Datalink

  Datalink -> Network

  Network -> Transport

  Transport -> Application

=======================
  
  
  
각 layer 는 
import socket, threading
from multiprocessing import Process, Pipe을 이용한다.
sender와 receiver는 socket통신을 한다.
각 layer간에는 processing을 한다. pipe를 사용하였다.
  
단, 통신 환경은 아주 이상적인 환경으로 bit 유실이 절대 발생하지 않는 환경을 만든다. 
