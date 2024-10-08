# coding utf-8
import socket

def main():
    HOST = '127.0.0.1'  # Adresse du serveur
    PORT = 50000        # Port du serveur

    # Création de la socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
            print("Connecté au serveur.")
            
            while True:
                message = input("Entrez votre message (ou 'exit' pour quitter) : ")
                if message.lower() == 'exit':
                    print("Déconnexion du serveur.")
                    break

                client.sendall(message.encode('utf-8'))  # Envoi du message
                print("Message envoyé.")

        except ConnectionRefusedError:
            print("Erreur : Impossible de se connecter au serveur. Assurez-vous qu'il est en cours d'exécution.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()
