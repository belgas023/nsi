def shell(taille):
    if taille > 30:
        for i in range(4):
            forward(taille)
            right(90)
        left(20)
        shell(0.9 * taille,)


from turtle import *
penup()
goto(0,0)
pendown()


shell(200)