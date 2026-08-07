"""
💰 نظام إدارة وتصنيف المصروفات - Categorized Expense Tracker

تطبيق متقدم لمفاهيم الـ OOP يوضح:
- استخدام القوائم المتداخلة (Nested Lists) لتخزين تفاصيل المعاملة.
- الوصول لعناصر البيانات باستخدام الـ Indexing.
- فلترة وحساب إجمالي المصروفات بناءً على تصنيف محدد (Filtering).
"""


class ExpenseTracker:

    def __init__(self):
        self.expenses = []  # قائمة رئيسية تحتوي على قوائم متداخلة [اسم، مبلغ، تصنيف]

    def start(self):
        while True:
            choice = input(
                "\nاختر (اضافة مصروف / عرض كل المصروفات / عرض الاجمالي / تصنيف / مسح كل المصروفات / خروج): "
            )

            if choice == "اضافة مصروف":
                item_name = input("ادخل اسم المصروف: ")
                amount = float(input("كم المبلغ: "))
                category = input("ادخل التصنيف: ")

                self.expenses.append([item_name, amount, category])
                print("تمت الاضافة بنجاح")

            elif choice == "عرض كل المصروفات":
                print("--- 📜 كل المصروفات المسجلة ---")
                if len(self.expenses) == 0:
                    print("لا توجد مصروفات مسجلة بعد!")
                else:
                    for item in self.expenses:
                        print(f"{item[0]} : {item[1]} جنيه - {item[2]}")

            elif choice == "عرض الاجمالي":
                total = 0
                for item in self.expenses:
                    total += item[1]
                print(f"الاجمالي هو {total} جنيه")

            elif choice == "تصنيف":
                target_category = input("ادخل اسم التصنيف: ")
                print(f"--- المصاريف في تصنيف {target_category} ---")
                category_total = 0
                found = False

                for item in self.expenses:
                    if item[2] == target_category:
                        print(f"{item[0]} : {item[1]} جنيه")
                        category_total += item[1]
                        found = True

                if not found:
                    print("لا توجد مصروفات مسجلة تحت هذا التصنيف!")
                else:
                    print(f"اجمالي تصنيف {target_category} = {category_total} جنيه")

            elif choice == "مسح كل المصروفات":
                self.expenses = []
                print("تم مسح المصروفات كلها")

            elif choice == "خروج":
                print("شكرا لزيارتك.. مع السلامة! 👋")
                break


# تشغيل البرنامج
tracker = ExpenseTracker()
tracker.start()
