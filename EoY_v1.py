import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime
from datetime import timedelta

root = tk.Tk()
root.title("")
root.geometry("520x750+300+90")

#image = Image.open("a_name.png")
#image = image.resize((100,100), Image.LANCZOS)
#image = ImageTk.PhotoImage(image)

data = {}
user_catalogue = {}
existed_catalogue = {}
#user_catalogue = {
#"Vexscream" : [1, 6, 21, 19],
#"Dawnmirage" : [5, 15, 18, 22], 
#"Blazegolem" : [15, 20, 23, 6], 
#"Moldvine" : [21, 18, 14, 5], 
#"Vortexwing" : [19, 13, 19, 2], 
#"Frostste" : [14, 14, 17, 4], 
#"Wispghoul" : [17, 19, 3, 2]}

#def find_card():

#def sort_card():

#def go_back():

def card_detail(name):
    root = tk.Toplevel()
    root.title(name)
    root.geometry("300x500+800+90")
    if name in user_catalogue:
        data = user_catalogue[name]
    else:
        data = existed_catalogue[name]
    name_label = tk.Label(root, text=name)
    strength_label = tk.Label(root, text=f"Strength: {data[0]}")
    speed_label = tk.Label(root, text=f"Speed: {data[1]}")
    stealth_label = tk.Label(root, text=f"Stealth: {data[2]}")
    cunning_label = tk.Label(root, text=f"Cunning: {data[3]}")
    totalscore_label = tk.Label(root, text=f"Total scores: {sum(map(int, data))}")
    name_label.pack()
    strength_label.pack()
    speed_label.pack()
    stealth_label.pack()
    cunning_label.pack()
    totalscore_label.pack()

def upload_catalogue():
    with open('user_catalogue_file.txt','r')as usercatalogue_file:
        for each in usercatalogue_file.readlines():
            if each:
                name, charatistic = each.strip().split(':', 1)
                user_catalogue[name.strip()] = [item.strip() for item in charatistic.split(',')]
    with open('existed_catalogue.txt','r')as existedcatalogue_file:
        for each in existedcatalogue_file.readlines():
            if each:
                name, charatistic = each.strip().split(':', 1)
                existed_catalogue[name.strip()] = [item.strip() for item in charatistic.split(',')]


def view_user_catalogue():
    for name, charactistic in user_catalogue.items():
        button = tk.Button(root, text=name, command=lambda name=name:card_detail(name))
        button.pack()

def view_existed_catalogue():
    for name, charactistic in existed_catalogue.items():
        button = tk.Button(root, text=name, command=lambda name=name:card_detail(name))
        button.pack()

def add_existing_card():
    test.py

def add_new_card():

def manage_user_catalogue():
    add_exist_button = tk.Button(root, text="Add from existing cards", command=add_existing_card)
    add_new_button = tk.Button(root, text="Make your own card", command=add_new_card)
    add_exist_button.pack()
    add_new_button.pack()


upload_catalogue()
user_catalogue_button = tk.Button(root, text="View your card catalogue", command=view_user_catalogue)
exist_catalogue_button = tk.Button(root, text="View existing card's catalogue", command=view_existed_catalogue)
manage_catalogue_button = tk.Button(root, text="Manage your card catalogue", command=manage_user_catalogue)
user_catalogue_button.pack()
exist_catalogue_button.pack()
manage_catalogue_button.pack()



#Find_button = tk.Button(root, text="Find", command=find_card)
#Sort_button = tk.Button(root, text="Sort", command=sort_card)
#Back_button = tk.Button(root, text="Go back", command=go_back)

#user_catalogue['name'] = [strength, speed, stealth, cunning, total_scores]
#del user_catalogue['name']

root.mainloop()
