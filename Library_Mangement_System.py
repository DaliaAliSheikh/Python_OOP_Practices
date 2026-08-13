"""
📚 نظام إدارة وسجل المكتبة - Library Management System

تطبيق عملي لمفاهيم الـ OOP يوضح:
- إنشاء كلاس (Library) لإدارة سجل الكتب.
- إضافة الكتب للشنطة (القائمة) وعرضها.
- البحث السريع عن كتاب محدد باستخدام المعامل (in).
- توفير واجهة تفاعلية بسيطة ومحمية من خيارات المدخلات الخاطئة.
"""


class Library:

    def __init__(self):
        self.books = []  # قائمة الكتب في المكتبة

    def add_book(self):
        """إضافة كتاب جديد للمكتبة"""
        book_name = input("ادخل اسم كتابك: ")
        self.books.append(book_name)
        print("📚 قائمة الكتب الحالية:", self.books)

    def show_books(self):
        """عرض جميع الكتب المسجلة"""
        print("\n--- 📖 قائمة الكتب في المكتبة ---")
        if len(self.books) == 0:
            print("المكتبة فارغة لسه!")
        else:
            for book in self.books:
                print(f"- {book}")

    def search_books(self):
        """البحث عن كتاب محدد"""
        search_term = input("ادخل اسم الكتاب للبحث عنه: ")
        if search_term in self.books:
            print(f"✅ نعم! الكتاب '{search_term}' موجود في المكتبة.")
        else:
            print(f"❌ عفواً، الكتاب '{search_term}' غير موجود.")


def show():
    # الواجهة التفاعلية للنظام
    my_library = Library()

    while True:
        print("\n=== 📚 نظام إدارة المكتبة ===")
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
            print("شكراً لاستخدام نظام المكتبة.. مع السلامة! 👋")
            break
        else:
            print("⚠️ الرجاء ادخال رقم من 1 إلى 4 فقط!")


# تشغيل البرنامج
show()
