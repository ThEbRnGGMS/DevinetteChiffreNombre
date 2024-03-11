import random
import time

print("Bienvenue dans le jeux de la devinette")

time.sleep(1)

print("Le tout est sur 20 !!!")

time.sleep(1)

nbr_de_vie = 3

a = random.randint(0,20)
b = int(input("Trouve le nombre ou le chiffre : "))
    
while a!=b:
    
    time.sleep(1)
    
    if b>a: 
        print("En dessous")
    elif b<a:
        print("Au dessus")
    elif b == a:
        print("TROUVER !!!")

    nbr_de_vie -= 1

    time.sleep(1)
    
    if nbr_de_vie == 0:
        print("PERDU")
        
        time.sleep(1)
        
        print("Fin du jeux ")
        
        break

    print("il te reste",nbr_de_vie,"vie")

    time.sleep(1)

    b = int(input("Trouve le nombre ou le chiffre: "))

print("Le nombre était le numéro",a,)