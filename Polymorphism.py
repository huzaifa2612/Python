class Dog:
    def speak(self):
        print("Dog Says: Woof!")

class Cat:
    def speak(self):
        print("Cat Says: Meow!")




animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()