n=int(input("enter your number:"))
t=n
c=0
r=0
while(t!=0):
    m=t%10
    t=t//10
    c=c+1
    r=r*10+m
print("no of digits:",c)
print("original no.",n)
print("reverse no.",r)
if r>=n:
    print("true")
    print("\n")
else:
    print("sorry")

