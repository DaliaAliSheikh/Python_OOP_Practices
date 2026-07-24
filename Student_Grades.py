"""
🎓 نظام تقييم درجات الطلاب - Student Grade Evaluator

برنامج يطبق مفاهيم الـ OOP لتقييم نتائج الطلاب في المواد المختلفة،
حيث يتم التحقق من درجة الطالب وتحديد ما إذا كان ناجحاً أم راسباً تلقائياً.
"""


class Student:
    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade

    def check_status(self):
        if self.grade >= 50:
            print(self.name, "ناجحة في مادة", self.subject, "بدرجة:", self.grade)
        else:
            print(self.name, "راسبة في مادة", self.subject, "بدرجة:", self.grade)


student1 = Student("Laila", "برمجة", 90)
student1.check_status()

student2 = Student("Dalia", "Math", 40)
student2.check_status()
