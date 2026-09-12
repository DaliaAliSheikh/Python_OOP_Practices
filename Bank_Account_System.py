"""
نظام إدارة الحسابات البنكية والعمليات المالية - Bank Account Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام كلاس لتمثيل بيانات الحساب (رقم الحساب، اسم العضو، والرصيد).
- استخدام القواميس (Dictionaries) لادارة الحسابات، تنفيذ عمليات السحب والإيداع، التعديل، والبحث الفوري.
"""

class BankAccount:
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance


class BankManager:
    def __init__(self):
        self.accounts = {}

    def open_account(self):
        account_num = input("ادخل رقم حسابك: ")
        if account_num in self.accounts:
            print("يوجد حساب بهذا الرقم مسبقاً")
            return
        
        name = input("ادخل اسمك: ")
        balance = int(input("ادخل كمية رصيدك: "))
        
        account = BankAccount(account_num, name, balance)
        self.accounts[account_num] = account
        print("تمت اضافة حساب جديد")

    def show_all_accounts(self):
        if not self.accounts:
            print("لا يوجد ارقام حسابات")
            return
        
        print("\n--- كل الحسابات البنكية ---")
        for account_num, account in self.accounts.items():
            print(f"رقم الحساب هو: {account_num} | اسم الشخص هو: {account.name} | رصيده يساوي: {account.balance}")

    def search_account(self):
        account_num = input("ادخل رقم حسابك: ")
        if account_num in self.accounts:
            account = self.accounts[account_num]
            print(f"رقم الحساب هو: {account_num} | اسم الشخص هو: {account.name} | رصيده يساوي: {account.balance}")
        else:
            print("لا يوجد حساب بهذا الرقم")

    def delete_account(self):
        account_num = input("ادخل رقم حسابك: ")
        if account_num in self.accounts:
            del self.accounts[account_num]
            print("تم حذف رقم هذا الحساب")
        else:
            print("لا يوجد رقم هذا الحساب")

    def deposit(self):
        account_num = input("ادخل رقم الحساب: ")
        if account_num in self.accounts:
            account = self.accounts[account_num]
            amount = int(input("ادخل كمية النقود التي تريد ايداعها: "))
            account.balance += amount
            print(f"تم ايداع المبلغ بنجاح. الرصيد الحالي هو: {account.balance}")
        else:
            print("لا يوجد حساب بهذا الرقم")

    def withdraw(self):
        account_num = input("ادخل رقم الحساب: ")
        if account_num in self.accounts:
            account = self.accounts[account_num]
            amount = int(input("ادخل كمية المبلغ الذي تريد سحبه: "))
            if account.balance >= amount:
                account.balance -= amount
                print(f"تم السحب بنجاح. الرصيد الحالي هو: {account.balance}")
            else:
                print("لا يوجد رصيد كافي للسحب")
        else:
            print("لا يوجد حساب بهذا الرقم")

    def update_account(self):
        account_num = input("ادخل رقم الحساب: ")
        if account_num in self.accounts:
            account = self.accounts[account_num]
            new_name = input("ادخل اسمك الجديد: ")
            if new_name:
                account.name = new_name
                print("تم تغير الاسم بنجاح")
        else:
            print("لا يوجد رقم حساب بهذا الرقم")


def main():
    manager = BankManager()
    while True:
        print("\n1. فتح حساب")
        print("2. عرض كل الحسابات")
        print("3. البحث عن حساب")
        print("4. حذف حساب")
        print("5. ايداع رصيد")
        print("6. سحب رصيد")
        print("7. تعديل الاسم حق الحساب")
        print("8. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.open_account()
        elif choice == "2":
            manager.show_all_accounts()
        elif choice == "3":
            manager.search_account()
        elif choice == "4":
            manager.delete_account()
        elif choice == "5":
            manager.deposit()
        elif choice == "6":
            manager.withdraw()
        elif choice == "7":
            manager.update_account()
        elif choice == "8":
            print("خروج")
            break
        else:
            print("ادخل رقم من الارقام الفوق")


main()
