import socket
import time

server = ''
channel = ''
bot_name = 'harmonia'

irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc_socket.connect((server, 6667))

irc_socket.send(f'NICK {bot_name}\r\n'.encode('utf-8'))
irc_socket.send(f'USER {bot_name} 0 * :Innovate. Build. Ship.\r\n'.encode('utf-8'))
irc_socket.send(f'JOIN {channel}\r\n'.encode('utf-8'))

while True:
    message = irc_socket.recv(2048).decode('utf-8').strip('\n\r')

    print(f'Received: {message}')

    if message.startswith('PING'):
        irc_socket.send(f'PONG {message[1:]}\r\n'.encode('utf-8'))

    if 'hello' in message.lower():
        irc_socket.send(f'PRIVMSG {channel} :Hello there!\r\n'.encode('utf-8'))

time.sleep(1)
