print ("Super Market Sale")
print ("_______**________")
print ("Shopping bill")
print ("       **    ")
b= int( input("enter the bill amount"))
if(b>=30000):
    d=b*.3;
elif(b>=25000):
   d=b*.25;
elif(b>=15000):
    d=b*.2;
elif(b>=10000):
    d=b*.1;
elif(b>=5000):
    d=b*.05;
elif(b<=5000):
    d=b*0;
B=b-d
print("total bill:",b)
print("Discount:",d)
print("you save eitna:",d)
print("payable amount:",B)

    

