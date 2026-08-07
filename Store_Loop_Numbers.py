"""
🔢 تخزين أرقام الـ Loop جوة الكائن - Storing Loop Numbers in Object Memory

تطبيق عملي لمفهوم الـ OOP يوضح:
- فائدة تهيئة القوائم جوة __init__ لتخزين البيانات.
- فصل عمليات المعالجة والـ loop في دالة منفصلة.
- حفظ نتائج التكرار بداخل الكائن واستدعائها لاحقاً.
"""


class NumberCollector:

    def __init__(self):
        self.numbers = []  # قائمة لتخزين الأرقام جوة ذاكرة الكائن

    def generate_numbers(self):
        count = 1
        while count <= 10:
            self.numbers.append(count)  # إحفاظ الرقم في القائمة
            print("الرقم الحالي:", count)
            count += 1


# تشغيل البرنامج
collector = NumberCollector()
collector.generate_numbers()

# عرض الأرقام المحفوظة من ذاكرة الكائن
print("\n--- 📜 الأرقام المخزنة جوة الكائن ---")
print(collector.numbers)
