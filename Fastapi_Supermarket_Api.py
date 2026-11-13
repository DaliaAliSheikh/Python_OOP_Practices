"""
نظام إدارة السوبرماركت والمبيعات باستخدام FastAPI وقاعدة بيانات SQLite
وصف النظام: تطبيق خلفي متقدم (Backend API) لإدارة المنتجات، تتبع المخزون، تسجيل المبيعات، والربط بين جداول المنتجات والمبيعات عبر علاقات قواعد البيانات (Relational Database).
"""

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("Supermarket.db")
    conn.row_factory = sqlite3.Row
    return conn
    
@app.on_event("startup")
def create_tables():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS products(product_id TEXT PRIMARY KEY, name TEXT, quantity INTEGER, price INTEGER)")
    conn.execute("CREATE TABLE IF NOT EXISTS sales(sale_id INTEGER PRIMARY KEY AUTOINCREMENT, product_id TEXT, sold_quantity INTEGER, FOREIGN KEY (product_id) REFERENCES products(product_id))")
    conn.commit()
    conn.close()
    
@app.get("/")
def home():
    return {"message": "النظام شغال جربه /docs"}
    
class Supermarket(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: int
    
class UpdateValue(BaseModel):
    amount: int
    
class UpdateName(BaseModel):
    new_name: str
    
@app.post("/add")
def add(supermarket: Supermarket):
    conn = get_db()
    try:
        conn.execute("INSERT INTO products(product_id, name, quantity, price) VALUES (?, ?, ?, ?)", 
                     (supermarket.product_id, supermarket.name, supermarket.quantity, supermarket.price))
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
    rows = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.get("/search/{product_id}")
def search(product_id: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM products WHERE product_id = ?", (product_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}
    
@app.delete("/delete/{product_id}")
def delete(product_id: str):
    conn = get_db()
    cur = conn.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم الحذف"}
    return {"message": "لا يوجد"}
    
@app.put("/quantity/{product_id}")
def add_quantity(product_id: str, data: UpdateValue):
    conn = get_db()
    conn.execute("UPDATE products SET quantity = quantity - ? WHERE product_id = ?", (data.amount, product_id))
    conn.commit()
    row = conn.execute("SELECT quantity FROM products WHERE product_id = ?", (product_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"الكمية اصبحت تساوي {row['quantity']}"}
    return {"message": "لا يوجد"}
    
@app.put("/name/{product_id}")
def add_name(product_id: str, data: UpdateName):
    conn = get_db()
    conn.execute("UPDATE products SET name = ? WHERE product_id = ?", (data.new_name, product_id))
    conn.commit()
    row = conn.execute("SELECT name FROM products WHERE product_id = ?", (product_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"الاسم اصبح هو {row['name']}"}
    return {"message": "لا يوجد"}
    
class SupermarketSale(BaseModel):
    product_id: str
    sold_quantity: int
    
@app.post("/add_sale")
def add_sale(supermarket: SupermarketSale):
    conn = get_db()
    row = conn.execute("SELECT * FROM products WHERE product_id = ?", (supermarket.product_id,)).fetchone()
    if not row:
        conn.close()
        return {"message": "لا يوجد هذا المنتج"}
    if row["quantity"] < supermarket.sold_quantity:
        conn.close()
        return {"message": f"الكمية لا تكفي وتساوي {row['quantity']}"}
    
    conn.execute("INSERT INTO sales(product_id, sold_quantity) VALUES (?, ?)", (supermarket.product_id, supermarket.sold_quantity))
    conn.execute("UPDATE products SET quantity = quantity - ? WHERE product_id = ?", (supermarket.sold_quantity, supermarket.product_id))
    conn.commit()
    conn.close()
    return {"message": "تم اضافة منتج"}
    
@app.get("/sales")
def get_sales():
    conn = get_db()
    rows = conn.execute("SELECT * FROM sales").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.delete("/delete_sale/{sale_id}")
def delete_sale(sale_id: int):
    conn = get_db()
    conn.execute("DELETE FROM sales WHERE sale_id = ?", (sale_id,))
    conn.commit()
    conn.close()
    return {"message": "تم الحذف"}
    
@app.get("/products_with_sales")
def products_with_sales():
    conn = get_db()
    rows = conn.execute("SELECT products.product_id, products.name, sales.sold_quantity FROM products JOIN sales ON products.product_id = sales.product_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.get("/sales_with_products")
def sales_with_products():
    conn = get_db()
    rows = conn.execute("SELECT products.name, products.quantity, sales.sold_quantity FROM sales JOIN products ON sales.product_id = products.product_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
