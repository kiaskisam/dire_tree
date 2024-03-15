import function
import tree
import function as f
import plottree
from collections import Counter
# list=f.getdata("./a.xlsx",'Sheet1')
# labels1=['weather','temperature']
# tr=tree.createtree(list,labels1,fa)

#list=f.getdata("./a.xlsx",'Sheet1')
#labels=["weather","temperature"]
#print(f.entropy(list))
# #print(tree.createtree(list,labels,a))
# print(tree.createtree(list,labels,a))
# print()
# new_list=f.new(c_list,1,0)
# new_list1=f.new(c_list,1,1)
# new_list2=f.new(c_list,1,2)

# print(f.entropy(new_list1,2))
# print(f.entropy(new_list2,2))
#print(f.addentropy(list,1))
# print(f.addentropy(list,0))
# dataSet = [
# [0, 0, 0, 0, 'no'],
# [0, 0, 0, 1, 'no'],
# [0, 1, 0, 1, 'yes'],
# [0, 1, 1, 0, 'yes'],
# [0, 0, 0, 0, 'no'],
# [1, 0, 0, 0, 'no'],
# [1, 0, 0, 1, 'no'],
# [1, 1, 1, 1, 'yes'],
# [1, 0, 1, 2, 'yes'],
# [1, 0, 1, 2, 'yes'],
# [2, 0, 1, 2, 'yes'],
# [2, 0, 1, 1, 'yes'],
# [2, 1, 0, 1, 'yes'],
# [2, 1, 0, 2, 'yes'],
# [2, 0, 0, 0, 'no']
# ]
dataSet = [
    [0, 1, 0, 1, 'yes'],
    [0, 0, 1, 2, 'no'],
    [1, 2, 0, 0, 'no'],
    [2, 0, 1, 2, 'yes'],
    [2, 0, 2, 2, 'yes'],
    [2, 2, 1, 2, 'yes'],
    [2, 1, 0, 1, 'yes'],
    [2, 0, 0, 1, 'yes'],
    [2, 2, 1, 0, 'yes'],
    [2, 2, 2, 1, 'no'],
    [0, 2, 2, 1, 'yes'],
    [1, 2, 0, 1, 'no'],
    [2, 2, 2, 2, 'no'],
    [0, 2, 2, 2, 'yes'],
    [0, 2, 0, 2, 'no'],
    [1, 1, 1, 1, 'yes'],
    [0, 2, 2, 1, 'no'],
    [1, 2, 0, 2, 'no'],
    [0, 2, 0, 1, 'no'],
    [1, 1, 0, 1, 'no']
]
fa=[]

# Mytree=tree.createtree(dataSet,labels1,fa)
# f.storetree(Mytree,'storetree.txt')
labels1 = ['F1-AGE', 'F2-WORK', 'F3-HOME', 'F4-LOAN']
tr=f.settree('storetree.txt')
# 可视化决策树


print(tr)
text=[0,1]
textlabel=tree.classify(tr,labels1,text)
print(textlabel)
plottree.createPlot(tr)