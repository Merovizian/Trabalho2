import socket
import time
import pickle
from threading import Thread
import threading
import os
import sys
import json



def sign_up(ip_server):

    user = input("Seu nome de usuario: ")
    passwd = input("Sua senha: ")

    HOST = ip_server
    PORT = 20672
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp.connect((HOST, PORT))   
    
    except socket.error as e:
        print(str(e))

    tcp.send(pickle.dumps([user, passwd]))
    msg = pickle.loads(tcp.recv(1024))
    print(msg)
    time.sleep(1)
    os.system('cls||clear') 

    tcp.close()
    

def sign_in(ip_server):

    HOST = ip_server
    PORT = 5000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    user = input("Login:")
    passwd= input("Senha:")

    try:
        tcp.connect((HOST, PORT))   
    
    except socket.error as e:
        print(str(e) + "connect")

    tcp.send(pickle.dumps([user,passwd]))

    msg = pickle.loads(tcp.recv(1024))
    tcp.close()

    return msg, user


def sign_out(user,ip_server):

    HOST = ip_server
    PORT = 21672
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp.connect((HOST, PORT))   
    
    except socket.error as e:
        print(str(e) + "connect")

    tcp.send(pickle.dumps(user))

    msg = pickle.loads(tcp.recv(1024))
    print(msg)
    tcp.close()


def recebe_mensagens():

    ip = ''
    PORT_server = 23672
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (ip, PORT_server)
    tcp.bind(orig)
    tcp.listen(1)

    while True:
        con, cliente = tcp.accept()

        while True:
            msg = con.recv(1024)

            if not msg:
                break

            msg = pickle.loads(msg)

            print(str(msg[0])+":"+ str(msg[1]))
            
            con.close()
            break


def envia_mensagens(user,ip_server):

    while True:

        IP = ip_server
        PORT = 24672
        contact = input("Usuario que deseja enviar mensagem: ")

        tcp_historico = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        tcp_historico.connect((IP, PORT))
        tcp_historico.send(pickle.dumps([user,contact]))
        msg = pickle.loads(tcp_historico.recv(1024))

        print(msg)

        while True:
            msg = input()

            if msg != "fim":

                tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                PORT = 22672

                try:
                    tcp_client.connect((IP, PORT))
                    tcp_client.send(pickle.dumps([user,contact ,msg]))

                    msg = pickle.loads(tcp_client.recv(1024))

                    if msg == "offline":
                        print("{} não está online".format(contact))
                    
                    else:
                        pass
                    
                    tcp_client.close()

                except socket.error:
                    print("Mensagem não enviada")
                    tcp_client.close()

            else:
                os.system('cls||clear') 
                break


if __name__ == '__main__':

    ip_server = sys.argv[1]

    while True:
        action = input("Digite cadastrar ou login: ")
        os.system('cls||clear') 

        if action == 'login':
            state = 'login'
            break
        
        elif action == 'cadastrar':
            sign_up(ip_server)
        
        else:
            print("Ação invalida")
        

    if state == 'login':
        clients, user = sign_in(ip_server)

        if clients != None:

            try:
                print("login realizado")
                time.sleep(1)
                os.system('cls||clear')

                envia = Thread(target=envia_mensagens,args=(user,ip_server,))
                recebe = Thread(target=recebe_mensagens)

                envia.start()
                recebe.start()

                while threading.active_count() > 1:
                # pausa de 0.1 segundo,
                # Evita que a CPU fique processando a comparação acima sem parar.
                    time.sleep(0.1)
            
            except KeyboardInterrupt:

                os.system('cls||clear')
                print("Programa finalizado...")
                sign_out(user,ip_server)
                time.sleep(2)
                os.system('cls||clear')

        else:
            print("Não foi possivel fazer login")
            print()
    

##V0
        



            



            
