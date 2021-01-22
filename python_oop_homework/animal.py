
class Animal:
    def __init__(self,name,color,age,gender):
        self.name=name
        self.color=color
        self.age=age
        self.gender=gender

    def run(self):
        print(f'我是{self.name}。我可以跑跑跑，像风一样跑！')

    def wow(self):
        print(f'我是{self.name}。我会嗷嗷叫，像雷一样大哦！')