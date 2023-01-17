#向量加法
#def add(v1,v2):
  #return (v1[0]+v2[0],v1[1]+v2[1])

#add(v1,v2)#调用函数，参数可以自己设置
#print(add((4,3),(-1,1)))
#from math import sqrt
#def length(v):
  #return (v[0]**2+v[1]**2)
  
#length((3,4))

#画图
#import matplotlib
#from matplotlib.patches import Polygon
#from matplotlib.collections import PatchCollection

#class Point():
     #def __init__(self,vectors,color=black):
       #self.vectors= list(vectors)
       #self.color= color

#from vector_drawing import *
#dino_vectors=[(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4)]
#draw(
  #Points(*dino_vectors)
#)

class Solution:
  def submatrixSum(self,matrix):
    if not matrix:
      return []
    wide=len(matrix[0])
    depth=len(matrix)
    res= None
    prefixsum=[[0 for j in range(wide+1)]for j in range(depth+1)]
    for dy in range(1,depth+1):
      for dx in range(1,wide+1):
  #prefixsum[dx][dy]= prefixsum[dy-1][dx]+prefixsum[dy][dx-1]-prefixsum[dy-1]+\
             matrix[dy-1][dx+1]
             for y in range(dy):
               for x in range(dx):
                 if prefixsum[dy][dx]== prefixsum[dy][dx]+prefixsum[y][dx]-prefixsum[y][x]:
                   res= [(y,x),(dy-1,dx-1)]
                   return res
                  
if __name__== "__main__":
  arr= [[1,5,7],[3,7,-8],[4,-8,9]]
  s= Solution()
  #print("输入的数组: ",arr)
 # print("输出的结果是: ",s.submatrixSum(arr))

class Solution:
  def searchMatrix(self,matrix,target):
    if matrix== None or len(matrix)== 0:
      return False
    n,m=len(matrix),len(matrix[0])
    x,y=0,m-1
    while x<=n-1 and y>= 0:
      goal= matrix[x][y]
      if target>goal:
        x+= 1
      if target<goal:
        y-= 1
      if target== goal:
        return True
    return  False
    
if __name__== "__main__":
  arr= [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
  target= 3
  s= Solution()
  #print("输入数组: ",arr)
  #print("目标值: ",target)
  #print("输出的结果: ",s.searchMatrix(arr,target))

class Solution:
  def searchMatrix(self,matrix,target):
    if matrix== [] or matrix[0]== []:
      return 0
    row,column=len(matrix),len(matrix[0])
    i,j= row-1,0
    count= 0
    while i>= 0 and j<column:
      if matrix[i][j]== target:
        count+= 1
        i-= 1
        j+= 1
      elif matrix[i][j]<target:
        j+= 1
      elif matrix[i][j]>target:
        i-= 1
    return count
if __name__== "__main__":
  arr= [[1,3,5,7],[2,4,7,8],[3,5,9,10]]
  target= 3
  s= Solution()
  #print("输入的数组: ",arr)
 # print("目标值: ",target)
 # print("该目标的次数: ",s.searchMatrix(arr,target))