"""
🏦 نظام الحساب البنكي مع إرجاع القيم - Bank Account with Return Values

برنامج يطبق مفاهيم الـ OOP لإدارة الحساب البنكي،
حيث تقوم الدوال بحساب الرصيد وإرجاعه (return) للاستفادة منه خارج الكلاس.
"""


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("تم الإيداع. رصيدك حالياً:", self.balance)
        return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("تم السحب. رصيدك الحالي:", self.balance)
        else:
            print("المبلغ غير كافي!")
        return self.balance


# تجربة الحساب واستقبال القيمة المرجعة
account1 = BankAccount("Ali", 1000)

# استقبال القيمة المرجعة من الدالة
current_balance = account1.withdraw(200)
print("الرصيد المستلم خارج الكلاس يساوي:", current_balance)
