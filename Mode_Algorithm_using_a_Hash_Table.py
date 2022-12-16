lst = [7, 8, 8, 8, 8, 14, 14, 25, 30, 30, 30, 30, 32, 32]
#checking method one
def method1(L)->list:
    '''function docstring'''
    set_L = list(set(L))
    count_list = list()
    c = 0
    for i in set_L :
        for j in L :
            if i == j :
                c+=1
        count_list.append(c)
        c = 0
    temp = list()
    for i in range(len(count_list)):
        if count_list[i]==max(count_list) :
            val = set_L[i]
            temp.append(val)
    return temp
print('result for method one :')
for i in method1(lst):
    print(i,end=' ')
#lets work with method two
def method2(L)->list:
    '''function docstring'''
    set_L = list(set(L))
    count_list = list()
    c = 0
    for i in set_L :
        for j in L :
            if i == j :
                c+=1
        count_list.append(c)
        c = 0
    dict_L  = dict()
    for i in range(len(count_list)) :
        key = set_L[i]
        dict_L[key]=count_list[i]
    temp = list()
    for i in dict_L.keys():
        if dict_L[i] == max(count_list):
            temp.append(i)
    return temp
    return dict_L
print('\n')
print('result for method two :')
for i in method2(lst):
    print(i,end=' ')
print('\n')
exit = input('enter any key to exit :')
