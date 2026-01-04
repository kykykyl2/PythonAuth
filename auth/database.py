import sqlite3
import os

# Chemin vers la base de données
DB_FOLDER = "data"
DB_PATH = os.path.join(DB_FOLDER, "users.db")

def create_database():
    # Créer le dossier data s'il n'existe pas
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)

    # Connexion à SQLite (le fichier sera créé automatiquement)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Création de la table users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash BLOB NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print(f"Base de données créée avec succès à : {DB_PATH}")

# Exécuter la fonction si ce fichier est lancé directement
if __name__ == "__main__":
    create_database()
