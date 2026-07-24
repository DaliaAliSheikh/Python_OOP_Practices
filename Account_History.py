"""
📜 كلاس الحساب مع سجل المعاملات - Account History Class

برنامج يطبق مفاهيم الـ OOP مع القوائم (Lists) والتكرار (For Loops)،
يقوم بتسجيل وتتبع كل عملية تغيير في الرصيد (إيداع/سحب) وعرض سجل الحركات.
"""


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.history = []  # قائمة لتسجيل تاريخ تغيرات الرصيد

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(self.balance)
            print("تم الإيداع. الرصيد الحالي:", self.balance)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(self.balance)
            print("تم السحب. الرصيد الحالي:", self.balance)
        else:
            print("لا يوجد نقود كافية!")

    def show_history(self):
        print("--- سجل معاملات الحساب للعميل:", self.name, "---")
        for record in self.history:
            print("الرصيد بعد العملية:", record)


# تجربة الكود
account1 = BankAccount("Ali")
account1.deposit(500)
account1.withdraw(300)

# عرض سجل التغييرات
account1.show_history()
