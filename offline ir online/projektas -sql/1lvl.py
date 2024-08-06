from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import pygame
from subprocess import call
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"level1_image")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sudoku_db"
    )
mycursor = db.cursor()


window = Tk()

window.geometry("1542x976")
window.configure(bg = "#FFFFFF")
window.title("Šudoku")

def play_music(window):
    pygame.mixer.init()
    pygame.mixer.music.load(r"music2.mp3")
    pygame.mixer.music.play(-1)
    
def stop_music():
    pygame.mixer.music.stop()
    
def on_closing():
    stop_music()
    window.destroy()

pygame.init()
play_music(window)

def home():
    stop_music()
    window.destroy()
    call(["python", "menu.py"])
    
def title():
    stop_music()
    window.destroy()
    call(["python", "title.py"])
    


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 976,
    width = 1542,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    521.0 + 150,
    15.0,
    anchor="nw",
    text="Šudoku",
    fill="#1E1E1E",
    font=("Inter ExtraBold", 64 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    771.0,
    463.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    423.5,
    245.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 20, "bold"),
    justify="center"
)
entry_1.place(
    x=391.0,
    y=217.0,
    width=65.0,
    height=55.0
)
#entry_1.insert(0, "")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    488.5,
    302.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_2.place(
    x=456.0,
    y=274.0,
    width=65.0,
    height=55.0
)
entry_2.insert(0, "6")
entry_2.configure(state="readonly")

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    488.5,
    245.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_3.place(
    x=456.0,
    y=217.0,
    width=65.0,
    height=55.0
)
entry_3.insert(0, "7")
entry_3.configure(state="readonly")

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    423.5,
    302.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_4.place(
    x=391.0,
    y=274.0,
    width=65.0,
    height=55.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    553.5,
    245.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_5.place(
    x=521.0,
    y=217.0,
    width=65.0,
    height=55.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    553.5,
    302.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_6.place(
    x=521.0,
    y=274.0,
    width=65.0,
    height=55.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    423.5,
    359.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_7.place(
    x=391.0,
    y=331.0,
    width=65.0,
    height=55.0
)
entry_7.insert(0, "2")
entry_7.configure(state="readonly")

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    488.5,
    359.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_8.place(
    x=456.0,
    y=331.0,
    width=65.0,
    height=55.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    553.5,
    359.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_9.place(
    x=521.0,
    y=331.0,
    width=65.0,
    height=55.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    625.5,
    245.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_10.place(
    x=593.0,
    y=217.0,
    width=65.0,
    height=55.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    625.5,
    302.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_11.place(
    x=593.0,
    y=274.0,
    width=65.0,
    height=55.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    625.5,
    359.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_12.place(
    x=593.0,
    y=331.0,
    width=65.0,
    height=55.0
)
entry_12.insert(0, "8")
entry_12.configure(state="readonly")

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    690.5,
    359.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_13.place(
    x=658.0,
    y=331.0,
    width=65.0,
    height=55.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    690.5,
    302.5,
    image=entry_image_14
)
entry_14 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_14.place(
    x=658.0,
    y=274.0,
    width=65.0,
    height=55.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    690.5,
    245.5,
    image=entry_image_15
)
entry_15 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_15.place(
    x=658.0,
    y=217.0,
    width=65.0,
    height=55.0
)
entry_15.insert(0, "2")
entry_15.configure(state="readonly")

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    755.5,
    245.5,
    image=entry_image_16
)
entry_16 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_16.place(
    x=723.0,
    y=217.0,
    width=65.0,
    height=55.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    755.5,
    302.5,
    image=entry_image_17
)
entry_17 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_17.place(
    x=723.0,
    y=274.0,
    width=65.0,
    height=55.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    755.5,
    359.5,
    image=entry_image_18
)
entry_18 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_18.place(
    x=723.0,
    y=331.0,
    width=65.0,
    height=55.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    827.5,
    245.5,
    image=entry_image_19
)
entry_19 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_19.place(
    x=795.0,
    y=217.0,
    width=65.0,
    height=55.0
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    827.5,
    302.5,
    image=entry_image_20
)
entry_20 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_20.place(
    x=795.0,
    y=274.0,
    width=65.0,
    height=55.0
)
entry_20.insert(0, "8")
entry_20.configure(state="readonly")

entry_image_21 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(
    827.5,
    359.5,
    image=entry_image_21
)
entry_21 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_21.place(
    x=795.0,
    y=331.0,
    width=65.0,
    height=55.0
)
entry_21.insert(0, "7")
entry_21.configure(state="readonly")

entry_image_22 = PhotoImage(
    file=relative_to_assets("entry_22.png"))
entry_bg_22 = canvas.create_image(
    892.5,
    245.5,
    image=entry_image_22
)
entry_22 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_22.place(
    x=860.0,
    y=217.0,
    width=65.0,
    height=55.0
)
entry_22.insert(0, '4')
entry_22.configure(state="readonly")

entry_image_23 = PhotoImage(
    file=relative_to_assets("entry_23.png"))
entry_bg_23 = canvas.create_image(
    891.5,
    302.5,
    image=entry_image_23
)
entry_23 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_23.place(
    x=859.0,
    y=274.0,
    width=65.0,
    height=55.0
)
entry_23.insert(0, '9')
entry_23.configure(state='readonly')

entry_image_24 = PhotoImage(
    file=relative_to_assets("entry_24.png"))
entry_bg_24 = canvas.create_image(
    891.5,
    359.5,
    image=entry_image_24
)
entry_24 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_24.place(
    x=859.0,
    y=331.0,
    width=65.0,
    height=55.0
)
entry_24.insert(0, '1')
entry_24.configure(state='readonly')

entry_image_25 = PhotoImage(
    file=relative_to_assets("entry_25.png"))
entry_bg_25 = canvas.create_image(
    957.5,
    245.5,
    image=entry_image_25
)
entry_25 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_25.place(
    x=925.0,
    y=217.0,
    width=65.0,
    height=55.0
)
entry_25.insert(0, '6')
entry_25.configure(state='readonly')

entry_image_26 = PhotoImage(
    file=relative_to_assets("entry_26.png"))
entry_bg_26 = canvas.create_image(
    956.5,
    302.5,
    image=entry_image_26
)
entry_26 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_26.place(
    x=924.0,
    y=274.0,
    width=65.0,
    height=55.0
)

entry_image_27 = PhotoImage(
    file=relative_to_assets("entry_27.png"))
entry_bg_27 = canvas.create_image(
    956.5,
    359.5,
    image=entry_image_27
)
entry_27 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_27.place(
    x=924.0,
    y=331.0,
    width=65.0,
    height=55.0
)
entry_27.insert(0, '5')
entry_27.configure(state='readonly')

entry_image_28 = PhotoImage(
    file=relative_to_assets("entry_28.png"))
entry_bg_28 = canvas.create_image(
    423.5,
    422.5,
    image=entry_image_28
)
entry_28 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_28.place(
    x=391.0,
    y=394.0,
    width=65.0,
    height=55.0
)

entry_image_29 = PhotoImage(
    file=relative_to_assets("entry_29.png"))
entry_bg_29 = canvas.create_image(
    423.5,
    479.5,
    image=entry_image_29
)
entry_29 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_29.place(
    x=391.0,
    y=451.0,
    width=65.0,
    height=55.0
)
entry_29.insert(0, '7')
entry_29.configure(state='readonly')

entry_image_30 = PhotoImage(
    file=relative_to_assets("entry_30.png"))
entry_bg_30 = canvas.create_image(
    423.5,
    536.5,
    image=entry_image_30
)
entry_30 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_30.place(
    x=391.0,
    y=508.0,
    width=65.0,
    height=55.0
)

entry_image_31 = PhotoImage(
    file=relative_to_assets("entry_31.png"))
entry_bg_31 = canvas.create_image(
    488.5,
    422.5,
    image=entry_image_31
)
entry_31 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_31.place(
    x=456.0,
    y=394.0,
    width=65.0,
    height=55.0
)
entry_31.insert(0, '8')
entry_31.configure(state='readonly')

entry_image_32 = PhotoImage(
    file=relative_to_assets("entry_32.png"))
entry_bg_32 = canvas.create_image(
    488.5,
    479.5,
    image=entry_image_32
)
entry_32 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_32.place(
    x=456.0,
    y=451.0,
    width=65.0,
    height=55.0
)
entry_32.insert(0, '1')
entry_32.configure(state='readonly')

entry_image_33 = PhotoImage(
    file=relative_to_assets("entry_33.png"))
entry_bg_33 = canvas.create_image(
    488.5,
    536.5,
    image=entry_image_33
)
entry_33 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_33.place(
    x=456.0,
    y=508.0,
    width=65.0,
    height=55.0
)

entry_image_34 = PhotoImage(
    file=relative_to_assets("entry_34.png"))
entry_bg_34 = canvas.create_image(
    553.5,
    422.5,
    image=entry_image_34
)
entry_34 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_34.place(
    x=521.0,
    y=394.0,
    width=65.0,
    height=55.0
)
entry_34.insert(0, '4')
entry_34.configure(state='readonly')

entry_image_35 = PhotoImage(
    file=relative_to_assets("entry_35.png"))
entry_bg_35 = canvas.create_image(
    553.5,
    479.5,
    image=entry_image_35
)
entry_35 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_35.place(
    x=521.0,
    y=451.0,
    width=65.0,
    height=55.0
)


entry_image_36 = PhotoImage(
    file=relative_to_assets("entry_36.png"))
entry_bg_36 = canvas.create_image(
    553.5,
    536.5,
    image=entry_image_36
)
entry_36 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_36.place(
    x=521.0,
    y=508.0,
    width=65.0,
    height=55.0
)

entry_image_37 = PhotoImage(
    file=relative_to_assets("entry_37.png"))
entry_bg_37 = canvas.create_image(
    625.5,
    422.5,
    image=entry_image_37
)
entry_37 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_37.place(
    x=593.0,
    y=394.0,
    width=65.0,
    height=55.0
)

entry_image_38 = PhotoImage(
    file=relative_to_assets("entry_38.png"))
entry_bg_38 = canvas.create_image(
    690.5,
    422.5,
    image=entry_image_38
)
entry_38 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_38.place(
    x=658.0,
    y=394.0,
    width=65.0,
    height=55.0
)
entry_38.insert(0, '9')
entry_38.configure(state='readonly')

entry_image_39 = PhotoImage(
    file=relative_to_assets("entry_39.png"))
entry_bg_39 = canvas.create_image(
    755.5,
    422.5,
    image=entry_image_39
)
entry_39 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_39.place(
    x=723.0,
    y=394.0,
    width=65.0,
    height=55.0
)
entry_39.insert(0, '7')
entry_39.configure(state='readonly')

entry_image_40 = PhotoImage(
    file=relative_to_assets("entry_40.png"))
entry_bg_40 = canvas.create_image(
    625.5,
    479.5,
    image=entry_image_40
)
entry_40 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_40.place(
    x=593.0,
    y=451.0,
    width=65.0,
    height=55.0
)

entry_image_41 = PhotoImage(
    file=relative_to_assets("entry_41.png"))
entry_bg_41 = canvas.create_image(
    690.5,
    479.5,
    image=entry_image_41
)
entry_41 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_41.place(
    x=658.0,
    y=451.0,
    width=65.0,
    height=55.0
)

entry_image_42 = PhotoImage(
    file=relative_to_assets("entry_42.png"))
entry_bg_42 = canvas.create_image(
    755.5,
    479.5,
    image=entry_image_42
)
entry_42 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_42.place(
    x=723.0,
    y=451.0,
    width=65.0,
    height=55.0
)

entry_image_43 = PhotoImage(
    file=relative_to_assets("entry_43.png"))
entry_bg_43 = canvas.create_image(
    625.5,
    536.5,
    image=entry_image_43
)
entry_43 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_43.place(
    x=593.0,
    y=508.0,
    width=65.0,
    height=55.0
)
entry_43.insert(0, '1')
entry_43.configure(state='readonly')

entry_image_44 = PhotoImage(
    file=relative_to_assets("entry_44.png"))
entry_bg_44 = canvas.create_image(
    690.5,
    536.5,
    image=entry_image_44
)
entry_44 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_44.place(
    x=658.0,
    y=508.0,
    width=65.0,
    height=55.0
)
entry_44.insert(0, '3')
entry_44.configure(state='readonly')

entry_image_45 = PhotoImage(
    file=relative_to_assets("entry_45.png"))
entry_bg_45 = canvas.create_image(
    755.5,
    536.5,
    image=entry_image_45
)
entry_45 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_45.place(
    x=723.0,
    y=508.0,
    width=65.0,
    height=55.0
)

entry_image_46 = PhotoImage(
    file=relative_to_assets("entry_46.png"))
entry_bg_46 = canvas.create_image(
    826.5,
    422.5,
    image=entry_image_46
)
entry_46 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_46.place(
    x=794.0,
    y=394.0,
    width=65.0,
    height=55.0
)

entry_image_47 = PhotoImage(
    file=relative_to_assets("entry_47.png"))
entry_bg_47 = canvas.create_image(
    891.5,
    422.5,
    image=entry_image_47
)
entry_47 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_47.place(
    x=859.0,
    y=394.0,
    width=65.0,
    height=55.0
)

entry_image_48 = PhotoImage(
    file=relative_to_assets("entry_48.png"))
entry_bg_48 = canvas.create_image(
    957.5,
    422.5,
    image=entry_image_48
)
entry_48 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_48.place(
    x=925.0,
    y=394.0,
    width=65.0,
    height=55.0
)

entry_image_49 = PhotoImage(
    file=relative_to_assets("entry_49.png"))
entry_bg_49 = canvas.create_image(
    827.5,
    479.5,
    image=entry_image_49
)
entry_49 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_49.place(
    x=795.0,
    y=451.0,
    width=65.0,
    height=55.0
)

entry_image_50 = PhotoImage(
    file=relative_to_assets("entry_50.png"))
entry_bg_50 = canvas.create_image(
    891.5,
    479.5,
    image=entry_image_50
)
entry_50 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_50.place(
    x=859.0,
    y=451.0,
    width=65.0,
    height=55.0
)
entry_50.insert(0, '5')
entry_50.configure(state='readonly')

entry_image_51 = PhotoImage(
    file=relative_to_assets("entry_51.png"))
entry_bg_51 = canvas.create_image(
    956.5,
    479.5,
    image=entry_image_51
)
entry_51 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_51.place(
    x=924.0,
    y=451.0,
    width=65.0,
    height=55.0
)
entry_51.insert(0, '9')
entry_51.configure(state='readonly')

entry_image_52 = PhotoImage(
    file=relative_to_assets("entry_52.png"))
entry_bg_52 = canvas.create_image(
    827.5,
    536.5,
    image=entry_image_52
)
entry_52 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_52.place(
    x=795.0,
    y=508.0,
    width=65.0,
    height=55.0
)
entry_52.insert(0, '4')
entry_52.configure(state='readonly')

entry_image_53 = PhotoImage(
    file=relative_to_assets("entry_53.png"))
entry_bg_53 = canvas.create_image(
    892.5,
    536.5,
    image=entry_image_53
)
entry_53 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_53.place(
    x=860.0,
    y=508.0,
    width=65.0,
    height=55.0
)
entry_53.insert(0, '8')
entry_53.configure(state='readonly')

entry_image_54 = PhotoImage(
    file=relative_to_assets("entry_54.png"))
entry_bg_54 = canvas.create_image(
    956.5,
    536.5,
    image=entry_image_54
)
entry_54 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_54.place(
    x=924.0,
    y=508.0,
    width=65.0,
    height=55.0
)

entry_image_55 = PhotoImage(
    file=relative_to_assets("entry_55.png"))
entry_bg_55 = canvas.create_image(
    423.5,
    599.5,
    image=entry_image_55
)
entry_55 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_55.place(
    x=391.0,
    y=571.0,
    width=65.0,
    height=55.0
)
entry_55.insert(0, '6')
entry_55.configure(state='readonly')

entry_image_56 = PhotoImage(
    file=relative_to_assets("entry_56.png"))
entry_bg_56 = canvas.create_image(
    488.5,
    599.5,
    image=entry_image_56
)
entry_56 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_56.place(
    x=456.0,
    y=571.0,
    width=65.0,
    height=55.0
)
entry_56.insert(0, '9')
entry_56.configure(state='readonly')

entry_image_57 = PhotoImage(
    file=relative_to_assets("entry_57.png"))
entry_bg_57 = canvas.create_image(
    553.5,
    599.5,
    image=entry_image_57
)
entry_57 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_57.place(
    x=521.0,
    y=571.0,
    width=65.0,
    height=55.0
)
entry_57.insert(0, '7')
entry_57.configure(state='readonly')

entry_image_58 = PhotoImage(
    file=relative_to_assets("entry_58.png"))
entry_bg_58 = canvas.create_image(
    423.5,
    656.5,
    image=entry_image_58
)
entry_58 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_58.place(
    x=391.0,
    y=628.0,
    width=65.0,
    height=55.0
)

entry_image_59 = PhotoImage(
    file=relative_to_assets("entry_59.png"))
entry_bg_59 = canvas.create_image(
    488.5,
    656.5,
    image=entry_image_59
)
entry_59 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_59.place(
    x=456.0,
    y=628.0,
    width=65.0,
    height=55.0
)
entry_59.insert(0, '5')
entry_59.configure(state='readonly')

entry_image_60 = PhotoImage(
    file=relative_to_assets("entry_60.png"))
entry_bg_60 = canvas.create_image(
    553.5,
    656.5,
    image=entry_image_60
)
entry_60 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_60.place(
    x=521.0,
    y=628.0,
    width=65.0,
    height=55.0
)
entry_60.insert(0, '8')
entry_60.configure(state='readonly')

entry_image_61 = PhotoImage(
    file=relative_to_assets("entry_61.png"))
entry_bg_61 = canvas.create_image(
    423.5,
    713.5,
    image=entry_image_61
)
entry_61 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_61.place(
    x=391.0,
    y=685.0,
    width=65.0,
    height=55.0
)
entry_61.insert(0, '4')
entry_61.configure(state='readonly')

entry_image_62 = PhotoImage(
    file=relative_to_assets("entry_62.png"))
entry_bg_62 = canvas.create_image(
    488.5,
    713.5,
    image=entry_image_62
)
entry_62 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_62.place(
    x=456.0,
    y=685.0,
    width=65.0,
    height=55.0
)
entry_62.insert(0, '3')
entry_62.configure(state='readonly')

entry_image_63 = PhotoImage(
    file=relative_to_assets("entry_63.png"))
entry_bg_63 = canvas.create_image(
    553.5,
    713.5,
    image=entry_image_63
)
entry_63 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_63.place(
    x=521.0,
    y=685.0,
    width=65.0,
    height=55.0
)

entry_image_64 = PhotoImage(
    file=relative_to_assets("entry_64.png"))
entry_bg_64 = canvas.create_image(
    625.5,
    599.5,
    image=entry_image_64
)
entry_64 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_64.place(
    x=593.0,
    y=571.0,
    width=65.0,
    height=55.0
)

entry_image_65 = PhotoImage(
    file=relative_to_assets("entry_65.png"))
entry_bg_65 = canvas.create_image(
    690.5,
    599.5,
    image=entry_image_65
)
entry_65 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_65.place(
    x=658.0,
    y=571.0,
    width=65.0,
    height=55.0
)

entry_image_66 = PhotoImage(
    file=relative_to_assets("entry_66.png"))
entry_bg_66 = canvas.create_image(
    755.5,
    599.5,
    image=entry_image_66
)
entry_66 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_66.place(
    x=723.0,
    y=571.0,
    width=65.0,
    height=55.0
)
entry_66.insert(0, '2')
entry_66.configure(state='readonly')

entry_image_67 = PhotoImage(
    file=relative_to_assets("entry_67.png"))
entry_bg_67 = canvas.create_image(
    625.5,
    656.5,
    image=entry_image_67
)
entry_67 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_67.place(
    x=593.0,
    y=628.0,
    width=65.0,
    height=55.0
)

entry_image_68 = PhotoImage(
    file=relative_to_assets("entry_68.png"))
entry_bg_68 = canvas.create_image(
    690.5,
    657.5,
    image=entry_image_68
)
entry_68 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_68.place(
    x=658.0,
    y=629.0,
    width=65.0,
    height=55.0
)

entry_image_69 = PhotoImage(
    file=relative_to_assets("entry_69.png"))
entry_bg_69 = canvas.create_image(
    755.5,
    657.5,
    image=entry_image_69
)
entry_69 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_69.place(
    x=723.0,
    y=629.0,
    width=65.0,
    height=55.0
)

entry_image_70 = PhotoImage(
    file=relative_to_assets("entry_70.png"))
entry_bg_70 = canvas.create_image(
    625.5,
    713.5,
    image=entry_image_70
)
entry_70 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_70.place(
    x=593.0,
    y=685.0,
    width=65.0,
    height=55.0
)

entry_image_71 = PhotoImage(
    file=relative_to_assets("entry_71.png"))
entry_bg_71 = canvas.create_image(
    690.5,
    713.5,
    image=entry_image_71
)
entry_71 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_71.place(
    x=658.0,
    y=685.0,
    width=65.0,
    height=55.0
)
entry_71.insert(0, '8')
entry_71.configure(state='readonly')

entry_image_72 = PhotoImage(
    file=relative_to_assets("entry_72.png"))
entry_bg_72 = canvas.create_image(
    755.5,
    714.5,
    image=entry_image_72
)
entry_72 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_72.place(
    x=723.0,
    y=686.0,
    width=65.0,
    height=55.0
)

entry_image_73 = PhotoImage(
    file=relative_to_assets("entry_73.png"))
entry_bg_73 = canvas.create_image(
    827.5,
    600.5,
    image=entry_image_73
)
entry_73 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_73.place(
    x=795.0,
    y=572.0,
    width=65.0,
    height=55.0
)

entry_image_74 = PhotoImage(
    file=relative_to_assets("entry_74.png"))
entry_bg_74 = canvas.create_image(
    891.5,
    600.5,
    image=entry_image_74
)
entry_74 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_74.place(
    x=859.0,
    y=572.0,
    width=65.0,
    height=55.0
)

entry_image_75 = PhotoImage(
    file=relative_to_assets("entry_75.png"))
entry_bg_75 = canvas.create_image(
    957.5,
    601.5,
    image=entry_image_75
)
entry_75 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_75.place(
    x=925.0,
    y=573.0,
    width=65.0,
    height=55.0
)
entry_75.insert(0, '8')
entry_75.configure(state='readonly')

entry_image_76 = PhotoImage(
    file=relative_to_assets("entry_76.png"))
entry_bg_76 = canvas.create_image(
    827.5,
    658.5,
    image=entry_image_76
)
entry_76 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_76.place(
    x=795.0,
    y=630.0,
    width=65.0,
    height=55.0
)

entry_image_77 = PhotoImage(
    file=relative_to_assets("entry_77.png"))
entry_bg_77 = canvas.create_image(
    892.5,
    658.5,
    image=entry_image_77
)
entry_77 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_77.place(
    x=860.0,
    y=630.0,
    width=65.0,
    height=55.0
)
entry_77.insert(0, '6')
entry_77.configure(state='readonly')

entry_image_78 = PhotoImage(
    file=relative_to_assets("entry_78.png"))
entry_bg_78 = canvas.create_image(
    827.5,
    715.5,
    image=entry_image_78
)
entry_78 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 2, "bold"),
    justify="center",
    highlightthickness=0
)
entry_78.place(
    x=795.0,
    y=687.0,
    width=65.0,
    height=55.0
)

entry_image_79 = PhotoImage(
    file=relative_to_assets("entry_79.png"))
entry_bg_79 = canvas.create_image(
    957.5,
    658.5,
    image=entry_image_79
)
entry_79 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_79.place(
    x=925.0,
    y=630.0,
    width=65.0,
    height=55.0
)

entry_image_80 = PhotoImage(
    file=relative_to_assets("entry_80.png"))
entry_bg_80 = canvas.create_image(
    891.5,
    715.5,
    image=entry_image_80
)
entry_80 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_80.place(
    x=859.0,
    y=687.0,
    width=65.0,
    height=55.0
)
entry_80.insert(0, '7')
entry_80.configure(state='readonly')

entry_image_81 = PhotoImage(
    file=relative_to_assets("entry_81.png"))
entry_bg_81 = canvas.create_image(
    827.5,
    715.5,
    image=entry_image_81
)
entry_81 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_81.place(
    x=795.0,
    y=687.0,
    width=65.0,
    height=55.0
)

entry_image_82 = PhotoImage(
    file=relative_to_assets("entry_82.png"))
entry_bg_82 = canvas.create_image(
    956.5,
    715.5,
    image=entry_image_82
)
entry_82 = Entry(
    bd=2,
    relief="solid",
#    bg="#D9D9D9",
    fg="#000716",
    font=("Arial", 20, "bold"),
    justify="center",
    highlightthickness=0
)
entry_82.place(
    x=924.0,
    y=687.0,
    width=65.0,
    height=55.0
)

canvas.create_text(
    924.0,
    77.0 + 50,
    anchor="nw",
    text="Laimėk šaldiklį!",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 64 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1181.0,
    464.0,
    image=image_image_2
)

def win():
    x=0
    #Pirmas blockas
    val1 = entry_1.get()
    val2 = entry_5.get()
    val3 = entry_4.get()
    val4 = entry_6.get()
    val5 = entry_8.get()
    val6 = entry_9.get()
    #Antras blockas       
    val7 = entry_10.get()
    val8 = entry_16.get()
    val9 = entry_11.get()
    val10 = entry_14.get()
    val11 = entry_17.get()
    val12 = entry_13.get()
    val13 = entry_18.get()
    #Trecias blokas
    val14 = entry_19.get()
    val15 = entry_26.get()
    #Ketvirtas blokas
    val16 = entry_28.get()
    val17 = entry_35.get()
    val18 = entry_30.get()
    val19 = entry_33.get()
    val20 = entry_36.get()
    #Penktas blokas
    val21 = entry_37.get()
    val22 = entry_40.get()
    val23 = entry_41.get()
    val24 = entry_42.get()
    val25 = entry_45.get()
    #Sestas blokas
    val26 = entry_46.get()
    val27 = entry_47.get()
    val28 = entry_48.get()
    val29 = entry_49.get()
    val30 = entry_54.get()
    #Septinas blokas
    val31 = entry_58.get()
    val32 = entry_63.get()
    #Astunas blokas
    val33 = entry_64.get()
    val34 = entry_65.get()
    val35 = entry_67.get()
    val36 = entry_68.get()
    val37 = entry_69.get()
    val38 = entry_70.get()
    val39 = entry_72.get()
    #Devintas
    val40 = entry_73.get()
    val41 = entry_74.get()
    val42 = entry_76.get()
    val43 = entry_79.get()
    val44 = entry_81.get()
    val45 = entry_82.get()
    
    #First
    if (val1 == '8'):
        x+=1;
    if (val2 == '5'):
        x+=1;
    if (val3 == '3'):
        x+=1
    if (val4 == '1'):
        x+=1
    if (val5 == '4'):
        x+=1
    if (val6 == '9'):
        x+=1
    #Antras  
    if (val7 == '9'):
        x+=1
    if (val8 == '1'):
        x+=1
    if (val9 == '7'):
        x+=1
    if (val10 == '5'):
        x+=1
    if (val11 == '4'):
        x+=1
    if (val12 == '6'):
        x+=1
    if (val13 == '3'):
        x+=1
    #Trecias
    if (val14 == '3'):
        x+=1
    if (val15 == '2'):
        x+=1
    #Ketvirtas
    if (val16 == '5'):
        x+=1
    if (val17 == '3'):
        x+=1
    if (val18 == '9'):
        x+=1
    if (val19 == '2'):
        x+=1
    if (val20 == '6'):
        x+=1
    #Penktas
    if (val21 == '6'):
        x+=1
    if (val22 == '2'):
        x+=1
    if (val23 == '4'):
        x+=1
    if (val24 == '8'):
        x+=1
    if (val25 == '5'):
        x+=1
    #Sestas
    if (val26 == '1'):
        x+=1
    if (val27 == '2'):
        x+=1
    if (val28 == '3'):
        x+=1
    if (val29 == '6'):
        x+=1
    if (val30 == '7'):
        x+=1
    #Septintas
    if (val31 == '1'):
        x+=1
    if (val32 == '2'):
        x+=1
    #Astuntas
    if (val33 == '4'):
        x+=1
    if (val34 == '1'):
        x+=1
    if (val35 == '3'):
        x+=1
    if (val36 == '7'):
        x+=1
    if (val37 == '9'):
        x+=1
    if (val38 == '5'):
        x+=1
    if (val39 == '6'):
        x+=1
    #Devintas
    if (val40 == '5'):
        x+=1
    if (val41 == '3'):
        x+=1
    if (val42 == '2'):
        x+=1
    if (val43 == '4'):
        x+=1
    if (val44 == '9'):
        x+=1
    if (val45 == '1'):
        x+=1
    
    record = x
    mycursor.execute("UPDATE Sudoku set level1 = %s", (record,))
    db.commit()
        
    if (record == 45):
        messagebox.showinfo("Information", "Sveikiname gavus šaldytuvą bei "+ str(record) +' tasku!')
        title()
        
    else:
        messagebox.showwarning("Warning", "Dėja šaldytuvo nebus "+ str(record) + ' ,nes tiek tasku')
    

A = Button(text ="🡆")
A.configure(font=("Arial", 20), bg='pink')
A.configure(command=win)
A.place(x=1200,y=700)

B = Button(text ="🏠")
B.configure(font=("Arial", 20), bg='pink')
B.configure(command=home)
B.place(x=1100,y=700)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    393.0,
    807.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1183.0,
    807.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    803.0,
    943.0,
    image=image_image_5
)
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.attributes('-fullscreen', True)
window.mainloop()
 