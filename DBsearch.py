import sqlite3

def search_users(conn, query):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users
        WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR phone LIKE ? OR dob LIKE ? OR address LIKE ?
    """, (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%","%{query}%", f"%{query}%"))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No results found.")
    else:
        print(f"Found {len(rows)} results:")
        for row in rows:
            print(f"{row[1]} {row[2]} ({row[3]}) - {row[6]}")

def display_all_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No users found.")
    else:
        print(f"Found {len(rows)} users:")
        for row in rows:
            print(f"{row[1]} {row[2]} ({row[3]}) - {row[6]}")

def main():
    conn = sqlite3.connect("e:/working code/random_users.db")
    while True:
        print("1. Search users")
        print("2. Display all users")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            query = input("Enter your search query: ")
            search_users(conn, query)
        elif choice == "2":
            display_all_users(conn)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
