op= input("Enter the oprator(+-/*):")
num1= float(input("Enter num1:"))
num2= float(input("Enter num2:"))

if op=="+":
 result=num1+num2
elif op=="-":
 result=num1-num2
elif op=="*":
 result=num1*num2
elif op=="/":
 result=num1/num2
else :
 print("Enter a valid operator !")


print(f"The result is {result}")






