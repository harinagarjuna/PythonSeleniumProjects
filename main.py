# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Desktop():
    company = 'HP'

    def purpose(self):
        print("This is for work purpose")

class Computer():

    def switch_on(self):
        print("computer switched on")

class Laptop(Desktop,Computer):
    def __init__(self):
        self.model=None

    def set_model(self,model):
        self.model = model

    def get_model(self):
        print("This is :",self.model)


laptop = Laptop()
laptop.set_model("workstation")
laptop.get_model()
laptop.purpose()
print(laptop.company)
laptop.switch_on()












# See PyCharm help at https://www.jetbrains.com/help/pycharm/

