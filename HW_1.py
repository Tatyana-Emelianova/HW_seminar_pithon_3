
def indexes_odd():
    a = list(map(int, input().split()))
    nechet=[]
    # print (sum(a[::2])) - как суммировать отбросив 0-й элемент???
    for i in range(len(a)):
        if i%2==1:
            nechet.append(a[i])
    print(nechet)
    print("Сумма элементов с нечетными индексами", sum(nechet))

indexes_odd()