import random
from math import pow as pow
from operator import itemgetter
from Calculate_J import  J
from copy import  deepcopy

#将质心的取值范围固定在数据中的最大恩格尔系数和最小恩格尔系数之间
def kmeans(k, dict_items, max_engle, min_engle):

    dict_cluster = {}

    tmp_cluster = {}  # 暂时存储聚类后的结果

    J_values = []    #存储每一次聚类之后的J值
    e = 0.0000001     #判断J值收敛的误差范围

    N = 1   #记录迭代次数
    U = []  #初始化质心
    for i in range(0, k):
        tmp = random.uniform(min_engle, max_engle)
        U.append(tmp)
        tmp_cluster[tmp] = []



    flag = 0
    while flag == 0:

            print('第%d次迭代后'%N, '质心为：', U)

            for city_key in dict_items.keys():

                distance = {}  # 存放每个城市恩格尔系数与质心的距离
                engle = dict_items[city_key]
                for n in tmp_cluster.keys():

                    d = pow(n -engle, 2)
                    distance[n] = d

                # 将distance按照字典的值进行排序,选出最小距离
                L = sorted(distance.items(), key=itemgetter(1))
                tmp_cluster[L[0][0]].append((city_key, engle, L[0][1]))

            dict_cluster = deepcopy(tmp_cluster)
            #print('聚类后结果',dict_cluster)
            J_values.append(J(dict_cluster))  # 聚类之后的J值

            # 更新一次质心
            N += 1
            U.clear()
            tmp_cluster.clear()
            for m in dict_cluster.keys():
                sum = 0
                for j in range(0, len(dict_cluster[m])):
                    sum += dict_cluster[m][j][1]

                if sum == 0:      #随机生成的质心可能没有一个数据点靠近它
                    U.append(m)
                    print('没有类别的质心：',m)

                else:
                    new_u = sum / len(dict_cluster[m])
                    U.append(new_u)
                    tmp_cluster[new_u] = []


            if len(J_values) != 1:
                t = pow(J_values[-1] - J_values[-2], 2)
                if t <= e:  #已收敛
                    flag = 1



    return dict_cluster






