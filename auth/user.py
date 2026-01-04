import sqlite3
from .database import DB_PATH
from .security import hash_password, verify_password


def create_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Logic to create a new user
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        print("Erreur : ce nom d'utilisateur existe déjà.")
        print(result)
        conn.close()
        return

    password_hash = hash_password(password)
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, password_hash)
    )

    conn.commit()
    conn.close()
    print(f"User {username} created.")

def authenticate_user(username, password):
    # Logic to authenticate a user
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if not result:
        print("Utilisateur inconnu.")
        conn.close()
        return False

    stored_hash = result[0]

    if verify_password(password, stored_hash):
        conn.close()
    else:
        print("Mot de passe incorrect.")
        conn.close()
        return False

    print(f"User {username} authenticated.")
    return True


def delete_account(username, password):
    # Logic to delete a user account
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if not result:
        print("Utilisateur inconnu.")
        conn.close()
        return False

    stored_hash = result[0]
    if not verify_password(password, stored_hash):
        print("Mot de passe incorrect.")
        conn.close()
        return False
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    conn.close()
    print(f"User {username} deleted.")