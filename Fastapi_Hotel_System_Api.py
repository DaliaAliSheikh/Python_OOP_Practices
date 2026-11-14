"""
نظام إدارة الفنادق والحجوزات باستخدام FastAPI وقاعدة بيانات SQLite
وصف النظام: تطبيق خلفي متقدم (Backend API) لإدارة الغرف، تتبع الأسعار والوجبات، تسجيل الحجوزات، والربط بين جداول الغرف والحجوزات عبر علاقات قواعد البيانات (Relational Database).
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("Hotel.db")
    conn.row_factory = sqlite3.Row
    return conn 
    
@app.on_event("startup")
def create_tables():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS rooms(room_id TEXT PRIMARY KEY, price INTEGER, available_rooms INTEGER, meal_type TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS bookings(booking_id INTEGER PRIMARY KEY AUTOINCREMENT, room_id TEXT, name TEXT, date TEXT, FOREIGN KEY(room_id) REFERENCES rooms(room_id))")
    conn.commit()
    conn.close()
    
@app.get("/")
def home():
    return {"message": "النظام شغال جربه /docs"}
    
class Hotel(BaseModel):
    room_id: str
    price: int
    available_rooms: int
    meal_type: Literal["breakfast", "lunch", "dinner"]
    
class UpdateValue(BaseModel):
    amount: int
    
@app.post("/add")
def add(hotel: Hotel):
    conn = get_db()
    try:
        conn.execute("INSERT INTO rooms (room_id, price, available_rooms, meal_type) VALUES (?, ?, ?, ?)", 
                     (hotel.room_id, hotel.price, hotel.available_rooms, hotel.meal_type))
        conn.commit()
        return {"message": "تمت الاضافة"}
    except Exception as error:
        print(error)
        return {"message": "موجود مسبقا"}
    finally:
        conn.close()
        
@app.get("/all")
def show_all():
    conn = get_db()
    rows = conn.execute("SELECT * FROM rooms").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.get("/search/{room_id}")
def search(room_id: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM rooms WHERE room_id = ?", (room_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}
    
@app.delete("/delete/{room_id}")
def delete(room_id: str):
    conn = get_db() 
    cur = conn.execute("DELETE FROM rooms WHERE room_id = ?", (room_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم الحذف"}
    return {"message": "لا يوجد"}
    
@app.put("/price/{room_id}")
def add_price(room_id: str, data: UpdateValue):
    conn = get_db()
    conn.execute("UPDATE rooms SET price = price - ? WHERE room_id = ?", (data.amount, room_id))
    conn.commit()
    row = conn.execute("SELECT price FROM rooms WHERE room_id = ?", (room_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"السعر اصبح يساوي {row['price']}"}
    return {"message": "لا يوجد"}
    
class HotelBooking(BaseModel):
    room_id: str
    name: str
    date: str
    
@app.post("/add_booking")
def add_booking(hotel: HotelBooking):
    conn = get_db()
    row = conn.execute("SELECT * FROM rooms WHERE room_id = ?", (hotel.room_id,)).fetchone()
    if not row:
        conn.close()
        return {"message": "لا يوجد حجز"}
    if row["available_rooms"] <= 0:
        conn.close()
        return {"message": f"لا يوجد غرف للحجز {row['available_rooms']}"}
    
    conn.execute("INSERT INTO bookings (room_id, name, date) VALUES (?, ?, ?)", (hotel.room_id, hotel.name, hotel.date))
    conn.execute("UPDATE rooms SET available_rooms = available_rooms - 1 WHERE room_id = ?", (hotel.room_id,))
    conn.commit()
    conn.close()
    return {"message": "تمت اضافة حجز"}
    
@app.get("/bookings")
def get_bookings():
    conn = get_db()
    rows = conn.execute("SELECT * FROM bookings").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.delete("/delete_booking/{booking_id}")
def delete_bokking(booking_id: int):
    conn = get_db()
    conn.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
    conn.commit()
    conn.close()
    return {"message": "تم الحذف"}
    
@app.get("/rooms_with_bookings")
def rooms_with_bookings():
    conn = get_db()
    rows = conn.execute("SELECT rooms.room_id, rooms.price, bookings.name FROM rooms JOIN bookings ON rooms.room_id = bookings.room_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.get("/bookings_with_rooms")
def bookings_with_rooms():
    conn = get_db()
    rows = conn.execute("SELECT bookings.name, bookings.date, bookings.room_id FROM bookings JOIN rooms ON bookings.room_id = rooms.room_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
