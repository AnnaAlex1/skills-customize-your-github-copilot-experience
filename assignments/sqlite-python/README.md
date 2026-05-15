# 📘 Assignment: Introduction to Databases with SQLite and Python

## 🎯 Objective

Teach students how to design a simple relational schema, interact with an SQLite database from Python, and perform basic CRUD operations and queries safely using parameterized SQL.

## 📝 Tasks

### 🛠️ Design a database schema

#### Description
Design a small relational schema for a school system that includes `students`, `courses`, and `enrollments` tables.

#### Requirements
Completed work should:

- Provide a `schema.sql` file containing CREATE TABLE statements for `students`, `courses`, and `enrollments`.
- Use primary keys, appropriate column types, and foreign keys where appropriate.
- Include sample INSERT statements to populate the database with a few rows.

### 🛠️ Implement CRUD operations in Python

#### Description
Write Python functions that connect to an SQLite database and perform Create, Read, Update, and Delete operations for `students` and `courses`.

#### Requirements
Completed program should:

- Provide a `starter-code.py` with helper functions: `init_db()`, `create_student()`, `get_student()`, `update_student()`, `delete_student()` (and equivalent for courses).
- Use `sqlite3` from the Python standard library with `row_factory` set to return rows as dictionaries or named tuples.
- Use parameterized queries to avoid SQL injection.
- Include example usage in a `main` block demonstrating each operation.

### 🛠️ Querying and joins

#### Description
Write queries that demonstrate selecting data with joins, for example listing students with their enrolled courses.

#### Requirements
Completed program should:

- Include a function `list_student_courses(student_id)` that returns a list of courses for the given student using a JOIN.
- Demonstrate the function with sample output in the `main` block.

### 🛠️ Optional: Export and backup

#### Description
Add a small utility to export query results to CSV and to create a SQL dump of the database.

#### Requirements
Completed program should:

- Provide a `export_to_csv(filename)` function that writes selected rows to a CSV file.
- Provide a `backup_db(backup_path)` function that copies the SQLite file or uses `iterdump()`.

---

### Delivery and assessment

- Students should submit the `README.md`, `starter-code.py`, and `schema.sql` files in the `assignments/sqlite-python/` folder.
- Grading rubric: schema correctness (30%), working CRUD functions (40%), use of parameterized queries (20%), demonstration and documentation (10%).
