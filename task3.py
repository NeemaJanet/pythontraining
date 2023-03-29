phone= input("Enter your phone number: ")
if("7" in phone[0]):
   print( '+254' + phone)
elif("254" in phone[0:3]):
   print( '+' + phone[0:]) 
elif("+254" not in phone[0:3]):
   print( '+254' + phone[1:])
elif("07" in phone[0:1]):
   print( '+254' + phone[1:])
elif("01" in phone[0:1]):
   print( '+254' + phone[1:])   
else:
   print(phone)   