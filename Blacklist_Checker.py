"""
🚫 نظام حظر المستخدمين (القائمة السوداء) - Blacklist Access Control

برنامج يطبق مفهوم الـ OOP لمنع أشخاص معينين من الدخول،
حيث يتم التكرار بـ while loop حتى يدخل مستخدم غير محظور.
"""


class AccessControl:

    def __init__(self):
        # قائمة الأسماء المحظورة من الدخول (Blacklist)
        self.blocked_users = ["omer", "ahmed", "ali"]

    def start_check(self):
        while True:
            name = input("أدخل اسمك للدخول: ")

            # التحقق هل الاسم ضمن القائمة المحظورة
            if name in self.blocked_users:
                print("عذراً، هذا الاسم محظور! حاول باسم آخر.")
                print("-----------------------------------")
            else:
                print("مرحباً بك، تم السماح لك بالدخول:", name)
                break  # الخروج من الـ loop بعد الدخول الناجح


# تجربة البرنامج
system = AccessControl()
system.start_check()
