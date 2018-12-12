import socket

def Main():
    host = '127.0.0.1'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local port
    s.connect((host, port))

    while True:
        message = input("What do you have to say to Bob? Type (q) for exit: ")
        print('Message is: ', message)
        if message == 'q':
            break

        print('message sent to server')
        s.sendall(message.encode('ASCII'))

        print('message received from server')
        data = s.recv(1024)

        #print the received message
        print("Bob said: ", str(data.decode('ASCII')))

if __name__ == '__main__':
    Main()