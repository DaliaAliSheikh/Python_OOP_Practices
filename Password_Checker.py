"""
🔐 نظام التحقق من كلمة السر وسجل المحاولات - Password & Login Tracker

برنامج يطبق مفهوم الـ OOP مع الـ while loop والـ input،
يقوم بالتحقق من بيانات الدخول، وفي حال الخطأ يحفظ المحاولة في قائمة المحاولات الفاشلة.
"""


class PasswordChecker:

    def __init__(self):
        self.failed_attempts = []  # قائمة لتخزين المحاولات الخاطئة

    def login(self):
        while True:
            name = input("أدخل اسم المستخدم: ")
            password = int(input("أدخل الرقم السري: "))

            # التحقق من صحة الاسم والرمز
            if name == "ali" and password == 1234:
                print("أهلاً بك مجدداً:", name)
                break  # إيقاف التكرار عند الدخول الصحيح
            else:
                # إضافة المحاولة الفاشلة إلى القائمة
                self.failed_attempts.append([name, password])
                print("بيانات غير صحيحة، حاول مرة أخرى!")
                print("سجل المحاولات الخاطئة حتى الآن:", self.failed_attempts)
                print("-----------------------------------")


# تجربة البرنامج
checker = PasswordChecker()
checker.login()
