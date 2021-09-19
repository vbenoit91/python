import json
import os.path
import sys

# RECUPERE LE REPERTOIRE PARENT DE MON SCRIPT
CUR_DIR = os.path.dirname(__file__)
# CONCATENATION DE CUR_DIR AVEC la chaine de caractère "liste.json"
LISTE_PATH = os.path.join(CUR_DIR, "liste.json")

if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as f:
        LISTE = json.load(f)
else:
    LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")
        
    # 1 - Ajouter un élément à la liste de courses        
    if user_choice == "1":
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté de la liste.")
    # 2 - Retirer un élément de la liste de courses
    elif user_choice == "2":
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"❌ L'élément {item} n'éxiste pas dans votre liste. Veuillez saisir un élément éxistant.")
    # 3 - Afficher les éléments de la liste de courses
    elif user_choice == "3":
        print("Voici le contenu de votre liste : ")
        if LISTE:
            for index, value in enumerate(LISTE, 1):
                print(f"{index}. {value}")
        else:
            print("❌ Votre liste ne contient au élément.")
    # 4 - Vider la liste de courses
    elif user_choice == "4":
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    # 5 - Quitter le programme
    elif user_choice == "5":
        with open(LISTE_PATH, "w") as f:
            json.dump(LISTE, f, indent=4)
        print("A bientôt !")
        sys.exit()

    print("-"*50)