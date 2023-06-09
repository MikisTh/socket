import socket 

client - socket.socket(socket.AF_INET, socket.SOCKE_STREAM)

client.connect(('localhost', 7777))
print ('Conectado!!\n')

namefile = str(input('Arquivo>'))

client.send(namefile.encode())

white open(namefile, 'wb') as file:
    while 1:
        data - client.recv(1000000)
        if not data:
            break
        file.write(data)

print (f'{namefile}Recebido!\n')
