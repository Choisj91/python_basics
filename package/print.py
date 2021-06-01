def print1():
    print("I'm handsome guy")

def print2():
    print("I'm Good guy")


# 단위 실행(독립적으로 파일 실행) :: 직접 실행의 경우는, 해당 패키지 있는 곳에서만 단위테스트로 실행해서만 테스트로 확인

if __name__ == "__main__":
    print1()
    print2()

