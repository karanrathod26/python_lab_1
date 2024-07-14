num1=int(input("Enter First Num:-"))
num2=int(input("Enter Second Num:-"))
print("Enter which opration would you like to perform?")
ch=input("Enter any of these char for specific operation +,-,*,/:")
result=0
if ch=='+':
    result = num1+num2
elif ch=='-':
    result = num1-num2
elif ch=='*':
    result = num1-num2
elif ch=='/':
    result = num1-num2
else:
    print("Input character is not recognised!")
print(num1,ch,num2,":",result)    