nums = [1, 2, 3]
squares = []
for n in nums:
    squares.append(n * 2)

s = [n * 2 for n in nums] # we cant use while loop in list comp   it doesnt suppor for whilw loop
print(s)