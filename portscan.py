#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import socket

ip = raw_input("Digite o IP ou endereco: ")

ports = []
count = 0

while count < 10:
    ports.append(int(raw_input("Digite a porta: ")))
    count += 1


for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print str(port) + " -> Porta aberta"
    else:
        print str(port) + " -> Porta fechada"

print "Scan Finalizado"