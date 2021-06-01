# Section07-1
# 파이썬 클래스 상세 이해 -> 방대한 어플리케이션의 운용을 위해서는 클래스로 구조화해서 일괄적 기계식 프로그램이 아닌 클래스방식의 코딩을 해야 유지보수의 생산성을 올린다
# 상속을 통한 재활용 & 객체지향프로그래밍의 방향 | 클래스단위로 기능 분류를 하는 것이 큰 프로젝트의 구조
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요 -> 클래스 형태로 코딩을 해서 변수를 할당해서 인스턴스화시켜서 메모리에 올려서 사용
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간 독립적인 저장된 공간!이 POINT
# 클래스 변수 : 직접 사용 가능, 객체 인스턴스보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# Section07-1
# 파이썬 클래스 상세 이해 -> 방대한 어플리케이션의 운용을 위해서는 클래스로 구조화해서 일괄적 기계식 프로그램이 아닌 
# 클래스방식의 코딩을 해야 유지보수의 생산성을 올린다
# 상속을 통한 재활용 & 객체지향프로그래밍의 방향 | 클래스단위로 기능 분류를 하는 것이 큰 프로젝트의 구조
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요 -> 클래스 형태로 코딩을 해서 변수를 할당해서 인스턴스화시켜서 메모리에 올려서 사용
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간(독립적인 저장된 공간!이 POINT)
# 클래스 변수 : 직접 사용 가능, 객체(인스턴스)보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

class SelfTest:
    # 클래스 메소드
    def function1():
        print('function1 called!')
    # 인스턴스 메소드
    # 이거는 인스턴스 Method | self로 인스턴스를 해야 각각의 네임스페이스에 이름을 넣어놨기 때문에 호출이 가능
    # Self가 들어간 것이 Instance함수라는 것을 인지!
    def function2(self):
        print(id(self))   #고유의 인스턴스 네임을 가지게 된다. 그대로 self인자를 전달해줘서 받았기 때문
        print('function2 called!')   

self_test = SelfTest()
# self_test.function1()    # Self인자가 없기 때문에 누구의 function1함수인지 모르는 것이다. 인스턴스로 호출할 수 없다. classmethod는 class에서 호출해야 한다
SelfTest.function1()       # 그래서 class함수로 호출을 해야만 한다
self_test.function2()      # self_test로 인스터스화해서 출력가능!
                           # self가 들어가면 인스턴스함수. self가 없으면 class에서 직접 호출할 수 있는 공통함수로 사용->여러 인스턴스가 공유하는 함수
#인스턴스를 생성해서 호출 가능!
print(id(self_test))
SelfTest.function2(self_test)  #이렇게 되면 네임스페이스를 직접 가지게 된다


# 예재3
# 클래스 변수, 인스턴스 변수

class Warehouse:
    # 클래스 변수
    stock_num = 0               #하나의 변수를 통해서 모든 인스턴스들이 공유하는 패턴! 중복된 코딩을 줄인다!
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1
    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Kim')
user2 = Warehouse('Choi')
user3 = Warehouse('Park')

# 네임스페이스
# self가 아니기 때문에, stock_nm의 숫자는 나오지 않는다
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(Warehouse.__dict__)   #클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

# 자기 네임스페이스(인스턴스)에 없으면 클래스의 네임스페이스를 찾아서 변수를 찾고 출력한다
print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)
