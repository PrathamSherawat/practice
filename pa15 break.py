n=int(input("enter the no."))
i=2
while(i<=n//2):
    if(n%i==0):
        break
    i=i+1
if(i==n//2+1):
    print("it is prime no.")
else:
    print("it is not prime no.")
