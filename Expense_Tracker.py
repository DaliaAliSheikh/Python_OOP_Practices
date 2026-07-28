"""
💰 نظام تتبع المصروفات - Expense Tracker

برنامج يطبق مفاهيم الـ OOP، الـ while loop، والـ lists،
يتيح للمستخدم تسجيل المصروفات، عرض كل المصروفات، حساب الإجمالي تلقائياً،
ومسح السجل أو الخروج.
"""


class ExpenseTracker:

    def __init__(self):
        self.expenses = []  # قائمة لتخزين النصوص (اسم المصروف والقبمة)
        self.amounts = []  # قائمة لتخزين المبالغ المالية فقط للحساب

    def start(self):
        print("--- 💰 نظام تتبع المصروفات الشخصية ---")
        while True:
            choice = input(
                "\nاختر (اضافة مصروف / عرض كل المصروفات / عرض الاجمالي / مسح كل المصروفات / خروج): "
            )

            if choice == "اضافة مصروف":
                item = input("أدخل اسم المصروف: ")
                amount = float(input("كم المبلغ: "))

                log = item + " : " + str(amount)
                self.expenses.append(log)
                self.amounts.append(amount)
                print("تمت إضافة المصروف بنجاح!")

            elif choice == "عرض كل المصروفات":
                print("--- 📜 قائمة المصروفات ---")
                if len(self.expenses) == 0:
                    print("لا توجد مصروفات مسجلة حتى الآن!")
                else:
                    for exp in self.expenses:
                        print(exp)

            elif choice == "عرض الاجمالي":
                total = sum(self.amounts)
                print("إجمالي المصروفات هو:", total)

            elif choice == "مسح كل المصروفات":
                self.expenses = []
                self.amounts = []
                print("تم مسح جميع المصروفات بنجاح!")

            elif choice == "خروج":
                print("شكراً لاستخدامك نظام المصروفات.. مع السلامة! 👋")
                break

            else:
                print("خيار غير صحيح، يرجى اختيار أحد الخيارات المتاحة!")


# تجربة البرنامج
tracker = ExpenseTracker()
tracker.start()
