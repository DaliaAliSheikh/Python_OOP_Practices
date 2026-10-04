# 🏨 Advanced FastAPI Hotel Management API
# تطبيق ويب متقدم ومكتمل لإدارة الفنادق:
# - استخدام FastAPI لإنشاء نقاط اتصال RESTful API.
# - استخدام SQLite كقاعدة بيانات دائمة لتخزين بيانات الغرف.
# - استخدام Pydantic للتحقق من صحة البيانات المدخلة (Data Validation)

From fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()
def get_db() :
    conn = sqlite3.connect("Supermarket.db")
    conn.row_factory = sqlite3.Row
    return conn
conn = get_db()
conn.execute("CREATE TABLE IF NOT EXISTS products (product_id TEXT PRIMARY KEY,name TEXT ,quantity INTEGER ,price INTEGER)")
conn.commit()
conn.close()
@app.get("/")
def home():
    return {"message": " النظام شغال جربه /docs"}
class Supermarket(BaseModel) :
    product_id: str
    name: str
    quantity: int
    price: int
@app.post("/add")
def add(supermarket: Supermarket) :
    conn = get_db()
    try:
        conn.execute("INSERT INTO products (product_id,name,quantity ,price) VALUES (? ,? ,? ,?)" ,(supermarket.product_id,supermarket.name,supermarket.quantity,supermarket.price))
        conn.commit()
        return {"message": " تمت الاضافة" }
    except Exception as error:
        print(error)
        return {"message": " موجود مسبقا" }
    finally :
        conn.close()
@app.get("/all")
def show_all() :
    conn = get_db()
    rows = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return [dict(row) for row in rows]
@app.get("/search/{product_id}")
def search(product_id: str) :
    conn = get_db()
    row = conn.execute("SELECT * FROM products WHERE product_id = ?", (product_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد" }
@app.delete("/delete/{product_id}")
def delete(product_id: str) :
    conn = get_db()
    cur = conn.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم الحذف" }
    return {"message": " لا يوجد"}
@app.put("/quantity/{product_id}")
def add_quantity(product_id: str) :
    conn = get_db()
    conn.execute("UPDATE products SET quantity = quantity + 400 WHERE product_id = ?", (product_id,))
    conn.commit()
    row = conn.execute("SELECT quantity FROM products WHERE product_id = ?", (product_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f" الكمية اصبحت تساوي{row['quantity']}"}
    return {"message": "لا يوجد"}
@app.put("/price/{product_id}")
def add_price(product_id: str) :
    conn = get_db()
    conn.execute("UPDATE products SET price = price + 4000 WHERE product_id = ?", (product_id,))
    conn.commit()
    row = conn.execute("SELECT price FROM products WHERE product_id = ?", (product_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"السعر اصبح يساوي{row['price']}"}
    return {"message": "لا يوجد"}
