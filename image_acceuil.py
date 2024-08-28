from tkinter import *
from PIL import ImageTk
from subprocess import call
import time


def center_window(window, width, height):
    ecran_width = window.winfo_screenwidth()
    ecran_height = window.winfo_screenheight()

    x_coordonne = (ecran_width - width) // 2
    y_coordonne = (ecran_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordonne}+{y_coordonne}")


def ecran_connection_Admin():
    call(["python", "sing_in.py"])


fenetre_splash = Tk()
center_window(fenetre_splash, 637, 398)
splash_Image = ImageTk.PhotoImage(file="img/splash_screen.png")
backGround_Label = Label(fenetre_splash, image=splash_Image)
backGround_Label.pack()
fenetre_splash.overrideredirect(1)

for i in range(5):
    imageDemarrage = Label(fenetre_splash, image=splash_Image)
    imageDemarrage.pack()
    fenetre_splash.update_idletasks()
    time.sleep(1)

fenetre_splash.destroy()
ecran_connection_Admin()
fenetre_splash.mainloop()
