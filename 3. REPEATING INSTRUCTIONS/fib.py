def fibonacci(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = c
            print(c)

# stating how far the sequence should run
fibonacci(15)
