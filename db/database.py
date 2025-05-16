import sqlite3
from models.account import Account
import os
from Security.Encryptor import Encryptor



encryptor = Encryptor()

def connect():
    project_dir = os.getcwd()
    db_path = os.path.join(project_dir, "accounts.db")
    return sqlite3.connect(db_path)

def create_table():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            whatfor TEXT NOT NULL,
            name TEXT,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            comment TEXT
        )
    """)
    connection.commit()
    connection.close()

def create_account(whatfor,name,email,password,comment):
    encrypted_password = encryptor.encrypt_password(password)  
    connection = connect()
    cursor = connection.cursor()
    cursor.execute ("""
        INSERT INTO accounts (whatfor, name, email, password, comment) 
        values (?,?,?,?,?)
    """, (whatfor,name,email,encrypted_password,comment))

    connection.commit()
    connection.close()

def get_accounts():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    connection.close()
    accounts = [Account(id,whatfor,name,email,encryptor.decrypt_password(password),comment) for id, whatfor, name,email,password,comment in accounts]

    return accounts

def get_account_by_id(id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE id = ? ", (id,))
    account_db = cursor.fetchone()
    connection.close()
    if account_db:
        return Account(*account_db)
    return None


def update_account(id,name,email,password,comment):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE accounts
        SET name = ?, email = ?, password = ?, comment = ?
        WHERE id = ?
    """, (name,email,password,id,comment))
    connection.commit()
    connection.close()

def delete_account(id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM accounts WHERE id = ?",(id,))
    connection.commit()
    connection.close()