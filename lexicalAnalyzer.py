
# this code is act for simple calcutor for lexical anaylsis
# Expected input: a = b + 5
code=input("Enter the source code ")
pretokenized_code=code.split(" ")
print(pretokenized_code)
operators=["=","+","-","*","/"]
loopvalue=len(pretokenized_code)
for x in range(0,loopvalue):
    if(ord(pretokenized_code[x][0])>98 and ord(pretokenized_code[x][0])<123):
         print("identifier:"+pretokenized_code[x])
    elif(ord(pretokenized_code[x][0])>65 and ord(pretokenized_code[x][0])<98):
         print("identifier:"+pretokenized_code[x])
    elif(ord(pretokenized_code[x])>47 and ord(pretokenized_code[x])<58):
        print("Integer: "+pretokenized_code[x])
    elif pretokenized_code[x] in operators:
        print("operator: "+pretokenized_code[x])
    else:
        print("Invalid Expression")
