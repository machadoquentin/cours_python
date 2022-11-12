import random

nb_max = 10
nb_min = 0
nb_operateur = random.randint(0,1)

if nb_operateur == 0:
    operateur = "+"
else:
    operateur = "*"
nb_question = 4

def demander_calcul(nb_max, nb_min, operateur):
    nb1= random.randint(nb_min,nb_max)
    nb2= random.randint(nb_min,nb_max)   
    reponse = input(f"Combien fait {nb1} {operateur} {nb2} ? ")
    return reponse







