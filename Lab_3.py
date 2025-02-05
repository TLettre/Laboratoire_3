#game
import tkinter as tk
from tkinter import ttk
import time
import math

root = tk.Tk()
root.geometry("200x200")
root.title("Idle game")
#size
windowsizeX = 200
windowsizeY = 500
root.minsize(windowsizeX, windowsizeY)
root.maxsize(windowsizeX, windowsizeY)
#variable
money = 0
click_power_base = 1
multiplier = 1
price = [10,500,7500]
afk_price = [50,700,2500]
afk_gain = 0
update_time = 1000
New_upgrade_price = 1000000
if_New_upgrade_is_buy = 0
#loop
def update_label():
    global money, afk_gain
    money = money + afk_gain * multiplier
    money = math.floor(money*10)/10
    T_money.config(text = f"{money} $")
    root.after(update_time,update_label)
#click
def on_click():
    global money, multiplier, click_power_base
    money = money + click_power_base*multiplier
    money = math.floor(money * 10)/10
    T_money.config(text = f"{money} $")
    T_tap.config(text = f"tap {math.floor(click_power_base * 10)/10} x {multiplier}")
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
        T_money.config(text=(f"{math.floor(money*10)/10} $"))
        T_tap.config(text = f"tap {math.floor(click_power_base*10)/10} x {multiplier}")
#upgrade +1
def upgrade2():
    global money, price, click_power_base
    if money >= price[1]:
        click_power_base=click_power_base+1
        money = money-price[1]
        price[1] = price[1]*1.1
        price[1] = math.floor(price[1])
        upgrade_button2.config(text=f"{price[1]}$ = +1")
        T_money.config(text=(f"{math.floor(money*10)/10} $"))
        T_tap.config(text = f"tap {math.floor(click_power_base*10)/10} x {multiplier}")
#upgrade +5
def upgrade3():
    global money, price, click_power_base
    if money >= price[2]:
        click_power_base=click_power_base+5
        money = money - price[2]
        price[2] = price[2] * 1.1
        price[2] = math.floor(price[2])
        upgrade_button3.config(text=f"{price[2]} $ = +5")
        T_money.config(text=(f"{math.floor(money*10)/10} $"))
        T_tap.config(text = f"tap {math.floor(click_power_base*10)/10} x {multiplier}")
#afk upgrade +1s
def afk_upgrade1():
    global money, afk_price, afk_gain
    if money >= afk_price[0]:
        afk_gain = afk_gain + 1
        money = money - afk_price[0]
        afk_price[0] = afk_price[0] * 1.1
        afk_price[0] = math.floor(afk_price[0])
        afk_button1.config(text = f"{afk_price[0]} $ = +1s")
        T_money.config(text=(f"{math.floor(money*10)/10} $"))
        T_gain_sec.config(text = f"AFK gain: {math.floor(afk_gain*10)/10} x {multiplier}")
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
            T_money.config(text=(f"{math.floor(money*10)/10} $"))
            T_gain_sec.config(text = f"AFK gain: {math.floor(afk_gain*10)/10} x {multiplier}")
#upgrade of multiplier and Time
def Window_2():
    global money, if_New_upgrade_is_buy
    if if_New_upgrade_is_buy == 0:
        if_New_upgrade_is_buy += 1
        money -=New_upgrade_price
        T_money.config(text=(f"{math.floor(money*10)/10} $"))
        
#definition
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
#UI
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

root.mainloop()