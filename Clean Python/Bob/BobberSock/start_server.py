import socket
from _thread import *
import threading
from BobberSock import BobSocket


def threaded(c):
    while True:
        print('data received from client')
        message = c.recv(1024)

        if not message:
            print('Bye.')
            #self.lock.release()
            break

        bob = BobSocket()
        print("bob has been created")
        data = bob.hey(message)
        print('Bob gave you an answer')

        # send data back to server
        c.sendAll(data)

    c.close()

def Main():
    host = ""
    port = 12345

    #lock = threading.Lock()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print('socket bind to port', port)
    s.listen(5)
    print('socket is listening')

    while True:
        c, addr = s.accept()
        #lock.acquire()

        start_new_thread(threaded, (c,))

    c.close()

if __name__ == '__main__':
    Main()