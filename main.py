import cesar
import affine
import hill
import vigenere

CHIFFREMENTS = [cesar, affine, hill, vigenere, "Exit"]

if __name__ == '__main__':
    print("\n\nChoisir un chiffrement depuis le menu suivant:\n")
    print("_________________________________________________________________MENU_________________________________________________________________\n")
    i = 0
    for chiffrement in CHIFFREMENTS:
        i = i + 1
        if hasattr(chiffrement, "__name__"):
            print(i, f".\t{chiffrement.__name__}\n")
        else:
            print(i, f".\t{chiffrement}\n")
    choix = input("Choix: ")
    while CHIFFREMENTS[int(choix) - 1] != "Exit":
        print("_______________________________________________________________OPERATION______________________________________________________________\n")
        chiffrement = CHIFFREMENTS[int(choix) - 1]
        print(f"Chiffrement: {chiffrement.__name__}\n")
        print("\nOptions:\n")
        print("1.\tEncrypt\n2.\tDecrypt\n\n")
        option = input("Option: ")
        processus = int(option) - 1
        text = input("Saisir le texte: ")
        chiffrement.process(processus, text)
        print("\n\nChoisir un chiffrement depuis le menu suivant:\n")
        print("_________________________________________________________________MENU_________________________________________________________________\n")
        i = 0
        for chiffrement in CHIFFREMENTS:
            i = i + 1
            if hasattr(chiffrement, "__name__"):
                print(i, f".\t{chiffrement.__name__}\n")
            else:
                print(i, f".\t{chiffrement}\n")
        choix = input("Choix: ")
