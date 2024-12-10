from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect("university.db")
    conn.row_factory = sqlite3.Row
    return conn

# Route: Home (Advisor Dashboard)
@app.route("/")
def index():
    return render_template("index.html")

# Route: View All Students
@app.route("/students")
def view_students():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("students.html", students=students)

# Route: View All Courses
@app.route("/courses")
def view_courses():
    conn = get_db_connection()
    courses = conn.execute("SELECT * FROM courses").fetchall()
    conn.close()
    return render_template("courses.html", courses=courses)

# Route: Add a New Course
@app.route("/add_course", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        course_ids = request.form.getlist("course_id[]")
        names = request.form.getlist("name[]")
        categories = request.form.getlist("category[]")

        conn = get_db_connection()
        for course_id, name, category in zip(course_ids, names, categories):
            try:
                conn.execute("INSERT INTO courses (course_id, name, category) VALUES (?, ?, ?)",
                             (course_id, name, category))
            except sqlite3.IntegrityError:
                print(f"Course ID {course_id} already exists.")
        conn.commit()
        conn.close()
        return redirect(url_for("view_courses"))
    return render_template("add_course.html")


# Route: Delete a Course
@app.route("/delete_course/<course_id>", methods=["POST"])
def delete_course(course_id):
    conn = get_db_connection()
    try:
        # Delete the course from the 'courses' table
        conn.execute("DELETE FROM courses WHERE course_id = ?", (course_id,))
        conn.commit()
        print(f"Course {course_id} deleted successfully.")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}")
    conn.close()
    return redirect(url_for("view_courses"))


# Route: View All Registrations
@app.route("/registrations")
def view_registrations():
    conn = get_db_connection()
    registrations = conn.execute("SELECT * FROM registrations").fetchall()
    conn.close()
    return render_template("registrations.html", registrations=registrations)

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
