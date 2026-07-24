"""
🎮 كلاس اللاعب - Player Class

برنامج يطبق مفاهيم الـ OOP لإدارة نقاط اللاعبين في لعبة،
مع التحقق من أن النقاط المضافة موجبة قبل تحديث رصيد النقاط الإجمالي.
"""


class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def add_points(self, point):
        if point > 0:
            self.points += point
            print(self.name, "أضيفت له:", point, "| إجمالي النقاط:", self.points)
        else:
            print("النقاط لازم تكون موجبة!")


player1 = Player("Ali", 60)
player1.add_points(0)

player2 = Player("Ahmed", 50)
player2.add_points(4)
