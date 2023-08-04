string=input("Enter the string ")
arr=list(string)
store=1 #store variable to keep the check of success of iteration
if(ord(arr[0])==99): # ascii value of c is 99
   for i in range(1,len(arr)):
        if(arr[i]=="a" or arr[i]=="b" or arr[i]==None):
           store+=1
        else: 
            break
   if(store==len(arr)):
       print("its a valid expression ")
   else:
        print("its an invalid expression")

else:
    print("its not a valid expression ")
