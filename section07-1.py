# Section07-1
# 파이썬 클래스 상세 이해 -> 방대한 어플리케이션의 운용을 위해서는 클래스로 구조화해서 일괄적 기계식 프로그램이 아닌 클래스방식의 코딩을 해야 유지보수의 생산성을 올린다
# 상속을 통한 재활용 & 객체지향프로그래밍의 방향 | 클래스단위로 기능 분류를 하는 것이 큰 프로젝트의 구조
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요 -> 클래스 형태로 코딩을 해서 변수를 할당해서 인스턴스화시켜서 메모리에 올려서 사용
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간(독립적인 저장된 공간!이 POINT)
# 클래스 변수 : 직접 사용 가능, 객체(인스턴스)보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 예제1

# class UserInfo:
#     # 속성(사람의 클래스, 이름, 나이, 성별 등등), 메소드(움직임이 있는 것, 걷다, 뛰다, 누워있다)
#     pass

# class UserInfo:
#     def __init__(self):
#         print("초기화")

#     user1 = UserInfo()

class UserInfo:
    def __init__(self, name):   #클래스를 초기화할 때 사용하는 함수
        self.name = name        #self라는 이 user의 instance 변수 안에 name을 넣어주는 것이다 self라는 자신만의 영역에 name값을 넣어서 저장하는 것이다
                                #하나의 userinfo를 저장하는 어떤 class를 만들어서 이렇게 instance화를 해서 할당해서 독립된 네임스페이스에 저장해서 관리
    def user_info_p(self):
        print("Name: " + self.name) #self.name은 클래스를 사용하는 user instance의 이름

    def __del__(self):
        print("Instance removed!")

#이 namespace안에 전혀 다른 값이 들어가 있다! user1과user2는 전혀 같지 않다
user1 = UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()
print(user1.__dict__)  # 클래스 네임스페이스의 구성을 확인 가능
print(user2.__dict__)

print(id(user1))  #둘다 다른 값을 가지고 있다는 것이 POINT
print(id(user2))

user1.print_info()
user2.print_info()

print('user1 : ', user1.__dict__)  # 클래스 네임스페이스 확인
print('user2 : ', user2.__dict__)

print(user1.name)

# 예제2
# self의 이해
class SelfTest:
    def function1():
        print("function1 called!")   #이거는 클래스 Method | self인자가 없기 때문에 호출이 불가능!
    def function2(self):                 #이거는 인스턴스 Method | self로 인스턴스를 해야 각각의 네임스페이스에 이름을 넣어놨기 때문에 호출이 가능!
        print(id(self))                  #Self가 들어간 것이 Instance함수라는 것을 인지!
        print("function2 called!")            
        

self_test = SelfTest()
self_test.function1()                #function1은 self인자가 없기 때문에 누구의 function1함수인지 모르는 것. 인스턴스로 호출할 수 없다. classmethod는 class에서 호출해야 한다
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function1(self_test)          #self가 들어가면 인스턴스함수. self가 없으면 class에서 직접 호출할 수 있는 공통함수로 사용->여러 인스턴스가 공유하는 함수


f = SelfTest()
# print(dir(f))
print(id(f))
# f.function1() #예외 발생
f.function2()
print(SelfTest.function1())


# print(SelfTest.function2()) #예외 발생


# 예제3
# 클래스 변수 , 인스턴스 변수

# class Warehouse:
#     # 클래스 변수
#     stock_num = 0

#     def __init__(self, name):
#         # 인스턴스 변수
#         self.name = name            #창고의 주인은 Name을 받기로 하기
#         Warehouse.stock_num += 1

#     def __del__(self):
#         Warehouse.stock_num -= 1


# user1 = Warehouse('Kim')
# user2 = Warehouse('Park')

# print(user1.name)
# print(user2.name)
# print(user1.__dict__)
# print(user2.__dict__)
# print(Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)

# # Warehouse.stock_num = 50 # 직접 접근 가능

# print(user1.stock_num)
# print(user2.stock_num)