from Loaddata import loaddata
from CalculateEngle import calculate_engle
from Kmeans import kmeans

if __name__ == '__main__':

    Path = 'data.txt'
    #对数据进行预处理
    data_dict = loaddata(Path)

    #计算恩格尔系数
    engle_dict ,Max_engle, Min_engle = calculate_engle(data_dict)

    #print(engle_dict)
    #聚类
    K = int(input("请输入K值："))
    result_dict = kmeans(K, engle_dict, Max_engle, Min_engle)

    for m in result_dict.keys():
        cluster = []
        for j in range(len(result_dict[m])):
            cluster.append(result_dict[m][j][0])

        print("质心：", m)
        print(cluster)

