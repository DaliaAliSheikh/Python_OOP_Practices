"""
نظام إدارة المكتبات واستعارة الكتب - Library Book Borrowing System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام كلاس لتمثيل بيانات الكتاب (رقم ISBN، العنوان، المؤلف، والحالة).
- استخدام القواميس (Dictionaries) لإدارة الكتب، استعارتها، إرجاعها، والبحث والحذف الفوري.
"""

class BookItem:
    def __init__(self, isbn, title, author, stats):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.stats = stats


class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self):
        isbn = input("ادخل رقم الكتاب: ")
        if isbn in self.books:
            print("يوجد كتاب بهذا الرقم مسبقاً")
            return
        
        title = input("ادخل عنوان الكتاب: ")
        author = input("ادخل اسم الكاتب: ")
        stats = "متاح"
        
        book = BookItem(isbn, title, author, stats)
        self.books[isbn] = book
        print("تمت اضافة كتاب جديد")

    def show_all_books(self):
        if not self.books:
            print("لا يوجد اي كتب")
            return
        
        print("\n--- كل الكتب ---")
        for isbn, book in self.books.items():
            print(f"رقم الكتاب هو: {isbn} | عنوانه: {book.title} | الكاتب هو: {book.author} | حالة الكتاب هي: {book.stats}")

    def search_book(self):
        isbn = input("ادخل رقم الكتاب: ")
        if isbn in self.books:
            book = self.books[isbn]
            print(f"عنوان الكتاب هو: {book.title} | اسم الكاتب هو: {book.author} | رقمه هو: {isbn} | حالة الكتاب هي: {book.stats}")
        else:
            print("لا يوجد كتاب بهذا الرقم")

    def borrow_book(self):
        isbn = input("ادخل رقم الكتاب: ")
        if isbn in self.books:
            book = self.books[isbn]
            if book.stats == "متاح":
                book.stats = "مستعار"
                print("تمت استعارة هذا الكتاب")
            else:
                print("الكتاب مستعار اصلا")
        else:
            print("لا يوجد كتاب بهذا الرقم")

    def return_book(self):
        isbn = input("ادخل رقم الكتاب: ")
        if isbn in self.books:
            book = self.books[isbn]
            if book.stats == "مستعار":
                book.stats = "متاح"
                print("شكرا لارجاعك الكتاب")
            else:
                print("الكتاب دا ما مستعار اساساً")
        else:
            print("لا يوجد كتاب بهذا الرقم")

    def delete_book(self):
        isbn = input("ادخل رقم الكتاب: ")
        if isbn in self.books:
            del self.books[isbn]
            print("تم حذف هذا الكتاب")
        else:
            print("لا يوجد رقم لهذا الكتاب")


def main():
    manager = LibraryManager()
    while True:
        print("\n1. اضافة كتاب")
        print("2. عرض كل الكتب")
        print("3. البحث عن كتاب")
        print("4. استعارة كتاب")
        print("5. ارجاع كتاب")
        print("6. حذف كتاب")
        print("7. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_book()
        elif choice == "2":
            manager.show_all_books()
        elif choice == "3":
            manager.search_book()
        elif choice == "4":
            manager.borrow_book()
        elif choice == "5":
            manager.return_book()
        elif choice == "6":
            manager.delete_book()
        elif choice == "7":
            print("خروج")
            break
        else:
            print("ادخل رقم من الارقام الفوق")


main()
