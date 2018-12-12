import socket

def Main():
    host = '127.0.0.1'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))

    message = "Rado says hello mother f"

    while True:
        # message sent to server
        s.send(message.encode('ASCII'))

        # message received from server
        data = s.recv(1024)

        # print the received message
        # it will be reverse of sent message
        print("Received from server: ", str(data.decode('ASCII')))

        ans = input('\nDo you want to continue (y/n) :')
        if ans == 'y':
            continue
        else:
            break

    # close connection
    s.close()

if __name__ == '__main__':
    Main()
