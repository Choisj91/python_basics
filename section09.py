# Section09
# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# Open 함수
# 파일 모드의 이해
# 파일 읽기 실습
# 파일 쓰기 실습

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r') #오픈으로 파일의 경로를 여는 것이 기본!
content = f.read()
print(content)
# print(dir(f))
#반드시 close 리소스 반환!!!!
f.close()

print("====================================================")

# # 예제2 :: with의 경우, 자동으로 반환이 되기 때문에 close사용할 필요 없다.
# with open('./resource/review.txt','r') as f:
#     c = f.read()
#     print(c)
#     print(iter(c))

# print("====================================================")

# # 예제3 : 한줄한줄 읽어온다는 사실을 알기
# with open('./resource/review.txt','r') as f:
#     for c in f:
#         print(c.strip())

# print("====================================================")

# # 예제4 : 
# with open('./resource/review.txt','r') as f:
#     content = f.read()
#     print(">",content)
#     content = f.read() # 이미 위에서 커서가 끝으로 갔기 때문에 한번더 읽히지 않음
#     print(">",content)

# print("====================================================")

# 예제5: 한문장 단위로 전처를 할 경우 사용
with open('./resource/review.txt','r') as f:
    line = f.readline() #한줄만 읽는 메소드
    # print(line)

    while line:
        print(line, end='### ')
        line = f.readline()

print(" ")
print("====================================================")

# 예제6
with open('./resource/review.txt','r') as f:
    contents = f.readline()
    for c in contents:
        print(c, end='***** ')

print(" ")
print("====================================================")

# 예제7
# score = []
# with open('./resource/review.txt','r') as f:
#     for line in f:
#         score.append(int(line))
#     print(score)

# print('Average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기
# 예제1
with open('./resource/text1.txt','w') as f:
    f.write('Niceman!\n')

# 예제2
with open('./resource/text1.txt','a') as f:
    f.write('Goodman!\n')

# 예제3
from random import randint

#0부터5까지 총 6번 랜덤인트로 6번을 반복해서 출력
with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6): 
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장 : 리스트 형태를 직접 써보는 것
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
# 파일로 연결해줘서 직접 파일에 쓰는 것도 로그로 나옴. 콘솔에 안나옴
with open('./resource/text4.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)