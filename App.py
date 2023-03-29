#Importar as bibliotecas necessarias
import pywhatkit
import keyboard
import time
from datetime import datetime
import sqlite3

#Definir os contatos que iremos enviar
connectionall = sqlite3.connect('lista.db')
c = connectionall.cursor()
contatos = c.execute("SELECT nome, telefone FROM clientes")
contatos = contatos.fetchall()

#Definir intervalo de envio
for contato in contatos:
    print(contato[1])
        #enviar mensagem
    pywhatkit.sendwhatmsg(contato[1],
                          
                          #Escreva sua mensagem aqui
                          f'Olá tudo bem, {contato[0]} escreva o restante da mensagem aqui',
                          

                          datetime.now().hour,datetime.now().minute+1)
    time.sleep(30)
    keyboard.press_and_release('ctrl + w')
    
    '''ATENÇÃO
    Para que tudo funcione você deverá:
    Ter o python instalado com a versão acima da 3.9
    ter baixado as bibliotecas necessarias
    Estar com o whatsapp aberto no seu navedador
    Ter cadastrado os clientes com nome e numero
    O numero de telefone deve ser colocado nesse formato: 11988998899 (O DDD acompanhado do numero sem espaço e sem outros caracteres)
    
    '''