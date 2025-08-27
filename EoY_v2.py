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
action = 1
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

def confirm_action(window2):
    window2.destroy()

def add_existed(name, window2):
    user_catalogue[name] = existed_catalogue[name]
    window2.destroy()

def add_new(name, strength, speed, stealth, cunning, window2):
    user_catalogue[name] = [strength, speed, stealth, cunning]
    window2.destroy()

def delete(name, window2):
    del user_catalogue[name]
    window2.destroy()

def card_detail(name, action):
    window2 = tk.Toplevel(root)
    window2.title(name)
    window2.geometry("300x500+800+90")
    if name in user_catalogue:
        data = user_catalogue[name]
    else:
        data = existed_catalogue[name]
    name_label = tk.Label(window2, text=name)
    strength_label = tk.Label(window2, text=f"Strength: {data[0]}")
    speed_label = tk.Label(window2, text=f"Speed: {data[1]}")
    stealth_label = tk.Label(window2, text=f"Stealth: {data[2]}")
    cunning_label = tk.Label(window2, text=f"Cunning: {data[3]}")
    totalscore_label = tk.Label(window2, text=f"Total scores: {sum(map(int, data))}")
    if action == 1:
        confirm_button = tk.Button(window2, text="Confirm", command=lambda:confirm_action(window2))
        confirm_button.pack()
    elif (action == 2) or (action == 4):
        if action == 2:
            add_button = tk.Button(window2, text="Add", command=lambda:add_existed(name, window2))
            add_button.pack()
        else:
            delete_button = tk.Button(window2, text="Delete", command=lambda:delete(name, window2))
            delete_button.pack()
        cancel_button = tk.Button(window2, text="Cancel", command=lambda:confirm_action(window2))
        cancel_button.pack()
    name_label.pack()
    strength_label.pack()
    speed_label.pack()
    stealth_label.pack()
    cunning_label.pack()
    totalscore_label.pack()

def add_new_card():
    window2 = tk.Toplevel(root)
    window2.title("Make your own card")
    window2.geometry("300x500+800+90")
    name_label = tk.Label(window2, text="Name:")
    name = tk.Entry(window2)
    strength_label = tk.Label(window2, text="Strength:")
    strength = tk.Entry(window2)
    speed_label = tk.Label(window2, text="Speed:")
    speed = tk.Entry(window2)
    stealth_label = tk.Label(window2, text="Stealth:")
    stealth = tk.Entry(window2)
    cunning_label = tk.Label(window2, text="Cunning:")
    cunning = tk.Entry(window2)
    name_label.pack()
    name.pack()
    strength_label.pack()
    strength.pack()
    speed_label.pack()
    speed.pack()
    stealth_label.pack()
    stealth.pack()
    cunning_label.pack()
    cunning.pack()
    add_button = tk.Button(window2, text="Add", command=lambda:add_new(name, strength, speed, stealth, cunning, window2))
    add_button.pack()
    cancel_button = tk.Button(window2, text="Cancel", command   =lambda:confirm_action(window2))
    cancel_button.pack()


def label_user_catalogue(action):
    for name, charactistic in user_catalogue.items():
        button = tk.Button(root, text=name, command=lambda name=name:card_detail(name, action))
        button.pack()
        if action == 4:
            Label = tk.Label(root, text=" ", bg="red")
            Label.pack()

def label_existed_catalogue(action):
    for name, charactistic in existed_catalogue.items():
        button = tk.Button(root, text=name, command=lambda name=name:card_detail(name, action))
        button.pack()


def manage_user_catalogue():
    add_exist_button = tk.Button(root, text="Add from existing cards", command=lambda:label_existed_catalogue(2))
    add_new_button = tk.Button(root, text="Make your own card", command=add_new_card)
    add_exist_button.pack()
    add_new_button.pack()
    delete_button = tk.Button(root, text="Removing a card", command=lambda:label_user_catalogue(4))
    delete_button.pack()


upload_catalogue()
user_catalogue_button = tk.Button(root, text="View your card catalogue", command=lambda: label_user_catalogue(action))
exist_catalogue_button = tk.Button(root, text="View existing card's catalogue", command=lambda: label_existed_catalogue(action))
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
