import mysql.connector


def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="95264637",
            database="contact_book"
        )
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    conn = create_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO contacts (name, phone, email) VALUES (%s,%s,%s)",
                (name, phone, email)
            )
        conn.commit()
        print("Contact added successfully.")
    except mysql.connector.IntegrityError:
        print("Duplicate phone or email not allowed.")
    except mysql.connector.Error as e:
        print("Error:", e)
    finally:
        conn.close()

def view_contacts():
    conn = create_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM contacts ORDER BY name")
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
            else:
                print("No contacts found.")
    except mysql.connector.Error as e:
        print("Error:", e)
    finally:
        conn.close()

def search_contact():
    keyword = input("Search: ")
    conn = create_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM contacts WHERE name LIKE %s OR phone LIKE %s OR email LIKE %s",
                (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
            )
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
            else:
                print("No match found.")
    except mysql.connector.Error as e:
        print("Error:", e)
    finally:
        conn.close()

def update_contact():
    try:
        cid = int(input("ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return
    phone = input("New Phone: ")
    email = input("New Email: ")
    conn = create_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE contacts SET phone=%s, email=%s WHERE id=%s",
                (phone, email, cid)
            )
        conn.commit()
        print("Contact updated.")
    except mysql.connector.Error as e:
        print("Error:", e)
    finally:
        conn.close()

def delete_contact():
    try:
        cid = int(input("ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    conn = create_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM contacts WHERE id=%s", (cid,))
        conn.commit()
        print("Contact deleted.")
    except mysql.connector.Error as e:
        print("Error:", e)
    finally:
        conn.close()

def main():
    while True:
        print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


