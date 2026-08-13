"""
📦 إدارة المصروفات باستخدام كائنات مخصصة - Custom Objects Expense Tracker

تطبيق متقدم جداً لمفاهيم الـ OOP يوضح:
- إنشاء Class مخصص (Expense) لتمثيل سجل البيانات.
- تخزين كائنات كاملة (Objects) داخل قائمة في كائن آخر (ExpenseManager).
- الفصل بين بنية البيانات (Data Class)، الإدارة (Manager Class)، وشاشة المستخدم (UI Function).
"""


class Expense:
    # الصندوق 1: الكرت (تمثيل بيانات المصروف)
    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date


class ExpenseManager:
    # الصندوق 2: الدفتر + المدير (إدارة البيانات)
    def __init__(self):
        self.expenses = []  # قائمة تخزن كائنات من Class Expense
        self.total_spent = 0

    def add_expense(self):
        name = input("اسم المصروف: ")
        amount = int(input("المبلغ: "))
        date = input("التاريخ: ")

        # إنشاء كائن جديد وإضافته للقائمة
        new_expense = Expense(name, amount, date)
        self.expenses.append(new_expense)
        self.total_spent += amount
        print("تمت الاضافة بنجاح 🤎")

    def show_total(self):
        print(f"\nاجمالي المصروفات: {self.total_spent} جنيه")

    def show_all(self):
        print("\n--- كل المصروفات ---")
        if len(self.expenses) == 0:
            print("مافي مصروفات لسه")
        else:
            # استخراج البيانات من الكائنات بـ Dot Notation
            for expense in self.expenses:
                print(
                    f"الحاجة: {expense.name} | المبلغ: {expense.amount} | التاريخ: {expense.date}"
                )


def run():
    # الصندوق 3: الشاشة والواجهة
    my_wallet = ExpenseManager()

    while True:
        print("\n1. اضافة مصروف")
        print("2. عرض الاجمالي")
        print("3. عرض كل المصروفات")
        print("4. خروج")

        choice = input("اختاري رقم: ")

        if choice == "1":
            my_wallet.add_expense()
        elif choice == "2":
            my_wallet.show_total()
        elif choice == "3":
            my_wallet.show_all()
        elif choice == "4":
            print("شكرا استخدمتي النظام 🤎")
            break
        else:
            print("رقم غلط حاولي تاني")


# تشغيل النظام
run()
