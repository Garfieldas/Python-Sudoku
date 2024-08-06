from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from subprocess import call
import pygame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"menu_image")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    
    
    
window = Tk()

window.geometry("790x485")
window.configure(bg = "#FFFFFF")
window.title("Menu")

def play_music(window):
    pygame.mixer.init()
    pygame.mixer.music.load(r"music.mp3")
    pygame.mixer.music.play(-1)
    
def stop_music():
    pygame.mixer.music.stop()
    
def on_closing():
    stop_music()
    window.destroy()
    with open("taskai/taskai1.txt", "r") as f:
        test = f.read()
        number = 0
        
    with open("taskai/taskai1.txt", "w") as f:
        f.write(str(number))
        
    with open("taskai/taskai2.txt", "r") as f:
        test = f.read()
        number = 0
        
    with open("taskai/taskai2.txt", "w") as f:
        f.write(str(number))
        
    with open("taskai/taskai3.txt", "r") as f:
        test = f.read()
        number = 0
        
    with open("taskai/taskai3.txt", "w") as f:
        f.write(str(number))
        
    with open("taskai/taskai4.txt", "r") as f:
        test = f.read()
        number = 0
        
    with open("taskai/taskai4.txt", "w") as f:
        f.write(str(number))
        
    with open("taskai/taskai5.txt", "r") as f:
        test = f.read()
        number = 0
        
    with open("taskai/taskai5.txt", "w") as f:
        f.write(str(number))

def open_file1():
    stop_music()
    window.destroy()
    call(["python", "video1.py"])
    
def open_file2():
    with open("taskai/taskai1.txt", "r") as f:
        test = f.read()
    if (int(test) == 45):
        stop_music()
        window.destroy()
        call(["python", "video2.py"])
    else:
        messagebox.showwarning("Warning", "Dėja pirmas lygis neišspręstas, ačiū ir viso gero") 
    
def open_file3():
    with open("taskai/taskai2.txt", "r") as f:
        test1 = f.read()
    with open("taskai/taskai3.txt", "r") as f:
        test2 = f.read()
    test3 = test1+test2
    print(test3)
    if (test3 == 90):
        stop_music()
        window.destroy()
        call(["python", "video3.py"])
    else:
        messagebox.showwarning("Warning", "Dėja pirmas ir antras lygis neišspręstas, ačiū ir viso gero")   

def open_file4():
    with open("taskai/taskai1.txt", "r") as f:
        test1 = f.read()
    with open("taskai/taskai2.txt", "r") as f:
        test2 = f.read()
    with open("taskai/taskai3.txt", "r") as f:
        test3 = f.read()
    test4 = test1+test2+test3
    if (test4 == 136):
        stop_music()
        window.destroy()
        call(["python", "video4.py"])
    else:
        messagebox.showwarning("Warning", "Dėja ne..ačiū ir viso gero")   
    
def open_file5():
    with open("taskai/taskai1.txt", "r") as f:
        test1 = f.read()
    with open("taskai/taskai2.txt", "r") as f:
        test2 = f.read()
    with open("taskai/taskai3.txt", "r") as f:
        test3 = f.read()
    with open("taskai/taskai4.txt", "r") as f:
        test4 = f.read()
    test5 = test1+test2+test3+test4
    if (test5 == 181):
        stop_music()
        window.destroy()
        call(["python", "video5.py"])
    else:
        messagebox.showwarning("Warning", "Pagalvosim, pažiurėsim..ačiū ir viso gero")   
    
pygame.init()
play_music(window)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 485,
    width = 790,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    439.0,
    261.0,
    image=image_image_1
)

canvas.create_text(
    266.0,
    12.0,
    anchor="nw",
    text="Čia Šudoku",
    fill="#000000",
    font=("Arial", 40 * -1, "bold")
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_file1,
    relief="flat"
)
button_1.place(
    x=92.0,
    y=70.0,
    width=119.0,
    height=125.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_file2,
    relief="flat"
)
button_2.place(
    x=266.0,
    y=75.0,
    width=129.0,
    height=120.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_file3,
    relief="flat"
)
button_3.place(
    x=439.0,
    y=79.0,
    width=126.0,
    height=107.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_file4,
    relief="flat"
)
button_4.place(
    x=193.0,
    y=221.0,
    width=121.0,
    height=112.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=open_file5,
    relief="flat"
)
button_5.place(
    x=444.0,
    y=215.0,
    width=116.0,
    height=107.0
)
def ending():
    with open("taskai/taskai1.txt", "r") as f:
        test = f.read()
        number1 = int(test)
        
    with open("taskai/taskai2.txt", "r") as f:
        test = f.read()
        number2 = int(test)
        
    with open("taskai/taskai3.txt", "r") as f:
        test = f.read()
        number3 = int(test)
        
    with open("taskai/taskai4.txt", "r") as f:
        test = f.read()
        number4 = int(test)
        
    with open("taskai/taskai5.txt", "r") as f:
        test = f.read()
        number5 = int(test)
    
    all_number = number1 + number2 + number3 + number4 + number5
        
    if (all_number == 226):
        stop_music()
        window.destroy()
        call(["python", "ending.py"])
    else:
        messagebox.showwarning("Warning", "Dėja nieko nebus "+ str(all_number) + ' ,nes tiek tasku')
        stop_music()
        window.destroy()
        call(["python", "title.py"])
    
    
A = Button(text ="🡆")
A.configure(font=("Arial", 20), bg='pink')
A.configure(command=ending)
A.place(x=600,y=350)
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
