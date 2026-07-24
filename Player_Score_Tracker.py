"""
🎮 نظام تتبع ونقاط اللاعبين - Player Score Tracker

برنامج يطبق مفاهيم الـ OOP مع القوائم (Lists) والدوال الجاهزة مثل sum()،
يقوم بتسجيل نقاط اللاعب وعرض كل نقطة على حدة ثم حساب المجموع الكلي.
"""


class PlayerScore:

    def __init__(self):
        self.points = []  # قائمة لتخزين النقاط المسجلة

    def add_point(self, point):
        if point > 0:
            self.points.append(point)
            print("تم تسجيل نقطة جديدة:", point)

    def show_score_summary(self):
        print("\n--- 📊 سجل النقاط التفصيلي ---")
        for p in self.points:
            print("نقطة:", p)

        # حساب المجموع الكلي باستخدام sum
        total = sum(self.points)
        print("المجموع الكلي للنقاط هو:", total)


# تجربة البرنامج
player = PlayerScore()
player.add_point(7)
player.add_point(9)

# عرض النتيجة النهائية
player.show_score_summary()
