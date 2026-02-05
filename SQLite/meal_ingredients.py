import sqlite3

def main():
    conn = sqlite3.connect('meal_planner', isolation_level=None)
    cursor = conn.cursor()

    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT')
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS igredients (name TEXT,
                meal_id INTEGER,
                FOREIGN KEY(meal_id) REFERENCES meals
                (rowid)
            ) STRICT
        """)
    except sqlite3.OperationalError as e:
        print(f"Database error: {e}")
        return
