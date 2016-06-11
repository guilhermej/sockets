#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 25

file = open("shell.php", 'w')


try:
    server.bind((ip, port))
    server.listen(5)
    print "Listening in: " + ip + ":" + str(port)

    (client_socket, address) = server.accept()

    print "Received from: " + address[0]

    data = client_socket.recv(1024)
    file.write(data)

    server.close()

except Exception as erro:
    print "Erro: " + str(erro)
    server.close()