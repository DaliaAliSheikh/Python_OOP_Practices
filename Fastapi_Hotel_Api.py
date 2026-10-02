"""
نظام إدارة الفنادق باستخدام FastAPI وقاعدة بيانات SQLite - Advanced FastAPI Hotel API

تطبيق ويب متقدم ومكتمل:
- استخدام FastAPI لإنشاء نقاط اتصال RESTful API.
- استخدام SQLite كقاعدة بيانات دائمة لتخزين بيانات الغرف.
- استخدام Pydantic للتحقق من صحة البيانات المدخلة (Data Validation).
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Hotel Management API", version="2.0")

def get_db():
    conn = sqlite3.connect("Room.db")
    conn.row_factory = sqlite3.Row
    return conn

# تهيئة جدول قاعدة البيانات عند تشغيل التطبيق
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS rooms(
            room_number TEXT PRIMARY KEY,
            name TEXT,
            date TEXT,
            stats TEXT,
            price INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def home():
    return {"message": "النظام شغال بنجاح، جرب الدخول إلى /docs لاختبار الـ APIs"}

class Room(BaseModel):
    room_number: str
    name: str
    date: str
    stats: str
    price: int

class RoomUpdate(BaseModel):
    name: str
    date: str
    stats: str
    price: int
    
@app.post("/add")
def add_room(room: Room):
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO rooms (room_number, name, date, stats, price) VALUES (?, ?, ?, ?, ?)",
            (room.room_number, room.name, room.date, room.stats, room.price)
        )
        conn.commit()
        return {"message": "تمت اضافة الغرفة بنجاح"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="رقم الغرفة موجود مسبقاً")
    finally:
        conn.close()

@app.get("/all")
def show_all_rooms():
    conn = get_db()
    rows = conn.execute("SELECT * FROM rooms").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/search/{room_number}")
def search_room(room_number: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM rooms WHERE room_number = ?", (room_number,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    raise HTTPException(status_code=404, detail="الغرفة غير موجودة")

@app.delete("/delete/{room_number}")
def delete_room(room_number: str):
    conn = get_db()
    cur = conn.execute("DELETE FROM rooms WHERE room_number = ?", (room_number,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم حذف الغرفة بنجاح"}
    raise HTTPException(status_code=404, detail="الغرفة غير موجودة")

@app.put("/edit/{room_number}")
def edit_room(room_number: str, room: RoomUpdate):
    conn = get_db()
    cur = conn.execute(
        "UPDATE rooms SET name = ?, date = ?, stats = ?, price = ? WHERE room_number = ?",
        (room.name, room.date, room.stats, room.price, room_number)
    )
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم تعديل بيانات الغرفة بنجاح"}
    raise HTTPException(status_code=404, detail="الغرفة غير موجودة")

@app.put("/price/increment/{room_number}")
def add_price(room_number: str):
    conn = get_db()
    conn.execute("UPDATE rooms SET price = price + 200 WHERE room_number = ?", (room_number,))
    conn.commit()
    row = conn.execute("SELECT price FROM rooms WHERE room_number = ?", (room_number,)).fetchone()
    conn.close()
    if row:
        return {"message": f"تم تحديث السعر بنجاح وأصبح يساوي: {row['price']}"}
    raise HTTPException(status_code=404, detail="الغرفة غير موجودة")
