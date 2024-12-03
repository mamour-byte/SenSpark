# coding utf-8
import socket
import threading

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"\nMessage reçu : {message}")
            else:
                print("Le serveur a fermé la connexion.")
                break
        except Exception as e:
            print(f"Erreur lors de la réception du message : {e}")
            break
    client.close()

def main():
    HOST = '127.0.0.1'
    PORT = 50000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
            print("Client connecté au serveur.")

            # Démarre un thread pour recevoir les messages
            threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

            while True:
                message = input("Entrez votre message (ou 'exit' pour quitter) : ")
                
                # S'assurer que l'utilisateur ne rentre pas un message vide
                if not message.strip():
                    print("Vous ne pouvez pas envoyer un message vide.")
                    continue
                
                if message.lower() == 'exit':
                    print("Déconnexion du serveur.")
                    break

                try:
                    client.sendall(message.encode('utf-8'))
                except Exception as e:
                    print(f"Erreur lors de l'envoi du message : {e}")
                    break

        except ConnectionRefusedError:
            print("Erreur : Impossible de se connecter au serveur.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()
