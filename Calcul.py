def nombreleplusgrand(a, b):
    if a > b:
        return a
    else:
        return b

def strlaplusgrande(a, b):
    if a > b:
        return a
    else:
        return b

première_valeur = int(input("Entrez la valeur du premier nombre (NOMBRE(S) ENTIER(S)) "))
seconde_valeur = int(input("Entrez la valeur du deuxième nombre (NOMBRE(S) ENTIER(S)) "))

première_str = str(input("Entrez une première chaîne de caractère "))
deuxième_str = str(input("Entrez une deuxième chaîne de caractère "))


print("Le plus grand nombre est", nombreleplusgrand(première_valeur, seconde_valeur))

print("La plus grande chaîne de caractère est", strlaplusgrande(première_str, deuxième_str))
