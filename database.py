import sqlite3

conn = sqlite3.connect("bizinsight.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    review TEXT,
    sentiment REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()


def insert_feedback_bulk(records):   
    try:
        cursor.executemany(
            "INSERT INTO feedback (review, sentiment) VALUES (?, ?)",
            records
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e


def fetch_feedback():
    cursor.execute("SELECT review, sentiment, created_at FROM feedback")
    return cursor.fetchall()



def clear_data():
    cursor.execute("DELETE FROM feedback")
    conn.commit()
