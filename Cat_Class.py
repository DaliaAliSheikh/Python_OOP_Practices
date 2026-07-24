"""
🐱 مشروع القطة - Cat Class

برنامج بسيط يوضح مفهوم الكلاس (Class) والكائن (Object) في لغة بايثون، 
حيث يتم إنشاء كلاس باسم Cat يحتوي على خصائص القطة مثل الاسم واللون وطباعتها.
"""


class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


cat1 = Cat("مشمش", "برتقالي")

print(cat1.name, cat1.colour)
