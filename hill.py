#chiffrement de hill
import crypto_tool
#----------------implementation--------------------
alphabetOrdreMaj = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
alphabetOrdreMin = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
alphabet_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
modulo = len(alphabet_maj)

def decouperTexte(text, dimension):
    textDecoupe = []
    bloc = []
    i = 0
    for c in text:
        bloc.append(c)
        i = i + 1
        if i == dimension:
            textDecoupe.append(bloc)
            bloc = []
            i = 0
    return textDecoupe

def numeriserBloc(bloc: str):
    blocNum = []
    memoire = []
    for c in bloc:
        if c.isupper():
            blocNum.append(alphabetOrdreMaj[c])
            memoire.append(1)
        else:
            blocNum.append(alphabetOrdreMin[c])
            memoire.append(0)
    return blocNum, memoire

def blocChar(blocNum, memoire):
    bloc  = []
    j = 0
    for i in blocNum:
        if memoire[j] == 1:
            bloc.append(alphabet_maj[i])
        else:
            bloc.append(alphabet_min[i])
        j = j + 1
    return bloc

def encryptBloc(blocNum, matrice, dimension):
    blocEncrypted = []
    i = 0
    j = 0
    buffer = 0
    while i < dimension:
        while j < dimension:
            buffer = buffer + blocNum[j] * matrice[i][j]
            j = j + 1
        blocEncrypted.append(buffer % modulo)
        buffer = 0
        j = 0
        i = i + 1
    return blocEncrypted

def decryptBloc(blocNum, matrice, dimension):
    matriceInv = crypto_tool.inverseMatrice(matrice, dimension)
    blocClair = []
    i = 0
    j = 0
    buffer = 0
    while i < dimension:
        while j < dimension:
            buffer = buffer + blocNum[j] * matriceInv[i][j]
            j = j + 1
        blocClair.append(buffer % modulo)
        buffer = 0
        j = 0
        i = i + 1
    return blocClair

def encrypt(matrice, dimension, textClair):
    textDecoupe = decouperTexte(textClair, dimension)
    textChiffre = ""
    for bloc in textDecoupe:
        blocNum, memoire = numeriserBloc(bloc)
        blocEncrypted = blocChar(encryptBloc(blocNum, matrice, dimension), memoire)
        for c in blocEncrypted:
            textChiffre = textChiffre + c
    print(f"texte clair: '{textClair}',\ttexte chiffré: '{textChiffre}'")

def decrypt(matrice, dimension, textChiffre):
    textDecoupe = decouperTexte(textChiffre, dimension)
    textClair = ""
    for bloc in textDecoupe:
        blocNum, memoire = numeriserBloc(bloc)
        blocClair = blocChar(decryptBloc(blocNum, matrice, dimension), memoire)
        for c in blocClair:
            textClair = textClair + c
    print(f"texte chiffré: '{textChiffre}',\ttexte clair: '{textClair}'")

PROCESSUS = [encrypt, decrypt]
def process(processus: int, text: str):
    dimension = int(input("Choisir la dimension de la matrice: "))
    print("Remplir la matrice:\n")
    matrice = []
    for i in range(dimension):
        line = []
        for j in range(dimension):
            while True:
                buffer = input(f"\nmatrice[{i}][{j}] = ")
                try:
                    buffer = int(buffer) % modulo
                    line.append(buffer)
                    break
                except ValueError:
                    print("Entrer un nombre valide s'il vous plait.")
        matrice.append(line)
    PROCESSUS[processus](matrice, dimension, text)
