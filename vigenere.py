#chiffrement de vigenere
import cesar
import crypto_tool

#----------------implementation--------------------

alphabetOrdreMaj = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
alphabetOrdreMin = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
alphabet_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
modulo = len(alphabet_maj)

def encryptCarreVigenere(textClair: str):
    textChiffre = ""
    for c in textClair:
        if c.isupper():
            ch = cesar.decalerLettreAvant(c, alphabetOrdreMaj[c])
        else:
            ch = cesar.decalerLettreAvant(c, alphabetOrdreMin[c])
        textChiffre = textChiffre + ch
    print(f"texte clair: '{textClair}',\ttexte chiffré: '{textChiffre}'")

def encryptCle(textClair: str, cle: str):
    textChiffre = ""
    cases = setCases(textClair)
    _textClair = textClair.lower()
    cle = cle.lower()
    length = len(cle)
    i = 0
    for c in _textClair:
        ch_ord = (alphabetOrdreMin[c] + alphabetOrdreMin[cle[i]]) % modulo
        ch = alphabet_min[ch_ord]
        textChiffre = textChiffre + ch
        if i < (length - 1):
            i = i + 1
        else:
            i = 0
    _textChiffre = resetCases(textChiffre, cases)
    print(f"texte clair: '{textClair}',\ttexte chiffré: '{_textChiffre}'")

def kasiski(textChiffre: str):
    textChiffre = textChiffre.lower()
    mot = ""
    dists = []
    for i in range(len(textChiffre) - 3):
        pos1 = i
        mot = textChiffre[i:i+5]
        for j in range(i+6, len(textChiffre)):
            pos2 = j
            if mot == textChiffre[j:j+5]:
                dist = pos2 - pos1
                dists.append(dist)
    facteurs = []
    for dist in dists:
        facteurs.append(crypto_tool.factoriser(dist))
    print(f"\nFACTEURS:\n{facteurs}")
    facteur_frequent = crypto_tool.facteur_frequent(facteurs)
    return facteur_frequent

LETTRE_FRANÇAISE_PLUS_FREQUENTE = 'e'

def lettre_frequente(text: str):
    if not text: return 'e'
    return max(set(text), key=text.count)

def analyseFrequence(textChiffre: str, longueur_clé: int):
    if not longueur_clé:
        return None
    textChiffre = textChiffre.lower()
    cle = ""
    for i in range(longueur_clé):
        echantillon = ""
        for j in range(i, len(textChiffre) - 1, longueur_clé):
            echantillon = echantillon + textChiffre[j]
        _lettre_frequente = lettre_frequente(echantillon)
        ord_lettre_cle = (alphabetOrdreMin[_lettre_frequente] - alphabetOrdreMin[LETTRE_FRANÇAISE_PLUS_FREQUENTE]) % modulo
        lettre_cle = alphabet_min[ord_lettre_cle]
        cle = cle + lettre_cle
    return cle

def setCases(textChiffre: str):
    cases = []
    for c in textChiffre:
        if c.isupper():
            cases.append(1)
        else:
            cases.append(0)
    return cases

def resetCases(textClair: str, cases):
    result = ""
    i = 0
    for c in textClair.lower():
        if cases[i] == 1:
            result = result + textClair[i].upper()
        else:
            result = result + textClair[i]
        i = i + 1
    return result

def decryptCle(textChiffre: str, cle: str):
    textClair = ""
    cases = setCases(textChiffre)
    _textChiffre = textChiffre.lower()
    i = 0
    length = len(cle)
    for c in _textChiffre:
        ch_ord = (alphabetOrdreMin[c] - alphabetOrdreMin[cle[i]]) % modulo
        ch = alphabet_min[ch_ord]
        textClair = textClair + ch
        if i < (length - 1):
            i = i + 1
        else:
            i = 0
    _textClair = resetCases(textClair, cases)
    return _textClair

def decrypt(textChiffre: str):
    facteur_frequent = kasiski(textChiffre)
    print(f"\nfacteur_frequent = {facteur_frequent}\n")
    cle = analyseFrequence(textChiffre, facteur_frequent)
    print(f"\ncle = {cle}\n")
    if not cle:
        print("\nImpossible!\n")
    else:
        textClair = decryptCle(textChiffre, cle)
        print(f"texte chiffré: '{textChiffre}',\ntexte clair: '{textClair}'")

PROCESSUS = [encryptCarreVigenere, encryptCle, decrypt]
def process(processus: int, text: str):
    if processus == 0:
        while True:
            try:
                choix = int(input("\n1.\tCarré de Vigenère\n2.\tClé de Chiffrement\n\nchoix: "))
                if choix == 2:
                    cle = input("Donner la cle de chiffrement: ")
                    processus = 1
                    PROCESSUS[processus](text, cle)
                elif choix == 1:
                    PROCESSUS[processus](text)
                else:
                    raise ValueError
                break
            except ValueError:
                print("\nEntrer un choix valide s'il vous plait.\n")
    else:  
        processus = 2
        PROCESSUS[processus](text)
