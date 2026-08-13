"""
🧠 نظام الاختبارات والتصحيح التلقائي - Quiz Engine System

تطبيق متقدم جداً يوضح:
- إنشاء كلاس (Question) لتخزين نص السؤال والإجابة الصحيحة.
- إدارة قائمة الأسئلة وحساب النتيجة (Score) في كلاس (QuizManager).
- تفاعل كامل مع المستخدم: إدخال الإجابة، التصحيح التلقائي، وعرض النتيجة النهائية.
"""


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizManager:

    def __init__(self):
        self.questions_list = []  # قائمة كائنات الأسئلة
        self.score = 0  # العداد للنتيجة

    def add_question(self):
        """إضافة سؤال جديد وإجابته النموذجية"""
        q_text = input("أدخل السؤال: ")
        q_answer = input("أدخل الإجابة الصحيحة: ")
        new_q = Question(q_text, q_answer)
        self.questions_list.append(new_q)
        print("✅ تمت إضافة السؤال بنجاح!")

    def show(self):
        """عرض جميع الأسئلة المسجلة"""
        print("\n--- 📜 قائمة الأسئلة المسجلة ---")
        if len(self.questions_list) == 0:
            print("لا توجد أسئلة مسجلة بعد!")
        else:
            for item in self.questions_list:
                print(f"- {item.text}")

    def start_quiz(self):
        """تشغيل الاختبار والتصحيح التلقائي"""
        if len(self.questions_list) == 0:
            print("❌ لا يوجد أسئلة لتشغيل الاختبار! قم بإضافة أسئلة أولاً.")
            return

        self.score = 0  # إعادة تصفيير النتيجة بداية كل اختبار
        print("\n=== 🏁 بدأ الاختبار! ===")

        for k in self.questions_list:
            print(f"\nسؤال: {k.text}")
            user_ans = input("إجابتك: ")

            # المقارنة والتصحيح التلقائي
            if user_ans == k.answer:
                self.score += 1
                print("✅ إجابة صحيحة!")
            else:
                print(f"❌ إجابة خاطئة! الإجابة الصحيحة هي: {k.answer}")

        # التقرير النهائي
        print("\n==========================")
        print(
            f"🎉 انتهى الاختبار! درجتك النهائية هي: {self.score} من {len(self.questions_list)}"
        )
        print("==========================")


def main():
    quiz = QuizManager()

    while True:
        print("\n=== 🧠 نظام إمتحانات الـ Quiz ===")
        print("1. إضافة سؤال")
        print("2. عرض قائمة الأسئلة")
        print("3. تشغيل الاختبار")
        print("4. خروج")

        choice = input("أدخل رقم الاختيار: ")

        if choice == "1":
            quiz.add_question()
        elif choice == "2":
            quiz.show()
        elif choice == "3":
            quiz.start_quiz()
        elif choice == "4":
            print("شكراً لاستخدام النظام.. بالتوفيق! 👋")
            break
        else:
            print("⚠️ اختيار غير صحيح، حاول مرة أخرى.")


# تشغيل البرنامج
main()
