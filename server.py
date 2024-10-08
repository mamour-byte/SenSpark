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
from fonctions import instanceServer  # Import spécifique

# Configuration du serveur
HOST = '127.0.0.1'
PORT = 50000
MAX_CONNECTIONS = 5

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(MAX_CONNECTIONS)
        print(f"Serveur démarré sur {HOST}:{PORT}")

        while True:
            client, infoClient = server.accept()
            print(f"Nouvelle connexion de {infoClient}")
            thread = threading.Thread(target=instanceServer, args=(client, infoClient))
            thread.start()

if __name__ == "__main__":
    start_server()
