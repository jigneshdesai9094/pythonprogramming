nc=(500,200,100,50,20,10,5,2,1)
price=int(input("Enter Price : "))
c=0
mycouter=0
k=0
p1=0
x=0
for i in range(0,len(nc)):
    
    for j in range(0,int(price/nc[i])):
        
        mycouter=0
        print("-------------")
        if(j==0):
            n=int(price/nc[i])
        else:
            n=int((price-(nc[i]*j))/nc[i])
        mys="{} : {}".format(nc[i],n)
    
        p=int(price-(n*nc[i]))
        if(p==0):
          print("{} : {}".format(nc[i],n))
        #print(p)
        if(i==len(nc)-1): 
            c+=1
            break
        if(x<len(nc)-1):
         x=i+1
        while(p!=0):
             
             k=0
             p1=p
            # print("my p  x ",p,x)
             for k in range(0,int(p/nc[x])):
              
                mycouter=0
                print("-------------")
                print(mys)
                if(k==0):
                    n1=int(p/nc[x])
                else:
                    n1=int((p-(nc[x]*k))/nc[x])
                print("{} : {}".format(nc[x],n1))
                p1=int(p-(n1*nc[x]))
                if(x==len(nc)-1):
                    
                    break
                if(p1!=0):
                    x2=x+1
                    while(p1!=0):
                    
                     n3=int(p1/nc[x2])
                     print("{} : {}".format(nc[x2],n3))
                     p1=p1-(n3*nc[x2])  
                     x2+=1
                c+=1
                mycouter+=1
             '''if(k==0):
               print(mys)'''
             if(x<len(nc)-1):
                x+=1
             if(x==len(nc)-1):
                 print(mys)
                 p=0
                 p1=0
             p=p1
        if(mycouter==0):
            c+=1   
print("Total Combination : ",c)