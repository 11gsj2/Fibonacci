def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b
for index, fibonacci_number in enumerate(fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
     if index == 10:
         break