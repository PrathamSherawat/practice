n=int(input("enter your number:"))
t=n
c=0
s=0
S=0
while(t!=0):
    m=t%10
    t=t//10
    c=c+1
    s=s+m
    S=S+(m*m*m)
print("no of digits:",c)
print("sum of digits:",s)
print("armstrong",S)

