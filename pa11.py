n=int(input("enter your number:"))
t=n
c=0
while(t!=0):
    m=t%10
    t=t//10
    c=c+1
print("no of digits:",c)


