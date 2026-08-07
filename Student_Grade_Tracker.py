"""
🎓 نظام تتبع وتحليل درجات الطلاب - Student Grade Tracker

تطبيق عملي لمفاهيم الـ OOP يجمع بين:
- الـ while loop واستخدام continue للتحقق من صحة المدخلات (Data Validation)
- تصنيف التقديرات باستخدام الشروط (If-Elif-Else)
- حساب المتوسط الحسابي (Average) وأعلى درجة (Max Grade) باستخدام دوال القوائم
"""


class GradeTracker:

    def __init__(self):
        self.grades = []  # قائمة لتخزين الدرجات المقبولة فقط

    def process_grades(self):
        print("--- 🎓 نظام تسجيل وتحديد تقديرات الدرجات ---")
        print("يرجى تسجيل 5 درجات (من 0 إلى 100):\n")

        count = 1
        while count <= 5:
            score = int(input(f"أدخل الدرجة رقم {count}: "))

            # التحقق من أن الدرجة في النطاق الصحيح
            if score < 0 or score > 100:
                print("❌ خطأ: الدرجة لازم تكون من 0 إلى 100! حاول مرة أخرى.")
                continue

            self.grades.append(score)

            # تحديد التقدير
            if score > 90:
                print("✨ التقدير: ممتاز")
            elif score > 70:
                print("👍 التقدير: جيد")
            elif score > 50:
                print("👌 التقدير: مقبول")
            else:
                print("⚠️ التقدير: راسب")

            count += 1

        print("\n--- 📜 قائمة الدرجات المسجلة ---")
        for g in self.grades:
            print("-", g)

        # حساب المتوسط وأعلى درجة
        average = sum(self.grades) / len(self.grades)
        highest = max(self.grades)

        print("\n--- 📊 الإحصائيات النهائية ---")
        print("المتوسط الحسابي للدرجات:", average)
        print("أعلى درجة تم تحقيقها:", highest)


# تشغيل البرنامج
tracker = GradeTracker()
tracker.process_grades()
