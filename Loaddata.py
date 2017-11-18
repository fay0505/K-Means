#读取数据,并用字典存储数据

def loaddata(path):

    with open(path, 'r') as f:
        lines = f.readlines()
        data = {}   #存储城市和对应的每项支出

        for line in lines:
            tmp = line.split(',')
            city_name = tmp[0]
            cost_list = []   #存储每个城市的各项支出
            for i in range(1, len(tmp)):
                if i != len(tmp) - 1:
                    cost_list.append(float(tmp[i]))
                else:
                    cost_list.append(float(tmp[i].split('\n')[0]))
            data[city_name] = cost_list
    #print(data)
    return data



