"""
Author: Matthew James
Class: CSE 111

Purpose of Code: Allow the user to save and generate passwords into a running program. 
"""
import tkinter as tk
import random
from functools import partial
import random
import string

#Assigns global variables

# Creates a list that holds the passwords entered. 
saved_entries = []

# Makes counts used in keeping track of how many characters are in the password box
count = 0
count2 = 0


def main():

    try:
        
        # Creates a tk root object and assigns size

        root = tk.Tk()
        root.geometry("600x150")
        
        # Makes input boxes
        save_box = make_user_input("Please enter the place to which this password applies",0,0)
        password_box = make_user_input("Please enter an 8 character password",2,0)
        
        # Makes labels and formats the window
        saved_passwords = tk.Label(text="Saved Passwords: ")
        filler = tk.Label(text="")

        # Makes a button that will "Save" a password
        save_button = tk.Button(root, text="Save",command=partial(save, save_box, password_box))
        random_button = tk.Button(root, text="Random Password", comman=partial(gen_random_password, password_box))

        # Formats the window
        save_button.grid( row=3, column=3, padx=3, pady=2)
        random_button.grid(row=4, column=3)
        filler.grid(row=0, column=3)
        saved_passwords.grid(row=0, column=4)

        # Names the window
        root.title('Password Saver/Maker')


        # Creates a loop that will process user events
        root.mainloop()
    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")

# This creates a text entry box at a specific grid space as well as returns the box for further formating
def make_user_input(name, row, column):
    label = tk.Label(text=name)
    entry = tk.Entry()
    entry.grid(row=row+1, column=column, padx=1,pady=2,sticky="n")
    label.grid(row=row, column=column, padx=1,pady=1,sticky="n")
    return entry

# Saves the password to a list and displays it in the window
def save(entry1, entry2):
    if len(entry2.get()) != 8:
        return
    global count
    global count2
    count = count + 1
    if count/4 == 1 or count/4 ==2 or count/4 == 3:
        count = 1
        count2 =+1
    saved_entries.append(entry1.get())
    saved_entries.append(entry2.get())
    saved_list_label = tk.Label(text=saved_entries)
    saved_list_label.grid(row=1+count, column=4+count2)    
    if len(saved_entries) == 2:
        saved_entries.pop(0)
        saved_entries.pop(0)

# Creates a random password and inserts it into the entry box
def gen_random_password(entry1):
    letters = string.ascii_lowercase
    numbers_special = ['1','2','3','4','5','6','7','8','9','0','$','@','!','%']
    random_str = (''.join(random.choice(letters) for i in range(4)) )
    random_num = (''.join(random.choice(numbers_special) for i in range(4)) )
    random_pass = random_str + random_num
    entry1.insert(0,random_pass)



main()