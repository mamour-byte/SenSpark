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
                break
        except Exception as e:
            print(f"Erreur lors de la réception : {e}")
            break

def main():
    HOST = '127.0.0.1'
    PORT = 50000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
            print("Client 1 connecté au serveur.")

            # Démarre un thread pour recevoir les messages
            threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

            while True:
                message = input("Client 1, entrez votre message (ou 'exit' pour quitter) : ")
                if message.lower() == 'exit':
                    print("Client 1 déconnecté.")
                    break
                client.sendall(message.encode('utf-8'))

        except ConnectionRefusedError:
            print("Erreur : Impossible de se connecter au serveur.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()
