"""
نظام إدارة السجون باستخدام FastAPI وقاعدة بيانات SQLite - Advanced FastAPI Prison API

تطبيق ويب متقدم ومكتمل:
- استخدام FastAPI لإنشاء نقاط اتصال RESTful API.
- استخدام SQLite كقاعدة بيانات دائمة لتخزين بيانات السجناء.
- استخدام Pydantic للتحقق من صحة البيانات المدخلة (Data Validation).
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Prison Management API", version="2.0")

def get_db():
    conn = sqlite3.connect("Prison.db")
    conn.row_factory = sqlite3.Row
    return conn

# تهيئة جدول قاعدة البيانات عند تشغيل التطبيق
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS prisoners(
            prisoner_id TEXT PRIMARY KEY,
            name TEXT,
            cell TEXT,
            crime TEXT,
            date TEXT,
            Fine INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def home():
    return {"message": "النظام شغال بنجاح، جرب الدخول إلى /docs لاختبار الـ APIs"}

class Prison(BaseModel):
    prisoner_id: str
    name: str
    cell: str
    crime: str
    date: str
    Fine: int

class PrisonUpdate(BaseModel):
    name: str
    cell: str
    crime: str
    date: str
    Fine: int

@app.post("/add")
def add_prisoner(person: Prison):
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO prisoners (prisoner_id, name, cell, crime, date, Fine) VALUES (?, ?, ?, ?, ?, ?)",
            (person.prisoner_id, person.name, person.cell, person.crime, person.date, person.Fine)
        )
        conn.commit()
        return {"message": "تمت اضافة السجين بنجاح"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="رقم السجين موجود مسبقاً")
    finally:
        conn.close()

@app.get("/all")
def show_all_prisoners():
    conn = get_db()
    rows = conn.execute("SELECT * FROM prisoners").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/search/{prisoner_id}")
def search_prisoner(prisoner_id: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM prisoners WHERE prisoner_id = ?", (prisoner_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    raise HTTPException(status_code=404, detail="السجين غير موجود")

@app.delete("/delete/{prisoner_id}")
def delete_prisoner(prisoner_id: str):
    conn = get_db()
    cur = conn.execute("DELETE FROM prisoners WHERE prisoner_id = ?", (prisoner_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم حذف السجين بنجاح"}
    raise HTTPException(status_code=404, detail="السجين غير موجود")

@app.put("/edit/{prisoner_id}")
def edit_prisoner(prisoner_id: str, person: PrisonUpdate):
    conn = get_db()
    cur = conn.execute(
        "UPDATE prisoners SET name = ?, cell = ?, crime = ?, date = ?, Fine = ? WHERE prisoner_id = ?",
        (person.name, person.cell, person.crime, person.date, person.Fine, prisoner_id)
    )
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم تعديل بيانات السجين بنجاح"}
    raise HTTPException(status_code=404, detail="السجين غير موجود")

@app.put("/Fine/increment/{prisoner_id}")
def add_fine(prisoner_id: str):
    conn = get_db()
    conn.execute("UPDATE prisoners SET Fine = Fine + 2000 WHERE prisoner_id = ?", (prisoner_id,))
    conn.commit()
    row = conn.execute("SELECT Fine FROM prisoners WHERE prisoner_id = ?", (prisoner_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"تم تحديث الغرامة بنجاح وأصبحت تساوي: {row['Fine']}"}
    raise HTTPException(status_code=404, detail="السجين غير موجود")
