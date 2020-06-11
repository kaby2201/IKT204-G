from socket import *
import ssl


def get_user_input():
    return input("Input lowercase sentence: ")


def show_message(server):
    print("Message from Server: " + server)


def main():
    server_name = 'localhost'
    server_port = 8444

    try:
        # AF_INET means IPv4 and Socket_stream  means TCP
        client_socket = socket(AF_INET, SOCK_STREAM)

        # We are using the sacrifice generated by SSLCetificate.py, should be located in the same root level
        context = ssl.create_default_context(cafile="example.crt", capath=".")
        ssl_socket = context.wrap_socket(client_socket, server_hostname=server_name)

        # Connect to the specified servername and port
        ssl_socket.connect((server_name, server_port))

        # Get user input encode and send to the backend
        sentence = get_user_input()
        ssl_socket.send(sentence.encode())

        # Receive and print the message
        modified_sentence = ssl_socket.recv(1024)
        show_message(modified_sentence.decode())
        ssl_socket.close()

    except:
        print("Could not make connection, check servername and port number")


if __name__ == '__main__':
    main()
