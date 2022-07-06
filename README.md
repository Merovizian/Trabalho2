# TRABALHO 1  - Laboratório de Redes
por Eric Giobini, Mateus Sobrinho

## O que é?

São programas que simulam um chat em uma rede local via container, onde existe sistema de login, cadastro, historico de mensagem.



## Requisitos

- Python3

- Docker

- Máquinas virtuais

### Máquinas virtuais

Para funcionamento do modo de conexão automatica é necessário que as máquinas virtuais sejam:


para o servidor

para cada cliente conectado


## Tutorial

As imagens estão upadas no docker hub, logo os comandos abaixo é necessario ter o docker instalado na máquina.
Primeiro passo é rodas o container em uma máquina virtual do servidor, deixando ele alocado e sabendo seu IP para os clients se conectarem.
O comando abaixo, inicializa o container do servidor na máquina:

~~~
sudo docker run -it --rm --network=host mateusmenines/trabalhoredes_2:server python3 server.py
~~~

Esse programa necessita firar sempre rodando, é ele que disponibiliza todo os serviços de conexão e de barramento de mensagem.

O próximo passo é abrir o segundo programa.
Em outra máquina virtual o usuário deverá abrir o programa do client usando o seguinte comando:

~~~
sudo docker run --init -it --rm --network=host mateusmenines/trabalhoredes_2:client python3 client.py < IP AONDE O SERVIDOR ESTÁ ALOCADO >
~~~ 
Lembre-se de tirar o <>

Ao abrir o programa, o usuario irá se deparar com um sistema de cadastro e login, nisso, com o usuário novo tem a necessidade de se cadastrar, e posteriormente fazer o login.
Depois do login realizado, o usuário se depara com uma pergunta para quem ele quer mandar mensagem, nisso ele poderá mandar mensagem para quem estiver online, caso o outro usuário não esteja online, essa mensagem estará salva e quando ele estiver logado, a mensagem irá aparecer.

## Caracteristicas.

Para encerrar as aplicações: Control+C no terminal, isso faz que o usuário se desconecte do chat.

Toda mensagem é salva em um historico de conversa.

Ip dinâmico do usuário, isso é, ele pode logar em outras máquinas com seu login e senha que a conversa estará salva, podendo mandar mensagem para qualquer outro usuário.

## Funcionalidade

Ao escrever com quem o cliente quer enviar mensagem para outro usuário, o terminal ficará esperando sua mensagem, logo no terminal, ira exibir mensagens vindas de outros usuários mostrando quem as mandaram, e terá sempre disponivel uma entrada de mensagem para poder enviar.

Para poder enviar mensagem para outro usuário, deve-se digitar "fim" sem aspas, que em seu terminal irá mostrar a pergunta de novo " Para quem deseja enviar mensagem".


## Feedback

Caso tenha alguma dúvida, sugestão ou tenha encontrado algum erro, por favor mande um email para ericgmicaela@gmail.com
