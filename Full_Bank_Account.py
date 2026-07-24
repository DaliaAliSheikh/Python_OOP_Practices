"""
🏦 نظام الحساب البنكي المتكامل - Complete Bank Account Class

برنامج يطبق مفاهيم الـ OOP لإدارة الحساب البنكي شاملاً:
الإيداع، السحب، مع التحقق من كفاية الرصيد قبل عملية السحب.
"""


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("تم الإيداع، ورصيدك الحالي يساوي:", self.balance)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("تم السحب بنجاح، الرصيد المتبقي:", self.balance)
        else:
            print("عذراً، الرصيد غير كافي أو المبلغ غير صالح!")


account1 = BankAccount("Ali")

# تجربة الإيداع والسحب
account1.deposit(60)
account1.withdraw(5)
