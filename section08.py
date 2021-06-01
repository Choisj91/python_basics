# Section08
# 파이썬 모듈과 패키지

# 패키지 예제1
# 상대 경로 패키지
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)
from package.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
# 인스턴스 초기화 후에 title을 출력
print("ex2 : ", Fibonacci().title)

# 사용2(클래스) : 여러개의 클래스를 한번에 모두 가지고 오겠다
# 메모리를 너무 많이 차지함. 불필요한 것도 import하기 때문
from package.fibonacci import *

# 사용3(클래스) :: 권장하는 방법
from package.fibonacci import Fibonacci as fb

fb.fib(100)

print("ex1 : ", fb.fib2(400))
print("ex2 : ", fb().title)

#사용4(함수) :: 
import package.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

#사용5(함수) :: 리소스를 낭비하지 말고 딱 필요한 부분만 import해서 사용 권장
from package.calculations import div as d
print("ex5 :", int(d(100,10)))

#사용6 :: builtins->파이썬에서 기본적으로 제공하는 함수 모음
import package.print as p
import builtins
p.print1()
p.print2()
print(dir(builtins)) #이제것 사용했던 함수의 모음이 보임. 빌트인은 import굳이 안해도 자동 적용됨


