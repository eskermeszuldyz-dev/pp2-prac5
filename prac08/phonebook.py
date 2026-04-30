# phonebook_interface.py
from connect import get_connection

def pattern_search(pattern):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
            return cur.fetchall()

def paginate(limit, offset):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            return cur.fetchall()

def upsert(name, surname, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s, %s)", (name, surname, phone))
            conn.commit()

def bulk_upsert(names, surnames, phones):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL bulk_upsert_contacts(%s, %s, %s)", (names, surnames, phones))
            conn.commit()

def delete_contact(name=None, phone=None):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact(%s, %s)", (name, phone))
            conn.commit()

# ------------------ Interface ------------------ #
def main_menu():
    while True:
        print("\n=== PhoneBook Menu ===")
        print("1. Search contacts by pattern")
        print("2. View contacts with pagination")
        print("3. Add/Update contact")
        print("4. Bulk insert contacts")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Select an action: ")

        if choice == "1":
            pattern = input("Enter name, surname, or phone: ")
            results = pattern_search(pattern)
            if results:
                for r in results:
                    print(f"{r[0]} {r[1]} - {r[2]}")
            else:
                print("No contacts found.")

        elif choice == "2":
            limit = int(input("How many contacts to show: "))
            offset = int(input("How many contacts to skip: "))
            results = paginate(limit, offset)
            for r in results:
                print(f"{r[0]} {r[1]} - {r[2]}")

        elif choice == "3":
            name = input("First Name: ")
            surname = input("Last Name: ")
            phone = input("Phone (XXX-XXX-XXXX): ")
            upsert(name, surname, phone)
            print("Contact added/updated.")

        elif choice == "4":
            n = int(input("How many contacts to add: "))
            names, surnames, phones = [], [], []
            for i in range(n):
                names.append(input(f"{i+1}. First Name: "))
                surnames.append(input(f"{i+1}. Last Name: "))
                phones.append(input(f"{i+1}. Phone: "))
            bulk_upsert(names, surnames, phones)
            print("Bulk insert completed.")

        elif choice == "5":
            name = input("Name to delete (leave empty to delete by phone): ").strip()
            phone = input("Phone to delete (leave empty to delete by name): ").strip()
            delete_contact(name=name if name else None, phone=phone if phone else None)
            print("Contact deleted if it existed.")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

# ------------------ Run ------------------ #
if __name__ == "__main__":
    main_menu()