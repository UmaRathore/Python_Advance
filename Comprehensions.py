# list - comprehension

my_list_char = []

for char in "hello":
    my_list_char.append(char)


print(f'characters appending in a list : {my_list_char}')

my_list_char = [char for char in "hello"]
print(f'list after using comprehension : {my_list_char}')

my_list_num = [num for num in range(1, 10)]
print(f'list using comprehension to generate numbers in range 1-10: {my_list_num}')

my_list_num_multiply2 = [num*2 for num in range(1, 5)]
print(f'list using comprehension to generate numbers multiply by 2: {my_list_num_multiply2}')


# set - comprehension

my_list_char_set = {param for param in "hello"}
print(f'set using comprehension : {my_list_char_set}')

my_list_num_set = {num for num in range(1, 10)}
print(f'list using comprehension to generate numbers in range 1-10: {my_list_num_set}')

# Dictionary - comprehension

salary_dict = {
    'tom': 100,
    'bran': 200,
    'caren': 300
}

incremented_salary = {k: v*2 for k, v in salary_dict.items()}
print(incremented_salary)

my_dict = {num: num*2 for num in [1, 2, 3]}
print(my_dict)

# Exercise for comprehensions, in a set find duplicate values and print them in one line

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({item for item in my_list if my_list.count(item) > 1})

print(duplicates)
