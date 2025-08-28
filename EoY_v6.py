import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

root = tk.Tk()
root.title("")
root.geometry("520x750+300+90")

#image = Image.open("a_name.png")
#image = image.resize((100,100), Image.LANCZOS)
#image = ImageTk.PhotoImage(image)

#invalid
#laybel image
#sort
#laybel title subtitle
#bugs

total = 0
maximum_cards = 10
maximum_stats = 25
minimum_stats = 1
user_catalogue = {}
existed_catalogue = {}
frames = {}
window = {}
card = {}
action = {}
sort = "Alphabetical"
last_sort = {"sort_by": "Sort by..."}
general_catalogue = {}
reverse_flag = tk.BooleanVar(value=True)

def upload_catalogue():
    with open('user_catalogue_file.txt', 'r') as usercatalogueFile:
        for line in usercatalogueFile:
            if line.strip():
                name, stats = line.strip().split(':', 1)
                values = [int(item.strip()) for item in stats.split(',')]
                user_catalogue[name.strip()] = values
    with open('existed_catalogue.txt', 'r') as existedcatalogueFile:
        for line in existedcatalogueFile:
            if line.strip():
                name, stats = line.strip().split(':', 1)
                values = [int(item.strip()) for item in stats.split(',')]
                existed_catalogue[name.strip()] = values

def save_catalogue():
    with open('user_catalogue_file.txt', 'w') as usercatalogueFile:
        for name, stats in user_catalogue.items():
            each = f"{name}: {','.join(map(str, stats))}\n"
            usercatalogueFile.write(each)

def close_root():
    root.destroy()

def end_page():
    save_catalogue()
    root = tk.Toplevel()
    root.title("Over look")
    root.geometry("300x500+800+90")
    #label title
    for name, stats in user_catalogue.items():
        label = tk.Label(root, text=f"{name}: {stats}")
        label.pack()
    confirm_button = tk.Button(root, text="Confirm", command=close_root)
    confirm_button.pack()

def save_exit():
    response = messagebox.askquestion("Save & Exit", "Are you sure you want to end your program? (We will automatically save your catalogue)")
    if response == "yes":
        end_page()
    else:
        return
    
def error_popup(error_flag):
    if error_flag == 1:
        messagebox.showerror("Error", "You have reached the maximum number of cards!")
    elif error_flag == 2:
        messagebox.showerror("Error", "This card name already exists in the existing catalogue!")
    elif error_flag == 3:
        messagebox.showerror("Error", "This card name already exists in your catalogue!")
    elif error_flag == 4:
        messagebox.showerror("Error", "All stats must be integers!")
    elif error_flag == 5:
        messagebox.showerror("Error", f"Strength must be between {minimum_stats} and {maximum_stats}!")
    elif error_flag == 6:
        messagebox.showerror("Error", f"Speed must be between {minimum_stats} and {maximum_stats}!")
    elif error_flag == 7:
        messagebox.showerror("Error", f"Stealth must be between {minimum_stats} and {maximum_stats}!")
    elif error_flag == 8:
        messagebox.showerror("Error", f"Cunning must be between {minimum_stats} and {maximum_stats}!")


def check_invalid():
    if (card["name"].get() in existed_catalogue.keys()):
        error_popup(2)
        return
    if (card["name"].get() in user_catalogue.keys()):
        error_popup(3)
        return
    try:
        int(card["strength"].get())
        int(card["speed"].get())
        int(card["stealth"].get())
        int(card["cunning"].get())
    except ValueError:
        error_popup(4)
    if (int(card["strength"].get()) > maximum_stats) or (int(card["strength"].get()) < minimum_stats):
        error_popup(5)
        return
    if (int(card["speed"].get()) > maximum_stats) or (int(card["speed"].get()) < minimum_stats):
        error_popup(6)
        return
    if (int(card["stealth"].get()) > maximum_stats) or (int(card["stealth"].get()) < minimum_stats):
        error_popup(7)
        return
    if (int(card["cunning"].get()) > maximum_stats) or (int(card["cunning"].get()) < minimum_stats):
        error_popup(8)
        return

def check_invalid_len():
    #action
    if len(user_catalogue) == maximum_cards:
        error_popup(1)
        return

def find_card(entry):
    if entry in general_catalogue.keys():
        card["name"] = entry
        card_detail(1)
    else:
        messagebox.showinfo("Invalid Entry", f"There is no card named '{entry}' in the catalogue.")

def sort_card(sort, action, reverse_flag):
    if last_sort["sort_by"] == "Sort by...":
        sort = "Alphabetical"
    elif action == 7:
        sort = last_sort["sort_by"]
    if "catalogue" in frames:
        frames["catalogue"].destroy()
        del frames["catalogue"]
    if action == 7:
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
    general_catalogue.clear()
    general_catalogue.update(sorted_catalogue)
    last_sort["sort_by"] = sort
    label_catalogue(6) 

def inside_frame_label():
    find_label = tk.Label(frames["catalogue"], text="Find the card...")
    find_entry = tk.Entry(frames["catalogue"])
    find_button = tk.Button(frames["catalogue"], text="Find", command=lambda:find_card(find_entry.get()))
    action["sort_combo"] = ttk.Combobox(frames["catalogue"], 
                                                     values=["Alphabetical", "Total scored", "Strength", "Speed", "Stealth", "Cunning"])
    action["sort_combo"].set("Sort by...")
    sort_button = tk.Button(frames["catalogue"], text="Sort", command=lambda:sort_card(action["sort_combo"].get(), 6, reverse_flag))
    reverse_button = tk.Button(frames["catalogue"], text="↑↓", command=lambda:sort_card(action["sort_combo"].get(), 7, reverse_flag))
    go_back_button = tk.Button(frames["catalogue"], text="Go back", command=go_back)
    find_label.pack()
    find_entry.pack()
    find_button.pack()
    action["sort_combo"].pack()
    reverse_button.pack()
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

def confirm_action(action):
    #check is ok
    check_invalid()
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
        return

def card_detail(action):
    window["window2"] = tk.Toplevel(root)
    window["window2"].title(card["name"])
    window["window2"].geometry("300x500+800+90")
    name_label = tk.Label(window["window2"], text=card["name"])
    strength_label = tk.Label(window["window2"], text=f"Strength: {general_catalogue[card['name']][0]}")
    speed_label = tk.Label(window["window2"], text=f"Speed: {general_catalogue[card['name']][1]}")
    stealth_label = tk.Label(window["window2"], text=f"Stealth: {general_catalogue[card['name']][2]}")
    cunning_label = tk.Label(window["window2"], text=f"Cunning: {general_catalogue[card['name']][3]}")
    totalscore_label = tk.Label(window["window2"], text=f"Total scores: {general_catalogue[card['name']][4]}")
    confirm_button = tk.Button(window["window2"], text="Confirm", command=lambda: confirm_action(action))
    confirm_button.pack()
    if (action != 1) or (action != 2):
        cancel_button = tk.Button(window["window2"], text="Cancel", command=cancel_action)
        cancel_button.pack()
    name_label.pack()
    strength_label.pack()
    speed_label.pack()
    stealth_label.pack()
    cunning_label.pack()
    totalscore_label.pack()

def add_new_card():
    check_invalid_len()
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
    confirm_button = tk.Button(window["window2"], text="Confirm", command=lambda: confirm_action(3))
    confirm_button.pack()
    cancel_button = tk.Button(window["window2"], text="Cancel", command=cancel_action)
    cancel_button.pack()

def label_catalogue(action):
    check_invalid_len()
    frames["catalogue"] = tk.Frame(root, bg="grey")
    frames["catalogue"].pack()
    frames["catalogue"].grid_propagate(False)
    text_label = tk.Label(frames["catalogue"], text=f"Your Monster Card Catalogue: {len(user_catalogue)}/10")
    text_label.pack()
    if (action == 1) or (action == 5):
        general_catalogue.update(user_catalogue)
    elif (action == 2) or (action == 4):
        general_catalogue.update(existed_catalogue)
    for name, stats in general_catalogue.items():
        cards_button = tk.Button(frames["catalogue"], text=name, command=lambda name=name:(card.update({"name": name}), card_detail(action)))
        cards_button.pack()
        if action == 5:
            label = tk.Label(frames["catalogue"], text=" ", bg="red")
            label.pack()
    inside_frame_label()

def manage_user_catalogue():
    frames["manage"] = tk.Frame(root, bg="grey")
    frames["manage"].pack()
    frames["manage"].grid_propagate(False)
    add_exist_button = tk.Button(frames["manage"], text="Add from existing cards", command=lambda:label_catalogue(4))
    add_new_button = tk.Button(frames["manage"], text="Make your own card", command=add_new_card)
    add_exist_button.pack()
    add_new_button.pack()
    delete_button = tk.Button(frames["manage"], text="Removing a card", command=lambda:label_catalogue(5))
    delete_button.pack()

upload_catalogue()
user_catalogue = dict(sorted(user_catalogue.items(), key=lambda name: name[0].lower()))
existed_catalogue = dict(sorted(existed_catalogue.items(), key=lambda name: name[0].lower()))
for name, stats in user_catalogue.items():
        total = total + sum(stats[:4])
text_label = tk.Label(root, text=f"Your Monster Card Catalogue: {len(user_catalogue)}/10")
text_label.pack()
text_label = tk.Label(root, text=f"Your Monster Card's Stats': {total}")
text_label.pack()
user_catalogue_button = tk.Button(root, text="View your card catalogue", command=lambda: label_catalogue(1))
exist_catalogue_button = tk.Button(root, text="View existing card's catalogue", command=lambda: label_catalogue(2))
manage_catalogue_button = tk.Button(root, text="Manage your card catalogue", command=manage_user_catalogue)
exit_button = tk.Button(root, text="Save & Exit", command=save_exit)
user_catalogue_button.pack()
exist_catalogue_button.pack()
manage_catalogue_button.pack()
exit_button.pack()

#action1 : label user catalgoue
#action2 : label existed catalgoue
#action3 : made and add new cards
#action4 : label existed catalgoue and add from existed cards
#action5 : label user catalgoue and delete cards
#action6 : label cards that was beeing sorted and also used to mark no reverse
#action7 : used to mark as reversed

root.mainloop()