import pandas
import pickle
from collections import Counter

import math
import pandas as pd


def getdata(path,name):
    excel_path = path # Excel文件路径
    sheet_name = name  #工作表名称

    # 使用pandas的read_excel函数读取数据
    df = pd.read_excel(excel_path,
                       sheet_name=sheet_name) # 将DataFrame转换为字典\n# to_dict的参数'records'表示将每行转换为一个字典，整个DataFrame变为字典列表
    #data_dict_list = df.to_dict('records')
    data_list = df.values.tolist()
    # 输出结果查看
    print(data_list)
    return data_list

def changedata(list_path,std):#根据实际情况进行创建对应的std,好像没什么用
    nlist=list_path
    h_num=len(nlist)
    l_num=len(nlist[0])
    for i in range(0,h_num):
        for j in range(0,l_num):
            if nlist[i][j] in std.keys():
                nlist[i][j]=std.get(nlist[i][j])
    return nlist

def new(list_path,condition,path1):#path是分支条件，需按照情况改变
    n_list=[]
    list = list_path
    h_num = len(list)
    for i in range(0, h_num):
        if list[i][condition]==path1:
             dire_list=list[i][:condition]
             dire_list.extend(list[i][condition+1:])
             #print(dire_list)
            # dire_list.extend(list[i+1:])
             n_list.append(dire_list)
             #n_list.append(list[i])
    #print(n_list)
    return n_list

# def entropy(list):####修改为最后一个值,计算原熵
#     direct_path = len(list[0])-1
#     data_length = len(list)
#     if data_length == 0:
#         return 0
#     l=[]
#     for i in range(0,data_length):
#         l.append(list[i][direct_path])
#     counts=Counter(l)#记录频数
#     #print(counts)
#     probabilities= [count / data_length for count in counts.values()]
#     #print(probabilities)
#     # 使用概率计算熵值
#     entropy = sum(-probability * math.log(probability, 2) for probability in probabilities if probability !=0 )
#
#     return entropy

def entropy(list):
    direct_path = len(list[0]) - 1  # 获取最后一个值的索引
    data_length = len(list)
    if data_length == 0:
        return 0
    l = [item[direct_path] for item in list]  # 提取最后一个值
    counts = {}  # 使用字典记录频数
    for vals in list:
       current=vals[-1]
       if current not in counts.keys():
           counts[current]=0
       counts[current]+=1
    entropy=0
    for key in counts:# 计算概率
        probability=float(counts[key])/data_length
        entropy -= probability*math.log(probability,2) # 使用概率计算熵值
    return entropy

def addentropy(list,path):#加权熵,path为分支参数
    data_length=len(list)
    l=[]
    for i in range(0,data_length):
        l.append(list[i][path])
    counts=Counter(l)
    adeps=[]
    #print(counts)
    # probabilities = [count / data_length for count in counts.values()]
    # print(probabilities)
    # adep=sum(probability*entropy(new(list,path,condition),2) for condition in counts.keys() for probability in probabilities)
    for condition in counts.keys():
        probility=counts.get(condition)/data_length
        adeps.append(probility*entropy(new(list,path,condition)))##############记得换label
    adep=sum(adeps)
    return adep

# def addentropy(list):
#     basetropy=entropy(list)
#     numfeat=len(list[0])-1
#     bestinfogain=0
#     bestfeat=-1
#     for i in range(numfeat):
#         featlist=[example[i] for example in list]
#         uniquevals=set(featlist)
#         addentropy=0
#         for val in uniquevals:
#             subdata=new(list,i,val)
#             prob=len(subdata)/float(len(list))
#             addentropy+=prob*entropy(subdata)
#         infogain=basetropy-addentropy
#         if(infogain>basetropy):
#             bestinfogain=infogain
#             bestfeat=i
#     return bestfeat



def clean(dataSet):
    cleaned_data = list(set(tuple(row) for row in dataSet))
    cleaned_data = [list(row) for row in cleaned_data]

    # 数据类型转换
    for row in cleaned_data:
        for i in range(len(row)):
            if i != len(row) - 1:  # 不处理目标值所在的列
                row[i] = int(row[i])  # 假设所有特征值都应为整数

    # 处理缺失值
    has_missing = any(None in row for row in cleaned_data)
    if has_missing:
        for row in cleaned_data:
            for i in range(len(row)):
                if row[i] is None:
                    row[i] = 1############缺失值赋值
    return cleaned_data

def storetree(tree,filename):
    fw=open(filename,'wb')
    pickle.dump(tree,fw)
    fw.close()

def settree(filename):
    fw=open(filename,'rb')
    return pickle.load(fw)