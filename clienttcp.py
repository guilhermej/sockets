#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    client.connect(("127.0.0.1", 889))
    data = raw_input("Mensagem: ")
    client.send(data)

    pacotes_recebidos = client.recv(1024)

    print pacotes_recebidos
except:
    print "Conexao falhou"

