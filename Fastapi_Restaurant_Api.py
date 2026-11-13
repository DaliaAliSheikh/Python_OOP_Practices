"""
نظام إدارة المطاعم والطلبات باستخدام FastAPI وقاعدة بيانات SQLite
وصف النظام: تطبيق خلفي متقدم (Backend API) لإدارة الوجبات، تتبع المخزون، تسجيل طلبات العملاء، والربط بين جداول الوجبات والطلبات عبر علاقات قواعد البيانات (Relational Database).
"""

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("Restaurant.db")
    conn.row_factory = sqlite3.Row
    return conn
    
@app.on_event("startup")
def create_tables():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS meals(meal_id TEXT PRIMARY KEY, name TEXT, quantity INTEGER, price INTEGER)")
    conn.execute("CREATE TABLE IF NOT EXISTS orders(order_id INTEGER PRIMARY KEY AUTOINCREMENT, meal_id TEXT, customer_name TEXT, order_date TEXT, FOREIGN KEY(meal_id) REFERENCES meals(meal_id))")
    conn.commit()
    conn.close()
    
@app.get("/")
def home():
    return {"message": "النظام شغال جربه /docs"}
    
class Restaurant(BaseModel):
    meal_id: str
    name: str
    quantity: int
    price: int
    
class UpdateValue(BaseModel):
    amount: int
    
class UpdateName(BaseModel):
    new_name: str
    
@app.post("/add")
def add(restaurant: Restaurant):
    conn = get_db()
    try:
        conn.execute("INSERT INTO meals(meal_id, name, quantity, price) VALUES (?, ?, ?, ?)", 
                     (restaurant.meal_id, restaurant.name, restaurant.quantity, restaurant.price))
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
    rows = conn.execute("SELECT * FROM meals").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.get("/search/{meal_id}")
def search(meal_id: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM meals WHERE meal_id = ?", (meal_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}
    
@app.delete("/delete/{meal_id}")
def delete(meal_id: str):
    conn = get_db()
    cur = conn.execute("DELETE FROM meals WHERE meal_id = ?", (meal_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم الحذف"}
    return {"message": "لا يوجد"}
    
@app.put("/price/{meal_id}")
def add_price(meal_id: str, data: UpdateValue):
    conn = get_db()
    conn.execute("UPDATE meals SET price = price - ? WHERE meal_id = ?", (data.amount, meal_id))
    conn.commit()
    row = conn.execute("SELECT price FROM meals WHERE meal_id = ?", (meal_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"السعر اصبح يساوي {row['price']}"}
    return {"message": "لا يوجد"}
    
@app.put("/quantity/{meal_id}")
def add_quantity(meal_id: str, data: UpdateValue):
    conn = get_db()
    conn.execute("UPDATE meals SET quantity = quantity + ? WHERE meal_id = ?", (data.amount, meal_id))
    conn.commit()
    row = conn.execute("SELECT quantity FROM meals WHERE meal_id = ?", (meal_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"الكمية اصبحت تساوي {row['quantity']}"}
    return {"message": "لا يوجد"}
    
@app.put("/name/{meal_id}")
def add_name(meal_id: str, data: UpdateName):
    conn = get_db()
    conn.execute("UPDATE meals SET name = ? WHERE meal_id = ?", (data.new_name, meal_id))
    conn.commit()
    row = conn.execute("SELECT name FROM meals WHERE meal_id = ?", (meal_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"تم تغير الاسم الى {row['name']}"}
    return {"message": "لا يوجد"}
    
class RestaurantOrder(BaseModel):
    meal_id: str
    customer_name: str
    order_date: str
    
@app.post("/add_order")
def add_order(restaurant: RestaurantOrder):
    conn = get_db()
    row = conn.execute("SELECT * FROM meals WHERE meal_id = ?", (restaurant.meal_id,)).fetchone()
    if not row:
        conn.close()
        return {"message": "لا يوجد هذا الطلب"}
    if row["quantity"] <= 0:
        conn.close()
        return {"message": f"الكمية غير كافية وهي {row['quantity']}"}
    
    conn.execute("INSERT INTO orders(meal_id, customer_name, order_date) VALUES (?, ?, ?)", 
                 (restaurant.meal_id, restaurant.customer_name, restaurant.order_date))
    conn.execute("UPDATE meals SET quantity = quantity - 1 WHERE meal_id = ?", (restaurant.meal_id,))
    conn.commit()
    conn.close()
    return {"message": "تمت اضافة الطلب"}
    
@app.get("/orders")
def get_orders():
    conn = get_db()
    rows = conn.execute("SELECT * FROM orders").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.delete("/delete_order/{order_id}")
def delete_order(order_id: int):
    conn = get_db()
    conn.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
    conn.commit()
    conn.close()
    return {"message": "تم الحذف"}
    
@app.get("/meals_with_orders")
def meals_with_orders():
    conn = get_db()
    rows = conn.execute("SELECT meals.meal_id, meals.name, orders.customer_name FROM meals JOIN orders ON meals.meal_id = orders.meal_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.get("/orders_with_meals")
def orders_with_meals():
    conn = get_db()
    rows = conn.execute("SELECT orders.order_id, orders.order_date, meals.quantity, orders.customer_name FROM orders JOIN meals ON orders.meal_id = meals.meal_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
