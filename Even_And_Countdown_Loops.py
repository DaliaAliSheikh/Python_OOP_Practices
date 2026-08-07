"""
🔄 أنماط الـ Loops المتطورة وتخزينها - Advanced Loop Patterns in OOP

تطبيق عملي لمفاهيم الـ OOP يوضح:
- استخراج الأرقام الزوجية باستخدام for loop وشرط باقي القسمة (Modulo %).
- إنشاء عد تنازلي (Countdown) وحفظ تسلسل الأرقام التنازلي بداخل القائمة.
"""


class LoopPatterns:

    def __init__(self):
        self.even_numbers = []  # قائمة لتخزين الأرقام الزوجية
        self.countdown_list = []  # قائمة لتخزين أرقام العد التنازلي

    def generate_even_numbers(self):
        """توليد الأرقام الزوجية من 2 إلى 10 وحفظها"""
        print("--- 🔢 الأرقام الزوجية من 2 إلى 10 ---")
        for num in range(2, 11):
            if num % 2 == 0:
                self.even_numbers.append(num)
                print("رقم زوجي تم العثور عليه:", num)

        print("القائمة المكتملة للأرقام الزوجية:", self.even_numbers)

    def start_countdown(self):
        """عد تنازلي من 5 إلى 1 وحفظ الأرقام"""
        print("\n--- ⏳ بدء العد التنازلي ---")
        count = 5
        while count > 0:
            print("العدد الحالي:", count)
            self.countdown_list.append(count)
            count -= 1

        print("سجل العد التنازلي المخزن:", self.countdown_list)


# تجربة تشغيل الأنماط المختلفة
demo = LoopPatterns()
demo.generate_even_numbers()
demo.start_countdown()
