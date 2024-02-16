n= int(input("enter the no."))
N=int(input("enter the no. till you want")) 
for i in range(1,N+1):
    if(i%n==0):
        continue
    print(i)
