"""
نظام إدارة السيارات باستخدام FastAPI وقاعدة بيانات SQLite
وصف النظام: تطبيق خلفي (Backend API) لإدارة السيارات، مواقفها، وأسعارها.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("Car.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db()
conn.execute("CREATE TABLE IF NOT EXISTS cars (car_number TEXT PRIMARY KEY, name TEXT, parking TEXT, price INTEGER)") 
conn.commit()
conn.close()

@app.get("/")
def home():
    return {"message": "النظام شغال جربه /docs"}

class Car(BaseModel):
    car_number: str
    name: str
    parking: str
    price: int

@app.post("/add")
def add(car: Car):
    conn = get_db()
    try:
        conn.execute("INSERT INTO cars(car_number, name, parking, price) VALUES (?, ?, ?, ?)", 
                     (car.car_number, car.name, car.parking, car.price))
        conn.commit()
        return {"message": "تمت الاضافة"}
    except:
        return {"message": "موجود مسبقا"}
    finally:
        conn.close()

@app.get("/all")
def show_all():
    conn = get_db()
    rows = conn.execute("SELECT * FROM cars").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/search/{car_number}")
def search(car_number: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM cars WHERE car_number = ?", (car_number,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}

@app.delete("/delete/{car_number}")
def delete(car_number: str):
    conn = get_db()
    cur = conn.execute("DELETE FROM cars WHERE car_number = ?", (car_number,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم الحذف"}
    return {"message": "لا يوجد"}

@app.put("/edit/price/{car_number}/{new_price}")
def edit_price(car_number: str, new_price: int):
    conn = get_db()
    cur = conn.execute("UPDATE cars SET price = ? WHERE car_number = ?", (new_price, car_number))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم تعديل السعر"}
    return {"message": "لا يوجد"}

@app.put("/price/{car_number}")
def add_price(car_number: str):
    conn = get_db()
    conn.execute("UPDATE cars SET price = price + 5600 WHERE car_number = ?", (car_number,))
    conn.commit()
    row = conn.execute("SELECT price FROM cars WHERE car_number = ?", (car_number,)).fetchone()
    conn.close()
    if row:
        return {"message": f"السعر اصبح يساوي {row['price']}"}
    return {"message": "لا يوجد"}
