foods=[]
prices=[]
total=0
print("Enter the name of foods and their prices(pres q to quit)")

while True:
    food= input("Enter the name of the food:")
    if (food=="q"):
     break
    else :
     foods.append(food)
     price=float(input(f"Enter the price of {food} $:"))
     prices.append(price)

print("---------Your cart----------")
 
for food in foods:
   print(food,end=" ")
print()
for price in prices:
  total+=price 
print(f"Your Total is $:{total}")

