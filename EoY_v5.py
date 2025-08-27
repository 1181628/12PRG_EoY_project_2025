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

maximum_cards = 10
maximum_charactistics = 25
minimum_charactistics = 1
#stats
user_catalogue = {}
existed_catalogue = {}
frames = {}
window = {}
card = {}
sorted_keys = {}
general_catalogue = {}
reverse_flag = tk.BooleanVar(value=False)
sort_combo = ttk.Combobox(root, values=["Alphabetical", "Order of joining", "Total scored", "Strength", "Speed", "Stealth", "Cunning"])


def upload_catalogue():
    with open('user_catalogue_file.txt','r')as usercatalogueFile:
        for each in usercatalogueFile.readlines():
            if each:
                name, charatistic = each.strip().split(':', 1)
                values = [int(item.strip()) for item in charatistic.split(',')]
                total = sum(values)
                values.append(total)
                user_catalogue[name.strip()] = values
    with open('existed_catalogue.txt','r')as existedcatalogueFile:
        for each in existedcatalogueFile.readlines():
            if each:
                name, charatistic = each.strip().split(':', 1)
                values = [int(item.strip()) for item in charatistic.split(',')]
                total = sum(values)
                values.append(total)
                existed_catalogue[name.strip()] = values

def save_catalogue():
    with open('user_catalogue_file.txt','w')as usercatalogueFile:
        for each in range(len(user_catalogue)):
            usercatalogueFile.write(each+"\n")

def close_root():
    root.destroy()

def end_page():
    save_catalogue()
    root = tk.Toplevel()
    root.title("Over look")
    root.geometry("300x500+800+90")
    #label title
    label = tk.Label(root, text=user_catalogue)
    label.pack()
    for name, charactistics in user_catalogue.items():
        label = tk.Label(root, text=f"{name}: {charactistics}")
        label.pack()
        #these layout is different from my normal layout, so I copied it to here
    confirm_button = tk.Button(root, text="Confirm", command=close_root)
    confirm_button.pack()

def save_exit():
    response = messagebox.askquestion("Save & Exit", "Are you sure you want to end your program? (We will automatically save your catalogue)")
    if response == "yes":
        end_page()
    else:
        return
    #text_label = tk.Label(root, text="Are you sure you want to end your program? (We will automatically save for you)")
    #button = tk.Button(root, text="Yes", command=end_page)
    #button.pack()

def check_invalid():
    if len(user_catalogue) == maximum_cards:
        #error_popup(1)
        return
    if (card["name"].get() in existed_catalogue.keys()) or (card["name"].get() in user_catalogue.keys()):
        #error_popup(2)
        return
    try:
        int(card["strength"].get()) > 25
        int(card["speed"].get())
        int(card["stealth"].get())
        int(card["cunning"].get())
    except ValueError:
        print("error")
        #error_popup(3)
        return

def find_card(entry):
    if entry in general_catalogue.keys():
        card["name"] = entry
        card_detail(1)
    else:
        messagebox.showinfo("Invalid Entry", f"There is no card named '{entry}' in the catalogue.")

def reverse_card():
    reverse_flag.set(not reverse_flag.get())
    sort_card()

def sort_card():
    reverse = reverse_flag.get()
    if sort_combo.get() == "":
        return
    frames["catalogue"].destroy()
    del frames["catalogue"]
    if sort_combo.get() == "Alphabetical":
        default_rev = False
        sorted_keys = sorted(general_catalogue.keys(), reverse=reverse)
    else:
        default_rev = True
        return not default_rev if reverse_flag.get() else default_rev
    if sort_combo.get() == "Alphabetical":
        sorted_keys = sorted(general_catalogue.keys(), reverse=reverse)
    if sort_combo.get() == "Order of joining":
        sorted_keys = list(general_catalogue.keys())
        if reverse:
            sorted_keys.reverse()
    if sort_combo.get() == "Total scored":
        general_catalogue = sorted(general_catalogue.keys(), key=lambda k: general_catalogue[k][4], reverse=reverse)
    if sort_combo.get() == "Strength":
        general_catalogue = sorted(general_catalogue.keys(), key=lambda k: general_catalogue[k][0], reverse=reverse)
    if sort_combo.get() == "Speed":
        general_catalogue = sorted(general_catalogue.keys(), key=lambda k: general_catalogue[k][1], reverse=reverse)
    if sort_combo.get() == "Stealth":
        general_catalogue = sorted(general_catalogue.keys(), key=lambda k: general_catalogue[k][2], reverse=reverse)
    if sort_combo.get() == "Cunning":
        general_catalogue = sorted(general_catalogue.keys(), key=lambda k: general_catalogue[k][3], reverse=reverse)
    label_catalogue(5)

def inside_frame_label():
    find_label = tk.Label(frames["catalogue"], text="Find the card...")
    find_entry = tk.Entry(frames["catalogue"])
    find_button = tk.Button(frames["catalogue"], text="Find", command=lambda:find_card(find_entry.get()))
    sort_combo = ttk.Combobox(frames["catalogue"], values=["Alphabetical", "Order of joining", "Total scored", "Strength", "Speed", "Stealth", "Cunning"])
    sort_combo.set("Sort by...")
    reverse_button = tk.Button(frames["catalogue"], text="↑↓", command=reverse_card)
    text_label = tk.Label(frames["catalogue"], text=f"Your Monster Card Catalogue: {len(user_catalogue)}/10")
    sort_button = tk.Button(frames["catalogue"], text="Sort", command=sort_card)
    go_back_button = tk.Button(frames["catalogue"], text="Go back", command=go_back)
    find_label.pack()
    find_entry.pack()
    find_button.pack()
    sort_combo.pack()
    reverse_button.pack()
    text_label.pack()
    sort_button.pack()
    go_back_button.pack()    

def go_back():
    if "catalogue" in frames:
        frames["catalogue"].destroy()
        del frames["catalogue"]
    if "manage" in frames:
        frames["manage"].destroy()
        del frames["manage"]
    if "print" in frames:
        frames["print"].destroy()
        del frames["print"]

def confirm_action():
    if "window2" in window:
        window["window2"].destroy()
        #invalid here

def add_existed():
    #Check if ok
    user_catalogue[card["name"]] = existed_catalogue[card["name"]]
    window["window2"].destroy()

def add_new():
    check_invalid()
    #Check if ok
    user_catalogue[card["name"].get()] = [
    int(card["strength"].get()), 
    int(card["speed"].get()), 
    int(card["stealth"].get()), 
    int(card["cunning"].get())]
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
    name_label = tk.Label(window["window2"], text=card["name"])
    strength_label = tk.Label(window["window2"], text=f"Strength: {general_catalogue[card['name']][0]}")
    speed_label = tk.Label(window["window2"], text=f"Speed: {general_catalogue[card['name']][1]}")
    stealth_label = tk.Label(window["window2"], text=f"Stealth: {general_catalogue[card['name']][2]}")
    cunning_label = tk.Label(window["window2"], text=f"Cunning: {general_catalogue[card['name']][3]}")
    totalscore_label = tk.Label(window["window2"], text=f"Total scores: {sum(map(int, general_catalogue[card['name']]))}")
    if (action == 1) or (action == 2):
        confirm_button = tk.Button(window["window2"], text="Confirm", command=confirm_action)
        confirm_button.pack()
    elif (action == 3) or (action == 4):
        if action == 3:
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

def label_catalogue(action):
    frames["catalogue"] = tk.Frame(root, bg="grey")
    frames["catalogue"].pack()
    frames["catalogue"].grid_propagate(False)
    if (action == 1) or (action == 4):
        general_catalogue.update(user_catalogue)
    elif (action == 2) or (action == 3):
        general_catalogue.update(existed_catalogue)
    for name, charactistic in general_catalogue.items():
        cards_button = tk.Button(frames["catalogue"], text=name, command=lambda name=name:(card.update({"name": name}), card_detail(action)))
        cards_button.pack()
        if action == 4:
            label = tk.Label(frames["catalogue"], text=" ", bg="red")
            label.pack()
    inside_frame_label()

def manage_user_catalogue(action):
    frames["manage"] = tk.Frame(root, bg="grey")
    frames["manage"].pack()
    frames["manage"].grid_propagate(False)
    add_exist_button = tk.Button(frames["manage"], text="Add from existing cards", command=lambda:label_catalogue(3))
    add_new_button = tk.Button(frames["manage"], text="Make your own card", command=add_new_card)
    add_exist_button.pack()
    add_new_button.pack()
    delete_button = tk.Button(frames["manage"], text="Removing a card", command=lambda:label_catalogue(4))
    delete_button.pack()

upload_catalogue()
user_catalogue = dict(sorted(user_catalogue.items(), key=lambda x: int(x[1][0])))
existed_catalogue = dict(sorted(existed_catalogue.items(), key=lambda x: int(x[1][0])))
user_catalogue_button = tk.Button(root, text="View your card catalogue", command=lambda: label_catalogue(1))
exist_catalogue_button = tk.Button(root, text="View existing card's catalogue", command=lambda: label_catalogue(2))
manage_catalogue_button = tk.Button(root, text="Manage your card catalogue", command=lambda: manage_user_catalogue(3))
exit_button = tk.Button(root, text="Save & Exit", command=save_exit)
user_catalogue_button.pack()
exist_catalogue_button.pack()
manage_catalogue_button.pack()
exit_button.pack()

#action1 : label user catalgoue
#action2 : label existed catalgoue
#action3 : label existed catalgoue and add cards
#action4 : label user catalgoue delete

#action6 : label user catalgoue

#save()
#check_invalid()


root.mainloop()
