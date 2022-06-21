import socket
import pickle
from threading import Thread
import threading
import time
import json


def sign_up():

    IP = '' 
    PORT = 20672
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp.bind((IP, PORT))

    except socket.error as e:
        print(str(e) + "in sing in")
    
    tcp.listen(1)

    while True:
        con, cliente = tcp.accept()

        config_file = "etc/user.json"
        user_file = json.load(open(config_file,'r'))

        while True:
            msg = con.recv(1024)

            if not msg:
                print('Finalizando conexao do cliente', cliente)
                con.close()
                break

            msg = pickle.loads(msg)
            print("usuario {} do IP = {} está tentando se cadastrar".format(msg[0], cliente[0]))

            for user, passwd in user_file.items():
                if msg[0] != user:
                    user_file[msg[0]] = msg[1]

                    with open("etc/user.json", "w") as out:
                        out.write(json.dumps(user_file))        
                    
                    print("Usuario {} se cadastrou".format(msg[0]))
                    con.send(pickle.dumps("Usuario cadastrado"))
                    con.close()
                    break
                      
                else:
                    print("Usuario já cadastrado")
                    con.send(pickle.dumps("Usuario já cadastrado"))
                    con.close()
                    break 
            break


def sign_in():

    IP = '' 
    PORT = 5000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp.bind((IP, PORT))

    except socket.error as e:
        print("e")
    
    tcp.listen(1)

    while True:
        cont = 0
        con, cliente = tcp.accept()
        print ("cliente {} está tentando logar".format(cliente))
        print("...")

        config_file = "etc/user.json"
        user_file = json.load(open(config_file,'r'))

        config_file = "etc/connect.json"
        connect_file = json.load(open(config_file,'r'))

        while True:
            msg = con.recv(1024)

            if not msg:
                print('Finalizando conexao do cliente', cliente)
                con.close()
                break

            msg = pickle.loads(msg)

            for user, passwd in user_file.items():
                cont +=1

                if msg[0] == user and msg[1] == passwd:
                    print("{} realizou login!".format(msg[0]))

                    connect_file[user] = cliente[0]

                    with open("etc/connect.json", "w") as out:
                        out.write(json.dumps(connect_file))
        
                    con.send(pickle.dumps("cliente online"))
                    con.close()
                    break

                elif cont == len(user_file.items()):

                    con.send(pickle.dumps(None))
                    con.close() 
                    break
            break


def sign_out():

    IP = '' 
    PORT = 21672
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp.bind((IP, PORT))

    except socket.error as e:
        print("e")
    
    tcp.listen(1)

    while True:
        con, cliente = tcp.accept()
        config_file = "etc/connect.json"
        connect_file = json.load(open(config_file,'r'))

        while True:
            msg = con.recv(1024)

            if not msg:
                print('Finalizando conexao do cliente', cliente)
                con.close()
                break

            msg = pickle.loads(msg)

            try:
                del connect_file[msg]
                with open("etc/connect.json", "w") as out:
                    out.write(json.dumps(connect_file))
                
                print("{} desconectou".format(msg))
                con.send(pickle.dumps("Você foi desconectado"))

                con.close()
                break

            except:
                print("Erro ao desconectar")
                con.close()
                break


def broker():

    tcp_broker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = ''
    PORT = 22672

    try:
        tcp_broker.bind((IP, PORT))

    except socket.error as e:
        print(str(e))

    tcp_broker.listen(1)

    while True:
        con, cliente = tcp_broker.accept()
        
        config_file = "etc/connect.json"
        connect_file = json.load(open(config_file,'r'))

        while True:
            msg = con.recv(1024)

            if not msg:
                print('Finalizando conexao do cliente', cliente)
                con.close()
                break
               
            msg = pickle.loads(msg)

            try:
                tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcp_client.connect((connect_file[msg[1]],23672))
                tcp_client.send(pickle.dumps([msg[0],msg[2]]))
                print("mensagem de {} para {} foi enviada".format(msg[0],msg[1]))
                print()

                con.send(pickle.dumps("online"))
                tcp_client.close()
                con.close()
                break

            except:
                con.send(pickle.dumps("offline"))
                con.close() 
                break  


if __name__ == '__main__':

    login = Thread(target=sign_in)
    broker = Thread(target=broker)
    sign_up = Thread(target=sign_up)
    sign_out = Thread(target=sign_out)

    login.start()
    broker.start()
    sign_up.start()
    sign_out.start()

    while threading.active_count() > 1:
        # pausa de 0.1 segundo,
        # Evita que a CPU fique processando a comparação acima sem parar.
        time.sleep(0.1)

    print("Programa encerrado")


# V0