import sqlite3

# Function to add a student
def add_student(student_id, name):
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (student_id, name) VALUES (?, ?)", (student_id, name))
        conn.commit()
        print(f"Student {name} added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}. Student ID {student_id} already exists.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        conn.close()

# Function to add a course
def add_course(course_id, name, category):
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (course_id, name, category) VALUES (?, ?, ?)", (course_id, name, category))
        conn.commit()
        print(f"Course {course_id} - {name} added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Course ID {course_id} already exists.")
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
    conn.close()

if __name__ == "__main__":
    print("Adding courses...")
    add_course("CDS DS 701", "Tools for Data Science", "Mandatory")
    add_course("CAS MA 575", "Linear Models", "A1")
    add_course("CAS MA 576", "Generalized Linear Models", "A1")
    add_course("CDS DS 522", "Stochastic Methods for Algorithms", "A2")
    add_course("CDS DS 542", "Deep Learning for Data Science", "A3")
    print("Courses added. Check the database.")

    print('Adding Students...')
    add_student('U53450247','Xiang Li')
    add_student('U12345668', 'Chenjia Li')
    add_student('U12895668', 'Hanfei Qi')
    print('Students added', 'Check the datebase')
