from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from subprocess import call
from colors_fonts import *
import dataUser


def center_window(window, width, height):
    ecran_width = window.winfo_screenwidth()
    ecran_height = window.winfo_screenheight()

    x_coordinate = (ecran_width - width) // 2
    y_coordinate = (ecran_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


def login_page():
    registre_fenetre.destroy()
    call(["python", "sing_in.py"])


def registre():
    username = usernameEntry.get()
    password = passwordEntry.get()
    confirmpassword = confirmpasswordEntry.get()
    print(username, password, confirmpassword)
    if password != "" and confirmpassword != "" and username != "":
        if username == "username" or username == "Nom Administrateur":
            messagebox.showerror("Valeurs entrer Invalide", "Nom Administrateur Invalide")
        if password != confirmpassword and confirmpassword or password == "1234567890":
            messagebox.showerror("Valeurs entrer Invalide", "Mot de Passe Invalide")
        else:
            try:
                # Connection base de données SQLite
                dataUser.testConnexion()
                print("Connection Etablie")

            except:
                messagebox.showerror("Compte Administrateur", "Impossible de se connecter à la base de données")

            try:
                dataUser.creation_table_utilisateur()

            except:
                dataUser.insertion_administrateur(username, password)
                messagebox.showinfo("Enregistrement", "Nouveau Administrateur enregister avec successer!!!")
                registre_fenetre.destroy()
                call(["python", "sing_in.py"])
    else:
        messagebox.showerror("Valeurs entrer Invalide",  "Veuillez completer tout les champs de textes")


#-------------Creation fenetre
registre_fenetre = Tk()
center_window(registre_fenetre, 925, 500)
registre_fenetre.resizable(False, False)
registre_fenetre.title(' Creation Compte Administrateur RCSPC522')

registreImage = ImageTk.PhotoImage(file="img/registre_image.png")
bgLabel = Label(registre_fenetre, image=registreImage)
bgLabel.place(x=0, y=0)

registre_fenetre.iconbitmap('img/rfid.ico')

frame_boite_registre = Frame(registre_fenetre, width=350, height=450, background=coloration.BG_Neutre)
frame_boite_registre.place(x=490, y=40)

#--------------------Grand Titre
heading = Label(frame_boite_registre, text="CREATION COMPTE \n ADMINISTRATEUR", font=(fonts.Titre_Fonts, 25, 'bold'),
                background='white', foreground=coloration.BG_Couleur2)
heading.place(x=20, y=5)

#-------------nom admin
usernamelabel = Label(frame_boite_registre, text='Nom Administrateur', font=(fonts.Texte_Fonts, 12, 'bold'),
                      background='white', foreground=coloration.BG_Couleur2)
usernamelabel.place(x=10, y=130)
usernameEntry = Entry(frame_boite_registre, width=23, font=(fonts.Texte_Fonts, 12, 'bold'), border=0,
                      foreground=coloration.BG_Couleur2)
usernameEntry.place(x=10, y=150)
frame_username = Frame(frame_boite_registre, width=250, height=2, background=coloration.BG_Couleur6)
frame_username.place(x=10, y=170)

#-------------mot de passe admin
passwordlabel = Label(frame_boite_registre, text='Mot de Passe', font=(fonts.Texte_Fonts, 12, 'bold'),
                      background='white', foreground=coloration.BG_Couleur2)
passwordlabel.place(x=10, y=200)
passwordEntry = Entry(frame_boite_registre, width=23, font=(fonts.Texte_Fonts, 12, 'bold'), border=0,
                      foreground=coloration.BG_Couleur2)
passwordEntry.place(x=10, y=220)
frame_password = Frame(frame_boite_registre, width=250, height=2, background=coloration.BG_Couleur6)
frame_password.place(x=10, y=240)

confirmpasswordlabel = Label(frame_boite_registre, text='Cofirmer Mot de Passe', font=(fonts.Texte_Fonts, 12, 'bold'),
                             background='white', foreground=coloration.BG_Couleur2)
confirmpasswordlabel.place(x=10, y=270)
confirmpasswordEntry = Entry(frame_boite_registre, width=23, font=(fonts.Texte_Fonts, 12, 'bold'), border=0,
                             foreground=coloration.BG_Couleur2)
confirmpasswordEntry.place(x=10, y=290)
frame_confirmpassword = Frame(frame_boite_registre, width=250, height=2, background=coloration.BG_Couleur6)
frame_confirmpassword.place(x=10, y=310)

#----boutton
registreButton = Button(frame_boite_registre, text='Enregistrer', font=(fonts.Texte_Fonts, 17, 'bold'),
                        foreground='white',
                        border=0, width=15, background=coloration.BG_Couleur2, activebackground=coloration.BG_Couleur2,
                        activeforeground='white', command=registre)
registreButton.place(x=65, y=340)

singinLabel = Label(frame_boite_registre, text="Vous avez un Compte?", font=(fonts.Texte_Fonts, 12, 'bold'),
                    background='white', foreground=coloration.BG_Couleur2)
singinLabel.place(x=20, y=400)

loginButton = Button(frame_boite_registre, text='Connetez vous', font=(fonts.Texte_Fonts, 11, 'bold underline'),
                     foreground='blue', border=0, background='white', activeforeground='blue', command=login_page,
                     cursor='hand2 ')
loginButton.place(x=200, y=400)

registre_fenetre.mainloop()