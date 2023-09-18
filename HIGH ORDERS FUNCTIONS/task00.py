def funA(mot:str, nombre:int):
    compteur = 0
    for lettre in mot:
        if lettre.isupper():
            compteur += 1
    return f"Votre mot de passe contient {compteur} majuscules" if compteur >= nombre else f"Veuillez mettre au moins {nombre} majuscules dans votre mot de passe"

# print(funA(mot, nombre)) 

def funB(mot:str, nombre:int):
    compteur = 0
    for lettre in mot:
        if lettre.islower():
            compteur += 1
    return f"Votre mot de passe contient {compteur} minuscules" if compteur >= nombre else f"Veuillez mettre au moins {nombre} minuscules dans votre mot de passe"
# print(funB(mot, nombre))

def funC(mot:str, nombre:int):
    return len(mot) >= nombre
    
# print(funC(mot, nombre))

def funD(mot:str, nombre:int):
    compteur = 0
    for lettre in mot:
        if not lettre.isalpha() and lettre.isalnum() == False:   # le "not" simplifie:    if lettre.isalpha() == False
            compteur += 1
    return f"Le mot contient {compteur} caractères spéciaux ce qui est supérieur à {nombre}" if compteur >= nombre else f"Le mot contient {compteur} caractères spéciaux ce qui est inférieur à {nombre}" 
# print(funD(mot, nombre))

def funE(mot:str, nombre:int):
    compteur = 0
    for i in mot:
        if i.isalnum():
            compteur += 1
    return compteur >= nombre

# print(funE(mot, nombre))

# TASK 01

def fun_Minuscule(mot:str, nombre: int):
    compteur = 0
    for lettre in mot:
        if lettre.islower():
            compteur += 1
    return compteur >= nombre

def fun_Special(mot:str, nombre:int):
    compteur = 0
    nombre = 2
    for lettre in mot:
        if not lettre.isalpha() and lettre.isalnum() == False:   # le "not" simplifie:    if lettre.isalpha() == False
            compteur += 1
    return f"Le mot contient {compteur} caractères spéciaux ce qui est supérieur à {nombre}" if compteur == nombre else f"Le mot contient {compteur} caractères spéciaux ce qui est inférieur à {nombre}" 


def check_password(fonction, string, nombre):
    return fonction(string ,nombre)

mot_de_passe = input("Quel est votre mot de passe? ")
result_minuscules = check_password(funB, mot_de_passe, 4)
result_special = check_password(funD, mot_de_passe, 2)
print(result_minuscules)
print(result_special)
