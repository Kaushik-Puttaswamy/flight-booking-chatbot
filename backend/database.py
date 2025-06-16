import sqlite3

def save_booking(origin, destination, date):
    conn = sqlite3.connect("flights.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        origin TEXT,
        destination TEXT,
        date TEXT
    )''')
    c.execute("INSERT INTO bookings (origin, destination, date) VALUES (?, ?, ?)",
              (origin, destination, date))
    conn.commit()
    conn.close()