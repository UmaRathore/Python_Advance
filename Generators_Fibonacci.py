# Fibonacci series using Generators

def fibonacci_generator(number):
    for item in range(number):

        if item == 0:
            num1 = item
            yield item
        elif item == 1:
            num2 = item
            yield item
        else:
            add = num1 + num2
            num1 = num2
            num2 = add
            yield add


# fibonacci using next value of object 'obj'

obj = fibonacci_generator(21)
for j in range(21):
    print(next(obj))

# fibonacci using iterable (generator function)

for j in fibonacci_generator(21):
    print(j)
