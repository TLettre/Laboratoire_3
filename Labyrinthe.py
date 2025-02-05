def labyrinthe():
    position = "entrée"
    print("Bienvenue dans le labyrinthe ! Votre objectif est de trouver la sortie.")

    while position != "sortie":
        if position == "entrée":
            print("Vous êtes à l'entrée du labyrinthe. Vous pouvez aller à l'est ou au sud.")
            choix = input("Où voulez-vous aller ? (est/sud) : ")
            if choix == "est":
                position = "salle sombre"
            elif choix == "sud":
                position = "cul-de-sac 1"
            else:
                print("Direction invalide. Essayez encore.")

        elif position == "salle sombre":
            print("Vous êtes dans une salle sombre. Il y a des passages au nord, à l'ouest et au sud.")
            choix = input("Où voulez-vous aller ? (nord/ouest/sud) : ")
            if choix == "nord":
                position = "couloir étroit"
            elif choix == "ouest":
                position = "entrée"
            elif choix == "sud":
                position = "salle secrète"
            else:
                print("Direction invalide. Essayez encore.")

        elif position == "cul-de-sac 1":
            print("Vous êtes dans un cul-de-sac. Vous devez revenir sur vos pas.")
            choix = input("Revenez en arrière ? (oui/non) : ")
            if choix == "oui":
                position = "entrée"
            else:
                print("Vous ne pouvez pas rester ici éternellement.")

        elif position == "couloir étroit":
            print("Vous êtes dans un couloir étroit. Vous pouvez aller à l'est, au sud ou à l'ouest.")
            choix = input("Où voulez-vous aller ? (est/sud/ouest) : ")
            if choix == "est":
                position = "cul-de-sac 2"
            elif choix == "sud":
                position = "salle sombre"
            elif choix == "ouest":
                position = "galerie étroite"
            else:
                print("Direction invalide. Essayez encore.")

        elif position == "cul-de-sac 2":
            print("Encore un cul-de-sac. Il faut revenir en arrière.")
            choix = input("Revenez en arrière ? (oui/non) : ")
            if choix == "oui":
                position = "couloir étroit"
            else:
                print("Il n'y a pas d'autre choix ici.")

        elif position == "salle des échos":
            print("Vous êtes dans la salle des échos. Vous entendez un courant d'air à l'est.")
            choix = input("Où voulez-vous aller ? (est/sud) : ")
            if choix == "est":
                position = "sortie"
            elif choix == "sud":
                position = "galerie étroite"
            else:
                print("Direction invalide. Essayez encore.")

        elif position == "salle secrète":
            print("Vous avez trouvé une salle secrète. Il y a un passage caché à l'est.")
            choix = input("Voulez-vous explorer ? (est/nord) : ")
            if choix == "est":
                position = "galerie étroite"
            elif choix == "nord":
                position = "salle sombre"
            else:
                print("Direction invalide. Essayez encore.")

        elif position == "galerie étroite":
            print("Vous êtes dans une galerie étroite. Des passages mènent au nord et à l'est.")
            choix = input("Où voulez-vous aller ? (nord/est) : ")
            if choix == "nord":
                position = "salle des échos"
            elif choix == "est":
                position = "couloir étroit"
            else:
                print("Direction invalide. Essayez encore.")

    print("Félicitations ! Vous avez trouvé la sortie du labyrinthe.")

labyrinthe()
