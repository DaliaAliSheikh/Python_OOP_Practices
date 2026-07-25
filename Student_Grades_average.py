"""
🎓 نظام إدارة وحساب متوسط درجات الطلاب - Student Grades Tracker

برنامج يطبق مفاهيم الـ OOP مع القوائم (Lists)،
يتضمن إضافة الدرجات مع التحقق من صحتها (بين 0 و 100)،
وطباعة الدرجات وحساب المتوسط الحسابي باستخدام sum() و len().
"""


class GradeTracker:

    def __init__(self):
        self.grades = []  # قائمة لتخزين الدرجات

    def add_grade(self, score):
        # التحقق من أن الدرجة مدخلة بشكل صحيح بين 0 و 100
        if 0 <= score <= 100:
            self.grades.append(score)
            print("تم تسجيل الدرجة بنجاح:", score)
        else:
            print("خطأ: الدرجة يجب أن تكون بين 0 و 100!")

    def show_summary(self):
        print("\n--- 📝 قائمة الدرجات المسجلة ---")
        for score in self.grades:
            print("درجة:", score)

        # حساب المجموع والعدد والمتوسط برة الـ loop
        total = sum(self.grades)
        count = len(self.grades)

        if count > 0:
            average = total / count
            print("---------------------------------")
            print("المجموع الكلي:", total)
            print("عدد المواد:", count)
            print("المتوسط الحسابي يساوي:", average)
        else:
            print("لا توجد درجات مسجلة لحساب المتوسط!")


# تجربة البرنامج
tracker = GradeTracker()
tracker.add_grade(60)
tracker.add_grade(50)
tracker.add_grade(10)

# عرض النتيجة والمتوسط
tracker.show_summary()
