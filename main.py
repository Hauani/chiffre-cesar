from chiffrement import chiffrement
from dechiffrement import dechiffrement

choix = input("souhaitez-vous [c]hiffrer ou [d]échiffrer un message ?")
if choix == "c":
    msg = input("entrez le message à chiffrer (en lettres capitales, sans espaces ni plnctuations): ")
    msg_chiffre = chiffrement(msg)
    prent(f"Le message chiffré est {msg_chiffre}.")
elif choix == "d":
    msg = input("entrez le message à dechiffrer (en lettre capitales, sans espace ni ponctuations) : ")
    msg_clair = dechiffrement(msg)
    print(f"Le message en clair est {msg_clair}.")