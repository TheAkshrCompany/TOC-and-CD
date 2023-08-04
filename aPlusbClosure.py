string=input("Enter the string ")
arr=list(string)
store=0 #store variable to keep the check of success of iteration
for i in range(0,len(arr)):
        if(arr[i]=="a" or arr[i]=="b" or arr[i]==None):
           pass
           store+=1
        else: 
            break
if(store==len(arr)):
       print("its a valid expression ")
else:
        print("its an invalid expression")
