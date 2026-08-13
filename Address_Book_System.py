class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("أدخل الاسم: ")
        phone_number = input("أدخل رقم الهاتف: ")
        new_contact = Contact(name, phone_number)
        self.contacts.append(new_contact)
        print("تمت الإضافة بنجاح 🤎")

    def show_all(self):
        if len(self.contacts) == 0:
            print("لا توجد جهات اتصال")
        else:
            print("\n--- كل جهات الاتصال ---")
            for contact in self.contacts:
                print(f"الاسم: {contact.name}  |  الرقم: {contact.phone_number}")

    def search_contact(self):
        search_name = input("أدخل الاسم الذي تبحث عنه: ")
        found = False
        for contact in self.contacts:
            if contact.name == search_name:
                print(f"لقيناهو! الاسم: {contact.name} | الرقم: {contact.phone_number}")
                found = True
                break
        if not found:
            print("لا يوجد هذا الاسم")


def main():
    address_book = AddressBook()
    while True:
        print("\n1. إضافة شخص")
        print("2. عرض كل الأسماء")
        print("3. البحث عن شخص")
        print("4. خروج")
        choice = input("أدخل خيارك: ")

        if choice == "1":
            address_book.add_contact()
        elif choice == "2":
            address_book.show_all()
        elif choice == "3":
            address_book.search_contact()
        elif choice == "4":
            print("شكراً لاستخدامك دفتر العناوين 🤎")
            break
        else:
            print("أدخل رقماً صحيحاً")


main()
