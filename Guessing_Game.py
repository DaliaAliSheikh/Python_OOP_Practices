"""
🎯 لعبة تخمين الرقم السري - Number Guessing Game

تطبيق عملي لمفاهيم الـ OOP يجمع بين:
- الـ while loop والعد التنازلي للمحاولات (Counter)
- الشروط والتلميحات (Conditional Statements)
- حفظ وقراءة التخمينات باستخدام القوائم (Lists)
"""


class GuessingGame:

    def __init__(self):
        self.secret = 7  # الرقم السري المطلوب تخمينه
        self.tries = 5  # عدد المحاولات المتاحة
        self.history = []  # قائمة لتخزين تخمينات المستخدم

    def start_game(self):
        print("أنا فكرت في رقم من 1 إلى 10 وعندك 5 محاولات فقط!")

        while self.tries > 0:
            guess = int(input("أدخل الرقم المتوقع: "))
            self.history.append(guess)

            if guess == self.secret:
                print("🎉 مبروك! فزت والتخمين صح!")
                break
            elif guess < self.secret:
                print("💡 الرقم أفقياً أكبر من كده!")
            else:
                print("💡 الرقم أفقياً أصغر من كده!")

            self.tries -= 1

        if self.tries == 0:
            print("\n❌ خسرِت! المحاولات انتهت والرقم الصحيح كان:", self.secret)
            print("تخميناتك السابقة كانت:")
            for item in self.history:
                print("-", item)


# تشغيل اللعبة
game = GuessingGame()
game.start_game()
