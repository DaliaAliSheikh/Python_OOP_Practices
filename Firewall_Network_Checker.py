"""
🛡️ جدار حماية محاكي وفاحص اتصالات الشبكة - Firewall Network Checker

تطبيق متقدم جداً يربط الـ OOP بمفاهيم الأمن السيبراني والشبكات:
- كلاس (Network) لتمثيل تفاصيل طلب الاتصال (IP address & Service).
- كلاس (FirewallManager) لإدارة قوائم الحظر (Blacklist) وفحص اتصالات الشبكة.
- محاكاة قرار جدار الحماية بالسماح أو الحظر بناءً على عنوان الـ IP.
"""


class Network:
    # تمثيل بيانات طلب الاتصال بالشبكة
    def __init__(self, ip_address, service):
        self.ip_address = ip_address
        self.service = service


class FirewallManager:
    # جدار الحماية وإدارة الصلاحيات
    def __init__(self):
        self.blocked_ips = []  # قائمة العناوين المحظورة

    def block_ip(self):
        """إضافة عنوان IP لقائمة الحظر"""
        ip_to_block = input("أدخل عنوان الـ IP المراد حظره: ")
        self.blocked_ips.append(ip_to_block)
        print("🚫 تم الحظر بنجاح. قائمة الحظر الحالية:", self.blocked_ips)

    def display_blocked(self):
        """عرض جميع العناوين المحظورة"""
        print("\n--- 📜 عناوين الـ IP المحظورة حالياً ---")
        if len(self.blocked_ips) == 0:
            print("لا توجد عناوين محظورة بعد.")
        else:
            for ip in self.blocked_ips:
                print(f"- {ip}")

    def check_request(self):
        """فحص طلب الاتصال وتحويله لكائن شبكة"""
        ip = input("أدخل عنوان الـ IP الخاص بك: ")
        service = input("أدخل اسم الخدمة المطلوبة (مثال: HTTP, SSH, FTP): ")

        # إنشاء كائن شبكة يمثل طلب الاتصال
        connection = Network(ip, service)

        # قرار جدار الحماية
        if connection.ip_address in self.blocked_ips:
            print(f"❌ [Firewall Blocked] لا يمكنك الاتصال بالخدمة ({connection.service}) - الـ IP محظور!")
        else:
            print(f"✅ [Firewall Allowed] تم الاتصال بنجاح بالخدمة ({connection.service})!")


def main():
    firewall = FirewallManager()

    while True:
        print("\n=== 🛡️ نظام إدارة جدار الحماية (Firewall) ===")
        print("1. حظر عنوان IP")
        print("2. عرض العناوين المحظورة")
        print("3. فحص طلب اتصال")
        print("4. خروج")

        choice = input("ادخل رقم الاختيار: ")

        if choice == "1":
            firewall.block_ip()
        elif choice == "2":
            firewall.display_blocked()
        elif choice == "3":
            firewall.check_request()
        elif choice == "4":
            print("تم إغلاق نظام جدار الحماية.. شكراً لك! 🤎")
            break
        else:
            print("اختيار غير صحيح، حاولي مرة أخرى.")


# تشغيل النظام
main()
