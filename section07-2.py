# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 자식은 모든 속성, 메소드 사용 가능
# 상속은 객체지향언어에서 주는 메리트가 많다. 
# 코드의 생산성과 유지보수가 좋다. 복잡한 코드를 단순한 하기 위한 방법

class Car:
    """Parent Class"""
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        return 'Car Class "Show My Car!"'

class BMWCar(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color): #type과color는 부모님께 다시 전달해줘야 하는 것이다. 
        super().__init__(type, color)          #부모님에게 물려받은 것은 받은것대로 사용 -> 재사용성
        self.car_name = car_name               #초기화(BMW고유의 네임스페이스)

    def show_model(self) -> None:
        return "Your Car Name is : %s" % self.car_name

class RamboruGini(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color): #type과color는 부모님께 다시 전달해줘야 하는 것이다. 
        super().__init__(type, color)          #부모님에게 물려받은 것은 받은것대로 사용 -> 재사용성
        self.car_name = car_name               #초기화(BMW고유의 네임스페이스)

    def show_model(self) -> None:
        return "Your Car Name is : %s" % self.car_name
    
    def show(self):
        print(super().show()) #부모의 메소드도 호출하고 싶어라고 할 경우 
        return 'Car Info : %s %s %s' % (self.car_name, self.color,self.type)


# 일반 사용 => 이렇게 하면 인스턴스가 생성이 된다!!
model1 = BMWCar('520d', 'sedan', 'red')
print(model1.color) #Super
print(model1.type)  #Super
print(model1.car_name) #Sub
print(model1.show())   #Super
print(model1.show_model()) #Sub
print(model1.__dict__)  #부모에서 초기화된것과 자식이 가지고 있는 것이 공존함


# Method Overriding(오버라이딩) :: 부모의 모든 것을 찾아서 쓰는 것이 아니라 상속받을 것은 받고, 기능을 개선할 경우, 목적에 맞게 메소드를 구현할 경우 
# 부모의 것을 올려타서 자식의 것을 활용하는 것. 자식이 마음에 안들어서 새로운 코드의 구현을 활용하는 것
# 다른 패키지의 모듈 등을 분석해서 내것으로 활용할 수 있는 것이다.
model2 = RamboruGini("220v","suv","Blue")
print(model2.show())

# Parent Method Call
model3 = RamboruGini("110v","sports","Red")
print(model3.show())

# Inheritance Info(상속 정보를 리스트 형태로 반환해주는 것)
print(RamboruGini.mro())

# 예제2
# 다중 상속 :: 너무 많은 다중 상속은 좋지 못하다. 뎁스가 너무 깊으면 좋지 않다. 2개정도가 적당하다.
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())