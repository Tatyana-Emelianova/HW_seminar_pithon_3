
def binary ():
    n_10 = int(input("n_10 --> "))
    list = []
    x = n_10
    n_2 = ""
    while x>0:
        y = x - x//2*2
        x = x//2
        list.append(y)

    list.reverse()

    n_2="".join(map(str,list))

    print(n_2)

binary ()