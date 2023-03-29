num=float(input("Enter a number: "))
numb= num%2
numbe=num%4
if (numb==0 and numbe==0):
    print("Multiple of 4")
elif(numb==1):
    print("Odd")
else:
    print("Even")
