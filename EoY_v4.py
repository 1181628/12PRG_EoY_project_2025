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
frames = {}
window = {}
card = {}
reverse_flag = tk.BooleanVar(value=False)
sort_combo = ttk.Combobox(root, values=["Alphabetical", "Order of joining", "Total scored", "Strength", "Speed", "Stealth", "Cunning"])


def upload_catalogue():
    with open('user_catalogue_file.txt','r')as usercatalogue_file:
        for each in usercatalogue_file.readlines():
            if each:
                name, charatistic = each.strip().split(':', 1)
                values = [int(item.strip()) for item in charatistic.split(',')]
                total = sum(values)
                values.append(total)
                user_catalogue[name.strip()] = values
    with open('existed_catalogue.txt','r')as existedcatalogue_file:
        for each in existedcatalogue_file.readlines():
            if each:
                name, charatistic = each.strip().split(':', 1)
                values = [int(item.strip()) for item in charatistic.split(',')]
                total = sum(values)
                values.append(total)  # add the total as the last element
                existed_catalogue[name.strip()] = values


def close_root():
    root.destroy()

def save_exit():
    window["window3"] = tk.Toplevel(root)
    window["window3"].title("Over look")
    window["window3"].geometry("300x500+800+90")
    #Laybel title
    #label_user_catalogue(1)
    #new code for laybeling
    confirm_button = tk.Button(window["window3"], text="Confirm", command=close_root)
    confirm_button.pack()

#def find_card():
    #check
    #find_entry.get()

def reverse_card(action):
    reverse_flag.set(not reverse_flag.get())
    sort_card(action)

def sort_card(action):
    reverse = reverse_flag.get()
    if sort_combo.get() != "":
        frames["catalogue"].destroy()
        if sort_combo.get() == "Alphabetical":
            default_rev = False
        else:
            default_rev = True
            rev = reverse_flag.get() if reverse_flag.get() else default_rev
            sorted(user_catalogue, key=lambda x: x[0], reverse=rev)
        if sort_combo.get() == "Order of joining":
            sorted(user_catalogue.items())
        if sort_combo.get() == "Total scored":
            sorted(user_catalogue, value=lambda x: x[0], reverse=reverse)
        if sort_combo.get() == "Strength":
            sorted(user_catalogue, value=lambda x: x[0], reverse=reverse)
        if sort_combo.get() == "Speed":
            sorted(user_catalogue, value=lambda x: x[0], reverse=reverse)
        if sort_combo.get() == "Stealth":
            sorted(user_catalogue, value=lambda x: x[0], reverse=reverse)
        if sort_combo.get() == "Cunning":
            sorted(user_catalogue, value=lambda x: x[0], reverse=reverse)        
        label_user_catalogue(action)
    
#def save():


#def find_card():
    #check invalid

#def sort_card():

def inside_frame_label(parent_frame, action):
    find_label = tk.Label(parent_frame, text="Find the card...")
    find_entry = tk.Entry(parent_frame)
    sort_combo = ttk.Combobox(parent_frame, values=["Alphabetical", "Order of joining", "Total scored", "Strength", "Speed", "Stealth", "Cunning"])
    sort_combo.set("Sort by...")
    reverse_button = tk.Button(parent_frame, text="↑↓", command=lambda:reverse_card(action))
    text_label = tk.Label(parent_frame, text=f"Your Monster Card Catalogue: {len(user_catalogue)}/10")
    #find_button = tk.Button(parent_frame, text="Find", command=find_card)
    sort_button = tk.Button(parent_frame, text="Sort", command=lambda:sort_card(action))
    go_back_button = tk.Button(parent_frame, text="Go back", command=go_back)
    find_label.pack()
    find_entry.pack()
    sort_combo.pack()
    reverse_button.pack()
    text_label.pack()
    #find_button.pack()
    sort_button.pack()
    go_back_button.pack()

    

def go_back():
    if "catalogue" in frames:
        frames["catalogue"].destroy()
    if "manage" in frames:
        frames["manage"].destroy()
    if "print" in frames:
        frames["print"].destroy()

def confirm_action():
    window["window2"].destroy()

def add_existed():
    #Check if ok
    user_catalogue[card["name"]] = existed_catalogue[card["name"]]
    window["window2"].destroy()

def add_new():
    #check invalid
    #Check if ok
    user_catalogue[card["name"].get()] = [card["strength"].get(), card["speed"].get(), card["stealth"].get(), card["cunning"].get()]
    window["window2"].destroy()

def delete():
    #Are you sure want to delete this card?
    #(This card is going to removed from your catalogue)
    del user_catalogue[card["name"]]
    window["window2"].destroy()

def card_detail(action):
    window["window2"] = tk.Toplevel(root)
    window["window2"].title(card["name"])
    window["window2"].geometry("300x500+800+90")
    if card["name"] in user_catalogue:
        data = user_catalogue[card["name"]]
    else:
        data = existed_catalogue[card["name"]]
    name_label = tk.Label(window["window2"], text=card["name"])
    strength_label = tk.Label(window["window2"], text=f"Strength: {data[0]}")
    speed_label = tk.Label(window["window2"], text=f"Speed: {data[1]}")
    stealth_label = tk.Label(window["window2"], text=f"Stealth: {data[2]}")
    cunning_label = tk.Label(window["window2"], text=f"Cunning: {data[3]}")
    totalscore_label = tk.Label(window["window2"], text=f"Total scores: {sum(map(int, data))}")
    if action == 1:
        confirm_button = tk.Button(window["window2"], text="Confirm", command=confirm_action)
        confirm_button.pack()
    elif (action == 2) or (action == 4):
        if action == 2:
            add_button = tk.Button(window["window2"], text="Add", command=add_existed)
            add_button.pack()
        else:
            delete_button = tk.Button(window["window2"], text="Delete", command=delete)
            delete_button.pack()
        cancel_button = tk.Button(window["window2"], text="Cancel", command=confirm_action)
        cancel_button.pack()
    name_label.pack()
    strength_label.pack()
    speed_label.pack()
    stealth_label.pack()
    cunning_label.pack()
    totalscore_label.pack()

def add_new_card():
    window["window2"] = tk.Toplevel(root)
    window["window2"].title("Make your own card")
    window["window2"].geometry("300x500+800+90")
    name_label = tk.Label(window["window2"], text="Name:")
    card["name"] = tk.Entry(window["window2"])
    strength_label = tk.Label(window["window2"], text="Strength:")
    card["strength"] = tk.Entry(window["window2"])
    speed_label = tk.Label(window["window2"], text="Speed:")
    card["speed"] = tk.Entry(window["window2"])
    stealth_label = tk.Label(window["window2"], text="Stealth:")
    card["stealth"] = tk.Entry(window["window2"])
    cunning_label = tk.Label(window["window2"], text="Cunning:")
    card["cunning"] = tk.Entry(window["window2"])
    name_label.pack()
    card["name"].pack()
    strength_label.pack()
    card["strength"].pack()
    speed_label.pack()
    card["speed"].pack()
    stealth_label.pack()
    card["stealth"].pack()
    cunning_label.pack()
    card["cunning"].pack()
    add_button = tk.Button(window["window2"], text="Add", command=add_new)
    add_button.pack()
    cancel_button = tk.Button(window["window2"], text="Cancel", command=confirm_action)
    cancel_button.pack()

def label_user_catalogue(action):
    frames["catalogue"] = tk.Frame(root, bg="grey")
    frames["catalogue"].pack()
    frames["catalogue"].grid_propagate(False)
    inside_frame_label(frames["catalogue"], action)
    for name, charactistic in user_catalogue.items():
        cards_button = tk.Button(frames["catalogue"], text=name, command=lambda name=name:(card.update({"name": name}), card_detail(action)))
        cards_button.pack()
        if action == 4:
            Label = tk.Label(frames["catalogue"], text=" ", bg="red")
            Label.pack()
    go_back_button = tk.Button(frames["catalogue"], text="Go back", command=go_back)
    go_back_button.pack()

def label_existed_catalogue(action):
    frames["catalogue"] = tk.Frame(root, bg="grey")
    frames["catalogue"].pack()
    frames["catalogue"].grid_propagate(False)
    inside_frame_label(frames["catalogue"], action)
    for name, charactistic in existed_catalogue.items():
        card["name"] = name
        cards_button = tk.Button(frames["catalogue"], text=card["name"], command=lambda:card_detail(action))
        cards_button.pack()
    go_back_button = tk.Button(frames["catalogue"], text="Go back", command=go_back)
    go_back_button.pack()

def manage_user_catalogue(action):
    frames["manage"] = tk.Frame(root, bg="grey")
    frames["manage"].pack()
    frames["manage"].grid_propagate(False)
    inside_frame_label(frames["manage"], action)
    add_exist_button = tk.Button(frames["manage"], text="Add from existing cards", command=lambda:label_existed_catalogue(2))
    add_new_button = tk.Button(frames["manage"], text="Make your own card", command=add_new_card)
    add_exist_button.pack()
    add_new_button.pack()
    delete_button = tk.Button(frames["manage"], text="Removing a card", command=lambda:label_user_catalogue(4))
    delete_button.pack()
    go_back_button = tk.Button(frames["manage"], text="Go back", command=go_back)
    go_back_button.pack()

upload_catalogue()
user_catalogue_button = tk.Button(root, text="View your card catalogue", command=lambda: label_user_catalogue(1))
exist_catalogue_button = tk.Button(root, text="View existing card's catalogue", command=lambda: label_existed_catalogue(1))
manage_catalogue_button = tk.Button(root, text="Manage your card catalogue", command=lambda: manage_user_catalogue(2))
exit_button = tk.Button(root, text="Save & Exit", command=save_exit)
user_catalogue_button.pack()
exist_catalogue_button.pack()
manage_catalogue_button.pack()
exit_button.pack()

#Find_button = tk.Button(root, text="Find", command=find_card)
#Sort_button = tk.Button(root, text="Sort", command=sort_card)

#save()
#check_invalid()

#sort doesnot work

root.mainloop()
