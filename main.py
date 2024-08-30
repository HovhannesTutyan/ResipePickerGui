import numpy as np
import tkinter as tk
from PIL import ImageTk
import sqlite3
import random

bg_color = "#3d6466"

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def fetch_db():
    connection = sqlite3.connect("data/recipis.db")
    cursor = connection.cursor()
    tables = cursor.execute("SELECT * FROM recipis")
    all_tables = tables.fetchall() 
    idx =  random.randint(0, len(all_tables)-1)

    title = all_tables[idx][0]
    description = all_tables[idx][1]
    connection.close()
    return title, description

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False) # saving the background color when image is added

    logo_img = ImageTk.PhotoImage(file="assets/logo.png") # add image in the frame1
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label( # create label for ready in frame1
        frame1,
        text="ready for your random recipe?",
        bg=bg_color,
        fg="white", 
        font=("TkMenuFont", 14)
    ).pack(pady=20, padx=20)

    tk.Button(
        frame1,
        text="Suffel",
        font=("TkHeadingFont", 20),
        bg="#28393a", 
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
    ).pack()

def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    title, description = fetch_db()

    logo_img = ImageTk.PhotoImage(file="assets/logo.png") # add image in the frame1
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)
 
    tk.Label( # create label for ready in frame1
        frame2,
        text=title,
        bg=bg_color,
        fg="white", 
        font=("TkHeadingFont", 14)
    ).pack(pady=20, padx=20)

    tk.Label(
        frame2, 
        text=description,
        bg=bg_color, 
        fg="white",
        font=("TkMenuFont", 14)
    ).pack(padx=25)

    tk.Button(
        frame2,
        text="Back",
        font=("TkHeadingFont", 20),
        bg="#28393a", 
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame1()
    ).pack()

root = tk.Tk()
root.title("Recippe Picker")
root.eval("tk::PlaceWindow . center") # place the window in the center

frame1 = tk.Frame(root, width=500, height=500, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky='nesw')
load_frame1()


root.mainloop()