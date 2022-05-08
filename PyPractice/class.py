# 定义类
class Dog(object):



    # 定义__init__函数、
    def __init__(self, name, b, sex):
        self.name = name
        self.age = b
        self.sex = sex
        print(f"我叫{self.name},{self.age}我是__init__,我被调用{self.sex}")


    # 在类中定义的函数，称为方法
    def play(self, tall):
        self.high = tall
        print(f"小狗快乐的玩耍中。。。{self.high}")
    
    def wang(self):
        print("我是小狗，我正在汪汪的叫")

# 创建对象
dog = Dog("haha","liu","gun")

dog.play("180")
dog.wang()



class Animal(Dog):
    def __init__(self, name, b, sex):

        # 调用狗类的初始化方法
        super().__init__(name, b, sex)

animal = Animal("pege", "keke", "boy")

animal.wang()






class Dog():
    pass

class Dog:
    pass