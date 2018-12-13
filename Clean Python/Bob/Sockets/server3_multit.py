import socket
# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            print("Bye.")


            # Lock released on exit
            print_lock.release()
            break

        # reverse the given string from client
        data = data[::-1]

        # send back reversed string to client
        c.send(data)

    # connection closed
    c.close()

def Main():
    host = ""

    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port: ", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print("Connected to: ", addr[0], ':', addr[1])

        # start new thread and return its identifier
        start_new_thread(threaded, (c,))

    s.close()

if __name__ == '__main__':
    Main()