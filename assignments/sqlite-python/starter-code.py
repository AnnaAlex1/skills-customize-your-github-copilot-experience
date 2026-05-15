import sqlite3
import csv
from typing import List, Dict, Any

DB_PATH = "sample.db"


def get_connection(db_path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str = DB_PATH, schema_file: str = "schema.sql") -> None:
    conn = get_connection(db_path)
    try:
        with open(schema_file, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
    except FileNotFoundError:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            );
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                credits INTEGER
            );
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id)
            );
            """
        )
    conn.commit()
    conn.close()


# Student CRUD

def create_student(name: str, age: int, db_path: str = DB_PATH) -> int:
    conn = get_connection(db_path)
    cur = conn.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    student_id = cur.lastrowid
    conn.close()
    return student_id


def get_student(student_id: int, db_path: str = DB_PATH) -> Dict[str, Any]:
    conn = get_connection(db_path)
    cur = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def update_student(student_id: int, name: str = None, age: int = None, db_path: str = DB_PATH) -> bool:
    conn = get_connection(db_path)
    cur = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if cur.fetchone() is None:
        conn.close()
        return False
    if name is not None:
        conn.execute("UPDATE students SET name = ? WHERE id = ?", (name, student_id))
    if age is not None:
        conn.execute("UPDATE students SET age = ? WHERE id = ?", (age, student_id))
    conn.commit()
    conn.close()
    return True


def delete_student(student_id: int, db_path: str = DB_PATH) -> bool:
    conn = get_connection(db_path)
    cur = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    changed = cur.rowcount > 0
    conn.close()
    return changed


# Course CRUD

def create_course(title: str, credits: int, db_path: str = DB_PATH) -> int:
    conn = get_connection(db_path)
    cur = conn.execute("INSERT INTO courses (title, credits) VALUES (?, ?)", (title, credits))
    conn.commit()
    course_id = cur.lastrowid
    conn.close()
    return course_id


def list_student_courses(student_id: int, db_path: str = DB_PATH) -> List[Dict[str, Any]]:
    conn = get_connection(db_path)
    cur = conn.execute(
        """
        SELECT courses.* FROM courses
        JOIN enrollments ON courses.id = enrollments.course_id
        WHERE enrollments.student_id = ?
        """,
        (student_id,)
    )
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


# Utilities

def export_to_csv(query: str, csv_path: str, db_path: str = DB_PATH) -> None:
    conn = get_connection(db_path)
    cur = conn.execute(query)
    rows = cur.fetchall()
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(rows[0].keys() if rows else [])
        for r in rows:
            writer.writerow(list(r))
    conn.close()


def backup_db(backup_path: str, db_path: str = DB_PATH) -> None:
    conn = get_connection(db_path)
    with open(backup_path, "w", encoding="utf-8") as f:
        for line in conn.iterdump():
            f.write(f"{line}\n")
    conn.close()


# Demo usage

if __name__ == "__main__":
    init_db()
    # Create sample data
    sid = create_student("Alice", 20)
    cid = create_course("Intro to Databases", 3)
    # Enroll student
    conn = get_connection()
    conn.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (sid, cid))
    conn.commit()
    conn.close()

    print("Student created:", get_student(sid))
    print("Student courses:", list_student_courses(sid))
    export_to_csv("SELECT * FROM students", "students_export.csv")
    backup_db("backup.sql")
