
import threading 
import socket
#from digi.xbee.devices import XBeeDevice
import serial
import sys
import time


host = ''
port = 9000
locaddr = (host,port) 


megaBoard = serial.Serial('/dev/tty.usbserial-D308FBLV', 9600)
queue = []



# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

def xbeeRecv():
    while(True):
        message = megaBoard.readline().decode().strip()
        print("Received message: ",message)
        items = message.split(" ")


        if (items[0]=='FLY'):
            msg = "takeoff"
            queue.append(msg)
            print("Queue contents: ",queue)

        if (items[0]=='LAND'):
            msg = "land"
            queue.append(msg)
            print("Queue contents: ",queue)

        if (items[0]=='left'):
            msg = 'left '+ str(items[1])
            queue.append(msg)
            print("Left! Queue contents: ",queue)

        if (items[0]=='right'):
            msg = 'right '+ str(items[1])
            queue.append(msg)
            print("Right! Queue contents: ",queue)

        if (items[0]=='back'):
            msg = 'back '+ str(items[1])
            queue.append(msg)
            print("Back! Queue contents: ",queue)
        
        if (items[0]=='forward'):
            msg = 'forward '+ str(items[1])
            queue.append(msg)
            print("Forward !Queue contents: ",queue)

        if (items[0]=='stationary'):
            print("switching to stationary mode")
        
        if (items[0]=='tracking'):
            print("switching to tracking mode")

def droneFunc():
     firstCommandSent = 0
     while True: 
        try:
            #send command to enable correct mode on drone
            if (firstCommandSent == 0):
                msg = "command"
                firstCommandSent = 1

                # Send data
                msg = msg.encode(encoding="utf-8") 
                sent = sock.sendto(msg, tello_address)

            if queue:#if list has commands in it
                #print("msg recieved from queue\n")
                msg = queue[0] #get first message in queue
                print("value of msg: ",msg)

                queue.pop(0) #remove msg from queue


                # Send data
                msg = msg.encode(encoding="utf-8") 
                sent = sock.sendto(msg, tello_address)
        except KeyboardInterrupt:
            print ('\n . . .\n')
            sock.close()  
            break





print ('\r\n\r\nCS380 Tello Python Program .\r\n')

#create another thread that takes input and puts into message queue
#main thread checks if queue is empty, if not empty send msg to drone

if __name__ =="__main__":
    socketT = threading.Thread(target=recv)
    xbeeT = threading.Thread(target=xbeeRecv)
    droneT = threading.Thread(target=droneFunc)
 
    socketT.start()
    droneT.start()
    xbeeT.start()
 
    socketT.join()
    droneT.join()
    xbeeT.join()
 
    print("Done!")

    






