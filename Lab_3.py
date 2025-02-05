#game
import tkinter as tk
from tkinter import ttk
import math

root = tk.Tk()
root.title("Idle game")

#size = taille de la fenetre
windowsizeX = 200
windowsizeY = 500
root.minsize(windowsizeX, windowsizeY)
root.maxsize(windowsizeX, windowsizeY)

#variable
money = 0                    # l'argent en temps réel
click_power_base = 1         # Puissance de click
multiplier = 1               # Multiplicateur d'argent
price = [10,500,7500]        # prix des upgrade
afk_price = [50,700,2500]    # prix des upgrade AFK
afk_gain = 0                 # Puissance de gain AFK
update_time = 1000           # Vitesse de la loop (1000 = Chaque sec)(Rafraichissement d'image)
New_upgrade_price = 1000000  # prix de l'upgrade de nouvelle fenetre
if_New_upgrade_is_buy = 0    # variable qui permet de ne pas devoir repayer la nouvelle fenetre

#Fonction pour les répétition
def MoneyConfig():
    T_money.config(text = (f"{math.floor(money * 10)/10} $"))
def TapConfig():
    T_tap.config(text = f"tap {math.floor(click_power_base * 10)/10} x {multiplier}")
def AFK_gameConfig():
    T_gain_sec.config(text = f"AFK gain: {math.floor(afk_gain*10)/10} x {multiplier}")
    
#loop = lorsque activé elle permet d'activé des gain par seconde. 
def update_label():
    global money, afk_gain
    money = money + afk_gain * multiplier
    MoneyConfig()
    root.after(update_time, update_label)

#click = premier bouton
def on_click():
    global money, multiplier, click_power_base
    money = money + click_power_base*multiplier
    MoneyConfig()
    if money >= 0 and click_power_base >= 0:
        print(money)

#upgrade +0.1
def upgrade1():
    global money, price, click_power_base
    if money >= price[0]:
        click_power_base = click_power_base + 0.1
        money = money-price[0]
        price[0] = price[0] * 1.1
        price[0] = math.floor(price[0])
        upgrade_button1.config(text=f"{price[0]}$ = +0.1")
        MoneyConfig()
        TapConfig()

#upgrade +1
def upgrade2():
    global money, price, click_power_base
    if money >= price[1]:
        click_power_base=click_power_base+1
        money = money-price[1]
        price[1] = price[1]*1.1
        price[1] = math.floor(price[1])
        upgrade_button2.config(text = f"{price[1]}$ = +1")
        MoneyConfig()
        TapConfig()

#upgrade +5
def upgrade3():
    global money, price, click_power_base
    if money >= price[2]:
        click_power_base=click_power_base+5
        money = money - price[2]
        price[2] = price[2] * 1.1
        price[2] = math.floor(price[2])
        upgrade_button3.config(text = f"{price[2]} $ = +5")
        MoneyConfig()
        TapConfig()

#afk upgrade +1s
def afk_upgrade1():
    global money, afk_price, afk_gain
    if money >= afk_price[0]:
        afk_gain = afk_gain + 1
        money = money - afk_price[0]
        afk_price[0] = afk_price[0] * 1.1
        afk_price[0] = math.floor(afk_price[0])
        afk_button1.config(text = f"{afk_price[0]} $ = +1s")
        MoneyConfig()
        AFK_gameConfig()
        if afk_gain == 1:
            update_label()
        if afk_gain == 10:
            afk_button2.config(text = f"{afk_price[1]} $ = +5s")

#upgrade +5s
def afk_upgrade2():
    global money, afk_price, afk_gain
    if afk_gain >= 10:
        if money >= afk_price[1]:
            afk_gain = afk_gain + 5
            money = money - afk_price[1]
            afk_price[1] = afk_price[1] * 1.1
            afk_price[1] = math.floor(afk_price[1])
            afk_button2.config(text = f"{afk_price[1]} $ = +5s")
            MoneyConfig()
            AFK_gameConfig()

#upgrade of multiplier and Time = creation de la deuxieme fenetre
def Window_2():
    global money, if_New_upgrade_is_buy
    if if_New_upgrade_is_buy == 0:
        if_New_upgrade_is_buy += 1
        money -=New_upgrade_price
        MoneyConfig()
        
#definition = création de tout les bouton et zone de texte
button1 = ttk.Button(root, text="Click Here", command = on_click)
upgrade_button1 = ttk.Button(root, text = f"{price[0]} $ = +0.1",command = upgrade1)
upgrade_button2 = ttk.Button(root, text = f"{price[1]} $ = +1"  ,command = upgrade2)
upgrade_button3 = ttk.Button(root, text = f"{price[2]} $ = +5"  ,command = upgrade3)
afk_button1 = ttk.Button(root, text = f"{afk_price[0]} $ = +1s",command = afk_upgrade1)
afk_button2 = ttk.Button(root, text = "locked",command = afk_upgrade2)
Time_Mult_Upgrade_Button = ttk.Button(root, text = f"New Upgrade = {New_upgrade_price}$ ", command = Window_2)
T_money = ttk.Label(root, text=(f"{money} $"))
T_upgrade = ttk.Label(root, text= "Upgrade")
T_afk_upgrade = ttk.Label(root, text = "AFK Upgrade" )
T_tap = ttk.Label(root, text = f"tap: {click_power_base} x {multiplier}")
T_gain_sec = ttk.Label(root, text = f"AFK gain: {afk_gain}s x {multiplier}")

#UI = possition des bouton et zone de texte
T_money.pack(pady = 10)
T_tap.pack()
T_gain_sec.pack()
button1.pack(pady = 20)
T_upgrade.pack(pady = 5)
upgrade_button1.pack(pady = 1)
upgrade_button2.pack(pady = 1)
upgrade_button3.pack(pady = 1)
T_afk_upgrade.pack(pady = 5)
afk_button1.pack(pady = 1)
afk_button2.pack(pady = 1)
Time_Mult_Upgrade_Button.pack(pady = 50)

# loop qui permet d"actioner la fenetre
root.mainloop()