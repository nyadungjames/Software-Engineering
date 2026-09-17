count = 1
total = 0
# BUG 1: SyntaxRrror - Missing colon after while condition. Fixed by adding :
while count <= 5:
    total = total + count
    count = count + 1
# BUG 2: Logic Error - Original was while count < 5 which only sums 1+2+3+4=10. Changed to <= 5 to include 5 and get correct sum 15.
# BUG 3: TypeError - Cannot concatenate str + int. Fixed by converting total to string with str(total).
print("Sum of 1 to 5 is:" + str(total))