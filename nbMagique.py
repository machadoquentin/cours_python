#Imports
import random

#Declaration des varibales

NB_MAX = 10
NB_MIN = 1
NB_VIES = 4
reponse = random.randint(1,10)
proposition = 0
 
#Methodes
def demander_nombre(NB_MAX, NB_MIN):
    proposition = 0
    while proposition==0:
        proposition_str = input("Choisissez un nombre (entre 1 et 10) : ")
        try:
            proposition = int(proposition_str)
        except:
            print("Veuillez entrer un nombre entier")
        else:
            if proposition < NB_MIN or proposition > NB_MAX:
                print("Le nombre doit etre entre 1 et 10")

    return proposition


#Execution
print(reponse)
while not proposition == reponse and NB_VIES>0 :
    print (f"Il vous reste {NB_VIES} vie(s)") 
    proposition = demander_nombre(NB_MAX, NB_MIN)
    if proposition == reponse:
        print("C'est gagné, bravo")
    elif proposition > reponse:
        print("C'est plus petit")
        NB_VIES -=1
    else: 
        print("C'est plus grand")
        NB_VIES -=1

if NB_VIES == 0:
    print(f"Vous avez perdu, la réponse était {reponse}")