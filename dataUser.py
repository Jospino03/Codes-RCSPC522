import sqlite3


def testConnexion():
    connectionDB = sqlite3.connect("databases/adminregistration.db")
    curseur = connectionDB.cursor()


def creation_table_utilisateur():
    connectionDB = sqlite3.connect("databases/adminregistration.db")
    curseur = connectionDB.cursor()

    curseur.execute("CREATE TABLE Login("
                    "Id INTEGER NOT NULL UNIQUE, "
                    "Admin VARCHAR(30) NOT NULL UNIQUE, "
                    "Password VARCHAR(10) NOT NULL,"
                    "PRIMARY KEY(Id AUTOINCREMENT));")

    connectionDB.commit()
    connectionDB.close()


def insertion_administrateur(username, password):
    connectionDB = sqlite3.connect("databases/adminregistration.db")
    curseur = connectionDB.cursor()

    curseur.execute("INSERT INTO Login(Admin, Password) VALUES(?,?)", [username, password])
    connectionDB.commit()
    connectionDB.close()
