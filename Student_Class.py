"""
🎓 كلاس الطالب - Student Class

برنامج يوضح طريقة إضافة دالة (Method) داخل الكلاس لإجراء مهمة معينة،
حيث تم إنشاء دالة تقوم بتعريف اسم الطالب وعمره وطباعة البيانات.
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("اسمي هو", self.name, "عمري هو", self.age)


student1 = Student("Ali", 40)
student1.introduce()
