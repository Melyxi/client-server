# client
# Программа клиента, запрашивающего текущее время

import click
from socket import *
import datetime, time
import json


def client_message(name):
    msg = input("Введите сообщение: ")

    data = {
        "action": "msg",
        "time": datetime.datetime.now().timestamp(),
        "to": "#room_name",
        "from": name,
        "message": msg
    }
    return json.dumps(data)


def login():
    username = input('Введите имя: ')
    password = input('Введите пароль: ')
    data = {
        "action": "authenticate",
        "time": datetime.datetime.now().timestamp(),
        "user": {
            "account_name": username,
            "password": password
        }
    }
    return data


def convert(data):
    recv_str = data.decode('utf-8')
    recv_msg = json.loads(recv_str)
    return recv_msg


ENCODING = 'utf-8'


@click.command()
@click.option('--add', default='localhost', help='ip')
@click.option('--port', default=7777, help='port')
def send_message(add, port):
    with socket(AF_INET, SOCK_STREAM) as s:  # Создать сокет TCP
        s.connect((add, port))  # Соединиться с сервером
        while True:
            msg = login()  # логинемся
            log = json.dumps(msg)
            s.send(log.encode(ENCODING))
            data = s.recv(10000)
            # print(data)
            recv_msg = convert(data)
            # print(recv_msg)
            name = msg["user"]["account_name"]
            # print(name)
            print('Сообщение от сервера: ', recv_msg, ', длиной ', len(data), ' байт')
            while recv_msg["response"] == 200:
                message = client_message(name)
                # print(message)
                s.send(message.encode(ENCODING))
                data = s.recv(10000)
                recv_message = convert(data)
                print('Сообщение от сервера: ', recv_message, ', длиной ', len(data), ' байт')
                if json.loads(message)['message'] == 'quit':
                    break  # выходим на логировние


if __name__ == '__main__':
    send_message()
