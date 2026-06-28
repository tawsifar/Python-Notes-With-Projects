
# indexing = accessing elements of a sequence using []
# index starts at 0 from the left, -1 from the right

num = "123-456-889"
#      0123456789...  (left to right)
#      ....-3-2-1     (right to left)

print(num[0])         # 1 - first character
print(num[2])         # 3 - third character
print(num[-1])        # 9 - last character
print(num[-2])        # 8 - second last character

# slicing - [start:end] end is excluded
print(num[0:4])       # 123- - index 0,1,2,3
print(num[:4])        # 123- - same as above, start defaults to 0
print(num[5:])        # 56-889 - from index 5 to end
print(num[2:8])       # 3-456-

# slicing with step - [start:end:step]
print(num[1:9:2])     # 2-5- - every 2nd character from index 1 to 8
print(num[::2])       # 13-5-8 - every 2nd character of whole string

# negative indexing in slices
print(num[-5:])       # -889 - last 5 characters
print(num[-5:-2])     # -88 - from 5th last to 3rd last

# reversing
print(num[::-1])      # 988-654-321 - step -1 means go backwards

# practical example
phone = "Tawsif: 123-456-789"
print(phone[8:])      # 123-456-789 - extract just the number part
print(phone[:6])      # Tawsif - extract just the name

# Basic CP tricks 
# s[::-1] == s   checks if a string is a palindrome (similar to that previous string reversal trick)
# s[::2]         every other character, useful in pattern problems


#commit test 2