# phonebook.py
import csv
from connect import connect

# ---------------- CREATE TABLE ----------------
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# ---------------- INSERT FROM CONSOLE ----------------
def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

# ---------------- INSERT FROM CSV ----------------
def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for name, phone in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Contacts from CSV inserted successfully!")

# ---------------- SHOW ALL ----------------
def show_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found.")
    cur.close()
    conn.close()

# ---------------- SEARCH ----------------
def search(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No matching contacts found.")
    cur.close()
    conn.close()

# ---------------- UPDATE ----------------
def update(name, new_phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))
    if cur.rowcount == 0:
        print("No contact found to update.")
    else:
        print("Contact updated successfully.")
    conn.commit()
    cur.close()
    conn.close()

# ---------------- DELETE ----------------
def delete(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    if cur.rowcount == 0:
        print("No contact found to delete.")
    else:
        print("Contact deleted successfully.")
    conn.commit()
    cur.close()
    conn.close()

# ---------------- MENU ----------------
def main():
    create_table()  # создаём таблицу при старте

    while True:
        print("\nPHONEBOOK MENU")
        print("1 - Add from CSV")
        print("2 - Add manually")
        print("3 - Show all")
        print("4 - Search by name")
        print("5 - Update phone")
        print("6 - Delete contact")
        print("0 - Exit")
        choice = input("Choose: ")

        if choice == "1":
            file_path = input("Enter CSV file path: ")
            insert_from_csv(file_path)
        elif choice == "2":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)
            print("Contact added successfully.")
        elif choice == "3":
            show_all()
        elif choice == "4":
            name = input("Search by name: ")
            search(name)
        elif choice == "5":
            name = input("Name to update: ")
            new_phone = input("New phone: ")
            update(name, new_phone)
        elif choice == "6":
            name = input("Name to delete: ")
            delete(name)
        elif choice == "0":
            print("Exiting PhoneBook.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
