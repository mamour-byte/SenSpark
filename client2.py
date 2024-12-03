# coding: utf-8
import socket
import threading

def receive_messages(client):
    """Fonction qui reçoit les messages du serveur et les affiche."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"\nMessage reçu : {message}")
            else:
                # Si aucune donnée n'est reçue, la connexion est fermée.
                print("\nConnexion fermée par le serveur.")
                break
        except Exception as e:
            print(f"Erreur lors de la réception du message : {e}")
            break

def send_message(client):
    """Fonction qui permet à l'utilisateur d'envoyer des messages au serveur."""
    while True:
        message = input("Entrez votre message (ou 'exit' pour quitter) : ")
        if message.lower() == 'exit':
            print("Vous vous êtes déconnecté du serveur.")
            client.close()
            break
        elif message.strip():
            try:
                client.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Erreur lors de l'envoi du message : {e}")
                break
        else:
            print("Veuillez entrer un message valide.")

def main():
    """Fonction principale du client."""
    HOST = '127.0.0.1'  # Adresse du serveur
    PORT = 50000        # Port du serveur

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            print("Client connecté au serveur.")

            # Lancer un thread pour recevoir les messages du serveur
            threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

            # Lancer la fonction principale d'envoi de messages
            send_message(client)

    except ConnectionRefusedError:
        print("Erreur : Impossible de se connecter au serveur.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()
