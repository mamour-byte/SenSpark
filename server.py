# coding utf-8
# /* #######################################
#        _________     ________   _______                   ________    _______
#       /             !          !       \  \          /   !           !       \
#      /              !          !        )  \        /    !           !        )
#      \___________   !____      !  _____/    \      /     !____       !  _____/
#                  \  !          !       \     \    /      !           !       \
#                  /  !          !        \     \  /       !           !        \
#       __________/   !________  !         \     \/        !________   !         \ 

import socket 
import sqlite3 
import threading
from fonctions import *  

threadsclient = []

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(('127.0.0.1',50000))
# Ecoute sur le port 5000 
server.listen(5)
while True : 
    client , infoClient = server.accept()
    threadsclient.append(threading.Thread(None , instanceServer , None , (client , infoClient) , {}))
    threadsclient[-1].start()

server.close()

