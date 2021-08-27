# Le je comporte deux joueurs : vous et un ennemi
# Vous commencer tous les deux avec 50 points de vie
# Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.
# L'ennemi ne dispose d'aucune potion.
# Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
# Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.
# L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
# Lorsque vous utilisez une potion, vous passez le prochain tour.
from random import randint

#Initialisation de variables
myheart = 50
ennemyheart = 50
potion = 3

#Boucle while, boucle jusqu'à obtenir une variable égale à 0
while myheart > 0 and ennemyheart > 0:
    #Demande à l'utilisateur de choisir une variable entre 1 et 2
    check= input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    #Condition si myheart ou ennemyheart supérieur à 0 alors éxécute
    if (myheart > 0 and ennemyheart > 0):
        #Recherche un nombre aléatoire pour chaque variable
        myattack = randint(5,10)
        ennemyattack = randint(5,15)
        potionlife = randint(15,50)

        #Condition de vérification pour la saisie de l'utilisateur
        if check.isdigit() and check == "1":
            myheart = myheart - ennemyattack
            ennemyheart = ennemyheart - myattack
            print(f"Vous avez infligé {myattack} points de dégats à l'ennemi \u2694")
            print(f"L'ennemi vous a infligé {ennemyattack} points de dégats \u2694")
            print(f"Il vous reste {myheart} points de vie.")
            print(f"Il reste {ennemyheart} points de vie à l'ennemi.")
            print("--------------------------------------------------")
            
        elif check.isdigit() and check == "2":
            #Condition de verification, si l'utilisateur utilise une potion, on décrémente la variable potion de 1
            if potion != 0:
                potion -= 1            
            
                #Si les point de vies sont au maximum
                if myheart == 50:
                    print("Vous ne pouvez pas utiliser de potion car vos points de vies sont déjà au maximum.")
                    print("--------------------------------------------------")  
                    continue

                #Si les points de vies sont en dessous du maximum
                if myheart <= 50:
                    #Regain de point de vie            
                    myheart = myheart + potionlife
                    if myheart > 50:
                        myheart = 50
                        myheart = myheart - ennemyattack
                        print(f"Vous récupérer {potionlife} points de vie \u2764\uFE0F")
                        print(f"L'ennemi vous a infligé {ennemyattack} points de dégats \u2694")
                        print(f"Il vous reste {myheart} points de vie.")
                        print("--------------------------------------------------")
                        myheart = myheart - ennemyattack      
                        print("Vous passez votre tour...")                  
                        print(f"L'ennemi vous a infligé {ennemyattack} points de dégats \u2694")
                        print(f"Il vous reste {myheart} points de vie.")
                        print("--------------------------------------------------")                   
                    else:
                        myheart = myheart - ennemyattack
                        print(f"Vous récupérer {potionlife} points de vie \u2764\uFE0F")
                        print(f"L'ennemi vous a infligé {ennemyattack} points de dégats \u2694")
                        print(f"Il vous reste {myheart} points de vie.")
                        print("--------------------------------------------------")
                        myheart = myheart - ennemyattack
                        print("Vous passez votre tour...") 
                        print(f"L'ennemi vous a infligé {ennemyattack} points de dégats \u2694")
                        print(f"Il vous reste {myheart} points de vie.")
                        print("--------------------------------------------------")  

            else:
                print("Vous n'avez plus de potions...")
                print("--------------------------------------------------")   

        else:
            continue
    #Condition de verification si l'utilisateur n'a plus de points de vie.
    if myheart <= 0:
        myheart = 0
        print("[][][][][][[][][][][][[][][][][[][][][[][][][][[][][][[][][][]")
        print(f"Il vous reste {myheart} points de vie.")
        print(f"Il reste {ennemyheart} points de vie à l'ennemi.")
        print("Vous vous êtes fait ridiculisé par un Thanos, la prochaine fois appelez vos amis et amies Avengers pour vous aider ! Petite crotte de nez !")
        print("[][][][][][[][][][][][[][][][][[][][][[][][][][[][][][[][][][]")
        break
    #Condition de verification si l'ennemi n'a plus de points de vie.
    if ennemyheart <= 0:
        ennemyheart = 0
        print("[][][][][][[][][][][][[][][][][[][][][[][][][][[][][][[][][][]")
        print(f"Il vous reste {myheart} points de vie.")
        print(f"Il reste {ennemyheart} points de vie à l'ennemi.")        
        print("Bravo ! Vous avez ridiculisé Thanos ! Il lui aurait fallut encore 100 ans pour vous battre ! Félicitation vous avez le droit de manger des aubergines !")
        print("[][][][][][[][][][][][[][][][][[][][][[][][][][[][][][[][][][]")
        break