class Coin(object):
  def __init__(self,name,weight):
    self.name=name
    self.weight=weight

class FakeCoin(object):
  def __init__(self,char_weights):
    self.coins=[Coin(part[0],part[1]) for part in char_weights ]

  def coins_weight(self,low,height):
    sum_weight=0
    for i in range(low,height):
      sum_weight=sum_weight+self.coins[i].weight
    return sum_weight

  def find_fake_coin(self,low,height):
    if height-low>1:
      middle=int((low+height)/2)
      left_weight=self.coins_weight(low,middle)
      right_weight=self.coins_weight(middle,height)
      if left_weight==right_weight:
         print("no fake coin")
         return
      elif left_weight>right_weight:
         print("each coin has  %d  one,fake coin is on right"%((height-low)/2))
         self.find_fake_coin(middle,height)
      else:
         print('each coin has  %d  one,fake coin is on left'%((height-low)/2))
         self.find_fake_coin(low,middle)
    else:
      middle=int((low+height)/2)
      print("find  %s  is fake coin"%self.coins[middle].name)

if __name__=="__main__":
  char_weights=[]
  for i in range(1,17):
    if i==5:
      char_weights.append(("coin"+str(i),0))
    else:
      char_weights.append(("coin"+str(i),1))
  fake_coins=FakeCoin(char_weights)
  fake_coins.find_fake_coin(0,16)
