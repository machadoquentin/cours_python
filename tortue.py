import turtle

t = turtle.Turtle()

def escalier(taille, nb_marche):
    for i in range(0,nb_marche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -= 2

def carre(taille):
    for i in range(0,4):
        t.forward(taille)
        t.left(90)

def carres(taille, nb_carre):
    for i in range(0, nb_carre):
        carre(taille)
        taille += 10

escalier(30,10)
carre(100)
carres(100, 4)
turtle.done()