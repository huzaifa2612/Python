class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):

    @staticmethod   # humein self nhi chahiye tha hum sirf prit krhry ha isliye statis likha ha
    def bark():
        print("Bow Bow!")


Dog.bark()   # statis ki wja sy direct class k thorught without making object funciton call ho gya