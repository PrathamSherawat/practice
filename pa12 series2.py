n=int(input("enter the no.s in denomenator"))
x=int(input("enter the no."))
m=0
s=1
for i in range (1,(n+1)):
    s=(x*x)/i
    print(s,end=' ')
    m=m+s
print(" \n")
print("sum of the no.",m)
