#chiffrement de cesar

#----------------implementation--------------------

alphabetOrdreMaj = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
alphabetOrdreMin = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
alphabet_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
modulo = len(alphabet_maj)

def decalerLettreAvant(lettre, decalage: int):
    if lettre.isalpha():
        if lettre.isupper():
            return alphabet_maj[(alphabetOrdreMaj[lettre] + decalage) % modulo]
        else:
            return alphabet_min[(alphabetOrdreMin[lettre] + decalage) % modulo]

def decalerLettreArriere(lettre, decalage: int):
    if lettre.isalpha():
        if lettre.isupper():
            return alphabet_maj[(alphabetOrdreMaj[lettre] - decalage) % modulo]
        else:
            return alphabet_min[(alphabetOrdreMin[lettre] - decalage) % modulo]

def encrypt(textClair: str, decalage):
    textChiffre = ""
    for c in textClair:
        ch = decalerLettreAvant(c, decalage)
        textChiffre = textChiffre + ch
    print(f"texte clair: '{textClair}',\ttexte chiffré: '{textChiffre}'")

def decrypt(textChiffre: str, decalage):
    textClair = ""
    for c in textChiffre:
        ch = decalerLettreArriere(c, decalage)
        textClair = textClair + ch
    print(f"texte chiffré: '{textChiffre}',\ttexte clair: '{textClair}'")

PROCESSUS = [encrypt, decrypt]
def process(processus: int, text: str):
    try:
        decalage = int(input("\nDonner le décalage: "))
    except ValueError:
        print("Entrer un nombre valide s'il vous plait.\n")
    PROCESSUS[processus](text, decalage)
