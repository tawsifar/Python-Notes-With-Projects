import math

a=(int(input("Enter the value of side a:")))
b=(int(input("Enter the value of side b:")))

c=math.sqrt(pow(a,2)+pow(b,2))

print(f"The other value is {round(c,3)}")  #round(,) means setting precision
