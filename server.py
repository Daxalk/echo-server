import socket


def port_listening(sock):
    address, port = '', 9090
    sock.bind((address, port))
    sock.listen(1)
    print(f'Началось прослушивание порта {port}')


def connection(sock):
    conn, addr = sock.accept()
    print(f'Клиент {str(addr[0]) + ":" + str(addr[1])} подключен')
    return conn


def receive_data(conn):
    msg = ''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        print(f'Получено сообщение: {msg}')
        conn.send(data)
        print(f'Отправлено сообщение: {msg}')


def end_session(conn):
    conn.close()
    print('Отключение клиента')


def stop(sock):
    sock.close()
    print('Остановка сервера')


def main():
    sock = socket.socket()
    print('Сервер запустился')

    port_listening(sock)
    conn = connection(sock)
    receive_data(conn)
    end_session(conn)
    stop(sock)


main()
