import sqlite3


def testConnexion():
    connectionDB = sqlite3.connect("databases/studentsRegistration.db")
    curseur = connectionDB.cursor()


def creation_table_regitre_etudiants():
    connectionDB = sqlite3.connect("databases/studentsRegistration.db")
    curseur = connectionDB.cursor()
    requetteCreationTable_Registre_etudiant = """CREATE TABLE IF NOT EXISTS registre_etudiant (
                                   Id INTEGER  NOT NULL UNIQUE ,
                                   Matricules TEXT UNIQUE,
                                   Noms VARCHAR(50) NOT NULL,
                                   PostNoms VARCHAR(70) NOT NULL,
                                   PreNoms VARCHAR(50),
                                   Sexes CHAR(1),
                                   CodesPays CHAR(5),
                                   NumerosTel CHAR(10),
                                   Domaines CHAR(50),
                                   Promotions CHAR(50),
                                   Departements VARCHAR(50),
                                   Vacations CHAR(4),
                                   Systeme CHAR(3),
                                   DatesInscriptions VARCHAR(10),
                                   AnneesAcademiques VARCHAR(9),
                                   PRIMARY KEY("Id","Matricules"))"""
    curseur.execute(requetteCreationTable_Registre_etudiant)
    connectionDB.commit()
    connectionDB.close()


def insertion_DataEtudiants(identifiant, matricule, nom, postnom, prenom, sexe, codePays, num_tel, domaine, promotion,
                            departement, vacation, systeme, date_enregistrement, annee_academiques):
    connectionDB = sqlite3.connect("databases/studentsRegistration.db")
    curseur = connectionDB.cursor()
    requetteinsertion_DataEtudiants = """INSERT INTO registre_etudiant (
                                Id,
                                Matricules,
                                Noms,
                                PostNoms,
                                PreNoms,
                                Sexes,
                                CodesPays,
                                NumerosTel,
                                Domaines,
                                Promotions,
                                Departements,
                                Vacations,
                                Systeme,
                                DatesInscriptions,
                                AnneesAcademiques) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    curseur.execute(requetteinsertion_DataEtudiants,
                    [identifiant, matricule, nom, postnom, prenom, sexe, codePays, num_tel, domaine, promotion,
                     departement, vacation, systeme, date_enregistrement, annee_academiques])
    connectionDB.commit()
    connectionDB.close()


def fetch_Etudiants():
    connectionDB = sqlite3.connect("databases/studentsRegistration.db")
    curseur = connectionDB.cursor()
    informationEtudiants = curseur.execute("SELECT * FROM  registre_etudiant")
    etudiants = curseur.fetchall()
    curseur.close()
    return etudiants


def supprimerEtudiants(identifiant, matricule):
    connectionDB = sqlite3.connect("databases/studentsRegistration.db")
    curseur = connectionDB.cursor()
    curseur.execute("DELETE FROM  registre_etudiant  WHERE Id=? AND Matricules=?", (identifiant, matricule))
    connectionDB.commit()
    connectionDB.close()


def mise_a_jourEtudinat(N_identifiant, N_nom, N_postnom, N_prenom, N_sexe, N_codePays, N_num_tel, N_domaine,
                        N_promotion, N_departement, N_vacation, N_systeme, N_date_enregistrement, N_annee_academiques):
    connectionDB = sqlite3.connect("databases/studentsRegistration.db")
    curseur = connectionDB.cursor()
    requetteAjoutEtudiants = """UPDATE  registre_etudiant SET
                                Id=?,
                                Noms=?,
                                PostNoms=?,
                                PreNoms=?,
                                Sexes=?,
                                CodesPays=?,
                                NumerosTel=?,
                                Domaines=?,
                                Promotions=?,
                                Departements=?,
                                Vacations=?,
                                Systeme=?,
                                DatesInscriptions=?,
                                AnneesAcademiques=?"""
    curseur.execute(requetteAjoutEtudiants,
                    (N_identifiant, N_nom, N_postnom, N_prenom, N_sexe, N_codePays, N_num_tel, N_domaine, N_promotion,
                     N_departement, N_vacation, N_systeme, N_date_enregistrement, N_annee_academiques))
    connectionDB.commit()
    connectionDB.close()


def identifiant_exists(identifiant, matricule):
    connectionDB = sqlite3.connect("databases/studentsRegistration.db")
    curseur = connectionDB.cursor()
    curseur.execute("SELECT COUNT (*) FROM  registre_etudiant WHERE Id=? and Matricules =?", (identifiant, matricule))
    resultat = curseur.fetchone()
    connectionDB.close()
    return resultat[0] > 0


def fetch_all_ids():
    connectionDB = sqlite3.connect("databases/studentsRegistration.db")
    curseur = connectionDB.cursor()
    curseur.execute("SELECT Id FROM  registre_etudiant")
    ids = curseur.fetchall()
    connectionDB.close()
    return [i[0] for i in ids]


def fetch_all_matricules():
    connectionDB = sqlite3.connect("databases/studentsRegistration.db")
    curseur = connectionDB.cursor()
    curseur.execute("SELECT Matricules FROM  registre_etudiant")
    matri = curseur.fetchall()
    connectionDB.close()
    return [i[0] for i in matri]
