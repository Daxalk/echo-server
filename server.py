import socket
import config


def port_listening(sock):
    address, port = '', config.port
    sock.bind((address, port))
    sock.listen(0)
    print(f'Началось прослушивание порта {port}')


def connection(sock):
    conn, addr = sock.accept()
    print(f'Клиент {str(addr[0]) + ":" + str(addr[1])} подключен')
    return conn


def receive_data(conn):
    msg = ''
    while not(config.breakmsg in msg):
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
    msg = msg.replace(config.breakmsg, '',)
    print(f'Получено сообщение: {msg}')
    return msg


def send_data(conn, msg):
    conn.send(msg.encode())
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
    msg = receive_data(conn)
    send_data(conn, msg)
    end_session(conn)
    stop(sock)


main()

