"""
نظام إدارة الموارد البشرية باستخدام FastAPI وقاعدة بيانات SQLite
وصف النظام: تطبيق خلفي (Backend API) لإدارة الموظفين، الأقسام، والرواتب.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("System.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db()
conn.execute("CREATE TABLE IF NOT EXISTS employees(employee_id TEXT PRIMARY KEY, name TEXT, department TEXT, salary INTEGER)")
conn.commit()
conn.close()

@app.get("/")
def home():
    return {"message": "النظام شغال جربه/docs"}

class Employee(BaseModel):
    employee_id: str
    name: str
    department: str
    salary: int

@app.post("/add")
def add_employee(employee: Employee):
    conn = get_db()
    try:
        conn.execute("INSERT INTO employees (employee_id, name, department, salary) VALUES (?, ?, ?, ?)", 
                     (employee.employee_id, employee.name, employee.department, employee.salary))
        conn.commit()
        return {"message": "تمت الاضافة"}
    except:
        return {"message": "موجود مسبقا"}
    finally:
        conn.close()

@app.get("/all")
def show_all():
    conn = get_db()
    rows = conn.execute("SELECT * FROM employees").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/search/{employee_id}")
def search(employee_id: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}

@app.delete("/delete/{employee_id}")
def delete(employee_id: str):
    conn = get_db()
    cur = conn.execute("DELETE FROM employees WHERE employee_id = ?", (employee_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم الحذف"}
    return {"message": "لا يوجد"}

@app.put("/edit/department/{employee_id}/{new_department}")
def edit_department(employee_id: str, new_department: str):
    conn = get_db()
    cur = conn.execute("UPDATE employees SET department = ? WHERE employee_id = ?", (new_department, employee_id))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم تعديل القسم"}
    return {"message": "لا يوجد"}

@app.put("/salary/{employee_id}")
def add_salary(employee_id: str):
    conn = get_db()
    conn.execute("UPDATE employees SET salary = salary + 3000 WHERE employee_id = ?", (employee_id,))
    conn.commit()
    row = conn.execute("SELECT salary FROM employees WHERE employee_id = ?", (employee_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"الراتب اصبح يساوي {row['salary']}"}
    return {"message": "لا يوجد"}
