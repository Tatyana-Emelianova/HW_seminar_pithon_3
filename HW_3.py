def fract ():
    my_list = list(map(float, input().split()))
    fractions = []
    for i in range(len(my_list)):
        fractions.append(round(my_list[i]%1,3))
    print(fractions)
    print(max(fractions) - min(fractions))

fract ()