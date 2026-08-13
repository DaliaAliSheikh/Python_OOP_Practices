"""
🎓 نظام إدارة درجات الطلاب وحساب المعدلات - Student Grades Manager

تطبيق متقدم جداً لمفاهيم الـ OOP يوضح:
- ربط الكائنات المخصصة (Grade Object) داخل قائمة رئيسية.
- فلترة البيانات وحساب المعدل الحسابي لطالب محدد بالاسم.
- فصل بنية البيانات عن المنطق البرمجي والواجهة التفاعلية.
"""


class Grade:
    # الصندوق 1: كرت بيانات الدرجة
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject


class GradeManager:
    # الصندوق 2: الدفتر والمدير (إدارة البيانات والعمليات)
    def __init__(self):
        self.grades = []  # قائمة تخزن كائنات من Class Grade

    def add(self, name, grade, subject):
        """إضافة سجل درجة جديد"""
        g = Grade(name, grade, subject)
        self.grades.append(g)
        print("تمت الاضافة بنجاح 🤎")

    def show_all(self):
        """عرض جميع السجلات"""
        print("\n--- 📜 كل السجلات المسجلة ---")
        if len(self.grades) == 0:
            print("لا توجد درجات مسجلة بعد")
        else:
            for c in self.grades:
                print(f"الطالب: {c.name} | الدرجة: {c.grade} | المادة: {c.subject}")

    def average(self, name):
        """حساب المعدل الحسابي لطالب محدد"""
        total_score = 0
        count = 0

        for k in self.grades:
            if k.name == name:  # البحث باسم الطالب
                total_score += k.grade
                count += 1

        if count > 0:
            avg = total_score / count
            print(f"📊 معدل الطالب '{name}' هو: {avg}")
        else:
            print(f"❌ الطالب '{name}' ليس لديه درجات مسجلة بعد!")


def G():
    # الصندوق 3: شاشة التعامل مع المستخدم
    manager = GradeManager()

    while True:
        print("\n1. اضافة درجة")
        print("2. عرض الكل")
        print("3. عرض المعدل")
        print("4. خروج")

        choice = input("ادخل رقم الاختيار: ")

        if choice == "1":
            n = input("اسم الطالب: ")
            gr = int(input("الدرجة: "))
            s = input("المادة: ")
            manager.add(n, gr, s)
        elif choice == "2":
            manager.show_all()
        elif choice == "3":
            n = input("اسم الطالب العايزة معدلو: ")
            manager.average(n)
        elif choice == "4":
            print("شكراً لاستخدام النظام 🤎")
            break
        else:
            print("رقم غلط حاولي تاني")


# تشغيل النظام
G()
