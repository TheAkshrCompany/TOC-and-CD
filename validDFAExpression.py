string=input("Enter the string ");
arr=list(string)

if(ord(arr[0])>98 and ord(arr[0])<123):
    print("its a valid expression")
elif(ord(arr[0])>65 and ord(arr[0])<98):
    print("its a valid expression")
else:print("its a invalid expression")
