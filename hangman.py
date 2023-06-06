import random,turtle,time

window = turtle.Screen()

turtle.bgpic('background.png')
turtle.color("white", "darkblue")


emri = turtle.textinput("Emri","Si quheni?")

print("\nTung "+ emri +', koha per te luajtur "Qello fjalen sekrete"')
time.sleep(2)

print("\nProvo te qellosh fjalen sekrete...")

time.sleep(0.5)
def teknologji():
    fjalet= ["kompjuter","ekran","softuer","harduer","folder"]
        
    fjala_sekrete = random.choice(fjalet)

    qello = ""

    radha = 12

    shkronjaeperdorur = ""

    vijat = ""
    
    shkronjaa=0
    
    radhaa=0
    
    for i in range(len(fjala_sekrete)):
        vijat+="_ "
    
    turtle.penup()
    turtle.setposition(-120, -195)
    style = ("Courier",20,"bold")
    turtle.write(vijat, font=style)
    turtle.pendown()    
    while radha > 0:
        deshtim = 0

        for shkronja in fjala_sekrete:
            if shkronja in qello:
                print(shkronja)
                if shkronjaa>=1 or radhaa>=1:
                    shkronjae_perdorur.clear()
                    gabim.clear()    
                
            else:
                print("_")
                deshtim += 1
        if deshtim == 0:
            print("***Fitove***")
            turtle.penup()
            turtle.setposition(-150, -195)
            style = ("Courier",20,"bold")
            turtle.write("Ti fitove, "+emri,"!", font=style)
            turtle.pendown()
            break
        print("")
        qello_shkronjen = turtle.textinput("Shkronja","Shkruaj nje shkronje: ")
        qello += qello_shkronjen
        if qello_shkronjen not in shkronjaeperdorur:
            shkronjaeperdorur += qello_shkronjen
            if qello_shkronjen not in fjala_sekrete:
                radha -=1
                radhaa+=1
                if radha ==11:
                    gabim = turtle.Turtle()
                    gabim.color("white")
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.penup()
                    turtle.left(90)
                    turtle.forward(150)
                    turtle.right(90)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(50)
                    turtle.end_fill()
                elif radha == 10:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    gabim.clear()
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.right(90)
                    turtle.forward(50)
                elif radha == 9:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.right(45)
                    turtle.forward(80)
                    turtle.right(180)
                    turtle.forward(80)
                elif radha == 8:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.right(90)
                    turtle.forward(80)
                    turtle.backward(80)
                elif radha == 7:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.right(45)
                    turtle.forward(150)
                elif radha == 6:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.right(45)
                    turtle.forward(80)
                    turtle.right(180)
                    turtle.forward(80)
                elif radha == 5:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.right(90)
                    turtle.forward(80)
                    turtle.backward(80)
                elif radha == 4:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.pensize(3)
                    turtle.penup()
                    turtle.goto(-20,205)
                    turtle.pendown()
                    turtle.color("white", "blue")
                    turtle.circle(5)
                elif radha == 3:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.penup()
                    turtle.goto(15,205)
                    turtle.pendown()
                    turtle.color("white", "blue")
                    turtle.circle(5)
                elif radha == 2:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.penup()
                    turtle.goto(0,195)
                    turtle.pendown()
                    turtle.right(45)
                    turtle.forward(10)
                elif radha == 1:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    if shkronjaa>=1:
                        shkronjae_perdorur.clear()
                    gabim.clear()
                    gabim.penup()
                    gabim.setposition(-240, -240)
                    style = ("Courier",15,"bold")
                    gabim.write("Gabim, ti ke edhe "+str(radha)+" here per te provuar!", font=style)
                    gabim.pendown()
                    turtle.penup()
                    turtle.goto(-15,170)
                    turtle.pendown()
                    turtle.left(90)
                    turtle.forward(30)
                    turtle.penup()
                    turtle.goto(-110,195)
                if radha == 0:
                    print("\nHumbe!")
                    turtle.penup()
                    turtle.setposition(-150, -195)
                    style = ("Courier",20,"bold")
                    turtle.write("Ti humbe, "+emri+"!", font=style)
                    turtle.pendown()
        else:
            if shkronjaa==0:
                shkronjae_perdorur = turtle.Turtle()
                shkronjae_perdorur.color("white")
                shkronjae_perdorur.penup()
                gabim.clear()
                shkronjae_perdorur.setposition(-180, -240)
                style = ("Courier",15,"bold")
                shkronjae_perdorur.write('Shkronja "'+qello_shkronjen+'" eshte perdorur!', font=style)
                shkronjae_perdorur.pendown()
                shkronjaa=+1
            else:
                gabim.clear()
                shkronjae_perdorur.clear()
                shkronjae_perdorur.penup()
                shkronjae_perdorur.setposition(-180, -240)
                style = ("Courier",15,"bold")
                shkronjae_perdorur.write('Shkronja "'+qello_shkronjen+'" eshte perdorur!', font=style)
                shkronjae_perdorur.pendown()
                
def kafshe():
    fjalet= ["lepuri","breshka","macja","qeni","leopardi"]
        
    fjala_sekrete = random.choice(fjalet)

    qello = ""

    radha = 12

    shkronjaeperdorur = ""

    while radha > 0:
        deshtim = 0

        for shkronja in fjala_sekrete:
            if shkronja in qello:
                print(shkronja)
            else:
                print("_")
                deshtim += 1
        if deshtim == 0:
            print("***Fitove***")
            turtle.penup()
            turtle.setposition(-150, -195)
            style = ("Courier",20,"bold")
            turtle.write("Ti fitove, "+emri,"!", font=style)
            turtle.pendown()
            break

        print("")
        qello_shkronjen = input("Shkruaj nje shkronje: ")

        qello += qello_shkronjen
        if qello_shkronjen not in shkronjaeperdorur:
            shkronjaeperdorur += qello_shkronjen
            if qello_shkronjen not in fjala_sekrete:
                radha -=1
                if radha ==11:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.pensize(5)
                    turtle.penup()
                    turtle.left(90)
                    turtle.forward(150)
                    turtle.right(90)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(50)
                    turtle.end_fill()
                elif radha == 10:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(90)
                    turtle.forward(50)
                elif radha == 9:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(45)
                    turtle.forward(80)
                    turtle.right(180)
                    turtle.forward(80)
                elif radha == 8:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(90)
                    turtle.forward(80)
                    turtle.backward(80)
                elif radha == 7:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(45)
                    turtle.forward(150)
                elif radha == 6:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(45)
                    turtle.forward(80)
                    turtle.right(180)
                    turtle.forward(80)
                elif radha == 5:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(90)
                    turtle.forward(80)
                    turtle.backward(80)
                elif radha == 4:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.pensize(3)
                    turtle.penup()
                    turtle.goto(-20,205)
                    turtle.pendown()
                    turtle.color("white", "blue")
                    turtle.circle(5)
                elif radha == 3:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.penup()
                    turtle.goto(15,205)
                    turtle.pendown()
                    turtle.color("white", "blue")
                    turtle.circle(5)
                elif radha == 2:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.penup()
                    turtle.goto(0,195)
                    turtle.pendown()
                    turtle.right(45)
                    turtle.forward(10)
                elif radha == 1:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.penup()
                    turtle.goto(-15,170)
                    turtle.pendown()
                    turtle.left(90)
                    turtle.forward(30)
                    turtle.penup()
                    turtle.goto(-110,195)
                if radha == 0:
                    print("\nHumbe!")
                    turtle.penup()
                    turtle.setposition(-150, -195)
                    style = ("Courier",20,"bold")
                    turtle.write("Ti humbe, "+emri+"!", font=style)
                    turtle.pendown()
        else:
            print("Shkronja",qello_shkronjen,"eshte perdorur!")
            
def sporte():
    fjalet = ["futboll","basketboll","hendboll","tenis","pingpong"]
        
    fjala_sekrete = random.choice(fjalet)

    qello = ""

    radha = 12

    shkronjaeperdorur = ""

    while radha > 0:
        deshtim = 0

        for shkronja in fjala_sekrete:
            if shkronja in qello:
                print(shkronja)
            else:
                print("_")
                deshtim += 1
        if deshtim == 0:
            print("***Fitove***")
            turtle.penup()
            turtle.setposition(-150, -195)
            style = ("Courier",20,"bold")
            turtle.write("Ti fitove, "+emri,"!", font=style)
            turtle.pendown()
            break

        print("")
        qello_shkronjen = input("Shkruaj nje shkronje: ")

        qello += qello_shkronjen
        if qello_shkronjen not in shkronjaeperdorur:
            shkronjaeperdorur += qello_shkronjen
            if qello_shkronjen not in fjala_sekrete:
                radha -=1
                if radha ==11:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.pensize(5)
                    turtle.penup()
                    turtle.left(90)
                    turtle.forward(150)
                    turtle.right(90)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(50)
                    turtle.end_fill()
                elif radha == 10:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(90)
                    turtle.forward(50)
                elif radha == 9:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(45)
                    turtle.forward(80)
                    turtle.right(180)
                    turtle.forward(80)
                elif radha == 8:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(90)
                    turtle.forward(80)
                    turtle.backward(80)
                elif radha == 7:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(45)
                    turtle.forward(150)
                elif radha == 6:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(45)
                    turtle.forward(80)
                    turtle.right(180)
                    turtle.forward(80)
                elif radha == 5:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.right(90)
                    turtle.forward(80)
                    turtle.backward(80)
                elif radha == 4:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.pensize(3)
                    turtle.penup()
                    turtle.goto(-20,205)
                    turtle.pendown()
                    turtle.color("white", "blue")
                    turtle.circle(5)
                elif radha == 3:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.penup()
                    turtle.goto(15,205)
                    turtle.pendown()
                    turtle.color("white", "blue")
                    turtle.circle(5)
                elif radha == 2:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.penup()
                    turtle.goto(0,195)
                    turtle.pendown()
                    turtle.right(45)
                    turtle.forward(10)
                elif radha == 1:
                    print("\n***Gabim***")
                    print("\nJu keni edhe",radha, "here per te provuar!")
                    turtle.penup()
                    turtle.goto(-15,170)
                    turtle.pendown()
                    turtle.left(90)
                    turtle.forward(30)
                    turtle.penup()
                    turtle.goto(-110,195)
                if radha == 0:
                    print("\nHumbe!")
                    turtle.penup()
                    turtle.setposition(-150, -195)
                    style = ("Courier",20,"bold")
                    turtle.write("Ti humbe, "+emri+"!", font=style)
                    turtle.pendown()
        else:
            print("Shkronja",qello_shkronjen,"eshte perdorur!")


