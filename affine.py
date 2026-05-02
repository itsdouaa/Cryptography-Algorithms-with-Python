#chiffrement affine

import crypto_tool
#----------------implementation--------------------

alphabetOrdreMaj = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
alphabetOrdreMin = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
alphabet_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_min = ['a', 'b', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
modulo = len(alphabet_maj)

def encryptLetter(a, b, x):
    if x.isupper():    
        y_ord = (a * alphabetOrdreMaj[x] + b) % modulo
        y = alphabet_maj[y_ord]
    else:
        y_ord = (a * alphabetOrdreMin[x] + b) % modulo
        y = alphabet_min[y_ord]
    return y

def decryptLetter(a, b, y):
    if y.isupper():    
        x_ord = ((alphabetOrdreMaj[y] - b) * crypto_tool.inverse_multiplicatif(a, modulo)) % modulo
        x = alphabet_maj[x_ord]
    else:
        x_ord = ((alphabetOrdreMin[y] - b) * crypto_tool.inverse_multiplicatif(a, modulo)) % modulo
        x = alphabet_min[x_ord]
    return x

def encrypt(a, b, textClair):
    textChiffre = ""
    for x in textClair:
        y = encryptLetter(a, b, x)
        textChiffre = textChiffre + y
    print(f"texte clair: '{textClair}',\ttexte chiffré: '{textChiffre}'")

def decrypt(a, b, textChiffre):
    textClair = ""
    for y in textChiffre:
        x = decryptLetter(a, b, y)
        textClair = textClair + x
    print(f"texte chiffré: '{textChiffre}',\ttexte clair: '{textClair}'")

def verifier_a(a: int):
    if crypto_tool.euclide_algo(a, modulo)[0] != 1:
        return False
    else:
        return True

def verifier_b(b: int):
    if b < 0 or b > modulo:
        return False
    else:
        return True

PROCESSUS = [encrypt, decrypt]
def process(processus: int, text: str):
    print("Donner les facteur a et b: \n")
    while True:
        a = input("a = ")
        try:
            a = int(a)
            if verifier_a(a):
                break
            else:
                print(f"a invalide! donner un élément inversible modulo '{modulo}'\n")
                continue
        except:
            print("Entrer un nombre valide s'il vous plait.\n")
        
    while True:
        b = input("b = ")
        try:
            b = int(b)
            if verifier_b(b):
                break
            else:
                print(f"b invalide! donner un élément entre '0' et '{modulo}'\n")
                continue
        except:
            print("Entrer un nombre valide s'il vous plait.\n")
    PROCESSUS[processus](a, b, text)
