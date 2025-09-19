import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

#Create the main window for the application
#Set the window title, size, and background color
main_window = tk.Tk()
main_window.title("")
main_window.geometry("820x670+350+100")
main_window.configure(bg="white")

#-----------setting-----------
#Set maximum number of cards, stats limits, and initialize empty dictionaries/variables
maximum_cards = 10
maximum_stats = 25
minimum_stats = 1
max_image_num = 20 
user_catalogue = {}
existed_catalogue = {}
stored_images = {}
frames = {}
window = {}
card = {}
sort_controls = {}
sorted_catalogue = {}
displayed_catalogue = {}
image_dictionary = {}
parent_frame = {}
error_flag = {"flag": "no"}
text_update = {"1": None, "2": None, "3": None, "4": None}
total = {"scores": 0, "cards": 0, "empty_slot": 0}
image_number = {"current": 1}
sort = "Alphabetical"
last_sort = {"sort_by": "Sort by..."}
reverse_flag = tk.BooleanVar(value=True)

#Set the style and colors for different parts through the programe (titles, buttons, cards, etc.)
themes = {
    "title":   {"font": ("Impact", 20), "bg": "#f2d243", "fg": "#2f58e0"},
    "inform":  {"font": ("Impact", 16), "bg": "#f2d243", "fg": "#2f58e0"},
    "button":  {"font": ("Impact", 22), "bg": "#2f58e0", "fg": "white", "width": 29},
    "catalogue": {"font": ("Impact", 14), "bg": "#2f58e0", "fg": "white", "width": 27},
    "manage": {"font": ("Impact", 22), "bg": "#2f58e0", "fg": "white", "width": 29},
    "card": {"font": ("Impact", 16), "bg": "white", "fg": "#2f58e0"},
    "sort":  {"font": ("Impact", 16), "bg": "#2f58e0", "fg": "white", "width": 5},
    "print": {"font": ("Impact", 20), "bg": "#2f58e0", "fg": "white", "width": 15},
    "exit": {"font": ("Impact", 22), "bg": "#2f58e0", "fg": "white", "width": 17},
    "relief": "flat"
    }

#path to the files
image_dir = r'D:\Visual Studio code\EoY_Project_2025\prg_project_images'

user_catalogue_dir = r'D:\Visual Studio code\EoY_Project_2025\user_catalogue_file.txt'

existed_catalogue_dir = r'D:\Visual Studio code\EoY_Project_2025\existed_catalogue_file.txt'

#Load the main front image for display
image = Image.open(os.path.join(image_dir, "front_image.png"))
image = image.resize((250,350), Image.LANCZOS)
front_image = ImageTk.PhotoImage(image)

#Load all numbered images and store them in a dictionary
for num in range(1, max_image_num+1):
    image = Image.open(os.path.join(image_dir, f"{num}.png"))
    image = image.resize((250,350), Image.LANCZOS)
    image_dictionary[num] = ImageTk.PhotoImage(image)

#Create buttons for selecting images
def create_image_buttons():
    for n, name in enumerate(image_dictionary.keys()):
        image_button = tk.Button(main_window, image=image_dictionary[name], command=lambda n=name: select_image(n))
        image_button.pack(side="left", padx=5, pady=5)

#Load existing cards from a file into existed_catalogue
def upload_catalogue():
    with open(existed_catalogue_dir, 'r') as existedcatalogueFile:
        for line in existedcatalogueFile:
            if line.strip():
                parts = line.strip().split(':')
                name = parts[0].strip()
                values_part = parts[1].strip()
                values = [int(item.strip()) for item in values_part.split(',')]
                existed_catalogue[name] = values
    #Copy them to user_catalogue for initial display
    user_catalogue.update(existed_catalogue) 

#Update user catalogue totals and optionally sort
def update_catalogue(action):
    sorted_dict = dict(sorted(user_catalogue.items(), key=lambda name: name[0].lower()))
    user_catalogue.clear()
    user_catalogue.update(sorted_dict)
    #Recalculate total scores, card count, and empty slots
    total["scores"] = 0
    for name, stats in user_catalogue.items():
        total["scores"] = total["scores"] + stats[4]
    total["cards"] = len(user_catalogue)
    total["empty_slot"] = maximum_cards - total["cards"]
    if "catalogue_inform" in frames:
        display_catalogue(action)

#Save the current user catalogue to a file
def save_catalogue(action):
    update_catalogue(action)
    with open(user_catalogue_dir, 'w') as usercatalogueFile:
        for name, stats in user_catalogue.items():
            line = f"{name}: {','.join(map(str, stats))}\n"
            usercatalogueFile.write(line)

#Close any active frames or windows and refresh the catalogue display
def close_active_frame():
    subtitle_label.config(text="Choose what you want to do:")
    for key in ["manage", "sort", "catalogue_inform", "print", "window4"]:
        if key in frames:
            frames[key].destroy()
            del frames[key]
        if key in window:
            window[key].destroy()
            del window[key]
    update_catalogue(0)
    text_update["1"].config(text=f"{total['cards']}/10")
    text_update["2"].config(text=total["scores"])

#Exit the application completely
def exit_application():
    main_window.destroy() 

#----------sub functions----------    
#Show a table of cards in a new window with all stats and images
def print_table(action):
    save_catalogue(action)
    window["window4"] = tk.Toplevel(main_window)
    window["window4"].title("Your Monster Card Catalogue")
    window["window4"].geometry("800x580+360+140")
    window["window4"].configure(bg="#f0f0f0")    
    title_label = tk.Label(window["window4"], text="YOUR MONSTER CARD COLLECTION", 
        font=themes["print"]["font"], bg=themes["print"]["bg"], fg=themes["print"]["fg"])
    title_label.place(x=230, y=20)   
    column_settings = {
    "Card Name": {"width": 150},
    "Strength": {"width": 90},
    "Speed": {"width": 90},
    "Stealth": {"width": 90}, 
    "Cunning": {"width": 90},
    "Total Score": {"width": 100},
    "Image No.": {"width": 120}}
    columns = tuple(column_settings.keys())
    tree = ttk.Treeview(window["window4"], columns=tuple(column_settings.keys()), show="headings", height=12)
    for rows in columns:
        tree.heading(rows, text=rows)
        tree.column(rows, width=column_settings[rows]["width"], anchor="center")   
    for name, stats in user_catalogue.items():
        tree.insert("", "end", values=(
            name, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]))
    #Add empty slots if needed
    for Empty in range(len(user_catalogue), maximum_cards):
        tree.insert("", "end", values=("Empty Slot", "-", "-", "-", "-", "-", "-"))   
    tree.place(x=34, y=100)
 
    stats_label = tk.Label(window["window4"], text=f"Card Space: {total['cards']}/10 | Empty Slots: {total['empty_slot']} | Total Scores: {total['scores']}",
        font=("Impact", 14), bg=themes["print"]["bg"], fg=themes["print"]["fg"])
    stats_label.place(x=200, y=400)    
    if action == 7:
        confirm_button = tk.Button(window["window4"], text="CONFIRM & EXIT", command=exit_application,
            font=themes["print"]["font"], bg=themes["print"]["bg"], fg=themes["print"]["fg"], width=themes["print"]["width"])
        confirm_button.place(x=300, y=470)
    else:
        confirm_button = tk.Button(window["window4"], text="Confirm", command=close_active_frame,
            font=themes["print"]["font"], bg=themes["print"]["bg"], fg=themes["print"]["fg"], width=themes["print"]["width"])
        confirm_button.place(x=300, y=470)

#Ask the user to confirm before saving and exiting
def confirm_exit():
    response = messagebox.askquestion("Save & Exit", "Are you sure you want to end your program? (We will automatically save your catalogue)")
    if response == "yes":
        print_table(7)
    else:
        return

#Find a card by name and show its details if it exists    
def find_card(entry):
    if entry in displayed_catalogue.keys():
        card["name"] = entry
        display_card_details(1)
    else:
        messagebox.showinfo("Invalid Entry", f"There is no card named {entry} in the catalogue.")

#Sort the displayed catalogue based on the selected criteria
def sort_card(sort_action):   
    sort = sort_controls["sort_combo"].get()
    if "catalogue" in frames:
        frames["catalogue"].destroy()
        del frames["catalogue"]
    else:
        return   
    if sort_controls["sort_combo"].get() == "Sort by...":
        if last_sort["sort_by"] == "Sort by...":
            sort = "Alphabetical"
        else: 
            sort = last_sort["sort_by"]
    #Handle reverse order if the reverse button is clicked
    if sort_action == 7:
        reverse_flag.set(not reverse_flag.get())
        reverse = reverse_flag.get()
        reverse2 = (not reverse_flag.get())
    else: 
        reverse_flag2 = tk.BooleanVar(value=True)
        reverse = reverse_flag2.get()
        reverse2 = (not reverse_flag2.get())
    if sort == "Alphabetical":
        sorted_catalogue = dict(sorted(displayed_catalogue.items(), key=lambda name: name[0].casefold(), reverse=reverse2))
    elif sort == "Total scored":
        sorted_catalogue = dict(sorted(displayed_catalogue.items(), key=lambda name: name[1][4], reverse=reverse))
    elif sort == "Strength":
        sorted_catalogue = dict(sorted(displayed_catalogue.items(), key=lambda name: name[1][0], reverse=reverse))
    elif sort == "Speed":
        sorted_catalogue = dict(sorted(displayed_catalogue.items(), key=lambda name: name[1][1], reverse=reverse))
    elif sort == "Stealth":
        sorted_catalogue = dict(sorted(displayed_catalogue.items(), key=lambda name: name[1][2], reverse=reverse))
    elif sort == "Cunning":
        sorted_catalogue = dict(sorted(displayed_catalogue.items(), key=lambda name: name[1][3], reverse=reverse))
    last_sort["sort_by"] = sort
    displayed_catalogue.clear()
    displayed_catalogue.update(sorted_catalogue)
    display_catalogue(6) 

#Set up the sort and search frame for catalogue display
def setup_sort_frame():
    if "manage" in frames:
        parent_frame = frames["manage"]
        y_axis = 44
    else:
        frames["sort"] = tk.Frame(main_window, bg="#f2d243")
        frames["sort"].place(x=340, y=160, height=490, width=460)
        frames["sort"].grid_propagate(False)
        parent_frame = frames["sort"]
        y_axis = 150
    find_entry = tk.Entry(parent_frame,
        font=themes["sort"]["font"], bg="white", fg=themes["sort"]["bg"])
    find_entry.place(x=17, y=y_axis, width=120)
    find_entry.insert(5, "Find card...")
    find_button = tk.Button(parent_frame, text="FIND", command=lambda:find_card(find_entry.get()),
        font=themes["sort"]["font"], bg=themes["sort"]["bg"], fg=themes["sort"]["fg"], width=themes["sort"]["width"], relief=themes["relief"])
    find_button.place(x=142, y=y_axis-9)
    style = ttk.Style()
    style.configure("TCombobox", foreground="#2f58e0")
    sort_controls["sort_combo"] = ttk.Combobox(parent_frame, 
                values=["Alphabetical", "Total scored", "Strength", "Speed", "Stealth", "Cunning"],
                font=themes["sort"]["font"])
    sort_controls["sort_combo"].set("Sort by...")
    sort_controls["sort_combo"].place(x=222, y=y_axis, width=120)
    sort_button = tk.Button(parent_frame, text="SORT", command=lambda:sort_card(6),
        font=themes["sort"]["font"], bg=themes["sort"]["bg"], fg=themes["sort"]["fg"], width=themes["sort"]["width"], relief=themes["relief"])
    sort_button.place(x=347, y=y_axis-9)
    reverse_button = tk.Button(parent_frame, text="↑↓", command=lambda:sort_card(7),
        font=themes["sort"]["font"], bg=themes["sort"]["bg"], fg=themes["sort"]["fg"], width=2, relief=themes["relief"])
    reverse_button.place(x=412, y=y_axis-9, width=30)
    if "sort" in frames:
        close_active_frame_button = tk.Button(parent_frame, text="Go back", command=close_active_frame,
            font=themes["exit"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=themes["exit"]["width"], relief=themes["relief"])
        close_active_frame_button.place(x=102, y=240)

#----------main functions----------
#Show error popups for different invalid inputs
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
    #Lift my display of card to the top
    if "window2" in window and window["window2"].winfo_exists():
        window["window2"].lift()
        window["window2"].focus_force()

#Check if card input values are valid and call error_popup if needed
def check_invalid(action):
    if action == 3:
        if (card["name"].get() in existed_catalogue.keys()):
            error_popup(2)
            return
        if (card["name"].get() in user_catalogue.keys()):
            error_popup(3)
            return
    elif action == 4:
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

#Check if the user has reached the maximum card limit
def check_card_limit():
    if len(user_catalogue) == maximum_cards: 
        error_popup(1)
        error_flag["flag"] = "yes"

#Confirm actions like adding, copying, or deleting cards
def confirm_action(action):   
    if (action == 3) or (action == 4) or (action == 5):
        error_flag["flag"] = "no" 
        check_invalid(action)        
        if error_flag["flag"] == "yes":
            return        
        if action != 5:
            if action == 3:
                card["name"] = card["name"].get()
                strength = int(card["strength"].get())
                speed = int(card["speed"].get())
                stealth = int(card["stealth"].get())
                cunning = int(card["cunning"].get())
                total = strength + speed + stealth + cunning
                displayed_catalogue[card["name"]] = [strength, speed, stealth, cunning, total, image_number["current"]]
            else:
                displayed_catalogue[card["name"]] = existed_catalogue[card["name"]]
            display_card_details(8)
        else:
            response = messagebox.askquestion("Yes/no", "Are you sure you want to delete this card?")
            if response == "yes":
                del user_catalogue[card["name"]]
            else:
                window["window2"].lift()
                window["window2"].focus_force()
                return
        save_catalogue(action)
    if "window2" in window:
        window["window2"].destroy()

def confirm_update(action):
    if action == 8:
        user_catalogue.update(displayed_catalogue)
        save_catalogue(action)
        window["window2"].destroy()
    window["window3"].destroy()

#Cancel the current action with a confirmation popup
def cancel_action():
    response = messagebox.askquestion("Cancel", "Are you sure you want to stop editing this card?")
    if response == "yes":
        window["window2"].destroy()
    else:
        window["window2"].lift()
        window["window2"].focus_force()
        return

#Show all details of a single card in a window
#Include stats, total score, and image
def display_card_details(action):
    if action != 8:
        window["window2"] = tk.Toplevel(main_window, bg="white")
        window["window2"].title(card["name"])
        window["window2"].geometry("340x600+800+90")
        frames["labeling"] = tk.Frame(window["window2"], bg="#f2d243")
    else:
        window["window3"] = tk.Toplevel(main_window, bg="white")
        window["window3"].title(card["name"])
        window["window3"].geometry("340x600+800+90")
        frames["labeling"] = tk.Frame(window["window3"], bg="#f2d243")
    frames["labeling"].place(x=5, y=5, height=590, width=330)
    frames["labeling"].grid_propagate(False)
    image = tk.Label(frames["labeling"], image=image_dictionary[displayed_catalogue[card['name']][5]], bg="white")
    image.image = image_number["current"] = image_dictionary[displayed_catalogue[card['name']][5]]
    image.place(x=38, y=5)
    frames["card"] = tk.Frame(frames["labeling"], bg="white")
    frames["card"].place(x=10, y=354, height=175, width=310)
    frames["card"].grid_propagate(False)
    name_label = tk.Label(frames["card"], text=f"NAME:  {card['name']}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    name_label.place(x=5, y=5)
    label = tk.Label(frames["card"], text="", bg="#f2d243", width=50)
    label.place(x=0, y=40)
    strength_label = tk.Label(frames["card"], text=f"Strength:  {displayed_catalogue[card['name']][0]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    strength_label.place(x=5, y=65)
    speed_label = tk.Label(frames["card"], text=f"Speed:  {displayed_catalogue[card['name']][1]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    speed_label.place(x=150, y=65)
    stealth_label = tk.Label(frames["card"], text=f"Stealth:  {displayed_catalogue[card['name']][2]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    stealth_label.place(x=5, y=95)
    cunning_label = tk.Label(frames["card"], text=f"Cunning:  {displayed_catalogue[card['name']][3]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    cunning_label.place(x=150, y=95)
    totalscore_label = tk.Label(frames["card"], text=f"TOTAL SCORES:  {displayed_catalogue[card['name']][4]}",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    totalscore_label.place(x=5, y=135)
    if action == 8:
        confirm_button = tk.Button(window["window3"], text="Add", command=lambda: confirm_update(8),
        font=themes["card"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=10, relief=themes["relief"])
        confirm_button.place(x=45, y=540)
        cancel_button = tk.Button(window["window3"], text="Cancel", command=lambda: confirm_update(0),
            font=themes["card"]["font"], bg="red", fg=themes["exit"]["fg"], width=10, relief=themes["relief"])
        cancel_button.place(x=185, y=540)
    elif (action != 1) and (action != 2) and (action != 6):
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

#Allow user to select images for cards without repeating used ones
def select_image(direction, image_label):
    used_images = set()
    for stats in user_catalogue.values():
        used_images.add(stats[5])
   
    if direction == "left":
        image_number["current"] -= 1
    else:
        image_number["current"] += 1
    if image_number["current"] < 1:
        image_number["current"] = max_image_num 
    elif image_number["current"] > max_image_num :
        image_number["current"] = 1
    while image_number["current"] in used_images:
        if direction == "left":
            image_number["current"] -= 1
            if image_number["current"] < 1:
                image_number["current"] = max_image_num
        else:
            image_number["current"] += 1
            if image_number["current"] > max_image_num:
                image_number["current"] = 1
    image_label.config(image=image_dictionary[image_number["current"]])
    image_label.image = image_dictionary[image_number["current"]]

#Open a window to create a new card
def add_new_card():
    error_flag["flag"] = "no"
    check_card_limit()
    if error_flag["flag"] == "yes":
        return
    window["window2"] = tk.Toplevel(main_window, bg="white")
    window["window2"].title("Design your own card")
    window["window2"].geometry("340x600+800+90")
    frames["labeling"] = tk.Frame(window["window2"], bg="#f2d243")
    frames["labeling"].place(x=5, y=5, height=590, width=330)
    frames["labeling"].grid_propagate(False)   
    image_number["current"] = 1
    image_label = tk.Label(frames["labeling"])
    image_label.place(x=38, y=5)
    image_label.config(image=image_dictionary[image_number["current"]])
    image_label.image = image_dictionary[image_number["current"]]
    select_left_button = tk.Button(frames["labeling"], text="◀", command=lambda: select_image("left", image_label),
        font=themes["card"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], relief=themes["relief"])
    select_left_button.place(x=4, y=300)
    select_right_button = tk.Button(frames["labeling"], text="▶", command=lambda: select_image("right", image_label),
        font=themes["card"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], relief=themes["relief"])
    select_right_button.place(x=294, y=300)
    frames["card"] = tk.Frame(frames["labeling"], bg="white")
    frames["card"].place(x=10, y=354, height=175, width=310)
    frames["card"].grid_propagate(False)
    name_label = tk.Label(frames["card"], text="NAME:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    name_label.place(x=5, y=5)
    card["name"] = tk.Entry(frames["card"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=15)
    card["name"].place(x=68, y=5)
    label = tk.Label(frames["card"], text="", bg="#f2d243", width=50)
    label.place(x=0, y=40)
    strength_label = tk.Label(frames["card"], text="Strength:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    strength_label.place(x=5, y=70)
    card["strength"] = tk.Entry(frames["card"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=4)
    card["strength"].place(x=93, y=70)
    speed_label = tk.Label(frames["card"], text="Speed:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    speed_label.place(x=150, y=70)
    card["speed"] = tk.Entry(frames["card"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=4)
    card["speed"].place(x=220, y=70)
    stealth_label = tk.Label(frames["card"], text="Stealth:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    stealth_label.place(x=5, y=110)
    card["stealth"] = tk.Entry(frames["card"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=4)
    card["stealth"].place(x=82, y=110)
    cunning_label = tk.Label(frames["card"], text="Cunning:",
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"])
    cunning_label.place(x=150, y=110)
    card["cunning"] = tk.Entry(frames["card"],
        font=themes["card"]["font"], bg=themes["card"]["bg"], fg=themes["card"]["fg"], width=4)
    card["cunning"].place(x=235, y=110)
    confirm_button = tk.Button(window["window2"], text="Confirm", command=lambda: confirm_action(3),
        font=themes["card"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=10, relief=themes["relief"])
    confirm_button.place(x=45, y=540)
    cancel_button = tk.Button(window["window2"], text="Cancel", command=cancel_action,
        font=themes["card"]["font"], bg="red", fg=themes["exit"]["fg"], width=10, relief=themes["relief"])
    cancel_button.place(x=185, y=540)

#Display the list of cards in a frame
def display_catalogue(action):
    error_flag["flag"] = "no"
    if action == 4:
        check_card_limit()
        if error_flag["flag"] == "yes":
            return
    if "catalogue_inform" in frames:
        frames["catalogue_inform"].destroy()
        del frames["catalogue_inform"]        
    frames["catalogue_inform"] = tk.Frame(main_window, bg="#f2d243")
    frames["catalogue_inform"].place(x=20, y=20, height=630, width=300)
    frames["catalogue_inform"].grid_propagate(False)
    text_update["3"] = tk.Label(frames["catalogue_inform"], text="MY   MONSTER   CARD", 
    font=("Impact", 20), bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
    text_update["3"].place(x=15, y=15)
    text_update["4"] = tk.Label(frames["catalogue_inform"], text=f"CATALOGUE:                {total['cards']}/10", 
    font=("Impact", 20), bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
    text_update["4"].place(x=15, y=50)
    if action == 2 or action == 4 or action == 8 or action == 9:
        text_update["3"].config(text="AVAILABLE    CARD")
        text_update["4"].config(text=f"CATALOGUE:                {len(existed_catalogue)}/10")
    frames["catalogue"] = tk.Frame(frames["catalogue_inform"], bg="white")
    frames["catalogue"].place(x=14, y=106, height=512, width=272)
    frames["catalogue"].grid_propagate(False)
    if (action == 1) or (action == 5):
        if action == 1:
            subtitle_label.config(text="     View my card catalogue:")
        else:
            subtitle_label.config(text="              Remove a card:")
        displayed_catalogue.clear()
        displayed_catalogue.update(user_catalogue)
    elif (action == 2) or (action == 4):
        if action == 2:
            subtitle_label.config(text="       View available cards:")
        else:
            subtitle_label.config(text="       Add an available card:")
        displayed_catalogue.clear()
        displayed_catalogue.update(existed_catalogue)
    #Display te catalogue
    card_num = 0
    for name, stats in displayed_catalogue.items():
        cards_button = tk.Button(frames["catalogue"], text=name, command=lambda name=name:(card.update({"name": name}), display_card_details(action)),
            font=themes["catalogue"]["font"], bg=themes["catalogue"]["bg"], fg=themes["catalogue"]["fg"], width=themes["catalogue"]["width"], relief=themes["relief"])
        cards_button.place(x=9, y=10+card_num*50)
        if action == 5:
            label = tk.Label(frames["catalogue"], text="", bg="red", font=themes["catalogue"]["font"], borderwidth=7)
            label.place(x=245, y=10+card_num*50)
        card_num = card_num + 1
    #Show empty slots if there are fewer than max cards
    for each in range(maximum_cards):
        if each >= card_num:
            laybel = tk.Label(frames["catalogue"], text="Empty Slot",
                font=themes["catalogue"]["font"], bg=themes["catalogue"]["bg"], fg=themes["catalogue"]["fg"], width=26, borderwidth=8)
            laybel.place(x=9, y=10+card_num*50)
            card_num = card_num + 1
    #Call setup_sort_frame if needed
    if action == 1 or action == 2:
        setup_sort_frame()

#Open the management window for creating, adding, or deleting cards
def manage_user_catalogue():
    subtitle_label.config(text=" Manage my card catalogue:")
    frames["manage"] = tk.Frame(main_window, bg="#f2d243")
    frames["manage"].place(x=340, y=160, height=490, width=460)
    frames["manage"].grid_propagate(False)
    setup_sort_frame()
    add_new_button = tk.Button(frames["manage"], text="Create a new card", command=add_new_card,
        font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
    add_new_button.place(x=22,y=115)
    add_exist_button = tk.Button(frames["manage"], text="Add an available card", command=lambda:display_catalogue(4),
        font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
    add_exist_button.place(x=22,y=205)
    delete_button = tk.Button(frames["manage"], text="Remove a card", command=lambda:display_catalogue(5),
        font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
    delete_button.place(x=22,y=295)
    close_active_frame_button = tk.Button(frames["manage"], text="Go back", command=close_active_frame,
        font=themes["exit"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=themes["exit"]["width"], relief=themes["relief"])
    close_active_frame_button.place(x=106, y=390)

#----------main code----------
#Upload existing catalogue from file
upload_catalogue()
existed_catalogue = dict(sorted(existed_catalogue.items(), key=lambda name: name[0].lower()))
update_catalogue(0)

#Set up the title frame with main heading and subtitle
frames["title"] = tk.Frame(main_window, bg="#f2d243")
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

#Set up the information frame showing total cards and total stats
frames["inform"] = tk.Frame(main_window, bg="#f2d243")
frames["inform"].place(x=20, y=20, height=630, width=300)
frames["inform"].grid_propagate(False)
text_label = tk.Label(frames["inform"], text="Your Monster Card Collection:", 
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=10, y=80)
text_label = tk.Label(frames["inform"], text="____", 
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=10, y=110)
text_update["1"] = tk.Label(frames["inform"], text=f"{total['cards']}/10", 
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_update["1"].place(x=10, y=105)
text_label = tk.Label(frames["inform"], text="Total Stats of Your Cards:",
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=10, y=150)
text_label = tk.Label(frames["inform"], text="___", 
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_label.place(x=10, y=180)
text_update["2"] = tk.Label(frames["inform"], text=total["scores"],
    font=themes["inform"]["font"], bg=themes["inform"]["bg"], fg=themes["inform"]["fg"])
text_update["2"].place(x=10, y=175)
image_lable = tk.Label(frames["inform"], image=front_image, bg=themes["inform"]["bg"])
image_lable.place(x=0, y=276)

#Set up the main button frame
frames["button"] = tk.Frame(main_window, bg="#f2d243")
frames["button"].place(x=340, y=160, height=490, width=460)
frames["button"].grid_propagate(False)
user_catalogue_button = tk.Button(frames["button"], text="View my card catalogue", command=lambda: display_catalogue(1),
    font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
user_catalogue_button.place(x=22, y=39)
exist_catalogue_button = tk.Button(frames["button"], text="View available card's catalogue", command=lambda: display_catalogue(2),
    font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
exist_catalogue_button.place(x=22, y=124)
manage_catalogue_button = tk.Button(frames["button"], text="Manage my card catalogue", command=manage_user_catalogue,
    font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
manage_catalogue_button.place(x=22, y=214)
print_catalogue_button = tk.Button(frames["button"], text="Print my collections", command=lambda: print_table(6),
    font=themes["button"]["font"], bg=themes["button"]["bg"], fg=themes["button"]["fg"], width=themes["button"]["width"], relief=themes["relief"])
print_catalogue_button.place(x=22, y=300)
exit_button = tk.Button(frames["button"], text="Save & Exit", command=confirm_exit,
    font=themes["exit"]["font"], bg=themes["exit"]["bg"], fg=themes["exit"]["fg"], width=themes["exit"]["width"], relief=themes["relief"])
exit_button.place(x=106, y=388)

#action0 : no meaning
#action1 : label user catalgoue
#action2 : label existed catalgoue
#action3 : made and add new cards
#action4 : label existed catalgoue and add from existed cards
#action5 : label user catalgoue and delete cards
#action6 : print function
#action7 : confirm and exit 
#action8 : displaying the card that need to be check by the user

#Start the main application loop
main_window.mainloop()