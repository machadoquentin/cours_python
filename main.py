def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quelle est votre nom ? ")
    return nom
    
def demander_age(unNom):
    age=0
    while age==0:
        age_str = input(unNom + " quelle est votre age ? ")
        try:
            age = int(age_str)
        except:
            print("ERREUR: Vous devez entrez un nombre pour l'age")
    return age


def afficher_infos(nom, age):
    print()
    print(nom + " t'as " + str(age) + " ans.")
    if age>18:
        print("Tu es majeur")
    elif age == 18:
        print("Tout juste majeur")
    else:
        print("Tu es mineur")
    print(f"{nom} l'année prochaine tu auras {age+1} ans.") # f devant la chaine de caractere permet de concatener le contenu
    print("%s l'année prochaine tu auras %s ans." % (nom, (age+1))) # %s remplacer les variables et on les definies a la fin de la chaine de caractere

nom1 = demander_nom()
nom2 = demander_nom()
age1 = demander_age(nom1)
age2 = demander_age(nom2)


afficher_infos(nom1, age1)
afficher_infos(nom2, age2)

print("""
    On peut
        afficher 
            ce que l'on veux
""")