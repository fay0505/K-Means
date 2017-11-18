from operator import  itemgetter
#计算恩格尔系数,并且算出最大和最小的恩格尔系数

def calculate_engle(dict_items):

    for key in dict_items.keys():
        sum = 0
        length = len(dict_items[key])
       # print('len:',length)

        #对每一个城市的各项支出求和
        for j in range(length):
            sum += dict_items[key][j]

        engle  = dict_items[key][0] / sum
        dict_items[key] = engle #将字典中的城市所对应的值更改为恩格尔系数


    L = sorted(dict_items.items(), key = itemgetter(1))
    max_engle = L[-1][1]
    min_engle = L[0][1]


    return dict_items, max_engle, min_engle

