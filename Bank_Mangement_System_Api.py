# 🏦 Bank Management RESTful API
# تطبيق ويب متقدم ومكتمل لإدارة الحسابات البنكية:
# - استخدام FastAPI لإنشاء نقاط اتصال RESTful API.
# - استخدام SQLite كقاعدة بيانات دائمة لتخزين بيانات الحسابات.
# - استخدام Pydantic للتحقق من صحة البيانات المدخلة (Data Validation).

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()
def get_db() :
    conn= sqlite3.connect("Bank.db")
    conn.row_factory=sqlite3.Row
    return conn
conn = get_db()
conn.execute("CREATE TABLE IF NOT EXISTS accounts(account_number TEXT PRIMARY KEY,name TEXT,balance INTEGER)")
conn.commit()
conn.close()
@app.get("/")
def home() :
    return {"message" : "النظام شغال جربه/docs"}
class Bank(BaseModel) :
    account_number: str
    name: str
    balance: int
@app.post("/add")
def add(bank:Bank) :
    conn = get_db()
    try:
        conn.execute("INSERT INTO accounts(account_number,name,balance) VALUES(? ,? ,?)" ,(bank.account_number,bank.name,bank.balance))
        conn.commit()
        return {"message": "تمت اضافة" }
    except Exception as error :
        print(error)
        return {"message": "موجود مسبقا" }
    finally:
        conn.close()
@app.get("/all")
def show_all() :
    conn =get_db()
    rows = conn.execute("SELECT * FROM accounts").fetchall()
    conn.close()
    return [dict(row) for row in rows]
@app.get("/search/{account_number}")
def search(account_number: str) :
    conn = get_db()
    row = conn.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}
@app.delete("/delete/{account_number}")
def delete(account_number: str) :
    conn = get_db()
    cur = conn.execute("DELETE FROM accounts WHERE account_number = ?",(account_number,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": " تم الحذف"}
    return {"message": " لا يوجد"}
@app.put("/balance/{account_number}")
def add_balance(account_number: str):
    conn = get_db()
    conn.execute("UPDATE accounts SET balance = balance + 5700 WHERE account_number= ?", (account_number,))
    conn.commit()
    row = conn.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,)).fetchone()
    conn.close()
    if row:
        return {"message": f"الرصيد اصبح يساوي{row['balance']}" }
    return {"message": "لا يوجد" }
