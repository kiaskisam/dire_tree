import function
import function as f
from collections import  Counter
def majoryitycnt(clist):
    s=[]
    for i in range(0,len(clist)):
        s.append(clist[i][0])
    c=Counter(s)
    sorted_dict = dict(sorted(c.items(),key=lambda item: item[1],reverse=True))
    print(sorted_dict)
    return list(sorted_dict.keys())[0]


def getfeat(data):
    feat = []

    # 初始化feat列表内的子列表
    for j in range(len(data[0])):
        feat.append([])

    for j in range(len(data[0])):
        for i in range(len(data)):
            feat[j].append(data[i][j])

    r_feat = [set(f) for f in feat]#不可哈希，不能直接set
    r_feat.pop(-1)
    return r_feat


def choosebestfeat(data):#返回特征值索引
    numfeat=len(data[0])-1
    baseEntrop=f.entropy(data)

    feat=getfeat(data)
    data_length = len(data)
    adeps = []
    for path in range(len(feat)):
     adeps.append( baseEntrop-f.addentropy(data,path))
    #print(adeps)
    return adeps.index(max(adeps))






def createtree(data,labels,featlabels):
    classlist=[example[-1] for example in data]#当该节点数据目标值全部相同,全为yes or no
    #print(data)
    if classlist.count(classlist[0])==len(data):
        return classlist[0]
    if len(data[0])==1:#当特征值只有一个时
        return majoryitycnt(classlist)
    bestfeat=choosebestfeat(data)#选择最好特征
    #print(f"bestfeat:{bestfeat}")
    bestfeatlabel=labels[bestfeat]
    #print(f"bestfeatlabel:{bestfeatlabel}")
    featlabels.append(bestfeatlabel)
    Mytree={bestfeatlabel:{}}#字典型存储,节点：数据（字典）
    del (labels[bestfeat])
    #print(labels)
    featvalue=[value[bestfeat] for value in data]
    uniquevals=set(featvalue)
    #print(uniquevals)

    for values in uniquevals:
        sublabel=labels[:]
        Mytree[bestfeatlabel][values]=createtree(f.new(data,bestfeat,values),sublabel,featlabels)
    return Mytree

# def classify(tree,label,data):
#     it=iter(tree)
#     firstfeat=next(it)
#     seconddirt=tree[firstfeat]
#     featindex=label.index(firstfeat)
#     for key in seconddirt.keys():
#         if data[featindex]==key:
#             if type(seconddirt[key]).__name__=='dirt':
#                 classlabel=classify(seconddirt[key],label,data)
#             else:
#                 classlabel=seconddirt[key]
#     return classlabel

def classify(input_tree, feat_labels, test_vec):
    first_str = list(input_tree.keys())[0]
    second_dict = input_tree[first_str]
    feat_index = feat_labels.index(first_str)
    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if isinstance(second_dict[key], dict):
                class_label = classify(second_dict[key], feat_labels, test_vec)
            else:
                class_label = second_dict[key]
    return class_label