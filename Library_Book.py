"""
📚 نظام استعارة الكتب - Library Book Class

برنامج يطبق مفاهيم الـ OOP لإدارة استعارة الكتب،
حيث يتم التحقق من توفر الكتاب وتغيير حالته إلى غير متاح بعد الاستعارة بنجاح.
"""


class Book:
    def __init__(self, title, is_available=True):
        self.title = title
        self.is_available = is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print("كتاب", self.title, "متوفر وتمت استعارته بنجاح!")
        else:
            print("عذراً، كتاب", self.title, "غير متاح حالياً!")


book1 = Book("Python Basics")

# الاستعارة الأولى (حينجح)
book1.borrow_book()

# المحاولة الثانية لنفس الكتاب (حيقول غير متاح)
book1.borrow_book()
