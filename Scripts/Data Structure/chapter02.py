dataset = [4, True, 'Dave', 2.1, 3]


# [출력표현식 for 요소 in 입력 sequence [if 조건식]]
# int_data = [num for num in dataset if type(num) == int]

# print(int_data)
# print(type(int_data))

# int_square_data = [num*num for num in dataset if type(num) == int]

# print(type(int_square_data))
# print(int_square_data)


# int_number = [num for num in range(1,101) if num % 21 == 0]
# print(int_number)

# Set Comprehension
# int_data = [1, 1, 2, 3, 3, 4]

# square_data_set = {num*num for num in int_data if num > 3}
# print(type(square_data_set))
# print(square_data_set)

# Dictionary comprehension
id_name = {1:'Dave', 2:'David', 3:'Anthony'}

print(type(id_name))
print(id_name.items())

name_id = {key:val for key,val in id_name.items() if key > 1}
print(name_id)