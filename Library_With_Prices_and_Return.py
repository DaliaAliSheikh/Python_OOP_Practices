"""
📚 نظام المكتبة المتقدم مع الأسعار وتحسين البحث - Library with Prices & Return

تطبيق متقدم لمفاهيم الـ OOP يوضح:
- استخدام القوائم المتداخلة (2D Lists) لتخزين البيانات والمرتبطة (الاسم والسعر).
- استخدام العبارة (return) لإيقاف الخوارزمية فور العثور على النتيجة لزيادة كفاءة البحث.
- تحسين واجهة الاستعلام لعرض تفاصيل السعر عند العثور على الكتاب.
"""


class Library:

    def __init__(self):
        # كتب افتراضية مبدئية بتنسيق [الاسم، السعر]
        self.books = [["my life", 40.0], ["my true", 50.0]]

    def add_book(self):
        """إضافة كتاب جديد مع السعر"""
        book_name = input("ادخل اسم كتابك: ")
        price = float(input("ادخل سعر الكتاب: "))
        self.books.append([book_name, price])
        print("✅ تمت الإضافة بنجاح! القائمة الحالية:", self.books)

    def show_books(self):
        """عرض جميع الكتب وأسعارها"""
        print("\n--- 📖 قائمة الكتب والأسعار ---")
        if len(self.books) == 0:
            print("المكتبة فارغة!")
            return  # الخروج فوراً لو القائمة فاضية

        for item in self.books:
            print(f"اسم الكتاب: {item[0]} | السعر: {item[1]} جنيه")

    def search_books(self):
        """البحث عن كتاب وعرض سعره"""
        search_term = input("ادخل اسم الكتاب للبحث عنه: ")
        for item in self.books:
            if search_term == item[0]:
                print(f"✅ الكتاب موجود! سعره هو: {item[1]} جنيه")
                return  # الخروج فوراً بمجرد العثور على الكتاب

        print("❌ لا يوجد هذا الكتاب في المكتبة.")


def show():
    # الواجهة التفاعلية للنظام
    my_library = Library()

    while True:
        print("\n=== 📚 نظام إدارة المكتبة والأسعار ===")
        print("1. اضافة كتاب")
        print("2. عرض الكتب")
        print("3. البحث عن كتاب")
        print("4. خروج")

        choice = input("ادخل رقم الاختيار: ")

        if choice == "1":
            my_library.add_book()
        elif choice == "2":
            my_library.show_books()
        elif choice == "3":
            my_library.search_books()
        elif choice == "4":
            print("شكراً لاستخدام النظام.. مع السلامة! 👋")
            break
        else:
            print("⚠️ الرجاء ادخال رقم من 1 إلى 4 فقط!")


# تشغيل البرنامج
show()
