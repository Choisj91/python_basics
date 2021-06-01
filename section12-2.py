# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/python_basic/resource/database.db')  # 본인 DB 파일 경로

# 커서 바인딩 : 커서 바인딩을 통해서 SQL을 실행할 수 있는 것!
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경 된다.
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
#print('All -> \n', c.fetchall())

print()

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 >', row)

# 순회2 (가장 선호되는 방법)
for row in c.fetchall():
    print('retrieve2 >', row)

# 순회3
# for row in c.execute("SELECT * FROM users ORDER BY id desc"):
#     print('retrieve3 > ', row)

print()

# WHERE Retrieve1 조회 조건
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # 결국 여기는 데이터 없음

# WHERE Retrieve2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2)  # %s %d %f
print('param2', c.fetchone())
print('param2', c.fetchall())

# WHERE Retrieve3(Dictionary형태로 검색)
c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())

# WHERE Retrieve4
param4 = (1, 4)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4', c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())

# WHERE Retrieve6(Dictionary형태로 검색)
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())

# Dump 출력(with문 이용) : 데이터베이스를 BACKUP해서 데이터베이스 재구성하는 방법
with conn:
    # Dump 출력(데이터베이스 백업 시 중요)
    with open('C:/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')