"""
🎮 نظام نقاط اللعبة - Player Game Points

برنامج يطبق مفاهيم الـ OOP لإدارة نقاط اللاعبين أثناء اللعب،
بحيث يبدأ كل لاعب برصيد نقاط يساوي (0)، ويتم زيادة نقاطه عند الفوز.
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def play(self, new_points):
        if new_points > 0:
            self.points += new_points
            print("رائع!", self.name, "أحرزت:", new_points, "نقاط. | مجموع نقاطك الآن:", self.points)
        else:
            print("النقاط المضافة غير صالحة!")


player1 = Player("Dalia")

# تجربة اللعب وإضافة نقاط
player1.play(10)
player1.play(25)
