def inhalf ():
    my_list = list(map(int, input().split()))
    x = []
    i = 0
    b = 1
    if len(my_list)%2==0:
        my_len = int(len(my_list)/2)
        while i<my_len:
            x.append(my_list[i]*my_list[len(my_list)-b])
            i +=1
            b +=1
    else:
        my_len = int(len(my_list)//2+1)
        while i<(my_len-1):
            x.append(my_list[i]*my_list[len(my_list)-b])
            i +=1
            b +=1
        x.append(my_list[my_len-1])
    print(x)
inhalf ()

# почему не работает то же самое с range???
# my_list = list(map(int, input().split()))
# x = []
# b = 1
# if len(my_list)%2==0:
#     my_len = int(len(my_list)/2)
    
#     for i in range(my_len):
#         x.append((my_list[i]*my_list[len(my_list)-b]))
#         b = b+1
# else:
#     my_len = int(len(my_list)//2+1)
#     for i in range(my_len-1):
#         x.append((my_list[i]*my_list[len(my_list)-b]))
#         b = b+1
#     x.append(my_list[my_len-1])
# print(x)