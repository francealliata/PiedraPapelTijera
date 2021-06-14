import random, os, sys 
computerscore = 0
userscore = 0
numgames = int(input("Bienvenido.\nCuantas veces te gustaria jugar?\n"))
userinput = ""
computerchoice = ""
userwin = False
draw = False
choice = ""
clear = lambda: os.system("cls")

for x in range(0, numgames):
    generatednum = random.randint(1,3)
    if generatednum == 1:
        computerchoice = "Piedra"
    elif generatednum == 2:
        computerchoice = "Papel"
    elif generatednum == 3:
        computerchoice = "Tijera"

    userinput = input("Seleccionar Piedra, Papel, or Tijera\n")

    if userinput == "Piedra" and computerchoice == "Tijera":
        print("Elegiste",userinput,"Y la computadora eligio: ",computerchoice,", Ganaste!")
        userscore += 1
    elif userinput == "Piedra" and computerchoice == "Papel":
        print("Elegiste",userinput,"Y la computadora eligio: ",computerchoice,", Perdiste!")
        computerscore += 1
    if userinput == "Papel" and computerchoice == "Piedra":
        print("Elegiste",userinput,"Y la computadora eligio: ",computerchoice,", Ganaste!")
        userscore += 1
    elif userinput == "Papel" and computerchoice == "Tijera":
        print("Elegiste",userinput,"Y la computadora eligio: ",computerchoice,", Perdiste!")
        computerscore += 1
    if userinput == "Tijera" and computerchoice == "Papel":
        print("Elegiste",userinput,"Y la computadora eligio: ",computerchoice,", Ganaste!")
        userscore += 1
    elif userinput == "Tijera" and computerchoice == "Piedra":
        print("Elegiste",userinput,"Y la computadora eligio: ",computerchoice,", Perdiste!")
        computerscore += 1

if userscore > computerscore:
    userwin = True
elif userscore == computerscore:
    draw = True

if userwin == True:
    print("Felicitaciones, Ganaste!\nTu puntuacion es:",userscore,"\nLa puntuacion de la computadora es:",computerscore)
elif draw == True:
    print("Empate!\nTu puntuacion es:",userscore,"\nLa puntuacion de la computadora es:",computerscore)
elif userwin == False:
    print("Perdiste.\nTu puntuacion es:",userscore,"\nLa puntuacion de la computadora es:",computerscore)

choice = str(input("Queres jugar de nuevo? s/n\n"))
if choice == "s":
    clear()
    os.system("piedrapapeltijera.py")
