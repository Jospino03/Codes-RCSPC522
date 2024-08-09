from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from subprocess import call
from datetime import date
import datetime
import os
import sqlite3
import dataStudents
from colors_fonts import *

dataStudents.creation_table_regitre_etudiants()


# pour centre la fenetre au centre de l'ecran
def center_window(window, width, height):
    ecran_width = window.winfo_screenwidth()
    ecran_height = window.winfo_screenheight()

    x_coordinate = (ecran_width - width) // 2
    y_coordinate = (ecran_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


class Acceuil:
    # Quitter l'application
    def quitter_fenetre(self):
        reponse = messagebox.askyesno("RCSPC522",
                                      "Voulez-vous réellement quitter ? \n Cliquer sur « OUI » pour finir")
        if reponse:
            ## On quitte le programme acceuille
            home_fenetre.destroy()

    # Fonction de gestion des événements du menu Fichier
    def menu_fichier_comptabilite_action(self):
        print("Action du menu Fichier comptabilite")
        return comptabilite()

    def menu_fichier_gestion_action(self):
        print("Action du menu Fichier gestion")
        return gestion()

    def menu_fichier_insctiption_action(self):
        print("Action du menu inscription")
        return inscriptions()

    def menu_fichier_control_action(self):
        print("Action controle")
        return controles()

    # Fonction de gestion des événements du menu APropos
    def menu_guide_action(self):
        print("Action du menu Guide")
        Guide_text = "Bienvenue dans le guide de l'application de controle \nde paiement avec carte RFID (RCSPC522)! \nVoici quelques informations utiles:"
        messagebox.showinfo("GUIDE UTILISATEUR", Guide_text)

    def menu_fichier_quitter(self):
        principale.quitter_fenetre()


# ========================================================= DEBUT COMPTABILITE========================================================================
def comptabilite():
    # =============FRAME
    frameComptabilite = tk.Frame(home_fenetre, background=coloration.BG_Couleur3, width=835, height=560, borderwidth=1,
                                 relief=tk.SOLID)
    frameComptabilite.place(x=235, y=74)

    # -----------------------frame elements comptabilite
    frame_elements_comptabilite = tk.Frame(frameComptabilite, background=coloration.BG_Couleur3, width=829, height=554,
                                           borderwidth=1, relief=tk.SOLID)
    frame_elements_comptabilite.place(x=2, y=2)

    frameImage = tk.Frame(frameComptabilite, relief=tk.GROOVE)
    frameImage.place(x=560, y=140, width=160, height=160)
    # -----------------------------Entete------------------------
    entete_comptabilite = Label(frame_elements_comptabilite, text="COMPTABILITE & CAISSE",
                                font=(fonts.Titre_Fonts, 20, 'bold'),
                                background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    entete_comptabilite.place(x=250, y=10)
    # ---------------------------------------INFOS----------------------------
    lblIDentifiant = Label(frame_elements_comptabilite, text="ID", font=(fonts.Texte_Fonts, 14),
                           background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblIDentifiant.place(x=20, y=100)

    txtIdentifiant = tk.Entry(frame_elements_comptabilite, bd=2, font=(fonts.Texte_Fonts, 14),
                              foreground=coloration.BG_Couleur5)
    txtIdentifiant.place(x=50, y=100, width=150)
    btnID = Button(frame_elements_comptabilite, text="Charger Id", font=(fonts.Texte_Fonts, 14),
                   foreground=coloration.BG_Couleur3, border=1, background='white',
                   activebackground=coloration.BG_Neutre, activeforeground=coloration.BG_Couleur5)
    btnID.place(x=210, y=100, height=28)

    lblMotifPayemement = Label(frame_elements_comptabilite, text="Motif", font=(fonts.Texte_Fonts, 14),
                               background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblMotifPayemement.place(x=340, y=100)

    txtMotifPayement = Entry(frame_elements_comptabilite, bd=2, font=(fonts.Texte_Fonts, 14),
                             foreground=coloration.BG_Couleur5)
    txtMotifPayement.place(x=400, y=100, width=240)

    listMotifPayement = ["Motif de Paiement", "FRAIS INSCRIPTION", "FRAIS REINSCRIPTION", "FRAIS ACADEMIQUE",
                         "FRAIS COMPLEMENT"]
    comboMotifPayement = ttk.Combobox(frame_elements_comptabilite, font=(fonts.Texte_Fonts, 14),
                                      values=listMotifPayement,
                                      foreground=coloration.BG_Couleur5)
    comboMotifPayement.current(0)
    comboMotifPayement.place(x=400, y=100, width=240)

    lblBanque = Label(frame_elements_comptabilite, text="Banque", font=(fonts.Texte_Fonts, 14),
                      background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblBanque.place(x=20, y=60)
    txtBanque = tk.Entry(frame_elements_comptabilite, bd=2, font=(fonts.Texte_Fonts, 14),
                         foreground=coloration.BG_Couleur5)
    txtBanque.place(x=100, y=60, width=210)

    listBanques = ["Selection Banque", "EQUITY BCDC", "RAWBANK", "TMB", "TUJENGE PAMOJA"]
    comboBanques = ttk.Combobox(frame_elements_comptabilite, font=(fonts.Texte_Fonts, 14), values=listBanques,
                                foreground=coloration.BG_Couleur5)
    comboBanques.current(0)
    comboBanques.place(x=100, y=60, width=210)

    lblReferenceBanque = Label(frame_elements_comptabilite, text="Ref", font=(fonts.Texte_Fonts, 14),
                               background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblReferenceBanque.place(x=320, y=60)

    txtReferenceBanque = tk.Entry(frame_elements_comptabilite, bd=2, font=(fonts.Texte_Fonts, 14),
                                  foreground=coloration.BG_Couleur5)
    txtReferenceBanque.place(x=360, y=60)

    lblMontantPayer = Label(frame_elements_comptabilite, text="Montant", font=(fonts.Texte_Fonts, 14),
                            background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblMontantPayer.place(x=590, y=60)

    txtMontantPayer = tk.Entry(frame_elements_comptabilite, bd=2, font=(fonts.Texte_Fonts, 14),
                               foreground=coloration.BG_Couleur5)
    txtMontantPayer.place(x=680, y=60, width=100)
    lblDevise = Label(frame_elements_comptabilite, text="$", font=(fonts.Texte_Fonts, 15),
                      background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblDevise.place(x=780, y=60)
    # ---------------------------------
    lblMatticule = Label(frame_elements_comptabilite, text="MATRICULE", font=(fonts.Texte_Fonts, 14),
                         background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblMatticule.place(x=20, y=140)

    txtMatricule = tk.Entry(frame_elements_comptabilite, bd=1, font=(fonts.Texte_Fonts, 14),
                            foreground=coloration.BG_Couleur5)
    txtMatricule.place(x=180, y=140, width=150)

    lblNom = Label(frame_elements_comptabilite, text="NOM", font=(fonts.Texte_Fonts, 14),
                   background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblNom.place(x=20, y=180)

    txtNom = tk.Entry(frame_elements_comptabilite, bd=1, font=(fonts.Texte_Fonts, 14),
                      foreground=coloration.BG_Couleur5)
    txtNom.place(x=180, y=180)

    lblPostNom = Label(frame_elements_comptabilite, text="POST-NOM", font=(fonts.Texte_Fonts, 14),
                       background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblPostNom.place(x=20, y=220)

    txtPostNom = tk.Entry(frame_elements_comptabilite, bd=1, font=(fonts.Texte_Fonts, 14),
                          foreground=coloration.BG_Couleur5)
    txtPostNom.place(x=180, y=220)

    lblPreNom = Label(frame_elements_comptabilite, text="PRENOM", font=(fonts.Texte_Fonts, 14),
                      background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblPreNom.place(x=20, y=260)

    txtPreNom = tk.Entry(frame_elements_comptabilite, bd=1, font=(fonts.Texte_Fonts, 14),
                         foreground=coloration.BG_Couleur5)
    txtPreNom.place(x=180, y=260)

    lblDomaine = Label(frame_elements_comptabilite, text="DOMAINE", font=(fonts.Texte_Fonts, 14),
                       background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblDomaine.place(x=20, y=300)

    txtDomaine = tk.Entry(frame_elements_comptabilite, bd=1, font=(fonts.Texte_Fonts, 14),
                          foreground=coloration.BG_Couleur5)
    txtDomaine.place(x=180, y=300, width=300)

    lblDepartement = Label(frame_elements_comptabilite, text="DEPARTEMENT", font=(fonts.Texte_Fonts, 14),
                           background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblDepartement.place(x=20, y=340)

    txtDepartement = tk.Entry(frame_elements_comptabilite, bd=1, font=(fonts.Texte_Fonts, 14),
                              foreground=coloration.BG_Couleur5)
    txtDepartement.place(x=180, y=340, width=300)

    lblPromotion = Label(frame_elements_comptabilite, text="PROMOTION", font=(fonts.Texte_Fonts, 14),
                         background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblPromotion.place(x=20, y=380)

    txtPromotion = tk.Entry(frame_elements_comptabilite, bd=1, font=(fonts.Texte_Fonts, 14),
                            foreground=coloration.BG_Couleur5)
    txtPromotion.place(x=180, y=380)

    lblVacation = Label(frame_elements_comptabilite, text="VACATION", font=(fonts.Texte_Fonts, 14),
                        background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblVacation.place(x=20, y=420)

    txtVacation = tk.Entry(frame_elements_comptabilite, bd=1, font=(fonts.Texte_Fonts, 14),
                           foreground=coloration.BG_Couleur5)
    txtVacation.place(x=180, y=420)

    lblTotalPayer = Label(frame_elements_comptabilite, text="Total à Payer:  0$", font=(fonts.Texte_Fonts, 14),
                          background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblTotalPayer.place(x=555, y=310)

    lblMontantPayer = Label(frame_elements_comptabilite, text="Solde actuel: 0$", font=(fonts.Texte_Fonts, 14),
                            background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblMontantPayer.place(x=555, y=340)

    lblRestePayer = Label(frame_elements_comptabilite, text="Nouveau solde:  0$", font=(fonts.Texte_Fonts, 14),
                          background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblRestePayer.place(x=555, y=415)

    btnScanerCarte = tk.Button(frameComptabilite, text="Valider Infos", font=(fonts.Texte_Fonts, 15),
                               foreground=coloration.BG_Couleur3, background=coloration.BG_Neutre,
                               activebackground=coloration.BG_Neutre, activeforeground=coloration.BG_Couleur3)
    btnScanerCarte.place(x=565, y=375)

    btnSauvegarde = tk.Button(frameComptabilite, text="Sauvegarder", font=(fonts.Texte_Fonts, 15),
                              foreground=coloration.BG_Couleur3, background=coloration.BG_Neutre,
                              activebackground=coloration.BG_Neutre, activeforeground=coloration.BG_Couleur3)
    btnSauvegarde.place(x=480, y=450)

    btnAnnuler = tk.Button(frameComptabilite, text="Annuler", font=(fonts.Texte_Fonts, 15),
                           foreground=coloration.BG_Couleur3, background=coloration.BG_Neutre,
                           activebackground=coloration.BG_Neutre, activeforeground=coloration.BG_Couleur3)
    btnAnnuler.place(x=650, y=450)

    # --------------------------->PHOTO----------------------------------------------
    imgProfil = PhotoImage(file="")
    lblPhoto_profil = Label(frameImage, background=coloration.BG_Neutre, image=imgProfil)
    lblPhoto_profil.place(x=0, y=0)


# ========================================================= FIN  COMPTABILITE=======================================================================

# ========================================================= DEBUT CONTROLES========================================================================
def controles():
    # ==================FRAMES=============================
    frameControle = tk.Frame(home_fenetre, background=coloration.BG_Couleur3, width=835, height=560, borderwidth=1,
                             relief=tk.SOLID)
    frameControle.place(x=235, y=74)

    # ----------------------------------------frame elements controle-----------------------------
    frame_elements_controle = tk.Frame(frameControle, background=coloration.BG_Couleur3, width=829, height=554,
                                       borderwidth=1, relief=tk.SOLID)
    frame_elements_controle.place(x=2, y=2)
    # -------------------------------------------frame image profil---------------------
    frameImage = tk.Frame(frameControle, relief=tk.GROOVE)
    frameImage.place(x=560, y=60, width=160, height=160)

    frameInfoControle = tk.Frame(frameControle, width=200, height=30, relief=tk.GROOVE)
    frameInfoControle.place(x=555, y=350)
    # -----------------------------Entete------------------------
    entete_controle = Label(frame_elements_controle, text="CONTROLE FINANCIER", font=(fonts.Titre_Fonts, 20, 'bold'),
                            background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    entete_controle.place(x=250, y=10)
    # -------------------------------------------------->INFOS-----------------------
    lblIDentifiant = Label(frame_elements_controle, text="ID", font=(fonts.Texte_Fonts, 14),
                           background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblIDentifiant.place(x=20, y=60)

    txtIdentifiant = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                              foreground=coloration.BG_Couleur5)
    txtIdentifiant.place(x=180, y=60, width=150)

    lblMatticule = Label(frame_elements_controle, text="MATRICULE", font=(fonts.Texte_Fonts, 14),
                         background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblMatticule.place(x=20, y=100)

    txtMatricule = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                            foreground=coloration.BG_Couleur5)
    txtMatricule.place(x=180, y=100, width=150)

    lblNom = Label(frame_elements_controle, text="NOM", font=(fonts.Texte_Fonts, 14),
                   background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblNom.place(x=20, y=140)

    txtNom = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                      foreground=coloration.BG_Couleur5)
    txtNom.place(x=180, y=140)

    txtNom = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                      foreground=coloration.BG_Couleur5)
    txtNom.place(x=180, y=140)

    lblPostNom = Label(frame_elements_controle, text="POST-NOM", font=(fonts.Texte_Fonts, 14),
                       background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblPostNom.place(x=20, y=180)

    txtPostNom = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                          foreground=coloration.BG_Couleur5)
    txtPostNom.place(x=180, y=180)

    lblPreNom = Label(frame_elements_controle, text="PRENOM", font=(fonts.Texte_Fonts, 14),
                      background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblPreNom.place(x=20, y=220)

    txtPreNom = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                         foreground=coloration.BG_Couleur5)
    txtPreNom.place(x=180, y=220)

    lblDomaine = Label(frame_elements_controle, text="DOMAINE", font=(fonts.Texte_Fonts, 14),
                       background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblDomaine.place(x=20, y=260)

    txtDomaine = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                          foreground=coloration.BG_Couleur5)
    txtDomaine.place(x=180, y=260, width=300)

    lblDepartement = Label(frame_elements_controle, text="DEPARTEMENT", font=(fonts.Texte_Fonts, 14),
                           background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblDepartement.place(x=20, y=300)

    txtDepartement = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                              foreground=coloration.BG_Couleur5)
    txtDepartement.place(x=180, y=300, width=300)

    txtDepartement = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                              foreground=coloration.BG_Couleur5)
    txtDepartement.place(x=180, y=300)

    lblPromotion = Label(frame_elements_controle, text="PROMOTION", font=(fonts.Texte_Fonts, 14),
                         background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblPromotion.place(x=20, y=340)

    txtPromotion = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                            foreground=coloration.BG_Couleur5)
    txtPromotion.place(x=180, y=340)

    lblVacation = Label(frame_elements_controle, text="VACATION", font=(fonts.Texte_Fonts, 14),
                        background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblVacation.place(x=20, y=380)

    txtVacation = tk.Entry(frame_elements_controle, bd=1, font=(fonts.Texte_Fonts, 14),
                           foreground=coloration.BG_Couleur5)
    txtVacation.place(x=180, y=380)

    lblTotalPayer = Label(frame_elements_controle, text="Total à Payer:  0$", font=(fonts.Texte_Fonts, 14),
                          background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblTotalPayer.place(x=555, y=230)

    lblMontantPayer = Label(frame_elements_controle, text="Montant payer: 0$", font=(fonts.Texte_Fonts, 14),
                            background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblMontantPayer.place(x=555, y=270)

    lblRestePayer = Label(frame_elements_controle, text="Reste à Payer:  0$", font=(fonts.Texte_Fonts, 14),
                          background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblRestePayer.place(x=555, y=310)

    btnScanerCarte = tk.Button(frameControle, text="Scanner la Carte", font=(fonts.Texte_Fonts, 15),
                               foreground=coloration.BG_Couleur3, background=coloration.BG_Neutre,
                               activebackground=coloration.BG_Neutre, activeforeground=coloration.BG_Couleur3, width=17)
    btnScanerCarte.place(x=555, y=390)
    # --------------------------->PHOTO----------------------------------------------
    imgProfil = PhotoImage(file="")
    lblPhoto_profil = Label(frameImage, background=coloration.BG_Neutre, image=imgProfil)
    lblPhoto_profil.place(x=0, y=0)


# ================================================================ FIN CONTROLES=========================================

# ========================================================= DEBUT GESTION========================================================================
def gestion():
    def fraisFixation():

        class FixationFrais:

            def generer_annees_academiques(self):
                annee_actuel = datetime.datetime.now().year
                if datetime.datetime.now().month < 10:
                    annee_debut = annee_actuel - 1
                else:
                    annee_debut = annee_actuel
                annee_fin = annee_debut + 1
                return f"{annee_debut}-{annee_fin}"

            def selectionDomaine(self, event):
                if comboDomaines.get() == 'Domaine':
                    comboPromotion.delete(0, END)

            def NonSectionDomaine(self, event):
                domaine = comboPromotion.get()
                if domaine == '':
                    comboDomaines.insert(0, "Selection du Domaine")

            def selectionPromotion(self, event):
                if comboPromotion.get() == 'Promotion':
                    comboPromotion.delete(0, END)

            def NonSectionPromotion(self, event):
                promotion = comboPromotion.get()
                if promotion == '':
                    comboPromotion.insert(0, "Selection de la Promotion")

            def generer_annees_academiques(self):
                annee_actuel = datetime.datetime.now().year
                if datetime.datetime.now().month < 10:
                    annee_debut = annee_actuel - 1
                else:
                    annee_debut = annee_actuel
                annee_fin = annee_debut + 1
                return f"{annee_debut}-{annee_fin}"

                # Fonction pour mettre à jour les filières en fonction du domaine sélectionné

            def mise_a_jour_filieres(self, event):
                domaine_selectionne = comboDomaines.get()
                filieres = ajouts_informations.domaines_filieres.get(domaine_selectionne, [])
                comboFiliere['values'] = filieres
                comboFiliere.current(0)
                ajouts_informations.mise_a_jour_promotions()

                # Fonction pour mettre à jour les promotions en fonction de la filière sélectionnée

            def mise_a_jour_promotions(self, event=None):
                filiere_selectionnee = comboFiliere.get()
                promotions = ajouts_informations.filieres_promotions.get(filiere_selectionnee, [])
                comboPromotion['values'] = promotions
                comboPromotion.current(0)

            # Données de test pour les domaines, filières et promotions
            domaines_filieres = {
                "SCIENCES DE L'HOMME ET DE LA SOCIETE": ["(SIC) Sciences de l'information et de la communication",
                                                         "(DAH) Développement et Action Humanitaire"],
                "SCIENCES ECONOMIQUES ET DE GESTION": ["Sciences Economiques", "Sciences de Gestion"],
                "SCIENCES ET TECHNOLOGIES ": ["Sciences et Technologies", "Génie Civil", "Génie Electrique"],
                "SCIENCES AGRONOMIQUE ET ENVIRONEMENT": ["Production Animale", "Production végetale"],
                "SCIENCES PSYCHOLOGIQUES ET DE L'EDUCATION": ["Sciences Psycologique"],
                "SCIENCES JURIDIQUES, POLITIQUE ET ADMINISTRATIVES": ["Droit"],
                "SCIENCES DE LA SANTE": ["Médécine Humaine", "Santé Publique"]
            }

            filieres_promotions = {
                "(SIC) Sciences de l'information et de la communication": ['Licence 1 (L1)', 'Licence 2 (L2)',
                                                                           'Licence 3 (L3)',
                                                                           'Master 1 (M1)', 'Master 2 (M2)'],
                "(DAH) Développement et Action Humanitaire": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)',
                                                              'Master 1 (M1)', 'Master 2 (M2)'],
                "Sciences Economiques": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                         'Master 2 (M2)'],
                "Sciences de Gestion": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                        'Master 2 (M2)'],
                "Sciences et Technologies": ['Pré Licence (L0)', 'Licence 1 (L1)'],
                "Génie Civil": ['Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)', 'Master 2(M2)'],
                "Génie Electrique": ['Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)', 'Master 2(M2)'],
                "Production Animale": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                       'Master 2 (M2)'],
                "Production végetale": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                        'Master 2 (M2)'],
                "Sciences Psycologique": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                          'Master 2 (M2)'],
                "Droit": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)', 'Master 2 (M2)'],
                "Médécine Humaine": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Doc 1', 'Doc 2', 'Doc 3',
                                     'Doc 4'],
                "Santé Publique": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                   'Master 2 (M2)']
            }

        ajouts_informations = FixationFrais()

        # ==================FRAMES FIXATION FRAIS=============================
        frameFixationFrais = tk.Frame(frame_elements_gestion, background=coloration.BG_Couleur3, width=823, height=490,
                                      borderwidth=1, relief=tk.SOLID)
        frameFixationFrais.place(x=2, y=60)

        frame_elements_frais_fixation_academique = tk.Frame(frameFixationFrais, background=coloration.BG_Couleur3,
                                                            width=410, height=488, borderwidth=1, relief=tk.SOLID)
        frame_elements_frais_fixation_academique.place(x=0, y=0)

        frame_elements_frais_fixation_complement = tk.Frame(frameFixationFrais, background=coloration.BG_Couleur3,
                                                            width=410, height=488, borderwidth=1, relief=tk.SOLID)
        frame_elements_frais_fixation_complement.place(x=411, y=0)

        frame_treeview_frais_academique = tk.Frame(frame_elements_frais_fixation_academique,
                                                   background=coloration.BG_Neutre, width=400, height=134,
                                                   borderwidth=1, relief=tk.SOLID)
        frame_treeview_frais_academique.place(x=5, y=350)

        frame_treeview_frais_complement = tk.Frame(frame_elements_frais_fixation_complement,
                                                   background=coloration.BG_Neutre, width=400, height=134,
                                                   borderwidth=1, relief=tk.SOLID)
        frame_treeview_frais_complement.place(x=5, y=350)

        # -------------------------Elements frais academique------------------------------------
        entete_frais_acadelique = Label(frame_elements_frais_fixation_academique, text="FRAIS ACADEMIQUE",
                                        font=(fonts.Titre_Fonts, 15, 'bold'),
                                        background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        entete_frais_acadelique.place(x=90, y=10)

        # --------------------------------->DOMAINE----------------------------------------------------
        lblDomaines = Label(frame_elements_frais_fixation_academique, text="DOMAINE", font=(fonts.Texte_Fonts, 14),
                            background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblDomaines.place(x=5, y=50)
        txtDomaines = Entry(frame_elements_frais_fixation_academique, bd=2, font=(fonts.Texte_Fonts, 14),
                            foreground=coloration.BG_Couleur5)
        txtDomaines.place(x=105, y=50, width=300)

        comboDomaines = ttk.Combobox(frame_elements_frais_fixation_academique, font=(fonts.Texte_Fonts, 14),
                                     values=list(ajouts_informations.domaines_filieres.keys()),
                                     foreground=coloration.BG_Couleur5)
        comboDomaines.place(x=105, y=50, width=300)
        comboDomaines.insert(0, "Selection du Domaine")
        comboDomaines.bind("<<ComboboxSelected>>", ajouts_informations.mise_a_jour_filieres)

        # ---------------------------------->OPTION-----------------------------------------------
        lblOption = Label(frame_elements_frais_fixation_academique, text="DEP.", font=(fonts.Texte_Fonts, 14),
                          background=coloration.BG_Couleur3, foreground='white')
        lblOption.place(x=5, y=90)
        txtOption = Entry(frame_elements_frais_fixation_academique, bd=2, font=(fonts.Texte_Fonts, 14),
                          foreground=coloration.BG_Couleur5)
        txtOption.place(x=105, y=90, width=300)
        comboFiliere = ttk.Combobox(frame_elements_frais_fixation_academique, font=(fonts.Texte_Fonts, 14), values=[])
        comboFiliere.place(x=105, y=90, width=300)
        comboFiliere.bind("<<ComboboxSelected>>", ajouts_informations.mise_a_jour_promotions)
        # ----------------------------------------->PROMOTION----------------------------------------
        lblPromotion = Label(frame_elements_frais_fixation_academique, text="PROMOTION", font=(fonts.Texte_Fonts, 14),
                             background=coloration.BG_Couleur3, foreground='white')
        lblPromotion.place(x=5, y=130)
        txtPromotion = Entry(frame_elements_frais_fixation_academique, bd=2, font=(fonts.Texte_Fonts, 14),
                             foreground=coloration.BG_Couleur5)
        txtPromotion.place(x=150, y=130, width=200)
        comboPromotion = ttk.Combobox(frame_elements_frais_fixation_academique, font=(fonts.Texte_Fonts, 14),
                                      foreground=coloration.BG_Couleur5)
        comboPromotion.place(x=150, y=130, width=200)

        lblPrixAcademique = Label(frame_elements_frais_fixation_academique, text="FRAIS ACA.",
                                  font=(fonts.Texte_Fonts, 14),
                                  background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblPrixAcademique.place(x=5, y=170)
        txtPrixAcademique = Entry(frame_elements_frais_fixation_academique, bd=2, font=(fonts.Texte_Fonts, 14),
                                  foreground=coloration.BG_Couleur5)
        txtPrixAcademique.place(x=150, y=170, width=200)

        lblDevise = Label(frame_elements_frais_fixation_academique, text="$", font=(fonts.Texte_Fonts, 14),
                          background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblDevise.place(x=360, y=170)

        # ---------------------Annee Academique---------------------------------
        lblAcademiqueAnnee = Label(frame_elements_frais_fixation_academique, text="ANNEE ACADEMIQUE",
                                   font=(fonts.Texte_Fonts, 14),
                                   background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblAcademiqueAnnee.place(x=5, y=210)
        txtAcademiqueAnnee = Entry(frame_elements_frais_fixation_academique, bd=2, font=(fonts.Texte_Fonts, 14))
        txtAcademiqueAnnee.place(x=220, y=210, width=130)

        comboAcademqueAnnee = ttk.Combobox(frame_elements_frais_fixation_academique, font=(fonts.Texte_Fonts, 14),
                                           foreground=coloration.BG_Couleur5)
        # Définition de la liste annee académique
        annees_academiques = ajouts_informations.generer_annees_academiques()
        # Ajout des annee academique au combobox
        comboAcademqueAnnee['values'] = annees_academiques
        # Définition de l'annee academique
        comboAcademqueAnnee.set(annees_academiques)
        comboAcademqueAnnee.place(x=220, y=210, width=130)

        lblMotDePasseAdmin = Label(frame_elements_frais_fixation_academique, text="Mot de passe Admin",
                                   font=(fonts.Texte_Fonts, 14),
                                   background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblMotDePasseAdmin.place(x=5, y=250)
        txtMotDePasseAdmin = Entry(frame_elements_frais_fixation_academique, bd=2, font=(fonts.Texte_Fonts, 14),
                                   foreground=coloration.BG_Couleur5)
        txtMotDePasseAdmin.place(x=200, y=250, width=180)

        btnSauvegardeFraisAcademique = Button(frame_elements_frais_fixation_academique, text="ENREGISTRER",
                                              font=(fonts.Texte_Fonts, 15),
                                              foreground=coloration.BG_Couleur3, border=1, background='white',
                                              activebackground=coloration.BG_Neutre,
                                              activeforeground=coloration.BG_Couleur3, relief=tk.RIDGE)
        btnSauvegardeFraisAcademique.place(x=50, y=290)

        btnModifierFraisAcademique = Button(frame_elements_frais_fixation_academique, text="MODIFIER",
                                            font=(fonts.Texte_Fonts, 15),
                                            foreground=coloration.BG_Couleur3, border=1, background='white',
                                            activebackground=coloration.BG_Neutre,
                                            activeforeground=coloration.BG_Couleur3, relief=tk.RIDGE)
        btnModifierFraisAcademique.place(x=250, y=290)

        # ----------------------------Element frais complement-----------------------------
        entete_frais_complement = Label(frame_elements_frais_fixation_complement, text="FRAIS DE COMPLEMENT",
                                        font=(fonts.Titre_Fonts, 15, 'bold'),
                                        background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        entete_frais_complement.place(x=90, y=10)

        # --------------------------------->DOMAINE----------------------------------------------------
        lblDomainesComplement = Label(frame_elements_frais_fixation_complement, text="DOMAINE",
                                      font=(fonts.Texte_Fonts, 14),
                                      background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblDomainesComplement.place(x=5, y=50)
        txtDomainesComplement = Entry(frame_elements_frais_fixation_complement, bd=2, font=(fonts.Texte_Fonts, 14),
                                      foreground=coloration.BG_Couleur5)
        txtDomainesComplement.place(x=105, y=50, width=300)
        # ---------------------------------->OPTION-----------------------------------------------
        lblOptionComplement = Label(frame_elements_frais_fixation_complement, text="DEP.", font=(fonts.Texte_Fonts, 14),
                                    background=coloration.BG_Couleur3, foreground='white')
        lblOptionComplement.place(x=5, y=90)
        txtOptionComplement = Entry(frame_elements_frais_fixation_complement, bd=2, font=(fonts.Texte_Fonts, 14),
                                    foreground=coloration.BG_Couleur5)
        txtOptionComplement.place(x=105, y=90, width=300)
        # ----------------------------------------->PROMOTION----------------------------------------
        lblPromotionComplement = Label(frame_elements_frais_fixation_complement, text="PROMOTION",
                                       font=(fonts.Texte_Fonts, 14),
                                       background=coloration.BG_Couleur3, foreground='white')
        lblPromotionComplement.place(x=5, y=130)
        txtPromotionComplement = Entry(frame_elements_frais_fixation_complement, bd=2, font=(fonts.Texte_Fonts, 14),
                                       foreground=coloration.BG_Couleur5)
        txtPromotionComplement.place(x=150, y=130, width=200)

        lblPrixComplement = Label(frame_elements_frais_fixation_complement, text="FRAIS COMPL.",
                                  font=(fonts.Texte_Fonts, 14),
                                  background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblPrixComplement.place(x=5, y=170)
        txtPrixComplement = Entry(frame_elements_frais_fixation_complement, bd=2, font=(fonts.Texte_Fonts, 14),
                                  foreground=coloration.BG_Couleur5)
        txtPrixComplement.place(x=150, y=170, width=200)

        lblDevise = Label(frame_elements_frais_fixation_complement, text="$", font=(fonts.Texte_Fonts, 14),
                          background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblDevise.place(x=360, y=170)
        # ---------------------Annee Academique---------------------------------
        lblAcademiqueAnnee = Label(frame_elements_frais_fixation_complement, text="ANNEE ACADEMIQUE",
                                   font=(fonts.Texte_Fonts, 14),
                                   background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblAcademiqueAnnee.place(x=5, y=210)
        txtAcademiqueAnnee = Entry(frame_elements_frais_fixation_complement, bd=2, font=(fonts.Texte_Fonts, 14))
        txtAcademiqueAnnee.place(x=220, y=210, width=130)

        lblMotDePasseAdmin = Label(frame_elements_frais_fixation_complement, text="Mot de passe Admin",
                                   font=(fonts.Texte_Fonts, 14),
                                   background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
        lblMotDePasseAdmin.place(x=5, y=250)
        txtMotDePasseAdmin = Entry(frame_elements_frais_fixation_complement, bd=2, font=(fonts.Texte_Fonts, 14),
                                   foreground=coloration.BG_Couleur5)
        txtMotDePasseAdmin.place(x=200, y=250, width=180)

        btnSauvegardeFraisComplement = Button(frame_elements_frais_fixation_complement, text="ENREGISTRER",
                                              font=(fonts.Texte_Fonts, 15),
                                              foreground=coloration.BG_Couleur3, border=1, background='white',
                                              activebackground=coloration.BG_Neutre,
                                              activeforeground=coloration.BG_Couleur3, relief=tk.RIDGE)
        btnSauvegardeFraisComplement.place(x=50, y=290)

        btnModifierFraisComplement = Button(frame_elements_frais_fixation_complement, text="MODIFIER",
                                            font=(fonts.Texte_Fonts, 15),
                                            foreground=coloration.BG_Couleur3, border=1, background='white',
                                            activebackground=coloration.BG_Neutre,
                                            activeforeground=coloration.BG_Couleur3, relief=tk.RIDGE)
        btnModifierFraisComplement.place(x=250, y=290)

    # ==============================================FIN FRAIS FIXATION ===============================================

    frameGestion = tk.Frame(home_fenetre, background=coloration.BG_Couleur3, width=835, height=560, borderwidth=1,
                            relief=tk.SOLID)
    frameGestion.place(x=235, y=74)

    # -----------------------frame elements gestion
    frame_elements_gestion = tk.Frame(frameGestion, background=coloration.BG_Couleur3, width=829, height=554,
                                      borderwidth=1, relief=tk.SOLID)
    frame_elements_gestion.place(x=2, y=2)

    frame_option_gestion = tk.Frame(frame_elements_gestion, background=coloration.BG_Couleur3, width=823, height=490,
                                    borderwidth=1, relief=tk.SOLID)
    frame_option_gestion.place(x=2, y=60)

    frame_bouton_gestion = tk.Frame(frame_elements_gestion, background=coloration.BG_Couleur3, width=300, height=400,
                                    borderwidth=1, relief=tk.SOLID)
    frame_bouton_gestion.place(x=250, y=100)

    # -----------------------------Entete------------------------
    entete_gestion = Label(frame_elements_gestion, text="ADMINISTRATION BUDGET",
                           font=(fonts.Titre_Fonts, 20, 'bold'),
                           background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    entete_gestion.place(x=230, y=10)

    btnFixation_frais = Button(frame_bouton_gestion, text="FIXATION FRAIS", font=(fonts.Texte_Fonts, 15),
                               foreground=coloration.BG_Couleur3, border=1, background='white',
                               activebackground='white',
                               activeforeground=coloration.BG_Couleur3, command=fraisFixation, relief=tk.RIDGE)
    btnFixation_frais.place(x=15, y=80, width=270)

    btnPermitionSpecifique = Button(frame_bouton_gestion, text="PERMITION SPECIFIQUE", font=(fonts.Texte_Fonts, 15),
                                    foreground=coloration.BG_Couleur3, border=1, background='white',
                                    activebackground='white',
                                    activeforeground=coloration.BG_Couleur3, relief=tk.RIDGE)
    btnPermitionSpecifique.place(x=15, y=140, width=270)

    btnGestionControle = Button(frame_bouton_gestion, text="GESTION CONTROLE", font=(fonts.Texte_Fonts, 15),
                                foreground=coloration.BG_Couleur3, border=1, background='white',
                                activebackground='white',
                                activeforeground=coloration.BG_Couleur3, relief=tk.RIDGE)
    btnGestionControle.place(x=15, y=200, width=270)

    btnGestionControle = Button(frame_bouton_gestion, text="GESTION RECOUVREMENT", font=(fonts.Texte_Fonts, 15),
                                foreground=coloration.BG_Couleur3, border=1, background='white',
                                activebackground='white',
                                activeforeground=coloration.BG_Couleur3, relief=tk.RIDGE)
    btnGestionControle.place(x=15, y=260, width=270)


# ========================================================= FIN  GESTION=======================================================================

# ======================================== DEBUT INSCRIPTION ET INFORMATION ======================================================================
def inscriptions():
    class Inscription:
        profile = {1: ""}

        def selectionDomaine(self, event):
            if comboDomaines.get() == 'Domaine':
                comboPromotion.delete(0, END)

        def NonSectionDomaine(self, event):
            domaine = comboPromotion.get()
            if domaine == '':
                comboDomaines.insert(0, "Selection du Domaine")

        def selectionPromotion(self, event):
            if comboPromotion.get() == 'Promotion':
                comboPromotion.delete(0, END)

        def NonSectionPromotion(self, event):
            promotion = comboPromotion.get()
            if promotion == '':
                comboPromotion.insert(0, "Selection de la Promotion")

        def generer_annees_academiques(self):
            annee_actuel = datetime.datetime.now().year
            if datetime.datetime.now().month < 10:
                annee_debut = annee_actuel - 1
            else:
                annee_debut = annee_actuel
            annee_fin = annee_debut + 1
            return f"{annee_debut}-{annee_fin}"

        # Fonction pour mettre à jour les filières en fonction du domaine sélectionné

        def mise_a_jour_filieres(self, event):
            domaine_selectionne = comboDomaines.get()
            filieres = ajouts_informations.domaines_filieres.get(domaine_selectionne, [])
            comboFiliere['values'] = filieres
            comboFiliere.current(0)
            ajouts_informations.mise_a_jour_promotions()

        # Fonction pour mettre à jour les promotions en fonction de la filière sélectionnée
        def mise_a_jour_promotions(self, event=None):
            filiere_selectionnee = comboFiliere.get()
            promotions = ajouts_informations.filieres_promotions.get(filiere_selectionnee, [])
            comboPromotion['values'] = promotions
            comboPromotion.current(0)

        def parcourirImage(self):
            global nom_fichierImage
            global imageProfil
            nom_fichierImage = filedialog.askopenfilename(initialdir=os.getcwd(), title="Selectioner l'image de profil",
                                                          filetypes=(
                                                          ("Fichier PNG", "*.png"), (" Fichier JPG", "*.jpg")))
            imageProfil = (Image.open(nom_fichierImage))
            redim_imageProfil = imageProfil.resize((160, 160))
            photoProfil = ImageTk.PhotoImage(redim_imageProfil)
            label_imageProfil.config(image=photoProfil)
            label_imageProfil.image = photoProfil

            print(nom_fichierImage)

        def informationsEtudiants(self):
            etudiants = dataStudents.fetch_Etudiants()
            informations.delete(*informations.get_children())
            for etudiant in etudiants:
                informations.insert("", END, values=etudiant)

        def cls(*cliked):
            if cliked:
                informations.selection_remove(informations.focus())
            txtIDentifiant.delete(0, END)
            txtNumeroMatricule.delete(0, END)
            txtNom.delete(0, END)
            txtPostnom.delete(0, END)
            txtPrenom.delete(0, END)
            valSexe.set("")
            txtContact.delete(0, END)
            comboDomaines.set("")
            comboDomaines.set("Selection du Domaine")
            comboPromotion.set("")
            comboPromotion.set("")
            comboFiliere.set("")
            comboVacation.set("")
            comboVacation.set("JOUR")
            comboSystme.set("")
            comboSystme.set("LMD")
            comboAcademqueAnnee.set("")
            comboAcademqueAnnee.set(annees_academiques)
            label_imageProfil.destroy()
            imgProfile = "img/avatar.png"
            lectureImage = Image.open(imgProfile)
            lectureImage.thumbnail((160, 160))
            photo = ImageTk.PhotoImage(lectureImage)
            ajouts_informations.profile[1] = photo

            lblProfil = Label(frame_child, background=coloration.BG_Neutre, image=photo)
            lblProfil.place(x=0, y=0)

        def numeroMatriculeGeneration(self, nom, postnom, prenom, annee_systeme):
            # Obtenez
            initial_nom = nom[:1].upper()
            initial_prenom = postnom[:1].upper()
            derniere_letre_prenom = prenom[-1:].upper()
            Date = StringVar()
            today = date.today()
            annee_systeme = today.strftime("%Y")
            connectionDB = sqlite3.connect("databases/studentsRegistration.db")
            curseur = connectionDB.cursor()
            curseur.execute("SELECT COUNT(*) FROM  registre_etudiant")
            count = curseur.fetchone()[0]
            connectionDB.commit()
            connectionDB.close()
            numeroMatricule = f"{initial_prenom}{initial_nom}{count + 1:03d}{derniere_letre_prenom}{annee_systeme}"
            return numeroMatricule

        def sauvegarde(self):
            identifiant = txtIDentifiant.get()
            # matricule = txtNumeroMatricule.get()
            nom = txtNom.get()
            postnom = txtPostnom.get()
            prenom = txtPrenom.get()
            sexe = valSexe.get()
            codePays = comboContact.get()
            num_tel = txtContact.get()
            domaine = comboDomaines.get()
            promotion = comboPromotion.get()
            departement = comboFiliere.get()
            vacation = comboVacation.get()
            systeme = comboSystme.get()
            date_enregistrement = date_systeme
            annee_academiques = comboAcademqueAnnee.get()
            Date = StringVar()
            today = date.today()
            annee_systeme = today.strftime("%Y")
            matricule = ajouts_informations.numeroMatriculeGeneration(nom, postnom, prenom, annee_systeme)

            print('Matricule est: ', matricule)
            print("Date d'enregistrement: ", date_enregistrement)
            if not (
                    identifiant and nom and postnom and prenom and sexe and codePays and num_tel and domaine and promotion and departement and vacation and systeme and date_enregistrement and annee_academiques):
                messagebox.showerror("Erreur d'information", "Veuillez completer tout les infomartion")
            elif dataStudents.identifiant_exists(identifiant, matricule):
                messagebox.showerror("Erreur identifiant", "ID ou MATRICULE existe!!!")
            else:
                dataStudents.insertion_DataEtudiants(identifiant, matricule, nom, postnom, prenom, sexe, codePays,
                                                     num_tel, domaine, promotion, departement, vacation, systeme,
                                                     date_enregistrement, annee_academiques)

                # imageProfil.save("img/photos_profils/profile_" + str(identifiant) + "." + "jpg")
                global file_name
                file_name = nom_fichierImage
                im = Image.open(file_name)
                rgb_img = im.convert('RGB')
                rgb_img.save(("img/photos_profils/profile_" + str(identifiant) + "." + "jpg"))

                messagebox.showinfo("Enregistrement",
                                    f"L'étudiant(e) {nom} {postnom} {prenom} est enregister avec successer!!!")
                ajouts_informations.informationsEtudiants()
                ajouts_informations.cls()

        def supprimerEtudiants(self):
            selection_item = informations.focus()
            if not selection_item:
                messagebox.showerror("Erreur", "Selectioner l'Etudiant à supprimer")
            else:
                identifiant = txtIDentifiant.get()
                matricule = txtNumeroMatricule.get()
                lienFichier_suppri = ("img/photos_profils/profile_" + str(identifiant) + "." + "jpg")
                if os.path.exists(lienFichier_suppri):
                    try:
                        os.remove(lienFichier_suppri)
                    except Exception as e:
                        messagebox.showerror('Erreur suppression',
                                             f"Une erreur s'est produite lors de la suppresion de l'image : {str(e)}")
                else:
                    messagebox.showerror('Erreur suppression', "Le fichier ou le chemin est incorrect.")

                reponse = messagebox.askyesno("Suppression",
                                              "Voulez-vous réellement supprimer cet étudiant ? \n Cliquer sur « OUI » pour finir")
                if reponse:
                    ## On supprime l'etudiant
                    dataStudents.supprimerEtudiants(identifiant, matricule)
                    ajouts_informations.informationsEtudiants()
                    ajouts_informations.cls()
                    messagebox.showinfo("Suppression", "Donnée supprimer!!!")

        def modificationEtudiant(self):
            selection_item = informations.focus()
            if not selection_item:
                messagebox.showerror("Erreur", "Selectioner l'Etudiant à modifier")
            else:
                identifiant = txtIDentifiant.get()
                nom = txtNom.get()
                postnom = txtPostnom.get()
                prenom = txtPrenom.get()
                sexe = valSexe.get()
                codePays = comboContact.get()
                num_tel = txtContact.get()
                domaine = comboDomaines.get()
                promotion = comboPromotion.get()
                departement = comboFiliere.get()
                vacation = comboVacation.get()
                systeme = comboSystme.get()
                date_enregistrement = date_systeme
                annee_academiques = comboAcademqueAnnee.get()
                Date = StringVar()
                today = date.today()
                annee_systeme = today.strftime("%Y")
                dataStudents.mise_a_jourEtudinat(identifiant, nom, postnom, prenom, sexe, codePays, num_tel, domaine,
                                                 promotion, departement, vacation, systeme, date_enregistrement,
                                                 annee_academiques)
                ajouts_informations.informationsEtudiants()
                ajouts_informations.cls()
                messagebox.showinfo("Modification", "Donnée modifier avec success")

        def afficherDonnees(self, event):
            selection_item = informations.focus()
            if selection_item:
                ligneSelectionner = informations.item(selection_item)["values"]
                ajouts_informations.cls()
                txtIDentifiant.insert(0, ligneSelectionner[0])
                txtNumeroMatricule.insert(0, ligneSelectionner[1])
                txtNom.insert(0, ligneSelectionner[2])
                txtPostnom.insert(0, ligneSelectionner[3])
                txtPrenom.insert(0, ligneSelectionner[4])
                valSexe.set(ligneSelectionner[5])
                comboContact.set(ligneSelectionner[6])
                txtContact.insert(0, ligneSelectionner[7])
                comboDomaines.set(ligneSelectionner[8])
                comboPromotion.set(ligneSelectionner[9])
                comboFiliere.set(ligneSelectionner[10])
                comboVacation.set(ligneSelectionner[11])
                comboAcademqueAnnee.set(ligneSelectionner[14])

                # load image
                idSelect = informations.item(selection_item)['values'][0]
                imgProfile = "img/photos_profils/profile_" + str(idSelect) + "." + "jpg"
                lectureImage = Image.open(imgProfile)
                lectureImage.thumbnail((160, 160))
                photo = ImageTk.PhotoImage(lectureImage)
                ajouts_informations.profile[1] = photo

                lblProfil = Label(frame_child, image=photo)
                lblProfil.place(x=0, y=0)
                print(imgProfile)

            else:
                pass

        def Recherche(self):
            for x in informations.get_children():
                informations.delete(x)
            rechercheEntre = txtRecherche.get()
            connectionDB = sqlite3.connect("databases/studentsRegistration.db")
            curseur = connectionDB.cursor()
            selectRecherche = curseur.execute("SELECT * FROM registre_etudiant WHERE Noms=?", (rechercheEntre,))
            connectionDB.commit()
            for row in selectRecherche:
                informations.insert('', END, values=row)
            connectionDB.close()

        # Données de test pour les domaines, filières et promotions
        domaines_filieres = {
            "SCIENCES DE L'HOMME ET DE LA SOCIETE": ["(SIC) Sciences de l'information et de la communication",
                                                     "(DAH) Développement et Action Humanitaire"],
            "SCIENCES ECONOMIQUES ET DE GESTION": ["Sciences Economiques", "Sciences de Gestion"],
            "SCIENCES ET TECHNOLOGIES ": ["Sciences et Technologies", "Génie Civil", "Génie Electrique"],
            "SCIENCES AGRONOMIQUE ET ENVIRONEMENT": ["Production Animale", "Production végetale"],
            "SCIENCES PSYCHOLOGIQUES ET DE L'EDUCATION": ["Sciences Psycologique"],
            "SCIENCES JURIDIQUES, POLITIQUE ET ADMINISTRATIVES": ["Droit"],
            "SCIENCES DE LA SANTE": ["Médécine Humaine", "Santé Publique"]
        }

        filieres_promotions = {
            "(SIC) Sciences de l'information et de la communication": ['Licence 1 (L1)', 'Licence 2 (L2)',
                                                                       'Licence 3 (L3)',
                                                                       'Master 1 (M1)', 'Master 2 (M2)'],
            "(DAH) Développement et Action Humanitaire": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)',
                                                          'Master 1 (M1)', 'Master 2 (M2)'],
            "Sciences Economiques": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                     'Master 2 (M2)'],
            "Sciences de Gestion": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                    'Master 2 (M2)'],
            "Sciences et Technologies": ['Pré Licence (L0)', 'Licence 1 (L1)'],
            "Génie Civil": ['Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)', 'Master 2(M2)'],
            "Génie Electrique": ['Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)', 'Master 2(M2)'],
            "Production Animale": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                   'Master 2 (M2)'],
            "Production végetale": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                    'Master 2 (M2)'],
            "Sciences Psycologique": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)',
                                      'Master 2 (M2)'],
            "Droit": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)', 'Master 2 (M2)'],
            "Médécine Humaine": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Doc 1', 'Doc 2', 'Doc 3',
                                 'Doc 4'],
            "Santé Publique": ['Licence 1 (L1)', 'Licence 2 (L2)', 'Licence 3 (L3)', 'Master 1 (M1)', 'Master 2 (M2)']
        }

    ajouts_informations = Inscription()
    # ==================FRAMES=============================
    frameInscription = tk.Frame(home_fenetre, background=coloration.BG_Couleur3, width=835, height=560, borderwidth=1,
                                relief=tk.SOLID)
    frameInscription.place(x=235, y=74)
    # ----------------------------------------frame elements inscriptions-----------------------------
    frame_elements_inscription = tk.Frame(frameInscription, background=coloration.BG_Couleur3, width=829, height=554,
                                          borderwidth=1)
    frame_elements_inscription.place(x=2, y=2)
    # -------------------------------------------frame image profil---------------------
    frameImage = ttk.Frame(frame_elements_inscription, width=200, height=200, relief=tk.GROOVE)
    frameImage.place(x=670, y=60, width=160, height=160)

    frame_parent = ttk.Frame(frameImage)
    frame_parent.pack(expand=True, fill="both")

    frame_child = ttk.Frame(frame_parent, borderwidth=2)
    frame_child.pack(expand=True, fill="both")
    # -------------------------------------------------frame treeview-----------------
    frame_treeview = tk.Frame(frameInscription, background=coloration.BG_Neutre, width=800, height=150, borderwidth=1,
                              relief=tk.SOLID)
    frame_treeview.place(x=7, y=380)

    # =====================================================IDENTIFICATION====================================================
    entete_inscription = Label(frameInscription, text="INSCRIPTION ETUDIANT(E)", font=(fonts.Titre_Fonts, 20, 'bold'),
                               background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    entete_inscription.place(x=200, y=10)
    # ------------------------------------------------>MATRICULE-----------------
    lblMatricule = Label(frame_elements_inscription, text="MATRICULE", font=(fonts.Texte_Fonts, 14),
                         background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblMatricule.place(x=20, y=60)
    txtNumeroMatricule = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14),
                               foreground=coloration.BG_Couleur5)
    txtNumeroMatricule.place(x=145, y=60, width=150)
    # -------------------------------------------------->ID-----------------------
    lblIDentifiant = Label(frame_elements_inscription, text="ID", font=(fonts.Texte_Fonts, 14),
                           background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblIDentifiant.place(x=350, y=60)
    txtIDentifiant = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14),
                           foreground=coloration.BG_Couleur5)
    txtIDentifiant.place(x=380, y=60, width=150)
    btnIdentifiant = Button(frame_elements_inscription, text="Charger l'ID", font=(fonts.Texte_Fonts, 14),
                            foreground=coloration.BG_Couleur3, border=1, background=coloration.BG_Neutre,
                            activebackground=coloration.BG_Neutre, activeforeground=coloration.BG_Couleur5)
    btnIdentifiant.place(x=540, y=60, height=30)
    # --------------------------------------------------->NOM---------------------
    lblNom = Label(frame_elements_inscription, text="NOM", font=(fonts.Texte_Fonts, 14),
                   background=coloration.BG_Couleur3, foreground='white')
    lblNom.place(x=20, y=100)
    txtNom = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14), foreground=coloration.BG_Couleur5)
    txtNom.place(x=75, y=100, width=220)
    # --------------------------------------------------->POSTNOM-------
    lblPostnom = Label(frame_elements_inscription, text="POST-NOM", font=(fonts.Texte_Fonts, 14),
                       background=coloration.BG_Couleur3, foreground='white')
    lblPostnom.place(x=300, y=100)
    txtPostnom = Entry(frame_elements_inscription, border=2, font=(fonts.Texte_Fonts, 14),
                       foreground=coloration.BG_Couleur5)
    txtPostnom.place(x=410, y=100, width=250)
    # --------------------------------------------------->PRENOM-----------
    lblPrenom = Label(frame_elements_inscription, text="PRENOM", font=(fonts.Texte_Fonts, 14),
                      background=coloration.BG_Couleur3, foreground='white')
    lblPrenom.place(x=20, y=140)
    txtPrenom = Entry(frame_elements_inscription, border=2, font=(fonts.Texte_Fonts, 14),
                      foreground=coloration.BG_Couleur5)
    txtPrenom.place(x=120, y=140, width=250)
    # --------------------->CONTACT--------------------------------------------------------------------
    lblContact = Label(frame_elements_inscription, text="CONTACT", font=(fonts.Texte_Fonts, 14),
                       background=coloration.BG_Couleur3, foreground='white')
    lblContact.place(x=20, y=180)
    txtContact = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14),
                       foreground=coloration.BG_Couleur5)
    txtContact.place(x=195, y=180, width=180)
    listContact = ['+243', '+250', '+255']
    comboContact = ttk.Combobox(frame_elements_inscription, font=(fonts.Texte_Fonts, 14), values=listContact,
                                foreground=coloration.BG_Couleur5)
    comboContact.current(0)
    comboContact.place(x=120, y=180, width=70)
    # ------------------------------------->SEXE-------------------------------------------------
    valSexe = StringVar()
    lblSexe = Label(frame_elements_inscription, text="SEXE", font=(fonts.Texte_Fonts, 14),
                    background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblSexe.place(x=380, y=140)
    lblSexeM = Radiobutton(frame_elements_inscription, text="MASCULIN", value="M", variable=valSexe, indicatoron=0,
                           font=(fonts.Texte_Fonts, 12), foreground=coloration.BG_Couleur5, border=1,
                           background=coloration.BG_Couleur3, activebackground=coloration.BG_Couleur4,
                           activeforeground=coloration.BG_Couleur3)
    lblSexeM.place(x=450, y=140, width=100)
    lblSexeF = Radiobutton(frame_elements_inscription, text="FEMININ", value="F", variable=valSexe, indicatoron=0,
                           font=(fonts.Texte_Fonts, 12), foreground=coloration.BG_Couleur5, border=1,
                           background=coloration.BG_Couleur3, activebackground=coloration.BG_Couleur4,
                           activeforeground=coloration.BG_Couleur3)
    lblSexeF.place(x=550, y=140, width=100)
    # --------------------------------->SECTION----------------------------------------------------
    lblDomaines = Label(frame_elements_inscription, text="DOMAINE", font=(fonts.Texte_Fonts, 14),
                        background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblDomaines.place(x=20, y=220)
    txtDomaines = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14),
                        foreground=coloration.BG_Couleur5)
    txtDomaines.place(x=120, y=220, width=300)

    comboDomaines = ttk.Combobox(frame_elements_inscription, font=(fonts.Texte_Fonts, 14),
                                 values=list(ajouts_informations.domaines_filieres.keys()),
                                 foreground=coloration.BG_Couleur5)
    comboDomaines.place(x=120, y=220, width=300)
    comboDomaines.insert(0, "Selection du Domaine")
    comboDomaines.bind("<<ComboboxSelected>>", ajouts_informations.mise_a_jour_filieres)
    # --------------------------------->SYSTEME-----------------------------------------------------------
    lblSysteme = Label(frame_elements_inscription, text="SYSTEME", font=(fonts.Texte_Fonts, 14),
                       background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblSysteme.place(x=430, y=220)
    txtSyteme = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14), foreground=coloration.BG_Couleur5)
    txtSyteme.place(x=530, y=220, width=127)
    listSysteme = ["LMD"]
    comboSystme = ttk.Combobox(frame_elements_inscription, font=(fonts.Texte_Fonts, 14), values=listSysteme,
                               foreground=coloration.BG_Couleur5)
    comboSystme.current(0)
    comboSystme.place(x=530, y=220, width=127)
    # ---------------------------------->OPTION-----------------------------------------------
    lblOption = Label(frame_elements_inscription, text="DEPARTEMENT", font=(fonts.Texte_Fonts, 14),
                      background=coloration.BG_Couleur3, foreground='white')
    lblOption.place(x=20, y=260)
    txtOption = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14), foreground=coloration.BG_Couleur5)
    txtOption.place(x=175, y=260, width=300)

    comboFiliere = ttk.Combobox(frame_elements_inscription, font=(fonts.Texte_Fonts, 14), values=[])
    comboFiliere.place(x=175, y=260, width=300)
    comboFiliere.bind("<<ComboboxSelected>>", ajouts_informations.mise_a_jour_promotions)
    # ----------------------------------------->PROMOTION----------------------------------------
    lblPromotion = Label(frame_elements_inscription, text="PROMOTION", font=(fonts.Texte_Fonts, 14),
                         background=coloration.BG_Couleur3, foreground='white')
    lblPromotion.place(x=20, y=300)
    txtPromotion = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14),
                         foreground=coloration.BG_Couleur5)
    txtPromotion.place(x=150, y=300, width=200)
    comboPromotion = ttk.Combobox(frame_elements_inscription, font=(fonts.Texte_Fonts, 14),
                                  foreground=coloration.BG_Couleur5)
    comboPromotion.place(x=150, y=300, width=200)
    # ------------------->VACATION-------------------------------------------------------------
    lblVacation = Label(frame_elements_inscription, text="VACATION", font=(fonts.Texte_Fonts, 14),
                        background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblVacation.place(x=400, y=180)
    txtVacation = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14))
    txtVacation.place(x=510, y=180, width=150)
    listVacation = ["JOUR", "SOIR"]
    comboVacation = ttk.Combobox(frame_elements_inscription, font=(fonts.Texte_Fonts, 14), values=listVacation,
                                 foreground=coloration.BG_Couleur5)
    comboVacation.current(0)
    comboVacation.place(x=510, y=180, width=150)
    # ---------------------Annee Academique---------------------------------
    lblAcademiqueAnnee = Label(frame_elements_inscription, text="ANNEE ACADEMIQUE", font=(fonts.Texte_Fonts, 14),
                               background=coloration.BG_Couleur3, foreground=coloration.BG_Neutre)
    lblAcademiqueAnnee.place(x=480, y=260)
    txtAcademiqueAnnee = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14))
    txtAcademiqueAnnee.place(x=683, y=260, width=130)

    comboAcademqueAnnee = ttk.Combobox(frame_elements_inscription, font=(fonts.Texte_Fonts, 14),
                                       foreground=coloration.BG_Couleur5)
    # Définition de la liste annee académique
    annees_academiques = ajouts_informations.generer_annees_academiques()
    # Ajout des annee academique au combobox
    comboAcademqueAnnee['values'] = annees_academiques
    # Définition de l'annee academique
    comboAcademqueAnnee.set(annees_academiques)
    comboAcademqueAnnee.place(x=683, y=260, width=130)
    # --------------DATE---------------------------------
    Date = StringVar()
    today = date.today()
    date_systeme = today.strftime("%d/%m/%Y")
    Date.set(date_systeme)
    # --------------------------->PHOTO----------------------------------------------
    # Charger l’image à l’aide de PIL
    imageAvatar_path = "img/avatar.png"  # Le chemin de image
    imageAvatar = Image.open(imageAvatar_path)
    imageAvatar = imageAvatar.resize((160, 160))  # Redimensionner l’image si nécessaire
    photoAvatar = ImageTk.PhotoImage(imageAvatar)

    # Créer un label pour afficher l’image
    label_imageProfil = tk.Label(frame_child, image=photoAvatar, background=coloration.BG_Neutre)
    label_imageProfil.image = photoAvatar  # Garder une référence de l’image pour éviter qu’elle soit garbage collected
    label_imageProfil.pack(expand=True)

    btnParcourir_profil = tk.Button(frame_elements_inscription, text="Parcourir", background='white',
                                    foreground=coloration.BG_Couleur5, font=(fonts.Texte_Fonts, 14),
                                    command=ajouts_informations.parcourirImage)
    btnParcourir_profil.place(x=700, y=225, height=30)

    # -------------Boutton fonctionnements--------------------------------------------------------------
    lblRecherche = Label(frame_elements_inscription, text="Rechercher", font=(fonts.Texte_Fonts, 14),
                         background=coloration.BG_Couleur3, foreground='white')
    lblRecherche.place(x=20, y=340)

    txtRecherche = Entry(frame_elements_inscription, bd=2, font=(fonts.Texte_Fonts, 14),
                         foreground=coloration.BG_Couleur5)
    # txtRecherche.bind("<Return>", ajouts_informations.Recherche)
    txtRecherche.place(x=150, y=340, width=230)

    btnRecherche = tk.Button(frame_elements_inscription, text="Recherche", background='white',
                             foreground=coloration.BG_Couleur3, font=(fonts.Texte_Fonts, 14),
                             activeforeground=coloration.BG_Couleur5, command=ajouts_informations.Recherche)
    btnRecherche.place(x=400, y=340, height=30)

    btnEnregistre = tk.Button(frame_elements_inscription, text="ENREGISTER", background=coloration.BG_Neutre,
                              foreground=coloration.BG_Couleur3, font=(fonts.Texte_Fonts, 14),
                              activeforeground=coloration.BG_Couleur5, command=ajouts_informations.sauvegarde)
    btnEnregistre.place(x=500, y=300, height=30)

    btnAjouter = tk.Button(frame_elements_inscription, text="NETTOYER", background='white',
                           foreground=coloration.BG_Couleur3, font=(fonts.Texte_Fonts, 14),
                           activeforeground=coloration.BG_Couleur5, command=lambda: ajouts_informations.cls(True))
    btnAjouter.place(x=650, y=300, height=30)

    btnModifier = tk.Button(frame_elements_inscription, text="MODIFIER", background='white',
                            foreground=coloration.BG_Couleur3, font=(fonts.Texte_Fonts, 14),
                            activeforeground=coloration.BG_Couleur5, command=ajouts_informations.modificationEtudiant)
    btnModifier.place(x=530, y=340, height=30)

    btnSupprimer = tk.Button(frame_elements_inscription, text="SUPPRIMER", background=coloration.BG_Neutre,
                             foreground=coloration.BG_Couleur3, font=(fonts.Texte_Fonts, 14),
                             activeforeground=coloration.BG_Couleur5, command=ajouts_informations.supprimerEtudiants)
    btnSupprimer.place(x=650, y=340, height=30)

    # TreeVieuw
    # ----------------creation treeview-----------------------
    informations = ttk.Treeview(frame_treeview)
    informations.place(x=0, y=0, height=150, width=800)

    # ------scrollbars------------------
    ascenseurHorizontal = Scrollbar(frame_elements_inscription, orient=HORIZONTAL)
    ascenseurVertical = Scrollbar(frame_elements_inscription, orient=VERTICAL)
    ascenseurVertical.place(x=805, y=377, width=22, height=150)
    ascenseurHorizontal.place(x=7, y=528, width=800, height=22)

    informations.configure(yscrollcommand=ascenseurVertical.set, xscrollcommand=ascenseurHorizontal.set)
    informations.configure(selectmode="extended")
    # -------commandes ascenseurs-------------
    ascenseurHorizontal.configure(command=informations.xview)
    ascenseurVertical.configure(command=informations.yview)
    # --------definition treeview-------------------------------
    informations.configure(columns=(
        "ID", "MATRICULES", "NOMS", "POST-NOMS", "PRENOMS", "SEXES", "CODES PAYS", "NUM PHONES", "DOMAINES",
        "PROMOTIONS", "DEPARTEMENTS", "VACATIONS", "SYSTEMES", "DATES", "ANNEES"), selectmode="browse", show='headings',
        style='BW.Treeview')

    informations.heading("ID", text="ID", anchor=tk.CENTER)
    informations.heading("MATRICULES", text="MATRICULES", anchor=tk.CENTER)
    informations.heading("NOMS", text="NOMS", anchor=tk.CENTER)
    informations.heading("POST-NOMS", text="POST-NOMS", anchor=tk.CENTER)
    informations.heading("PRENOMS", text="PRENOMS", anchor=tk.CENTER)
    informations.heading("SEXES", text="SEXES", anchor=tk.CENTER)
    informations.heading("CODES PAYS", text="CODES PAYS", anchor=tk.CENTER)
    informations.heading("NUM PHONES", text="CONTACTS", anchor=tk.CENTER)
    informations.heading("DOMAINES", text="DOMAINES", anchor=tk.CENTER)
    informations.heading("PROMOTIONS", text="PROMOTIONS", anchor=tk.CENTER)
    informations.heading("DEPARTEMENTS", text="DEPARTEMENTS", anchor=tk.CENTER)
    informations.heading("VACATIONS", text="VACATIONS", anchor=tk.CENTER)
    informations.heading("SYSTEMES", text="SYSTEMES", anchor=tk.CENTER)
    informations.heading("DATES", text="DATES", anchor=tk.CENTER)
    informations.heading("ANNEES", text="ANNEES", anchor=tk.CENTER)

    informations.column("#0", width=0)
    informations.column("ID", minwidth=40, width=70, anchor=tk.CENTER)
    informations.column("MATRICULES", minwidth=50, width=80, anchor=tk.CENTER)
    informations.column("NOMS", minwidth=80, width=100, anchor=tk.CENTER)
    informations.column("POST-NOMS", minwidth=100, width=120, anchor=tk.CENTER)
    informations.column("PRENOMS", minwidth=70, width=90, anchor=tk.CENTER)
    informations.column("SEXES", minwidth=30, width=50, anchor=tk.CENTER)
    informations.column("CODES PAYS", minwidth=50, width=100, anchor=tk.CENTER)
    informations.column("NUM PHONES", minwidth=60, width=80, anchor=tk.CENTER)
    informations.column("DOMAINES", minwidth=120, width=300, anchor=tk.CENTER)
    informations.column("PROMOTIONS", minwidth=60, width=90, anchor=tk.CENTER)
    informations.column("DEPARTEMENTS", minwidth=120, width=150, anchor=tk.CENTER)
    informations.column("VACATIONS", minwidth=50, width=80, anchor=tk.CENTER)
    informations.column("SYSTEMES", minwidth=80, width=100, anchor=tk.CENTER)
    informations.column("DATES", minwidth=80, width=100, anchor=tk.CENTER)
    informations.column("ANNEES", minwidth=80, width=100, anchor=tk.CENTER)

    informations.bind("<ButtonRelease>", ajouts_informations.afficherDonnees)
    ajouts_informations.informationsEtudiants()


# ===========================================================FIN INSCRIPTION=============================================
# -----APPELLE CLASSE
principale = Acceuil()

# -------------Creation fenetre
home_fenetre = Tk()
# home_fenetre.geometry("1080x674+120+15")
center_window(home_fenetre, 1080, 674)
home_fenetre.resizable(False, False)
home_fenetre.title('RCSPC522')

homeImage = ImageTk.PhotoImage(file="img/home_img.png")
bgLabel = Label(home_fenetre, image=homeImage, background=coloration.BG_Couleur3)
bgLabel.place(x=0, y=0)
home_fenetre.iconbitmap('img/rfid.ico')

imageRFID = ImageTk.PhotoImage(file="img/rfid_image.png")
imageRFID1 = ImageTk.PhotoImage(file="img/rfid_image1.png")
bgRFID = Label(home_fenetre, image=imageRFID, background=coloration.BG_Couleur3)
bgRFID2 = Label(home_fenetre, image=imageRFID1, background=coloration.BG_Couleur3)
bgRFID.place(x=0, y=0, width=230, height=180)
bgRFID2.place(x=0, y=470, width=230, height=180)

frameGrandTitre = tk.Frame(home_fenetre, background=coloration.BG_Couleur3, width=835, height=50, borderwidth=1,
                           relief=tk.SOLID)
frameGrandTitre.place(x=235, y=10)

# --------------------Grand Titre--------------------------
entete_acceuil = Label(frameGrandTitre, text=" CONTROLE  DE  PAIEMENT  PAR CARTE RFID (RC522) ",
                       font=(fonts.Titre_Fonts, 22, 'bold'), background=coloration.BG_Couleur3, foreground='white')
entete_acceuil.place(x=10, y=0)

# ==============================BOUTONS MENUS=====================
btnComptabilite = Button(home_fenetre, text="COMPTABILITE", font=(fonts.Texte_Fonts, 15),
                         foreground=coloration.BG_Couleur3, border=1, background='white', activebackground='white',
                         activeforeground=coloration.BG_Couleur3, relief=tk.RIDGE, command=comptabilite)
btnComptabilite.place(x=20, y=200, width=200)

btnControles = Button(home_fenetre, text="CONTROLES", font=(fonts.Texte_Fonts, 15), foreground=coloration.BG_Couleur3,
                      border=1, background='white', activebackground='white', activeforeground=coloration.BG_Couleur3,
                      relief=tk.RIDGE, command=controles)
btnControles.place(x=20, y=250, width=200)

btnGestion = Button(home_fenetre, text="GESTION", font=(fonts.Texte_Fonts, 15), foreground=coloration.BG_Couleur3,
                    border=1, background='white', activebackground='white', activeforeground=coloration.BG_Couleur3,
                    relief=tk.RIDGE, command=gestion)
btnGestion.place(x=20, y=300, width=200)

btnInformation = Button(home_fenetre, text="INSCRIPTION", font=(fonts.Texte_Fonts, 15),
                        foreground=coloration.BG_Couleur3, border=1, background='white', activebackground='white',
                        activeforeground=coloration.BG_Couleur3, command=inscriptions, relief=tk.RIDGE)
btnInformation.place(x=20, y=350, width=200)

btnQuitter = Button(home_fenetre, text="QUITTER", font=(fonts.Texte_Fonts, 15), foreground=coloration.BG_Couleur3,
                    border=1, background='white', activebackground='white', activeforeground=coloration.BG_Couleur3,
                    relief=tk.RIDGE,
                    command=principale.quitter_fenetre)
btnQuitter.place(x=20, y=400, width=200)
# ============================================ FIN BOUTON MENU=============================

# Création de la barre de menus principale
barre_menus = tk.Menu(home_fenetre)
home_fenetre.config(menu=barre_menus)

# ------------------------------------- Menu Fichier---------------------------------------------
menu_fichier = tk.Menu(barre_menus, tearoff=0)
menu_fichier.add_command(label="Comptabilité Etudiants", command=principale.menu_fichier_comptabilite_action)
menu_fichier.add_command(label="Controles de payements", command=principale.menu_fichier_control_action)
menu_fichier.add_command(label="Gestions Comptable", command=principale.menu_fichier_gestion_action)
menu_fichier.add_separator()
menu_fichier.add_command(label="Inscription Etudiants", command=principale.menu_fichier_insctiption_action)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=principale.menu_fichier_quitter)
barre_menus.add_cascade(label="Fichier", menu=menu_fichier)
# ----------------------------------- Menu Aide--------------------------------------------
menu_apropos = tk.Menu(barre_menus, tearoff=0)
menu_apropos.add_command(label="Guide", command=principale.menu_guide_action)
menu_apropos.add_command(label="Information Logiciel")
barre_menus.add_cascade(label="A propos", menu=menu_apropos)

home_fenetre.protocol("WM_DELETE_WINDOW", principale.quitter_fenetre)
home_fenetre.mainloop()
