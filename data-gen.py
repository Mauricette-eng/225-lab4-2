import sqlite3

DATABASE = '/nfs/demo.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def generate_test_data(num_songs):
    """Insert test songs into the songs table."""
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL
        );
    """)

    for i in range(num_songs):
        title = f"Test Song {i}"
        artist = f"Test Artist {i}"
        cursor.execute(
            "INSERT INTO songs (title, artist) VALUES (?, ?)",
            (title, artist)
        )

    db.commit()
    db.close()
    print(f"{num_songs} test songs added.")

if __name__ == "__main__":
    generate_test_data(10)
