class Quadrangle:
    width = 0
    height = 0
    color = "black"

class Dave:
    data = 0
    name = 'dave'

print(dir(Dave))
print(dir(Quadrangle))

# 인스턴스 선언
square1 = Quadrangle()
square2 = Quadrangle()
dave_object = Dave()

# 객체 square는 Quadrangle의 인스턴스
print(type(square1))


# 객체의 attribute 접근하기
print(square1.color)

square2.color = 'red'
print(square2.color)

print()

# 초간단 연습1
class Rectangle():
    width = 10
    height = 5
    color = 'red'

rec1 = Rectangle()
rec2 = Rectangle()

rec2.width  = 7
rec2.height = 7
rec2.color  = 'blue'

print(rec1.color)
print(rec2.color)

print()

# Method 넣어보기
class Quadrangles():
    width = 0
    height = 0
    color = 'white'

    def get_area(self):
        return self.width * self.height

    def set_area(self, data1, data2):
        self.width = data1
        self.height = data2 

# 객체의 method 접근하기 | 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용
# 객체명.method명
square3 = Quadrangles()
square3.set_area(5,5)

print(square3.width)

# method호출시, 첫번째 인자로 객체 자신이 넣어지기 때문에, self를 method 첫번째 인자로 항상 넣어야 함
print(square3.get_area())
print()

# 한발짝 더 나가보기(심화문제)
class MakeSomeNoise():
    width = 0
    height = 0
    color = 'black'

    def get_area(self):
        return self.width * self.height

    def set_area(self, data1, data2, data3):
        self.width = data1
        self.height = data2
        self.color = data3

jung = MakeSomeNoise()
jics = MakeSomeNoise()

jung.set_area(7,7,'blue')
jics.set_area(10,5,'red')

print(jung.get_area())
print(jics.get_area())