import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect('helpdesk.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        issue TEXT,
        status TEXT
    )
''')

# Functions
def create_ticket(user, issue):
    cursor.execute("INSERT INTO tickets (user, issue, status) VALUES (?, ?, 'Open')", (user, issue))
    conn.commit()

def view_tickets():
    cursor.execute("SELECT * FROM tickets")
    data = cursor.fetchall()
    for row in data:
        print(row)

def update_ticket(ticket_id, status):
    cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (status, ticket_id))
    conn.commit()

def delete_ticket(ticket_id):
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    conn.commit()

# Sample run
create_ticket("Anish", "Can't connect to Wi-Fi")
view_tickets()
update_ticket(1, "Resolved")
view_tickets()
