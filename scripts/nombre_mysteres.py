from random import randint

a = randint(0,100+1)
b = 0

while b < 6:
    try:
        if(b == 0):
            print("Il te reste 5 essais.")
            c = int(input("Devine le nombre : "))
            if(c > a):
                print("Le nombre mystère est plus petit.")
            elif(c < a):
                print("Le nombre mystère est plus grand.")
            else:
                print(f"Bravo ! Le nombre mystère était bien {a}")
                print(f"Tu as trouvé le nombre en {b+1} essais.")
                print("Fin de jeu.")
                break

        elif(b == 1):
            print("Il te reste 4 essais.")
            c = int(input("Devine le nombre : "))
            if(c > a):
                print("Le nombre mystère est plus petit.")
            elif(c < a):
                print("Le nombre mystère est plus grand.")
            else:
                print(f"Bravo ! Le nombre mystère était bien {a}")       
                print(f"Tu as trouvé le nombre en {b+1} essais.")
                print("Fin de jeu.")
                break

        elif(b == 2):
            print("Il te reste 3 essais.")
            c = int(input("Devine le nombre : "))
            if(c > a):
                print("Le nombre mystère est plus petit.")
            elif(c < a):
                print("Le nombre mystère est plus grand.")
            else:
                print(f"Bravo ! Le nombre mystère était bien {a}")
                print(f"Tu as trouvé le nombre en {b+1} essais.")
                print("Fin de jeu.")
                break     

        elif(b == 3):
            print("Il te reste 2 essais.")
            c = int(input("Devine le nombre : "))
            if(c > a):
                print("Le nombre mystère est plus petit.")
            elif(c < a):
                print("Le nombre mystère est plus grand.")
            else:
                print(f"Bravo ! Le nombre mystère était bien {a}")
                print(f"Tu as trouvé le nombre en {b+1} essais.")
                print("Fin de jeu.")
                break

        elif(b == 4):
            print("Il te reste 1 essai.")
            c = int(input("Devine le nombre : "))
            if(c != a):
                print(f"Dommage ! Le nombre mystère était {a}")
                print("Fin de jeu.")
                break
            else:
                print(f"Bravo ! Le nombre mystère était bien {a}")   
                print(f"Tu as trouvé le nombre en {b+1} essais.")
                print("Fin de jeu.")
                break
        
        b += 1
    
    except ValueError:
        print("Veuillez entrer un nombre valide.")

