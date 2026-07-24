"""
🏦 نظام الإيداع البنكي - Bank Deposit Class

برنامج يطبق مفاهيم الـ OOP لإدارة عمليات الإيداع البنكي،
مع تحديد قيمة افتراضية للرصيد الابتدائي (0) وتحديث الرصيد عند كل عملية إيداع.
"""


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("تم الإيداع بنجاح، ورصيدك الحالي يساوي:", self.balance)
        else:
            print("مبلغ الإيداع يجب أن يكون أكبر من الصفر!")


account1 = BankAccount("Ali")

# إيداع 60
account1.deposit(60)

# إيداع 100 إضافية
account1.deposit(100)
