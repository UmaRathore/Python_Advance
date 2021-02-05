# Generators

def generator_function():
    for i in range(10):
        yield i


g = generator_function()  # creates a new object
print(g)
print(next(g))  # prints next value of g
print(next(g))
g1 = generator_function()  # creates a new object
print(g1)
print(next(g1))  # prints next value of g1
print(next(g1))
