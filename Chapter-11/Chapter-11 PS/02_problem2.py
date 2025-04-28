class Animals:
    def show(self):
        pass

class Pets(Animals):
    def show(self):
        pass

class Dog(Pets):
    @staticmethod  #We are using static here because we dont want to use self in bark method     
    def bark():
        print("Dog is making a sound of woof!!!")


a = Dog()
a.bark()
