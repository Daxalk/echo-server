import socket
import config


def connection(sock, address, port):
    sock.connect((address, port))
    print('Произошло соединение с сервером')


def send_data(sock, data):
    sock.send(data.encode())
    print(f'Отправлены данные: {data}')
    sock.send(config.breakmsg.encode())


def receive_data(sock):
    msg = ''
    while True:
        data = sock.recv(1024)
        if not data:
            break
        msg += data.decode()

    print(f'Получено сообщение: {msg}')
    return data


def end_session(sock):
    sock.close()
    print(f'Соединение с сервером разорвано')


def main():
    sock = socket.socket()
    address, port = 'localhost', config.port
    connection(sock, address, port)
    msg = config.msg
    send_data(sock, msg)
    receive_data(sock)
    end_session(sock)


main()

