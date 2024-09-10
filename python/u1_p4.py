li=[10,20,30,40,50,60,70,80,90,100]
low=0
high=9
se=int(input("Enter Element you want to search"))
'''
while(low<=high):
    mid=int((low+high)/2)
    if(li[mid]>se):
        high=mid-1
    elif(li[mid]<se):
        low=mid+1
    else:
        print(se," Element is Found")
        break
else:
     print(se," Element is not Found")
'''
def recur(li,low,high,se):
  if(low<=high):
    mid=int((low+high)/2)
    if(li[mid]>se):
        high=mid-1
        recur(li,low,high,se)
    elif(li[mid]<se):
         low=mid+1
         recur(li,low,high,se)
    else:
        print(se,"element is found")
  else:
      print(se,"Element is not Found")

recur(li,low,high,se)