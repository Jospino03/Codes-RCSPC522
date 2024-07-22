#-------------------Importations bibliotheques
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from subprocess import call
from colors_fonts import *
from dataUser import *
import dataUser


def center_window(window, width, height):
    ecran_width = window.winfo_screenwidth()
    ecran_height = window.winfo_screenheight()

    x_coordinate = (ecran_width - width) // 2
    y_coordinate = (ecran_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


#---- Etat Oiel pour mot de pass
def hide():
    openeye.config(file='img/eye-close.png')
    passwordEntry.config(show='•')
    eyeButton.config(command=show)


def show():
    openeye.config(file='img/eye-open.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


#------------------Champ Nom Admin
#------Nom entrer
def user_enter(event):
    if usernameEntry.get() == 'Nom Administrateur':
        usernameEntry.delete(0, END)


#------Nom non entrer
def user_leave(event):
    name = usernameEntry.get()
    if name == '':
        usernameEntry.insert(0, "Nom Administrateur")


#----------------Champ mot de pass txt
#--Mot de Passer Entrer
def password_enter(event):
    if passwordEntry.get() == "Mot de Passe":
        passwordEntry.delete(0, END)


#--Mot de Passe non Entrer
def password_leave(event):
    if passwordEntry.get() == '':
        passwordEntry.insert(0, "Mot de Passe")


def mot_de_passe_oublie():
    def retour_login():
        restor_fenetre.destroy()
        call(["python", "sing_in.py"])

    def changer_mot_de_passe():
        username = userEntry.get()
        password = password_restorEntry.get()
        confirm_password = confirm_password_restorEntry.get()

        if username == '' or password == '' or confirm_password == '':
            messagebox.showerror('Erreur', 'Veuillez remplire tout les champs de textes', parent=restor_fenetre)
        elif password != confirm_password:
            messagebox.showerror('Erreur', 'Mot de passe ne correspond pas', parent=restor_fenetre)
        else:
            connectionDB = sqlite3.connect("databases/adminregistration.db")
            curseur = connectionDB.cursor()
            curseur.execute("SELECT * FROM Login WHERE Admin=?", [username])
            row = curseur.fetchone()
            if row is None:
                messagebox.showerror('Erreur', 'Nom Administrateur incorrect', parent=restor_fenetre)
            else:
                curseur.execute("UPDATE Login SET Password=? WHERE Admin=?", [password, username])
                connectionDB.commit()
                connectionDB.close()
                messagebox.showinfo('Validation', 'Mot de passe corriger avec success', parent=restor_fenetre)
                restor_fenetre.destroy()
                call(["python", "sing_in.py"])

    login_fenetre.destroy()

    restor_fenetre = Tk()
    center_window(restor_fenetre, 925, 500)
    restor_fenetre.resizable(False, False)
    restor_fenetre.title('Changer le mot de passe')
    restorImage = ImageTk.PhotoImage(file="img/reset_pass_image.png")
    bgLabel_restor = Label(restor_fenetre, image=restorImage)
    bgLabel_restor.pack()
    restor_fenetre.iconbitmap('img/rfid.ico')

    frame_boite_restor = Frame(restor_fenetre, width=350, height=450, background=coloration.BG_Neutre)
    frame_boite_restor.place(x=490, y=40)

    heading_restor = Label(frame_boite_restor, text='RESTORER \n LE MOT DE PASSE', font=(fonts.Titre_Fonts, 25, 'bold'),
                           background=coloration.BG_Neutre, foreground=coloration.BG_Couleur6)
    heading_restor.place(x=20, y=5)

    #--------Nom Administrateur
    userLabel = Label(frame_boite_restor, text='Nom Administrateur', font=(fonts.Texte_Fonts, 11, 'bold'), border=0,
                      foreground=coloration.BG_Couleur6, background=coloration.BG_Neutre)
    userLabel.place(x=10, y=130)
    userEntry = Entry(frame_boite_restor, width=30, font=(fonts.Texte_Fonts, 11, 'bold'), border=0,
                      foreground=coloration.BG_Couleur6)
    userEntry.place(x=10, y=150)
    frame_user = Frame(frame_boite_restor, width=250, height=2, background=coloration.BG_Couleur6)
    frame_user.place(x=10, y=170)
    #mot de passe
    password_restorLabel = Label(frame_boite_restor, text='Nouveau Mot de passe', font=(fonts.Texte_Fonts, 11, 'bold'),
                                 border=0, foreground=coloration.BG_Couleur6, background=coloration.BG_Neutre)
    password_restorLabel.place(x=10, y=200)
    password_restorEntry = Entry(frame_boite_restor, width=30, font=(fonts.Texte_Fonts, 11, 'bold'), border=0,
                                 foreground=coloration.BG_Couleur6)
    password_restorEntry.place(x=10, y=220)
    frame_password_restor = Frame(frame_boite_restor, width=250, height=2, background=coloration.BG_Couleur6)
    frame_password_restor.place(x=10, y=240)

    confirm_password_restorLabel = Label(frame_boite_restor, text='Confirmer le Mot de passe',
                                         font=(fonts.Texte_Fonts, 11, 'bold'), border=0,
                                         foreground=coloration.BG_Couleur6, background=coloration.BG_Neutre)
    confirm_password_restorLabel.place(x=10, y=270)
    confirm_password_restorEntry = Entry(frame_boite_restor, width=30, font=(fonts.Texte_Fonts, 11, 'bold'), border=0,
                                         foreground=coloration.BG_Couleur6)
    confirm_password_restorEntry.place(x=10, y=290)
    confirm_frame_password_restor = Frame(frame_boite_restor, width=250, height=2, background=coloration.BG_Couleur6)
    confirm_frame_password_restor.place(x=10, y=310)

    #Buttons
    submitButton = Button(frame_boite_restor, text='Enregistrer', font=(fonts.Texte_Fonts, 17, 'bold'),
                          foreground='white',
                          border=0, width=15, background=coloration.BG_Couleur6,
                          activebackground=coloration.BG_Couleur6, activeforeground='white',
                          command=changer_mot_de_passe)
    submitButton.place(x=65, y=340)

    retour_fleche = PhotoImage(file='img/retour_image.png')
    retourButton = Button(restor_fenetre, image=retour_fleche, border=0, background=coloration.BG_Neutre, cursor='hand2 ', command=retour_login)
    retourButton.place(x=10, y=10)

    restor_fenetre.mainloop()


#---------Compteur pour erreurs de tantative de connection avec erreus
global trial_no
trial_no = 0


def trial():
    global trial_no

    trial_no += 1
    print("Trial no est ", trial_no)
    if trial_no == 3:
        messagebox.showwarning("Attention", "Vous avez atteint 3 tantatives de connection avec echec!")
        login_fenetre.destroy()


#-----------------------Connection Administrateur
def userConnect():
    username = usernameEntry.get()
    password = passwordEntry.get()

    if (username == "" or username == "Nom Administrateur") or (
            password == "" or password == "Mot de Passe" or password == "1234" or password == "0000"):
        messagebox.showerror("Erreur de valeurs entrer", "Nom Administrateur ou Mot de Passe")

    else:
        try:
            #Connection base de données SQLite
            dataUser.testConnexion()
            print("Connection à la base de données")

        except:
            messagebox.showerror("Connexion", "Impossible de se connecter à la base de données")
            return
        mydb = sqlite3.connect("databases/adminregistration.db")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Login WHERE Admin=? and Password=?", [username, password])
        myresult = mycursor.fetchone()
        mydb.commit()
        mydb.close()
        print(myresult)

        if myresult is None:
            messagebox.showinfo("Information Invalide", "Nom Adminitrateur ou Mot de Pass Invalide!")
            trial()

        else:
            messagebox.showinfo("Connexion", "Connexion avec successer!!!")
            login_fenetre.destroy()
            call(["python", "main.py"])


#----Connexion page de Registre
def registre_page():
    login_fenetre.destroy()
    call(["python", "sing_up.py"])


#-------------Creation fenetre
login_fenetre = Tk()
center_window(login_fenetre, 925, 500)
login_fenetre.resizable(False, False)
login_fenetre.title(' Connexion Administrateur RCSPC522')

loginImage = ImageTk.PhotoImage(file="img/login_image.png")
bgLabel = Label(login_fenetre, image=loginImage)
bgLabel.pack()
login_fenetre.iconbitmap('img/rfid.ico')

frame_boite_connection = Frame(login_fenetre, width=350, height=450, background=coloration.BG_Neutre)
frame_boite_connection.place(x=490, y=40)

#--------------------Grand Titre
heading = Label(frame_boite_connection, text=" CONNEXION \n ADMINISTRATEUR", font=(fonts.Titre_Fonts, 25, 'bold'),
                background='white', foreground=coloration.BG_Couleur1)
heading.place(x=20, y=5)
#--------Nom Administrateur
usernameEntry = Entry(frame_boite_connection, width=25, font=(fonts.Texte_Fonts, 11, 'bold'), border=0,
                      foreground=coloration.BG_Couleur1)
usernameEntry.place(x=10, y=150)
usernameEntry.insert(0, 'Nom Administrateur')
usernameEntry.bind('<FocusIn>', user_enter)
usernameEntry.bind('<FocusOut>', user_leave)
frame_user = Frame(frame_boite_connection, width=250, height=2, background=coloration.BG_Couleur1)
frame_user.place(x=10, y=170)
#----------Mot de Pass
passwordEntry = Entry(frame_boite_connection, width=25, font=(fonts.Texte_Fonts, 11, 'bold'), border=0,
                      foreground=coloration.BG_Couleur1)
passwordEntry.place(x=10, y=200)
passwordEntry.insert(0, 'Mot de Passe')
passwordEntry.bind('<FocusIn>', password_enter)
passwordEntry.bind('<FocusOut>', password_leave)
frame_password = Frame(frame_boite_connection, width=250, height=2, background=coloration.BG_Couleur1)
frame_password.place(x=10, y=220)

openeye = PhotoImage(file='img/eye-open.png')
eyeButton = Button(frame_boite_connection, image=openeye, border=0, background='white', cursor='hand2 ', command=hide)
eyeButton.place(x=228, y=190)

forgetButton = Button(frame_boite_connection, text='Mot de Passe Oublier?', font=(fonts.Texte_Fonts, 11, 'bold'),
                      border=0,
                      background='white', foreground=coloration.BG_Couleur1, activebackground='white',
                      activeforeground=coloration.BG_Couleur1, cursor='hand2 ', command=mot_de_passe_oublie)
forgetButton.place(x=150, y=250)
#-------------Boutton Connexion
loginButton = Button(frame_boite_connection, text='Connexion', font=(fonts.Texte_Fonts, 17, 'bold'), foreground='white',
                     border=0, width=15, background=coloration.BG_Couleur1, activebackground=coloration.BG_Couleur1,
                     activeforeground='white', command=userConnect)
loginButton.place(x=65, y=300)

signupLabel = Label(frame_boite_connection, text="Vous n'avez pas un Compte?", font=(fonts.Texte_Fonts, 11, 'bold'),
                    background='white', foreground=coloration.BG_Couleur1)
signupLabel.place(x=5, y=370)

newaccountButton = Button(frame_boite_connection, text='Creer Un Compte',
                          font=(fonts.Texte_Fonts, 11, 'bold underline'),
                          foreground='blue', border=0, background='white', activeforeground='blue',
                          command=registre_page, cursor='hand2 ')
newaccountButton.place(x=215, y=370)

login_fenetre.mainloop()