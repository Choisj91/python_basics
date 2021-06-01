# def sum_all(n):
#     total = 0
#     for num in range(1, n+1):
#         total += num
#     return total

# print(sum_all(10))

# def sum_alls(n):
#     return int(n * (n+1) / 2)

# print(sum_alls(10))

# Hash Table 만들기
hash_table = list([i for i in range(10)])
print(hash_table)

def hash_func(key):
    return key % 5

# 우리가 썼던 파이썬의 Dictionary함수와 아주 유사한 형태를 띄게 된다
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('Andy', '0105555333')
storage_data('Jae', '0105555222')
storage_data('Dave', '0105555111')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))
print(hash_table)
