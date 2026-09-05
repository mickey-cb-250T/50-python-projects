from random import randint
class game:
    def __init__(self):
        self.s=randint(10,999)

class generator(game):
    def __init__(self):
        super().__init__()
        a=input("enter your name: ")
        print(f"your mail id is {a}{self.s}@gmail.com ")
p=generator()

