list1 = [1, 2, 4]
list2 = [0, 1, 3]

def func(list1, list2):
    res = []
    while not list1 and not list2:
        if list1[0] <= list2[0]:
            res.append(list1.pop(0))
        else:
            res.append(list2.pop(0))
        print(list1, list2, sep='\n')
    if list1:
        res += list1
    if list2:
        res += list2
    return res

print(func(list1, list2))