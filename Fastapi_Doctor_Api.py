"""
نظام إدارة العيادات والأطباء باستخدام FastAPI وقاعدة بيانات SQLite
وصف النظام: تطبيق خلفي متقدم (Backend API) لإدارة الأطباء، المواعيد، حجز الكشفيات، والربط بين الجداول عبر العلاقات (Relational Database).
"""

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("Doctor.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.on_event("startup")
def create_tables():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS doctors(doctor_id TEXT PRIMARY KEY, name TEXT, specialty TEXT, available_slots INTEGER, price INTEGER)")
    conn.execute("CREATE TABLE IF NOT EXISTS appointments(appointment_id INTEGER PRIMARY KEY AUTOINCREMENT, doctor_id TEXT, patient_name TEXT, appointment_time TEXT, FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id))")
    conn.commit()
    conn.close()

@app.get("/")
def home():
    return {"message": "النظام شغال جربه /docs"}

class Doctor(BaseModel):
    doctor_id: str
    name: str
    specialty: str
    available_slots: int
    price: int

class UpdateValue(BaseModel):
    amount: int

class UpdateName(BaseModel):
    new_specialty: str

@app.post("/add")
def add(doctor: Doctor):
    conn = get_db()
    try:
        conn.execute("INSERT INTO doctors(doctor_id, name, specialty, available_slots, price) VALUES (?, ?, ?, ?, ?)", 
                     (doctor.doctor_id, doctor.name, doctor.specialty, doctor.available_slots, doctor.price))
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
    rows = conn.execute("SELECT * FROM doctors").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/search/{doctor_id}")
def search(doctor_id: str):
    conn = get_db()
    row = conn.execute("SELECT * FROM doctors WHERE doctor_id = ?", (doctor_id,)).fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"message": "لا يوجد"}

@app.delete("/delete/{doctor_id}")
def delete(doctor_id: str):
    conn = get_db()
    cur = conn.execute("DELETE FROM doctors WHERE doctor_id = ?", (doctor_id,))
    conn.commit()
    conn.close()
    if cur.rowcount > 0:
        return {"message": "تم الحذف"}
    return {"message": "لا يوجد"}

@app.put("/price/{doctor_id}")
def add_price(doctor_id: str, data: UpdateValue):
    conn = get_db()
    conn.execute("UPDATE doctors SET price = price + ? WHERE doctor_id = ?", (data.amount, doctor_id))
    conn.commit()
    row = conn.execute("SELECT price FROM doctors WHERE doctor_id = ?", (doctor_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"السعر اصبح يساوي {row['price']}"}
    return {"message": "لا يوجد"}

@app.put("/available_slots/{doctor_id}")
def add_available_slots(doctor_id: str, data: UpdateValue):
    conn = get_db()
    conn.execute("UPDATE doctors SET available_slots = available_slots + ? WHERE doctor_id = ?", (data.amount, doctor_id))
    conn.commit()
    row = conn.execute("SELECT available_slots FROM doctors WHERE doctor_id = ?", (doctor_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"المواعيد اصبحت تساوي {row['available_slots']}"}
    return {"message": "لا يوجد"}

@app.put("/specialty/{doctor_id}")
def new_specialty(doctor_id: str, data: UpdateName):
    conn = get_db()
    conn.execute("UPDATE doctors SET specialty = ? WHERE doctor_id = ?", (data.new_specialty, doctor_id))
    conn.commit()
    row = conn.execute("SELECT specialty FROM doctors WHERE doctor_id = ?", (doctor_id,)).fetchone()
    conn.close()
    if row:
        return {"message": f"التخصص تغير الى {row['specialty']}"}
    return {"message": "لا يوجد"}

class DoctorAppointment(BaseModel):
    doctor_id: str
    patient_name: str
    appointment_time: str

@app.post("/add_appointment")
def add_appointment(doctor: DoctorAppointment):
    conn = get_db()
    row = conn.execute("SELECT available_slots FROM doctors WHERE doctor_id = ?", (doctor.doctor_id,)).fetchone()
    if not row:
        conn.close()
        return {"message": "الدكتور غير متاح حاليا"}
    if row["available_slots"] <= 0:
        conn.close()
        return {"message": "المواعيد خلصت"}
    
    conn.execute("INSERT INTO appointments(doctor_id, patient_name, appointment_time) VALUES (?, ?, ?)", 
                 (doctor.doctor_id, doctor.patient_name, doctor.appointment_time))
    conn.execute("UPDATE doctors SET available_slots = available_slots - 1 WHERE doctor_id = ?", (doctor.doctor_id,))
    conn.commit()
    conn.close()
    return {"message": "تم الحجز"}

@app.get("/appointments")
def get_appointments():
    conn = get_db()
    rows = conn.execute("SELECT * FROM appointments").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.delete("/delete_appointment/{appointment_id}")
def delete_appointment(appointment_id: int):
    conn = get_db()
    conn.execute("DELETE FROM appointments WHERE appointment_id = ?", (appointment_id,))
    conn.commit()
    conn.close()
    return {"message": "تم الحذف"}

@app.get("/doctors_with_appointments")
def doctors_with_appointments():
    conn = get_db()
    rows = conn.execute("SELECT doctors.doctor_id, doctors.name, appointments.patient_name, appointments.appointment_time FROM doctors JOIN appointments ON doctors.doctor_id = appointments.doctor_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/appointments_with_doctors")
def appointments_with_doctors():
    conn = get_db()
    rows = conn.execute("SELECT doctors.doctor_id, doctors.name, appointments.patient_name, appointments.appointment_time, doctors.available_slots FROM appointments JOIN doctors ON appointments.doctor_id = doctors.doctor_id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
