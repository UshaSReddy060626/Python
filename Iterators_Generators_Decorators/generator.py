def square_generator():
    for i in range(1, 11):
        yield i ** 2
for square in square_generator():
    print(square)