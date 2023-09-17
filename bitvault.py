import os
import shutil
import datetime
import nacl.pwhash
import nacl.utils
from pysqlcipher3 import dbapi2 as sqlite

DATABASE_NAME = 'password_manager.db'
DATABASE_PASSPHRASE = 'secure_passphrase'
BACKUP_DIRECTORY = 'backups/'


class PasswordManagerError(Exception):
    pass


class PasswordManager:
    def __init__(self):
        self.conn = self._connect_db()
        self._create_tables()

    def _connect_db(self):
        conn = sqlite.connect(DATABASE_NAME)
        conn.execute(f"PRAGMA key = '{DATABASE_PASSPHRASE}'")
        return conn

    def _create_tables(self):
        with self.conn:
            self.conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                hashed_password TEXT NOT NULL
            )
            ''')

    def add_password(self, username, password):
        if self._get_hashed_password(username):
            raise PasswordManagerError("Error processing request.")
        
        salt = nacl.utils.random(nacl.pwhash.argon2i.SALTBYTES)
        hashed_pw = nacl.pwhash.argon2i.str(password.encode('utf-8'), salt)
        
        with self.conn:
            self.conn.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_pw))

    def verify_password(self, username, password):
        hashed_pw = self._get_hashed_password(username)
        if not hashed_pw:
            raise PasswordManagerError("Error processing request.")
        
        try:
            nacl.pwhash.verify(hashed_pw, password.encode('utf-8'))
            return True
        except nacl.exceptions.CryptoError:
            return False

    def change_password(self, username, old_password, new_password):
        if not self.verify_password(username, old_password):
            raise PasswordManagerError("Error processing request.")
        
        salt = nacl.utils.random(nacl.pwhash.argon2i.SALTBYTES)
        hashed_pw = nacl.pwhash.argon2i.str(new_password.encode('utf-8'), salt)
        
        with self.conn:
            self.conn.execute("UPDATE users SET hashed_password = ? WHERE username = ?", (hashed_pw, username))

    def delete_account(self, username, password):
        if not self.verify_password(username, password):
            raise PasswordManagerError("Error processing request.")
        
        with self.conn:
            self.conn.execute("DELETE FROM users WHERE username = ?", (username,))

    def _get_hashed_password(self, username):
        cursor = self.conn.execute("SELECT hashed_password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return row[0] if row else None

    def backup_database(self):
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f"{BACKUP_DIRECTORY}backup_{timestamp}.db"
        
        if not os.path.exists(BACKUP_DIRECTORY):
            os.makedirs(BACKUP_DIRECTORY)
        
        shutil.copy2(DATABASE_NAME, backup_filename)
        print(f"Backup created at {backup_filename}!")

    def restore_database(self, backup_path):
        if not os.path.exists(backup_path):
            raise PasswordManagerError("Backup file does not exist!")
        
        shutil.copy2(backup_path, DATABASE_NAME)
        print("Database restored from backup!")


def main():
    pm = PasswordManager()

    while True:
        print("\nBitVault Password Manager Beta")
        print("1. Add Password")
        print("2. Verify Password")
        print("3. Change Password")
        print("4. Delete Account")
        print("5. Backup Database")
        print("6. Restore Database")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                pm.add_password(username, password)
                print("Password added successfully!")
            except PasswordManagerError:
                print("Error processing request.")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if pm.verify_password(username, password):
                print("Password is correct!")
            else:
                print("Password is incorrect!")

        elif choice == "3":
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            try:
                pm.change_password(username, old_password, new_password)
                print("Password changed successfully!")
            except PasswordManagerError:
                print("Error processing request.")

        elif choice == "4":
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                pm.delete_account(username, password)
                print("Account deleted successfully!")
            except PasswordManagerError:
                print("Error processing request.")

        elif choice == "5":
            pm.backup_database()

        elif choice == "6":
            backup_path = input("Enter the path to the backup file: ")
            try:
                pm.restore_database(backup_path)
            except PasswordManagerError as e:
                print(e)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()