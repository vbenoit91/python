import json
import os.path


# Vérifier si le fichier json existe ou non, si c'est le cas, tu dois lire le contenu de ce fichier et le stocker dans la variable LISTE afin qu'on puisse modifier la liste existante.
# Sinon, on part avec une liste vide.

# Quand l'utilisateur choisir de quitter le programme avec l'option 5, tu dois sauvegarder la liste sur le disque dans le fichier liste.json et l'écraser s'il existe déjà.

# Pour récupérer le chemin du dossier courant, vous pouvez utiliser cette ligne de code 
# CUR_DIR = os.path.dirname(__file__)


LISTE = []
chemin = "./liste.json"

# Le programme permet de réaliser 5 actions

while True:
    if os.path.exists(chemin) is True:
        print("1: Ajouter un élément à la liste\n2: Retirer un élément de la liste\n3: Afficher la liste\n4: Vider la liste\n5: Quitter")
        user_choice = input("👉 Votre choix : ")
        with open(chemin, "r") as f:
            LISTE = json.load(f)

        # 1 - Ajouter un élément à la liste de courses        
        if user_choice == "1":
            add = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
  
            if add not in LISTE:
                LISTE.append(add.capitalize())
                with open(chemin, "w") as f:
                    json.dump(LISTE, f, indent=4)
                print(f"L'élément {add} a bien été ajouté de la liste.")
            else:
                print(f"❌ L'élément {add} est déjà présent dans votre liste.")

        # 2 - Retirer un élément de la liste de courses
        elif user_choice == "2":
            delete = input("Entrez le nom d'un élément à retirer de la liste de courses : ")

            if delete in LISTE:
                LISTE.remove(delete)
                with open(chemin, "w") as f:
                    json.dump(LISTE, f, indent=4)
                print(f"L'élément {delete} a bien été supprimé de la liste.")
            else:
                print(f"❌ L'élément {delete} n'éxiste pas dans votre liste. Veuillez saisir un élément éxistant.")

        # 3 - Afficher les éléments de la liste de courses
        elif user_choice == "3":
            print("Voici le contenu de votre liste : ")
            if LISTE:
                for index, value in enumerate(LISTE, 1):
                    print(f"{index}. {value}")

        # 4 - Vider la liste de courses
        elif user_choice == "4":
            LISTE.clear()
            # ou
            # with open(chemin, "w") as f:
            #     json.dump([], f, indent=4)
            print("La liste a été vidée de son contenu.")

        # 5 - Quitter le programme
        elif user_choice == "5":
            print("A bientôt !")
            exit()

        else:
            print("Veuillez saisir un chiffre compris entre 1 et 5")        
            continue

    else: 
        open("./liste.json", "w")
        with open(chemin, "w") as f:
            json.dump([], f, indent=4)

    print("-"*50)

        
