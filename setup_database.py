import sqlite3

def setup_database():
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL CHECK(category IN ('A1', 'A2', 'A3', 'A4', 'A5', 'Elective','Mandatory'))
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            student_id INTEGER NOT NULL,
            student_name TEXT NOT NULL,
            course_id TEXT NOT NULL,
            semester TEXT NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(course_id) REFERENCES courses(course_id)
        )
    """)
    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
