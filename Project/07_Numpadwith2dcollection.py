#this is too easy to be added in exercises - never mind
#we're using tuple, cz we are not changing the values-within anyway
numpad= ({7,8,9},
        {4,5,6},
        {1,2,3},
        {"*","0","#"})

for num in numpad:
    for x in num:
        print(x, end=" ")
    print()