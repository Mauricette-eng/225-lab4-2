import sqlite3

DATABASE = '/nfs/demo.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def generate_test_data(num_songs):
    """Generate test data for the songs table."""
    db = connect_db()
    cursor = db.cursor()

    # Make sure the table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            album TEXT,
            year TEXT
        );
    """)

    # Insert test data
    for i in range(num_songs):
        title = f"Test Song {i}"
        artist = f"Test Artist {i}"
        album = f"Test Album {i}"
        year = f"200{i}"

        cursor.execute(
            "INSERT INTO songs (title, artist, album, year) VALUES (?, ?, ?, ?)",
            (title, artist, album, year)
        )

    db.commit()
    print(f"{num_songs} test songs added.")
    db.close()

if __name__ == "__main__":
    generate_test_data(10)
