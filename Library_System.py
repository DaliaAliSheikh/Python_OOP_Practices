"""
📚 نظام إدارة المكتبة واستعارة الكتب - Library Management System

برنامج يطبق مفاهيم الـ OOP مع القوائم (Lists)،
يتضمن إضافة الكتب، استعارتها مع التحقق من وجودها باستخدام (in) و (remove)،
وفحص حالة المكتبة باستخدام len().
"""


class Library:

    def __init__(self):
        self.books = []  # قائمة لتخزين أسماء الكتب

    def add_book(self, book_name):
        self.books.append(book_name)
        print("تمت إضافة الكتاب بنجاح:", book_name)

    def borrow_book(self, book_name):
        # التحقق هل الكتاب موجود في القائمة قبل الاستعارة
        if book_name in self.books:
            self.books.remove(book_name)
            print("تمت استعارة الكتاب:", book_name)
        else:
            print("عذراً، الكتاب غير متوفر حالياً:", book_name)

    def show_books(self):
        print("\n--- 📖 قائمة الكتب المتاحة ---")
        # الفحص إذا كانت المكتبة فارغة
        if len(self.books) == 0:
            print("المكتبة فارغة حالياً!")
        else:
            for book in self.books:
                print("-", book)


# تجربة البرنامج
library = Library()
library.add_book("قصة إنسان")
library.borrow_book("قصة إنسان")
library.borrow_book("كتاب غير موجود")
library.show_books()
