# 📚 Course Management RESTful API
# تطبيق ويب متقدم ومكتمل لإدارة الدورات التدريبية:
# - استخدام FastAPI لإنشاء نقاط اتصال RESTful API.
# - استخدام SQLite كقاعدة بيانات دائمة لتخزين بيانات الدورات.
# - استخدام Pydantic للتحقق من صحة البيانات المدخلة (Data Validation).

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()
def get_db() :
    conn = sqlite3.connect("Course.db")
    conn.row_factory = sqlite3.Row
    return conn
conn = get_db()
conn.execute("CREATE TABLE IF NOT EXISTS courses(course_id TEXT PRIMARY KEY,name TEXT ,instructor TEXT,hours INTEGER,price INTEGER)")
conn.commit()
conn.close()
@app.get("/")
def home() :
    return {"message": " النظام شغال جربه/docs"}
class Course(BaseModel) :
    course_id: str
    name: str
    instructor: str
    hours: int
    price: int
@app.post("/add")
def add(course: Course) :
    conn = get_db()
    try:
        conn.execute("INSERT INTO courses(course_id,name,instructor,hours,price) VALUES (? ,? ,? ,? ,?)" ,(course.course_id,course.name,course.instructor,course.hours,course.price))
        conn.commit()
        return {"message": " تمت الاضافة"}
    except Exception as error:
        print(error)
        return {"message": " موجود مسبقا"}
    finally :
        conn.close()
@app.get("/all")
def show_all() :
    conn= get_db()
    rows = conn.execute("SELECT * FROM courses").fetchall()
    conn.close()
    return [dict(row) for row in rows]
@app.get("/search/{course_id}")
def search(course_id: str) :
    conn = get_db()
    row = conn.execute("SELECT * FROM courses WHERE course_id = ?", (course_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}
@app.delete("/delete/{course_id}")
def delete(course_id: str) :
    conn = get_db()
    cur = conn.execute("DELETE FROM courses WHERE course_id = ?", (course_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0 :
        return {"message": "تم الحذف"}
    return {"message": " لا يوجد"}
@app.put("/edit/name/{course_id}/{new_name}")
def edit_name(course_id: str, new_name: str) :
    conn = get_db()
    cur = conn.execute("UPDATE courses SET name =? WHERE course_id =?", (new_name,course_id))
    conn.commit()
    conn.close()
    if cur.rowcount > 0 :
        return {"message": " تم تعديل الاسم" }
    return {"message": "لا يوجد"}
@app.put("/hours/{course_id}")
def add_hours(course_id: str) :
    conn = get_db()
    conn.execute("UPDATE courses SET hours = hours + 5 WHERE course_id = ?", (course_id,))
    conn.commit()
    row = conn.execute("SELECT hours FROM courses WHERE course_id = ?", (course_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f" عدد الساعات اصبح يساوي {row['hours']}"}
    return {"message": " لا يوجد"}
