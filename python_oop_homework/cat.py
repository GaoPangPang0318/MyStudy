from python_oop_homework.animal import Animal

class Cat(Animal):
     def __init__(self,name,color,age,gender,fur):
         super().__init__(name,color,age,gender)
         self.fur=fur

     def catch_mouse(self):
         print('本猫一出马，老鼠无影踪。我会抓老鼠哦！')

     def wow(self):
         print("喵喵喵，我是可爱的小花猫！")

if __name__ == '__main__':
    cat=Cat("猫","花","2","母","短毛")
    cat.wow()
    cat.run()
    print(f"我是{cat.name}，我是{cat.color}色的，我今年{cat.age}岁，我是{cat.gender}的，我是{cat.fur}哦！！")

