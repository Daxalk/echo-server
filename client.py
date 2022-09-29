import socket


def connection(sock, address, port):
    sock.connect((address, port))
    print('Произошло соединение с сервером')


def send_data(sock, data):
    sock.send(data.encode())
    print(f'Отправлены данные: {data}')


def receive_data(sock):
    data = sock.recv(1024)
    print(f'Получено сообщение: {data.decode()}')
    return data


def end_session(sock):
    sock.close()
    print(f'Соединение с сервером разорвано')


def main():
    sock = socket.socket()
    address, port = 'localhost', 9090
    connection(sock, address, port)

    msg = 'ABCdefG1231232131'
    send_data(sock, msg)
    receive_data(sock)
    end_session(sock)


main()
