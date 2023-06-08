import requests
import sqlite3

def create_database_and_table():
    db_path = "e:/working code/random_users.db"
    print(f"Database path: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            dob TEXT,
            address TEXT
        )
    """)
    conn.commit()
    return conn


def main():
    try:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        address = input("Enter address: ")
        
        conn = create_database_and_table()
        print("Database created successfully.")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (first_name, last_name, email, phone, dob, address)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, email, phone, dob, address))
        conn.commit()
        print("User data inserted successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()



def add_random_users(conn, num_users):
    if num_users > 0:
        random_user = fetch_random_user()
        insert_random_user(conn, random_user)
        add_random_users(conn, num_users-1)

if __name__ == "__main__":
    main()
