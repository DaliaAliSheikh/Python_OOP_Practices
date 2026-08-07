"""
🔒 نظام التحكم في الدخول والتحقق من الأسماء - Access Control System

تطبيق عملي لمفاهيم الـ OOP يوضح:
- فكرة القائمة السوداء (Blacklist) وحظر المدخلات غير المسموح بها.
- تسجيل كل المحاولات مقابل المدخلات المقبولة فقط.
- توليد تقرير نهائي شامل بعد الخروج.
"""


class AccessControl:

    def __init__(self):
        self.allowed_users = []  # قائمة المستخدمين المقبولين
        self.all_attempts = []  # قائمة بجميع محاولات الدخول
        self.blocked_users = ["omer", "ahmed", "ali"]  # القائمة السوداء للمحظورين

    def start_system(self):
        print("--- 🔒 نظام التحقق من صلاحيات الدخول ---")

        while True:
            name = input("\nأدخل الاسم (أو اكتب exit للخروج): ")

            if name == "exit":
                break

            self.all_attempts.append(name)  # تسجيل المحاولة

            if name in self.blocked_users:
                print(f"❌ الاسم '{name}' ممنوع من الدخول!")
            else:
                self.allowed_users.append(name)  # إضافة للمقبولين
                print(f"✅ تمت إضافة الاسم بنجاح: {name}")

        # التقرير النهائي
        print("\n======= 📊 التقرير النهائي =======")
        print("جميع محاولات الدخول:", self.all_attempts)
        print("المستخدمون المقبولون فقط:", self.allowed_users)


# تشغيل النظام
system = AccessControl()
system.start_system()
