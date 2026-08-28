"""
نظام إدارة الصالة الرياضية وعضويات الجيم - Gym Membership Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه يوضح:
- إنشاء كلاس لتمثيل بيانات العضو (الاسم، الرقم التعريفي، وشهر الاشتراك).
- إنشاء كلاس لإدارة الأعضاء (إضافة عضو، عرض الكل، البحث بالرقم التعريفي، تجديد الشهور، والحذف).
"""

class GymMember:
    def __init__(self, name, member_id, month):
        self.name = name
        self.member_id = member_id
        self.month = month


class GymManager:
    def __init__(self):
        self.members = []

    def add_member(self):
        name = input("ادخل اسمك: ")
        member_id = int(input("ادخل الرقم التعريفي حقك: "))
        month = int(input("ادخل رقم الشهر الذي اشتركت فيه: "))
        
        member = GymMember(name, member_id, month)
        self.members.append(member)
        print("تمت اضافة عضو جديد")

    def show_all_members(self):
        if len(self.members) == 0:
            print("لا يوجد بيانات")
            return
        
        print("\n--- كل الأعضاء ---")
        for member in self.members:
            print(f"اسمه هو {member.name} | رقمه التعريفي هو {member.member_id} | اشترك في شهر {member.month}")

    def search_member(self):
        target_id = int(input("ادخل رقمك التعريفي: "))
        if len(self.members) == 0:
            print("لا يوجد أعضاء")
            return
        
        found = False
        for member in self.members:
            if member.member_id == target_id:
                print(f"اسمه هو {member.name} | رقمه التعريفي هو {member.member_id} | اشترك في شهر {member.month}")
                found = True
        
        if not found:
            print("لم نجد تفاصيل عن هذا المشترك")

    def remove_member(self):
        target_id = int(input("ادخل الرقم التعريفي للعضو للحذف: "))
        if len(self.members) == 0:
            print("لا يوجد اسماء لحذفها")
            return
        
        found = False
        for member in self.members:
            if member.member_id == target_id:
                self.members.remove(member)
                print("تم حذف العضو")
                found = True
                break
        
        if not found:
            print("لم نجد هذا العضو")

    def renew_subscription(self):
        target_id = int(input("ادخل الرقم التعريفي للعضو: "))
        if len(self.members) == 0:
            print("لا يوجد أعضاء")
            return
        
        found = False
        for member in self.members:
            if target_id == member.member_id:
                months_to_add = int(input("ادخل عدد الشهور التي تريد تجديدها: "))
                member.month += months_to_add
                print("تم تجديد الاشتراك")
                found = True
        
        if not found:
            print("لا يوجد عضو بهذا الرقم لتجديد اشتراكه")


def main():
    manager = GymManager()
    while True:
        print("\n1. اضافة عضو")
        print("2. عرض جميع الأعضاء")
        print("3. بحث عن عضو")
        print("4. حذف بيانات عضو")
        print("5. تجديد الاشتراك")
        print("6. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_member()
        elif choice == "2":
            manager.show_all_members()
        elif choice == "3":
            manager.search_member()
        elif choice == "4":
            manager.remove_member()
        elif choice == "5":
            manager.renew_subscription()
        elif choice == "6":
            print("خروج")
            break
        else:
            print("ادخل رقم من الارقام ال فوق")


main()
