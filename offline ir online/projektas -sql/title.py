from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from subprocess import call
import mysql.connector

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"title_image")


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

window.geometry("758x545")
window.configure(bg = "#FFFFFF")
window.title("Title")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 545,
    width = 758,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    391.0,
    272.0,
    image=image_image_1
)
def on_closing():
    window.destroy()
    
    
def on_image_click(event):
    window.destroy()
    call(["python", "menu.py"])
    

def on_image_enter(event):
    canvas.config(cursor="hand2")

def on_image_leave(event):
    canvas.config(cursor="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    637.0,
    328.0,
    image=image_image_2
)
canvas.tag_bind(image_2, "<Button-1>", on_image_click)

canvas.tag_bind(image_2, "<Enter>", on_image_enter)
canvas.tag_bind(image_2, "<Leave>", on_image_leave)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    352.0,
    291.0,
    image=image_image_3
)

canvas.create_text(
    253.0,
    168.0,
    anchor="nw",
    text="TOP: ",
    fill="#FFFFFF",
    font=("Inter Black", 36 * -1)
)

canvas.create_text(
    310,
    46.0,
    anchor="nw",
    text="Pradžia",
    fill="#FFFFFF",
    font=("Arial", 50 * -1)
)


taskai_label = Label(window, font=("Inter Black", 25))
taskai_label.place(x=330, y=220)

def query():
    #Query
    mycursor.execute("SELECT * FROM Sudoku")
    records =  mycursor.fetchall()
    print(records)

        
    record = records[0][0] + records[0][1] + records[0][2] + records[0][3] + records[0][4]
    mycursor.execute("UPDATE Sudoku set all_levels = %s", (record,))
    db.commit()
    all_records = records[0][5]
    taskai_label.configure(text=all_records)

query()

window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
