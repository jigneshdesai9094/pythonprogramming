nc=(500,200,100,50,20,10)
price=int(input("Enter Price : "))
c=0


  



for i in range(0,len(nc)):
    
    for j in range(0,int(price/nc[i])):
        print("-------------")
        if(j==0):
            n=int(price/nc[i])
        else:
            n=int((price-(nc[i]*j))/nc[i])
        print("{} : {}".format(nc[i],n))
        p=int(price-(n*nc[i]))
        #print(p)
        if(p!=0):
             x=i+1
             while(p!=0):
               n=int(p/nc[x])
               print("{} : {}".format(nc[x],n))
               p=p-(n*nc[x])  
               x+=1
        if(i==len(nc)-1):
            break
        c+=1
print("Total Combination : ",c)