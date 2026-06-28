# format specifiers = {: flags} used to control how values are displayed
# flags:
# .nf     = round to n decimal places
# :n      = allocate n total spaces
# :0n     = allocate n spaces and zero pad
# :<      = left align
# :>      = right align
# :^      = center align
# :+      = show + for positive, - for negative
# :space  = space before positive numbers
# :,      = comma as thousand separator

price1 = 23.213123
price2 = -55.66
price3 = 25
price4 = 20000.1234
price5 = -2000.124

# decimal places
print(f"{price1:.2f}")      # 23.21
print(f"{price1:.4f}")      # 23.2131

# total width allocation
print(f"{price2:10}")       # -55.66 with 10 total spaces from left
print(f"{price1:020}")      # 0000000000023.213123 - zero padded to 20 digits

# alignment
print(f"|{price3:<15}|")    # |25             | - left align
print(f"|{price3:G<15}|")   # |25GGGGGGGGGGG| - left align, fill with G
print(f"|{price3:>15}|")    # |             25| - right align
print(f"|{price3:G>15}|")   # |GGGGGGGGGGGGG25| - right align, fill with G
print(f"|{price3:^15}|")    # |      25       | - center align
print(f"|{price3:F^15}|")   # |FFFFFF25FFFFFFF| - center align, fill with F

# signs
print(f"|{price2:+}|")      # |-55.66| - + flag doesnt remove minus
print(f"|{price2: }|")      # |-55.66| - space doesnt remove minus either
print(f"|{price3:+}|")      # |+25|    - + adds plus sign for positive numbers
print(f"|{price3: }|")      # | 25|    - space added before positive numbers

# thousand separator
print(f"|{price4:,}|")      # |20,000.1234|
print(f"|{price5:,}|")      # |-2,000.124|

# combining flags
print(f"|{price4:,.2f}|")   # |20,000.12|   - comma + 2 decimal places
print(f"|{price4:+,.3f}|")  # |+20,000.123| - plus + comma + 3 decimal places
print(f"|{price5:+,.3f}|")  # |-2,000.124|  - plus doesnt override minus

# basic CP usage (optional)
# print(f"{answer:.6f}")    # many CP problems ask for 6 decimal place float output
# print(f"{n:>10}")         # useful for formatting table style output in problems