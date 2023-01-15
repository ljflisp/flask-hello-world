class Solution:
   def sqrt(self,x):
     l,r= 0,x
     while l+l<r:
       n= (r+1)//2
       if n*n==  x:
         return n
       elif n*n>x:
            r= n
       else:
            l= n
     if l*l== x:
       return l
     if r*r== x:
       return r
     return l

if __name__== "__main__":
  temp= Solution()
  x1= 5
  x2= 10
  print("输入:"+str(x1))
  print("输出:"+str(temp.sqrt(x1)))
  print("输入:"+str(x2))
  print("输出:"+str(temp.sqrt(x2)))