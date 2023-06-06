import random,turtle,time

window = turtle.Screen()
turtle.bgpic('background.png')

turtle.color("lightyellow")
turtle.penup()
turtle.setposition(-190, 190)
style = ("Comic Sans MS",20,"bold")
turtle.write("ZGJIDHNI NJË KATEGORI", font=style)
turtle.pendown()

#teknologji
teknologji = turtle.Turtle()
teknologji.color("white", "lightgreen")
teknologji.hideturtle()
teknologji.penup()
teknologji.setpos(-100, 80)
teknologji.pendown()
teknologji.begin_fill()

for i in range(2):
    teknologji.forward(197)
    teknologji.left(90)
    teknologji.forward(50)
    teknologji.left(90)
    

teknologji.end_fill()
teknologji.penup()

teknologji.setposition(-100, 80)
style = ("Courier",25,"bold")
teknologji.write("Teknologji", font=style)
teknologji.pendown()

#Kafshe
kafshe = turtle.Turtle()
kafshe.color("white", "lightgreen")
kafshe.hideturtle()
kafshe.penup()
kafshe.setpos(-100, 0)
kafshe.pendown()
kafshe.begin_fill()

for i in range(2):
    kafshe.forward(197)
    kafshe.left(90)
    kafshe.forward(50)
    kafshe.left(90)
    

kafshe.end_fill()
kafshe.penup()

kafshe.setposition(-55, 0)
style = ("Courier",25,"bold")
kafshe.write("Kafsh\xeb", font=style)
kafshe.pendown()

#sporte
sporte = turtle.Turtle()
sporte.color("white", "lightgreen")
sporte.hideturtle()
sporte.penup()
sporte.setpos(-100, -80)
sporte.pendown()
sporte.begin_fill()

for i in range(2):
    sporte.forward(197)
    sporte.left(90)
    sporte.forward(50)
    sporte.left(90)
    

sporte.end_fill()
sporte.penup()

sporte.setposition(-55, -80)
style = ("Courier",25,"bold")
sporte.write("Sporte", font=style)
sporte.pendown()


def butoni(x,y):
    if x<97 and x>-100 and y>80 and y<130:
        window.clear()
        import hangman
        hangman.teknologji()
        
    if x<97 and x>-100 and y>0 and y<30:
        window.clear()
        import hangman
        hangman.kafshe()
        
    if x<97 and x>-100 and y>-60 and y<-30:
        window.clear()
        import hangman
        hangman.sporte()

turtle.onscreenclick(butoni,1)
turtle.listen()
turtle.done()
