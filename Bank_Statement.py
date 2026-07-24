"""
🏦 كشف حساب بنكي تفصيلي - Detailed Bank Statement

برنامج يطبق مفاهيم الـ OOP لتسجيل نوع العملية المالية (إيداع/سحب) 
مع قيمتها بداخل القائمة وعرض كشف حساب شامل للعميل.
"""


class BankAccountStatement:

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []  # قائمة لتخزين وصف الحركات المالية

    def deposit(self, money):
        if money > 0:
            self.balance += money
            self.transactions.append(f"إيداع: +{money}")
            print(f"تم إيداع {money} بنجاح.")

    def withdraw(self, money):
        if 0 < money <= self.balance:
            self.balance -= money
            self.transactions.append(f"سحب: -{money}")
            print(f"تم سحب {money} بنجاح.")
        else:
            print("عذراً، الرصيد غير كافٍ!")

    def show_report(self):
        print(f"\n--- 📄 كشف الحساب الخاص بالعميل: {self.account_holder} ---")
        for t in self.transactions:
            print(t)
        print("---------------------------------")
        print("الرصيد النهائي الحالي يساوي:", self.balance)


# تجربة الكود
account = BankAccountStatement("Dalia")
account.deposit(500)
account.withdraw(40)

# عرض كشف الحساب النهائي
account.show_report()
