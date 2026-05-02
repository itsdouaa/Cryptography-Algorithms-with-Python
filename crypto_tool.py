import math

def calc_reste(dividende: int, diviseur: int):
    reste = dividende
    while reste >= diviseur:
        reste = reste - diviseur
    return reste
    
def calc_quotient(dividende: int, diviseur: int):
    rest = calc_reste(dividende, diviseur)
    quotient = (dividende - rest) / diviseur
    return quotient
    
def euclide_algo(superieur: int, inferieur: int):
    details = {}
    reste = calc_reste(superieur, inferieur)
    quotient = calc_quotient(superieur, inferieur)
    details[reste] = [superieur, inferieur, quotient]
    while reste != 0:
        superieur = inferieur
        inferieur = reste
        reste = calc_reste(superieur, inferieur)
        quotient = calc_quotient(superieur, inferieur)
        details[reste] = [superieur, inferieur, quotient]
    if reste == 0:
        pgcd = inferieur
        return pgcd, details
    
def inverse_multiplicatif(number: int, modulo: int=26):
    return pow(number, -1, modulo)

def obtenir_sous_matrice(m, i, j):
    return [ligne[:j] + ligne[j+1:] for ligne in (m[:i] + m[i+1:])]

def calculer_determinant(m):
    n = len(m)
    if n == 1: return m[0][0]
    if n == 2: return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    
    det = 0
    for j in range(n):
        signe = (-1) ** j
        sous_det = calculer_determinant(obtenir_sous_matrice(m, 0, j))
        det += signe * m[0][j] * sous_det
    return det

def inverseMatrice(matrice, dimension):
    det = calculer_determinant(matrice) % 26
    if det == 0 or math.gcd(det, 26) != 1:
        return -1
    inv_det = pow(det, -1, 26)
    adj = []
    for i in range(dimension):
        ligne_adj = []
        for j in range(dimension):
            sous_matrice = obtenir_sous_matrice(matrice, j, i)
            signe = (-1) ** (i + j)
            cofacteur = (signe * calculer_determinant(sous_matrice)) % 26
            ligne_adj.append((cofacteur * inv_det) % 26)
        adj.append(ligne_adj) 
    return adj
