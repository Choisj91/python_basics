import math

class JungTriangle():
    def __init__(self, length, name):
        self.length = length
        self.name = name

    def get_area(self):
        return (math.sqrt(3) / 2) * self.length**2

    def get_name(self):
        return self.name

    def __del__(self):
        print("object is deleted")

trian = JungTriangle(6,'Choi')

trian.length
print(trian.get_area(), trian.get_name)