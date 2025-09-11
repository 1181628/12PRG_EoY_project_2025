import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
import os

root = tk.Tk()
root.title("")
root.geometry("820x670+350+100")
root.configure(bg="white")
#bugs
#layout for sort and manage and card and catagolue bugs

#-----------setting-----------
total = 0
maximum_cards = 10
maximum_stats = 25
minimum_stats = 1
image_label = ""
user_catalogue = {}
existed_catalogue = {}
stored_images = {}
frames = {}
window = {}
card = {}
sort_list = {}
sorted_catalogue = {}
error_flag = {"flag": "no"}
parent_frame = {}
sort = "Alphabetical"
last_sort = {"sort_by": "Sort by..."}
general_catalogue = {}
reverse_flag = tk.BooleanVar(value=True)

themes = {
    "title":   {"font": ("Impact", 20), "bg": "#f2d243", "fg": "#2f58e0"},
    "inform":  {"font": ("Impact", 16), "bg": "#f2d243", "fg": "#2f58e0"},
    "button":  {"font": ("Impact", 22), "bg": "#2f58e0", "fg": "white", "width": 29},
    "catalogue": {"font": ("Impact", 14), "bg": "#2f58e0", "fg": "white", "width": 27},
    "manage": {"font": ("Impact", 22), "bg": "#2f58e0", "fg": "white", "width": 29},
    "card": {"font": ("Impact", 16), "bg": "white", "fg": "#2f58e0"},
    "sort":  {"font": ("Impact", 16), "bg": "#2f58e0", "fg": "white", "width": 5},
    "exit": {"font": ("Impact", 22), "bg": "#2f58e0", "fg": "white", "width": 17},
    "relief": "flat"
    }

image_dir = r"G:\python\EoY_Project_2025\images"

image = Image.open(os.path.join(image_dir, "front_image.png"))
image = image.resize((230,330), Image.LANCZOS)
front_image = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "1.png"))
image = image.resize((230,330), Image.LANCZOS)
image1 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "2.png"))
image = image.resize((230,330), Image.LANCZOS)
image2 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "3.png"))
image = image.resize((230,330), Image.LANCZOS)
image3 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "4.png"))
image = image.resize((230,330), Image.LANCZOS)
image4 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "5.png"))
image = image.resize((230,330), Image.LANCZOS)
image5 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "6.png"))
image = image.resize((230,330), Image.LANCZOS)
image6 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "7.png"))
image = image.resize((230,330), Image.LANCZOS)
image7 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "8.png"))
image = image.resize((230,330), Image.LANCZOS)
image8 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "9.png"))
image = image.resize((230,330), Image.LANCZOS)
image9 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "10.png"))
image = image.resize((230,330), Image.LANCZOS)
image10 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "11.png"))
image = image.resize((230,330), Image.LANCZOS)
image11 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "12.png"))
image = image.resize((230,330), Image.LANCZOS)
image12 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "13.png"))
image = image.resize((230,330), Image.LANCZOS)
image13 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "14.png"))
image = image.resize((230,330), Image.LANCZOS)
image14 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "15.png"))
image = image.resize((230,330), Image.LANCZOS)
image15 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "16.png"))
image = image.resize((230,330), Image.LANCZOS)
image16 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "17.png"))
image = image.resize((230,330), Image.LANCZOS)
image17 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "18.png"))
image = image.resize((230,330), Image.LANCZOS)
image18 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "19.png"))
image = image.resize((230,330), Image.LANCZOS)
image19 = ImageTk.PhotoImage(image)

image = Image.open(os.path.join(image_dir, "20.png"))
image = image.resize((230,330), Image.LANCZOS)
image20 = ImageTk.PhotoImage(image)

image_dictionary = {
    "Vexscream": image1,
    "Dawnmirage": image2,
    "Blazegolem": image3,
    "Moldvine": image4,
    "Vortexwing": image5,
    "Froststep": image6,
    "Wispghoul": image7,
    "image8": image8,
    "image9": image9,
    "image10": image10,
    "image11": image11,
    "image12": image12,
    "image13": image13,
    "image14": image14,
    "image15": image15,
    "image16": image16,
    "image17": image17,
    "image18": image18,
    "image19": image19,
    "image20": image20
    }

def create_image_buttons():
    for n, name in enumerate(image_dictionary.keys()):
        btn = tk.Button(root, image=image_dictionary[name], command=lambda n=name: select_image(n))
        btn.pack(side="left", padx=5, pady=5)

def select_image(name):
    image_label.config(image=image_dictionary[name])
    image_label.image = image_dictionary[name]

def upload_catalogue():
    with open('G:\python\EoY_Project_2025\existed_catalogue.txt', 'r') as usercatalogueFile:
        for line in usercatalogueFile:
            if line.strip():
                parts = line.strip().split(':')
                name = parts[0].strip()
                values_part = parts[1].strip()
                values = [item.strip() for item in values_part.split(',')]
                numeric_values = [int(values[i]) for i in range(5)]
                image_name = values[5] if len(values) > 5 else name
                user_catalogue[name] = numeric_values
                stored_images[name] = image_name
    with open('G:\python\EoY_Project_2025\existed_catalogue.txt', 'r') as existedcatalogueFile:
        for line in existedcatalogueFile:
            if line.strip():
                parts = line.strip().split(':')
                name = parts[0].strip()
                values_part = parts[1].strip()
                values = [item.strip() for item in values_part.split(',')]
                numeric_values = [int(values[i]) for i in range(5)]
                image_name = values[5] if len(values) > 5 else name
                existed_catalogue[name] = numeric_values

def save_catalogue():
    with open('G:\python\EoY_Project_2025\existed_catalogue.txt', 'w') as usercatalogueFile:
        for name, stats in user_catalogue.items():
            image_name = stored_images.get(name, name)
            each = f"{name}: {','.join(map(str, stats))},{image_name}\n"
            usercatalogueFile.write(each)

def close_root():
    root.destroy()

def end_page():
    save_catalogue()
    window["window4"] = tk.Toplevel()
    window["window4"].title("")
    window["window4"].geometry("820x670+350+100")
    #label title
    for name, stats in user_catalogue.items():
        label = tk.Label(window["window4"], text=f"{name}: {stats}")
        label.pack()
    confirm_button = tk.Button(window["window4"], text="Confirm", command=close_root)
    confirm_button.pack()

def save_exit():
    response = messagebox.askquestion("Save & Exit", "Are you sure you want to end your program? (We will automatically save your catalogue)")
    if response == "yes":
        end_page()
    else:
        return

#----------sub functions----------    
def print_catalogue():
    save_catalogue()
    window["window3"] = tk.Toplevel()
    window["window3"].title("")
    window["window3"].geometry("300x500+800+90")
    with open('user_catalogue_file.txt', 'r') as usercatalogueFile:
        for line in usercatalogueFile:
            if line.strip():
                label = tk.Label(window["window3"], text=line.strip())
                label.pack()

def go_back():
    if "catalogue" in frames:
        frames["catalogue"].destroy()
        del frames["catalogue"]
    if "manage" in frames:
        frames["manage"].destroy()
        del frames["manage"]
    if "sort" in frames:
        frames["sort"].destroy()
        del frames["sort"]
    if "catalogue_inform" in frames:
        frames["catalogue_inform"].destroy()
    if "print" in frames:
        frames["print"].destroy()
        del frames["print"]

def find_card(entry):
    if entry in general_catalogue.keys():
        card["name"] = entry
        card_detail(1)
    else:
        messagebox.showinfo("Invalid Entry", f"There is no card named {entry} in the catalogue.")

def sort_card(sort_action):
    sort = sort_list["sort_combo"].get()
    if "catalogue" in frames:
        frames["catalogue"].destroy()
        del frames["catalogue"]
    else:
        return
    if sort_list["sort_combo"].get() == "Sort by...":
        if last_sort["sort_by"] == "Sort by...":
            sort = "Alphabetical"
        else: 
            sort = last_sort["sort_by"]
    if sort_action == 7:
        reverse_flag.set(not reverse_flag.get())
        reverse = reverse_flag.get()
        reverse2 = (not reverse_flag.get())
    else: 
        reverse_flag2 = tk.BooleanVar(value=True)
        reverse = reverse_flag2.get()
        reverse2 = (not reverse_flag2.get())
    if sort == "Alphabetical":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[0].casefold(), reverse=reverse2))
    elif sort == "Total scored":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][4], reverse=reverse))
    elif sort == "Strength":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][0], reverse=reverse))
    elif sort == "Speed":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][1], reverse=reverse))
    elif sort == "Stealth":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][2], reverse=reverse))
    elif sort == "Cunning":
        sorted_catalogue = dict(sorted(general_catalogue.items(), key=lambda name: name[1][3], reverse=reverse))
    last_sort["sort_by"] = sort
    general_catalogue.clear()
    general_catalogue.update(sorted_catalogue)
    label_catalogue(6) 

def inside_frame_label():
    if "manage" in frames:
        parent_frame = frames["manage"]
        y_axis = 44
    else:
        frames["sort"] = tk.Frame(root, bg="#f2d243")
        frames["sort"].place(x=340, y=160, height=490, width=460)
        frames["sort"].grid_propagate(False)
        parent_frame = frames["sort"]
        y_axis = 150
    find_entry = tk.Entry(parent_frame,
        font=themes["sort"]["font"], bg="white", fg=themes["sort"]["bg"])
    find_entry.place(x=17, y=y_axis, width=120)
    find_entry.insert(5, "Find card...")
    find_button = tk.Button(parent_frame, text="Find", command=lambda:find_card(find_entry.get()),
        font=themes["sort"]["font"], bg=themes["sort"]["bg"], fg=themes["sort"]["fg"], width=themes["sort"]["width"], relief=themes["relief"])
    find_button.place(x=142, y=y_axis-9)
    sort_list["sort_combo"] = ttk.Combobox(parent_frame, 
                values=["Alphabetical", "Total scored", "Strength", "Speed", "Stealth", "Cunning"],
                font=themes["sort"]["font"])
    sort_list["sort_combo"].set("Sort by...")
    sort_list["sort_combo"].place(x=222, y=y_axis, width=120)
    sort_button = tk.Button(parent_frame, text="Sort", command=lambda:sort_card(6),
        font=themes["sort"]["font"], bg=themes["sort"]["bg"], fg=themes["sort"]["fg"], width=themes["sort"]["width"], relief=themes["relief"])
    sort_button.place(x=347, y=y_axis-9)
    reverse_button = tk.Button(parent_frame, text="↑↓", command=lambda:sort_card(7),
        font=themes["sort"]["font"], bg=themes["sort"]["bg"], fg=themes["sort"]["fg"], width=2, relief=themes["relief"])
    reverse_button.place(x=412, y=y_axis-9, width=30)
    if "sort" in frames:
        go_back_button = tk.Button(parent_frame, text="Go back", command=go_back,
            font=themes["exit"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=themes["exit"]["width"], relief=themes["relief"])
        go_back_button.place(x=102, y=240)

#----------main functions----------
def error_popup(invalids):
    error_flag["flag"] = "yes"
    if invalids == 1:
        messagebox.showerror("Error", "You have reached the maximum number of cards!")
    elif invalids == 2:
        messagebox.showerror("Error", "This card name already exists in the existing catalogue!")
    elif invalids == 3:
        messagebox.showerror("Error", "This card name already exists in your catalogue!")
    elif invalids == 4:
        messagebox.showerror("Error", "All stats must be integers!")
    elif invalids == 5:
        messagebox.showerror("Error", f"Strength must be between {minimum_stats} and {maximum_stats}!")
    elif invalids == 6:
        messagebox.showerror("Error", f"Speed must be between {minimum_stats} and {maximum_stats}!")
    elif invalids == 7:
        messagebox.showerror("Error", f"Stealth must be between {minimum_stats} and {maximum_stats}!")
    elif invalids == 8:
        messagebox.showerror("Error", f"Cunning must be between {minimum_stats} and {maximum_stats}!")


def check_invalid(action):
    if action == 3:
        if (card["name"].get() in existed_catalogue.keys()):
            error_popup(2)
            return
        if (card["name"].get() in user_catalogue.keys()):
            error_popup(3)
            return
    elif action == 4:
        if (card["name"] in existed_catalogue.keys()):
            error_popup(2)
            return
        if (card["name"] in user_catalogue.keys()):
            error_popup(3)
            return
    if action == 3:
        try:
            strength = int(card["strength"].get())
            speed = int(card["speed"].get())
            stealth = int(card["stealth"].get())
            cunning = int(card["cunning"].get())
        except ValueError:
            error_popup(4)
            return
        if (strength > maximum_stats) or (strength < minimum_stats):
            error_popup(5)
            return
        if (speed > maximum_stats) or (speed < minimum_stats):
            error_popup(6)
            return
        if (stealth > maximum_stats) or (stealth < minimum_stats):
            error_popup(7)
            return
        if (cunning > maximum_stats) or (cunning < minimum_stats):
            error_popup(8)
            return

def check_invalid_len():
    if len(user_catalogue) == maximum_cards: 
        error_popup(1)
        error_flag["flag"] = "yes"

def confirm_action(action):
    if (action != 1) and (action != 2) and (action != 6):
        check_invalid(action)
        if error_flag["flag"] == "yes":
            return
        #card_detail(action)
    if action == 3:
        strength = int(card["strength"].get())
        speed = int(card["speed"].get())
        stealth = int(card["stealth"].get())
        cunning = int(card["cunning"].get())
        total = strength + speed + stealth + cunning
        user_catalogue[card["name"].get()] = [strength, speed, stealth, cunning, total]
    elif action == 4:
        user_catalogue[card["name"]] = existed_catalogue[card["name"]]
    elif action == 5:
        del user_catalogue[card["name"]]
        #bug
    save_catalogue()
    if "window2" in window:
        window["window2"].destroy()
        #bug

def cancel_action():
    response = messagebox.askquestion("Cancel", "Are you sure you want to stop editing this card?")
    if response == "yes":
        window["window2"].destroy()
    else:
        #?
        return

def card_detail(action):
    window["window2"] = tk.Toplevel(root, bg="white")
    window["window2"].title(card["name"])
    window["window2"].geometry("340x600+800+90")
    frames["labeling"] = tk.Frame(window["window2"], bg="#f2d243")
    frames["labeling"].place(x=5, y=5, height=590, width=330)
    frames["labeling"].grid_propagate(False)    
    image = tk.Label(frames["labeling"], image=image_dictionary[card["name"]], bg="white")
    image.image = image_dictionary[stored_images[card['name']]] 
    image.place(x=48, y=12)
    frames["card"] = tk.Frame(frames["labeling"], bg="white")
    frames["card"].place(x=10, y=354, height=175, width=310)
    frames["card"].grid_propagate(False)
    name_label = tk.Label(frames["card"], text=f"Name:  {card['name']}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    name_label.place(x=5, y=5)
    label = tk.Label(frames["card"], text="", bg="#f2d243", width=50)
    label.place(x=0, y=40)
    strength_label = tk.Label(frames["card"], text=f"Strength:  {general_catalogue[card['name']][0]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    strength_label.place(x=5, y=65)
    speed_label = tk.Label(frames["card"], text=f"Speed:  {general_catalogue[card['name']][1]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    speed_label.place(x=150, y=65)
    stealth_label = tk.Label(frames["card"], text=f"Stealth:  {general_catalogue[card['name']][2]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    stealth_label.place(x=5, y=95)
    cunning_label = tk.Label(frames["card"], text=f"Cunning:  {general_catalogue[card['name']][3]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    cunning_label.place(x=150, y=95)
    totalscore_label = tk.Label(frames["card"], text=f"Total scores:  {general_catalogue[card['name']][4]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    totalscore_label.place(x=5, y=135)
    if (action != 1) and (action != 2) and (action != 6):
        confirm_button = tk.Button(window["window2"], text="Confirm", command=lambda: confirm_action(action),
        font=themes["card"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=10, relief=themes["relief"])
        confirm_button.place(x=45, y=540)
        cancel_button = tk.Button(window["window2"], text="Cancel", command=cancel_action,
            font=themes["card"]["font"], bg="red", fg=themes["exit"]["fg"], width=10, relief=themes["relief"])
        cancel_button.place(x=185, y=540)
    else:
        confirm_button = tk.Button(window["window2"], text="Confirm", command=lambda: confirm_action(action),
        font=themes["card"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=themes["exit"]["width"], relief=themes["relief"])
        confirm_button.place(x=80, y=540)

def add_new_card():
    check_invalid_len()
    if error_flag["flag"] == "yes":
        return
    error_flag["flag"] = "no"
    window["window2"] = tk.Toplevel(root, bg="white")
    window["window2"].title("Make your own card")
    window["window2"].geometry("340x600+800+90")

    frames["labeling"] = tk.Frame(window["window2"], bg="#f2d243")
    frames["labeling"].place(x=5, y=5, height=590, width=330)
    frames["labeling"].grid_propagate(False)    

    #image = tk.Label(frames["labeling"], image=image_dictionary[card["name"]], bg="white")
    #image.image = image_dictionary[stored_images[card['name']]] 
    #image.place(x=48, y=12)
    select_button = tk.Button(root, text="Select Image", command=select_image)
    select_button.pack()
    
    name_label = tk.Label(window["window2"], text="Name:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    name_label.place(x=5, y=5)
    card["name"] = tk.Entry(window["window2"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=20)
    card["name"].place(x=55, y=5)
    strength_label = tk.Label(window["window2"], text="Strength:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    strength_label.place(x=5, y=65)
    card["strength"] = tk.Entry(window["window2"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=20)
    card["strength"].place(x=35, y=65)
    speed_label = tk.Label(window["window2"], text="Speed:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    speed_label.packplace(x=150, y=65)
    card["speed"] = tk.Entry(window["window2"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=20)
    card["speed"].place(x=180, y=65)
    stealth_label = tk.Label(window["window2"], text="Stealth:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    stealth_label.place(x=5, y=95)
    card["stealth"] = tk.Entry(window["window2"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=20)
    card["stealth"].place(x=35, y=95)
    cunning_label = tk.Label(window["window2"], text="Cunning:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    cunning_label.place(x=150, y=95)
    card["cunning"] = tk.Entry(window["window2"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=20)
    card["cunning"].place(x=180, y=95)
    confirm_button = tk.Button(window["window2"], text="Confirm", command=lambda: confirm_action(3),
        font=themes["card"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=10, relief=themes["relief"])
    confirm_button.place(x=45, y=540)
    cancel_button = tk.Button(window["window2"], text="Cancel", command=cancel_action,
        font=themes["card"]["font"], bg="red", fg=themes["exit"]["fg"], width=10, relief=themes["relief"])
    cancel_button.place(x=185, y=540)

def label_inform():
    frames["catalogue_inform"] = tk.Frame(root, bg="#f2d243")
    frames["catalogue_inform"].place(x=20, y=20, height=200, width=300)
    frames["catalogue_inform"].grid_propagate(False)
    text_label = tk.Label(frames["catalogue_inform"], text="Your  Monster  Card", 
    font=("Impact", 20), bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
    text_label.place(x=15, y=15)
    text_label = tk.Label(frames["catalogue_inform"], text=f"Catalogue:                    {len(user_catalogue)}/10", 
    font=("Impact", 20), bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
    text_label.place(x=15, y=50)

def label_catalogue(action):
    #error
    if action == 4:
        check_invalid_len()
        if error_flag["flag"] == "yes":
            return
    error_flag["flag"] = "no"
    label_inform()
    frames["catalogue"] = tk.Frame(root, bg="white")
    frames["catalogue"].place(x=34, y=125, height=512, width=272)
    frames["catalogue"].grid_propagate(False)
    if (action == 1) or (action == 5):
        general_catalogue.update(user_catalogue)
    elif (action == 2) or (action == 4):
        general_catalogue.update(existed_catalogue)
    card_num = 0
    for name, stats in general_catalogue.items():
        cards_button = tk.Button(frames["catalogue"], text=name, command=lambda name=name:(card.update({"name": name}), card_detail(action)),
            font=themes["catalogue"]["font"], bg=themes["catalogue"]["bg"], fg=themes["catalogue"]["fg"], width=themes["catalogue"]["width"], relief=themes["relief"])
        cards_button.place(x=9, y=10+card_num*50)
        if action == 5:
            label = tk.Label(frames["catalogue"], text="", bg="red", font=themes["catalogue"]["font"], borderwidth=7)
            label.place(x=245, y=10+card_num*50)
        card_num = card_num + 1
    for each in range(maximum_cards):
        if each >= card_num:
            laybel = tk.Label(frames["catalogue"], text="Empty Card Box",
                font=themes["catalogue"]["font"], bg=themes["catalogue"]["bg"], fg=themes["catalogue"]["fg"], width=26, borderwidth=8)
            laybel.place(x=9, y=10+card_num*50)
            card_num = card_num + 1
    if action == 1 or action == 2:
        inside_frame_label()
            #may be bug here

def manage_user_catalogue():
    frames["manage"] = tk.Frame(root, bg="#f2d243")
    frames["manage"].place(x=340, y=160, height=490, width=460)
    frames["manage"].grid_propagate(False)
    inside_frame_label()
    add_new_button = tk.Button(frames["manage"], text="Make your own card", command=add_new_card,
        font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
    add_new_button.place(x=22,y=115)
    add_exist_button = tk.Button(frames["manage"], text="Add from existing cards", command=lambda:label_catalogue(4),
        font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
    add_exist_button.place(x=22,y=205)
    delete_button = tk.Button(frames["manage"], text="Removing a card", command=lambda:label_catalogue(5),
        font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
    delete_button.place(x=22,y=295)
    go_back_button = tk.Button(frames["manage"], text="Go back", command=go_back,
        font=themes["exit"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=themes["exit"]["width"], relief=themes["relief"])
    go_back_button.place(x=106, y=390)

#----------main code----------
upload_catalogue()
user_catalogue = dict(sorted(user_catalogue.items(), key=lambda name: name[0].lower()))
existed_catalogue = dict(sorted(existed_catalogue.items(), key=lambda name: name[0].lower()))
for name, stats in user_catalogue.items():
        total = total + stats[4]

frames["title"] = tk.Frame(root, bg="#f2d243")
frames["title"].place(x=340, y=20, height=120, width=460)
frames["title"].grid_propagate(False)
text_label = tk.Label(frames["title"], text="———————————————",
    font=themes["title"]["font"], bg=themes["title"]["bg"], fg=themes["title"]["fg"])
text_label.place(x=23, y=35)
title_label = tk.Label(frames["title"], text="Monster Card Game Digital Catalogue", 
    font=themes["title"]["font"], bg=themes["title"]["bg"], fg=themes["title"]["fg"])
title_label.place(x=19, y=10)
subtitle_label = tk.Label(frames["title"], text="Choose what you want to do:",
    font=themes["title"]["font"], bg=themes["title"]["bg"], fg=themes["title"]["fg"])
subtitle_label.place(x=67, y=61)

frames["inform"] = tk.Frame(root, bg="#f2d243")
frames["inform"].place(x=20, y=20, height=630, width=300)
frames["inform"].grid_propagate(False)
text_label = tk.Label(frames["inform"], text="Your Monster Card Catalogue:", 
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=6, y=60)
text_label = tk.Label(frames["inform"], text="____", 
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=6, y=90)
text_label = tk.Label(frames["inform"], text=f"{len(user_catalogue)}/10", 
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=6, y=85)
text_label = tk.Label(frames["inform"], text="Your Monster Card's Stats':",
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=6, y=130)
text_label = tk.Label(frames["inform"], text="___", 
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=6, y=160)
text_label = tk.Label(frames["inform"], text=total,
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=6, y=155)

frames["button"] = tk.Frame(root, bg="#f2d243")
frames["button"].place(x=340, y=160, height=490, width=460)
frames["button"].grid_propagate(False)
user_catalogue_button = tk.Button(frames["button"], text="View your card catalogue", command=lambda: label_catalogue(1),
    font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
user_catalogue_button.place(x=22, y=39)
exist_catalogue_button = tk.Button(frames["button"], text="View existing card's catalogue", command=lambda: label_catalogue(2),
    font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
exist_catalogue_button.place(x=22, y=124)
manage_catalogue_button = tk.Button(frames["button"], text="Manage your card catalogue", command=manage_user_catalogue,
    font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
manage_catalogue_button.place(x=22, y=214)
print_catalogue_button = tk.Button(frames["button"], text="Print your catalogue", command=print_catalogue,
    font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
print_catalogue_button.place(x=22, y=300)
exit_button = tk.Button(frames["button"], text="Save & Exit", command=save_exit,
    font=themes["exit"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=themes["exit"]["width"], relief=themes["relief"])
exit_button.place(x=106, y=388)


#action1 : label user catalgoue
#action2 : label existed catalgoue
#action3 : made and add new cards
#action4 : label existed catalgoue and add from existed cards
#action5 : label user catalgoue and delete cards
#action6 : label cards that was beeing sorted and also used to mark no reverse
#action7 : used to mark as reversed

#run the code
root.mainloop()