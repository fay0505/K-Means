#计算J函数

def J(dict_items):
    sum = 0
    for k in dict_items.keys():
        length = len(dict_items[k])
        for j in range(length):
            sum += dict_items[k][j][-1]

    return sum