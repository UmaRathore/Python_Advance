from functools import reduce

# Functions are defined so that it has no side effects and are separated from outside world


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    print(f'new list is :  {new_list}')


multiply_by2([1, 2, 3])

# map() - define the action and the iterables

my_list = [1, 2, 3]


def addition_by3(li):
    return li+3


print(f'list after addition of 3 :{list(map(addition_by3, my_list))}') # map() creates a new list
print(f'Predefined list for addition of 3 : {my_list}') # the list is immutable it is not changed by the function

# filter() - filters data on basis of given condition


def only_even(number):

    if number % 2 == 0:
        return number


print('List to find even numbers : [1,2,3,4,5,6,7,8]')
print(f'Even numbers : {list(filter(only_even, [1,2,3,4,5,6,7,8]))}')

# zip() - combines data in tuples on basis of index numbers

user_name = ['Tom', 'Jase', 'Alice', 'Gilly']
Phone_numbers = [111,222,333,444]

print(f'Zipped vales : {list(zip(user_name, Phone_numbers))}')

# reduce() - reduces the list by adding the items in list


def sum_values(acc, item):
    return acc+item


print(f'Reduced value : {reduce(sum_values, [1, 2, 3], 10)}')

# Lambda expressions

print(f'Lambda with map function (multiply item by 2) : {list(map(lambda item: item*2, [1, 2, 3]))}')
print(f'Lambda with filter(Even numbers) function : {list(filter(lambda item: item % 2 == 0, [1, 2, 3, 4]))}')
print(f'Lambda with reduce(add item of list with 10) function : {reduce((lambda item, acc: item+acc), [5, 10, 15], 10)}')
