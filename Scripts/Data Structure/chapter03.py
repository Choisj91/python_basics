# 일반적인 hash 함수 구현
# hash_table = list([i for i in range(10)])
# print(hash_table)

# def hash_func(key):
#     return key % 5

# data1 = 'Andy'
# data2 = 'Dave'
# data3 = 'Trump'
# data4 = 'Jae'

# print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
# print(ord(data1[0]), ord(data2[0]), hash_func(ord(data3[0])))

# def storage_data(data, value):
#     key = ord(data[0])
#     hash_address = hash_func(key)
#     hash_table[hash_address] = value

# storage_data('Jae','111111')
# storage_data('David','222222')
# storage_data('Benjamin','333333')

# def get_data(data):
#     key = ord(data[0])
#     hash_address = hash_func(key)
#     return hash_table[hash_address]

# print(get_data('Jae'))
# print(get_data('David'))
# print(get_data('Benjamin'))
# print(hash_table)

# Chaining 기법
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_func(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None




