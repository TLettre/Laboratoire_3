"""    
### supression de Time qui est inutile pour mon code 

### supression de Root.Geometry qui est inutile il est déjà seté par les variable de
    minimum et maximum size de root. ce qui me permet de changé la grandeur de mon interface 
    vraiment facilement et rapidement.

    #size
    windowsizeX = 200
    windowsizeY = 500
    root.minsize(windowsizeX, windowsizeY)
    root.maxsize(windowsizeX, windowsizeY)

### mes variable son correct, claire et elle respecte les regles de codage.

### j'ai ajouté une section (Fonction pour les répétition) qui permet de simplifier l'ensemble du code

    ex: #Fonction pour les répétition

        def MoneyConfig():
        T_money.config(text = f"{money} $")

    dans cette section je pourai ajouter plein de fonction qui permeteront par la suite
    de rendre mon code beaucoup plus claire et facile a lire

### J'ai enlever des money = math.floor(money * 10)/10 qui ne servait a rien étant donné cette demande est dans MoneyConfig

### J'ai enlever T_tap.config(text = f"tap {math.floor(click_power_base * 10)/10} x {multiplier}") dans la section Click 
    car elle n'a aucune utiliter
    
### J'ai corigé les erreur de regles de codage

### J ai documenter mon code
"""