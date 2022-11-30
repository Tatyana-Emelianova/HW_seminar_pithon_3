def mirror_fibonacci():
    n = int(input("n --> "))
    fib=[0, 1 , 1]
    for i in range (3,n):
        a = fib[i-2] + fib[i-1]
        fib.append(a)

    fib_neg=[]
    count = n
    while count>1:
        b = (fib[count-1])*-1
        fib_neg.append(b)
        count=count-1

    print(fib_neg+fib)

mirror_fibonacci()
