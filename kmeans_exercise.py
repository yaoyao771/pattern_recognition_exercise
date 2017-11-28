from numpy import *
from math import sqrt
import itertools
'''
笛卡尔坐标系中计算两点距离
'''
def distance(a, b):
    sum = 0
    for dimension in range(len(a)):
        difference_sq = (a[dimension] - b[dimension]) ** 2
        sum+=difference_sq
    return sqrt(sum)

'''
更新聚点坐标
'''
def center(class1,class2):
    x,y=zip(*class1)
    j,k=zip(*class2)
    center1=(sum(x)/len(x),sum(y)/len(y))
    center2=(sum(j)/len(j),sum(k)/len(k))
    return center1,center2
'''
根据新的聚点重新分类
'''
def updateclass(data,center1,center2):

    class1,class2=[],[]
    for i in range (len(data)):
        if distance(data[i],center1)>=distance(data[i],center2):
            class2.append(data[i])
        else:
            class1.append(data[i])
    print(class1)
    print(class2)
    return (class1,class2)

'''
if 本次更新后的聚点与上次更新后的聚点相同
结束循环，输出分出的两类点坐标
elif 本次更新后的聚点与前一次的不一样
继续循环
'''
def kmeans(data,class1,class2,center1,center2):
    old_center1, old_center2 = [],[]
    while old_center1!=center1 or old_center2!=center2:
        old_center1,old_center2=center1,center2
#        center(class1,class2)
        updateclass(data,center1,center2)
        center(class1,class2)
    print (class1)
    print (class2)
if __name__=="__main__"
    data=[[0,0],[3,8],[2,2],[1,1],[5,3],[4,8],[6,3],[5,4],[6,4],[7,5]]         #输入的点
    center1,center2=data[0],data[1]                 #初始聚点
    class1,class2=[],[]
    center(center1,center2)
    kmeans(data,class1,class2,center1,center2)
