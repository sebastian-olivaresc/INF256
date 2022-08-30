#!/usr/bin/env python

import socket as skt
import sys
from time import sleep

import interface


address = 'localhost'
serverPort = 8080 
# se crea el socket en IPv4 en modo TCP
clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
clientSocket.connect((address, serverPort))

end_program = False

main_menu()
main_input = int(input())
while (end_program != False):
    win_bot = 0
    win_client = 0
    bot_option = 0
    if (main_input == jugar):
        options_game(win_bot, win_client, bot_option)
        client_option = int(input())

        clientSocket.send(client_option)
        bot_option = clientSocket.recv(1024)



    elif (main_input == salir):
        clientSocket.close()
        end_program = True

    else:
        clear()
        print("Elija una opcion correcta")
        sleep(2)
    end_program = True

# se termina el programa
clear()
print("Programa terminado.")
sleep(2)
sys.exit(0)
