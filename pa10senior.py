print("TO PRINT THE FACTOR OF A NUMBER")
print("###############################")
n= int (input("ENTER THE NO.:"))
f=0
for i in range (1,(n)+1):
    if (n%i==0):
        print(i)
        f=f+1
print("\n The number of factors in a no.")
print("=",f)
if f==2:
   print(n,"is a prime no.")
else:
    print(n,"is not a prime no.")
   



