"""
نظام إدارة قناة الفيديوهات والمشاهدات - Video Channel Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام كلاس لتمثيل بيانات الفيديو (الاسم، عدد المشاهدات، وعدد الإعجابات).
- استخدام القواميس (Dictionaries) لادارة الفيديوهات، زيادة المشاهدات والإعجابات، والبحث والحذف الفوري.
"""

class VideoItem:
    def __init__(self, name, views, likes):
        self.name = name
        self.views = views
        self.likes = likes


class ChannelManager:
    def __init__(self):
        self.videos = {}

    def add_video(self):
        name = input("ادخل اسم الفيديو: ")
        if name in self.videos:
            print("يوجد فيديو بهذا الاسم مسبقاً")
            return
        
        views = 0
        likes = 0
        
        video = VideoItem(name, views, likes)
        self.videos[name] = video
        print("تم نشر فيديو جديد")

    def show_all_videos(self):
        if not self.videos:
            print("لا يوجد فيديوهات")
            return
        
        print("\n--- كل الفيديوهات ---")
        for name, video in self.videos.items():
            print(f"اسم الفيديو هو {name} | عدد المشاهدات هو {video.views} | عدد الاعجابات هي {video.likes}")

    def search_video(self):
        name = input("ادخل اسم الفيديو: ")
        if name in self.videos:
            video = self.videos[name]
            print(f"اسم الفيديو هو {name} | عدد المشاهدات يساوي {video.views} | عدد الاعجابات يساوي {video.likes}")
        else:
            print("لا يوجد هذا العنوان")

    def update_video(self):
        name = input("ادخل اسم الفيديو: ")
        if name in self.videos:
            video = self.videos[name]
            video.views += 1
            print("تمت زيادة عدد المشاهدات")
        else:
            print("لم اجد اسم هذا الفيديو")

    def update_likes(self):
        name = input("ادخل اسم الفيديو: ")
        if name in self.videos:
            video = self.videos[name]
            video.likes += 1
            print("تمت زيادة عدد الاعجابات")
        else:
            print("لم اجد اسم هذا الفيديو")

    def delete_video(self):
        name = input("ادخل اسم الفيديو الذي تريد حذفه: ")
        if name in self.videos:
            del self.videos[name]
            print("تم حذف هذا الفيديو")
        else:
            print("لا يوجد فيديو بهذا الاسم للحذفه")


def main():
    manager = ChannelManager()
    while True:
        print("\n1. اضافة فيديو")
        print("2. عرض كل الفيديوهات")
        print("3. البحث عن فيديو")
        print("4. تحديث المشاهدات")
        print("5. تحديث الاعجابات")
        print("6. حذف فيديو")
        print("7. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_video()
        elif choice == "2":
            manager.show_all_videos()
        elif choice == "3":
            manager.search_video()
        elif choice == "4":
            manager.update_video()
        elif choice == "5":
            manager.update_likes()
        elif choice == "6":
            manager.delete_video()
        elif choice == "7":
            print("خروج")
            break
        else:
            print("ادخل رقم مناسب للاختيار")


main()
