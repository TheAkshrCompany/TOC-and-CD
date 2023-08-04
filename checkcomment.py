string=input("Enter the string")
arr=list(string)
if(ord(arr[0])==35): # ascii value of hash is 35
    print("its a comment ")
else:
    print("its not a comment")
