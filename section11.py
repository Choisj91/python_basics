# Section11
# 파이썬 외부 파일 처리 이해
# 파이썬 Excel, CSV 파일 읽기 및 쓰기
# CSV 읽기
# CSV 쓰기
# XSL, XLSX 읽기
# 패키지 설치

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵 ::1행의 내용을 SKIP하는 것
    # 확인
    print(reader)
    print(type(reader))   # 클래스안의 어떤 리스트 형식으로 적재
    # print(dir(reader))  # __iter__ 확인 => 반복문에서 사용 가능
    # print()

    for c in reader:
        print(c)          # 하나의 Row가 LIST로 나옴

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자 선택 문자열 기준으로 SPLIT으로 반환
    # next(reader) Header 스킵
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        print(c)

# 예제3 (Dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f) #Dict을 전환해서 보여줄 수 있는 메소드 사용!
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-----')

# 예제4 : 2차원 LIST
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

with open('./resource/sample3.csv', 'w', newline='') as f:  # newline='' 줄바꿈 없애줘!
    wt = csv.writer(f)
    # dir 확인
    print(dir(wt))
    print(type(wt))
    for v in wt:
        wt.writerow(v)

# 예제5 : 이미 검증됐어. 전부 다 써도 돼!의 경우
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    # dir 확인
    print(dir(wt))
    print(type(wt))

    wt.writerows(w)