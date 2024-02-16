print("TO PRINT THE FACTOR OF A NUMBER")
print("###############################")
n= int (input("ENTER THE NO.:"))
f=0
for i in range (2,(n//2)+1):
    if (n%i==0):
        print(i)
        f=f+1
print("\n The number of factors in a no.")
print("=",f)
   


