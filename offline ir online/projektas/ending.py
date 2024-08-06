from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"ending_image")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("639x364")
window.configure(bg = "#FFFFFF")
window.title('Pabaiga')




canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 364,
    width = 639,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    319.0,
    182.0,
    image=image_image_1
)

canvas.create_text(
    230.0,
    0.0,
    anchor="nw",
    text="Pabaiga",
    fill="#FFFFFF",
    font=("Inter", 48 * -1)
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
    x=184.0,
    y=137.0,
    width=270.0,
    height=70.0
)

canvas.create_text(
    197.0,
    218.0,
    anchor="nw",
    text="Vardas + žvaigždė",
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

def on_image_click(event):
    vardas = entry_1.get()
    messagebox.showwarning("Warning", 'Ačiū už tau '+ vardas + ',kad beprasmiškai skyriai laika šiam šudui,tiksliau šudoku')
    window.destroy()
    
    

def on_image_enter(event):
    canvas.config(cursor="hand2")  # Change cursor to hand when hover

def on_image_leave(event):
    canvas.config(cursor="")  # Reset cursor when not hovering

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    555.0,
    166.0,
    image=image_image_2
)

canvas.tag_bind(image_2, "<Button-1>", on_image_click)

# Bind hover events to the image
canvas.tag_bind(image_2, "<Enter>", on_image_enter)
canvas.tag_bind(image_2, "<Leave>", on_image_leave)



window.resizable(False, False)
window.mainloop()
