"""
نظام إدارة الصيدلية والمبيعات باستخدام FastAPI وقاعدة بيانات SQLite
وصف النظام: تطبيق خلفي متقدم (Backend API) لإدارة الأدوية، تتبع المخزون، تسجيل المبيعات، والربط بين جداول الأدوية والمبيعات عبر علاقات قواعد البيانات (Relational Database).
"""

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("Medicine.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.on_event("startup")
def create_tables():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS medicines(medicine_id TEXT PRIMARY KEY, name TEXT, quantity INTEGER)")
    conn.execute("CREATE TABLE IF NOT EXISTS sales(sale_id INTEGER PRIMARY KEY AUTOINCREMENT, medicine_id TEXT, customer_name TEXT, sold_quantity INTEGER, FOREIGN KEY (medicine_id) REFERENCES medicines(medicine_id))")
    conn.commit()
    conn.close()

@app.get("/")
def home():
    return {"message": "النظام شغال جربه /docs"}

class Medicine(BaseModel):
    medicine_id: str
    name: str
    quantity: int

class UpdateValue(BaseModel):
    amount: int

@app.post("/add")
def add(medicine: Medicine):
    conn = get_db()
    try:
        conn.execute("INSERT INTO medicines(medicine_id, name, quantity) VALUES (?, ?, ?)", 
                     (medicine.medicine_id, medicine.name, medicine.quantity))
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
    rows = conn.execute("SELECT * FROM medicines").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/search/{medicine_id}")
def search(medicine_id: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM medicines WHERE medicine_id = ?", (medicine_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}

@app.delete("/delete/{medicine_id}")
def delete(medicine_id: str):
    conn = get_db()
    cur = conn.execute("DELETE FROM medicines WHERE medicine_id = ?", (medicine_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم الحذف"}
    return {"message": "لا يوجد"}

@app.put("/quantity/{medicine_id}")
def sell_quantity(medicine_id: str, data: UpdateValue):
    conn = get_db()
    conn.execute("UPDATE medicines SET quantity = quantity - ? WHERE medicine_id = ?", (data.amount, medicine_id))
    conn.commit()
    row = conn.execute("SELECT quantity FROM medicines WHERE medicine_id = ?", (medicine_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"الكمية اصبحت تساوي {row['quantity']}"}
    return {"message": "لا يوجد"}

class MedicineSale(BaseModel):
    medicine_id: str
    customer_name: str
    sold_quantity: int

@app.post("/add_sale")
def add_sale(medicine: MedicineSale):
    conn = get_db()
    row = conn.execute("SELECT * FROM medicines WHERE medicine_id = ?", (medicine.medicine_id,)).fetchone()
    if not row:
        conn.close()
        return {"message": "لا يوجد هذا الدواء"}
    if row["quantity"] < medicine.sold_quantity:
        conn.close()
        return {"message": f"كمية الدواء تساوي {row['quantity']}"}
    
    conn.execute("INSERT INTO sales(medicine_id, customer_name, sold_quantity) VALUES (?, ?, ?)", 
                 (medicine.medicine_id, medicine.customer_name, medicine.sold_quantity))
    conn.execute("UPDATE medicines SET quantity = quantity - ? WHERE medicine_id = ?", (medicine.sold_quantity, medicine.medicine_id))
    conn.commit()
    conn.close()
    return {"message": "تمت الاضافة"}

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

@app.get("/medicines_with_sales")
def medicines_with_sales():
    conn = get_db()
    rows = conn.execute("SELECT medicines.medicine_id, medicines.name, sales.customer_name, sales.sold_quantity FROM medicines JOIN sales ON medicines.medicine_id = sales.medicine_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/sales_with_medicines")
def sales_with_medicines():
    conn = get_db()
    rows = conn.execute("SELECT sales.sale_id, sales.customer_name, medicines.name, sales.sold_quantity FROM sales JOIN medicines ON sales.medicine_id = medicines.medicine_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
