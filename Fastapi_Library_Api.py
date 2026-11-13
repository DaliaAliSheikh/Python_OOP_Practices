"""
نظام إدارة المكتبة والاستعارة باستخدام FastAPI وقاعدة بيانات SQLite
وصف النظام: تطبيق خلفي متقدم (Backend API) لإدارة الكتب، تتبع النسخ والمخزون، تسجيل استعارة الطلاب، والربط بين جداول الكتب والاستعارات عبر علاقات قواعد البيانات (Relational Database).
"""

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("Book.db")
    conn.row_factory = sqlite3.Row
    return conn
    
@app.on_event("startup")
def create_tables():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS books(book_id TEXT PRIMARY KEY, title TEXT, copies INTEGER)")
    conn.execute("CREATE TABLE IF NOT EXISTS borrows(borrow_id INTEGER PRIMARY KEY AUTOINCREMENT, book_id TEXT, student_name TEXT, borrow_date TEXT, FOREIGN KEY(book_id) REFERENCES books(book_id))") 
    conn.commit()
    conn.close()
    
@app.get("/")
def home():
    return {"message": "النظام شغال جربه /docs"}
    
class Book(BaseModel):
    book_id: str
    title: str
    copies: int
    
class UpdateValue(BaseModel):
    amount: int
    
@app.post("/add")
def add(book: Book):
    conn = get_db()
    try:
        conn.execute("INSERT INTO books(book_id, title, copies) VALUES (?, ?, ?)", (book.book_id, book.title, book.copies))
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
    rows = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.get("/search/{book_id}")
def search(book_id: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM books WHERE book_id = ?", (book_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}
    
@app.delete("/delete/{book_id}")
def delete(book_id: str):
    conn = get_db()
    cur = conn.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم الحذف"}
    return {"message": "لا يوجد"}
    
@app.put("/copies/{book_id}")
def add_copies(book_id: str, data: UpdateValue):
    conn = get_db()
    conn.execute("UPDATE books SET copies = copies - ? WHERE book_id = ?", (data.amount, book_id)) 
    conn.commit()
    row = conn.execute("SELECT copies FROM books WHERE book_id = ?", (book_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"عدد النسخ المتبقية تساوي {row['copies']}"}
    return {"message": "لا يوجد"}
    
class BookBorrow(BaseModel):
    book_id: str
    student_name: str
    borrow_date: str
    
@app.post("/add_borrow")
def add_borrow(book: BookBorrow):
    conn = get_db()
    row = conn.execute("SELECT * FROM books WHERE book_id = ?", (book.book_id,)).fetchone()
    if not row:
        conn.close()
        return {"message": "لا يوجد هذا الكتاب"}
    if row["copies"] <= 0:
        conn.close()
        return {"message": "لا يوجد نسخ حاليا"}
    conn.execute("INSERT INTO borrows(book_id, student_name, borrow_date) VALUES (?, ?, ?)", (book.book_id, book.student_name, book.borrow_date))
    conn.execute("UPDATE books SET copies = copies - 1 WHERE book_id = ?", (book.book_id,))
    conn.commit()
    conn.close()
    return {"message": "تمت اضافة كتاب"}
    
@app.get("/borrows")
def get_borrows():
    conn = get_db()
    rows = conn.execute("SELECT * FROM borrows").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.delete("/delete_borrow/{borrow_id}")
def delete_borrow(borrow_id: int):
    conn = get_db()
    conn.execute("DELETE FROM borrows WHERE borrow_id = ?", (borrow_id,))
    conn.commit()
    conn.close()
    return {"message": "تم الحذف"}
    
@app.get("/books_with_borrows")
def books_with_borrows():
    conn = get_db()
    rows = conn.execute("SELECT books.book_id, books.title, borrows.student_name, borrows.borrow_date FROM books JOIN borrows ON books.book_id = borrows.book_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
    
@app.get("/borrows_with_books")
def borrows_with_books():
    conn = get_db()
    rows = conn.execute("SELECT borrows.borrow_id, borrows.student_name, books.title FROM borrows JOIN books ON borrows.book_id = books.book_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
