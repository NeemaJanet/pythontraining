marks = float(input('Enter your marks: '))
if(marks> 79 and marks < 100 ):
    print("A")
elif(marks > 60 and marks < 79 ):
    print("B") 
elif(marks > 49 and marks < 59 ):
    print("C")
elif(marks > 40 and marks < 49 ):
    print("D")
elif(marks < 40):
    print("E")
else:
    print("Invalid")                   