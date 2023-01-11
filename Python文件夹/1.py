#向量加法
def add(v1,v2):
  return (v1[0]+v2[0],v1[1]+v2[1])

#add(v1,v2)#调用函数，参数可以自己设置
#print(add((4,3),(-1,1)))
from math import sqrt
def length(v):
  return (v[0]**2+v[1]**2)
  
length((3,4))

#画图
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

class Point():
     def __init__(self,vectors,color=black):
       self.vectors= list(vectors)
       self.color= color

from vector_drawing import *
dino_vectors=[(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4)]
draw(
  Points(*dino_vectors)
)