n=int(input("enter the no.s in denomenator"))
x=int(input("enter the no."))
m=0
r=1
for i in range (1,(n+1)):
    r=pow(x,i)/i
    print(r,end=' ')
    m=m+r
print(" \n")
print("sum of the no.",m)
