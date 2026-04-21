'''
#-----rhombus-------
n=2
for i in range(n):
    print(" "*(n-i)+"*"*((i*2)+1))
for j in range(n):
    print(" "*((2+j))+"*"*((n*2)-(j+(j+3))))  '''

'''# wap to print a triangle
a=7
for i in range(a):print(' '*(a-i+1),"*"*(2*i+1))'''

'''
a=True+False+True
print(a,type(a))

'''
# -----------------
# k=6
# j=[]
# for i in range(k):
#     j.append(i+1)
#     print(j)

# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6]

# -------------------------

# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

'''k=5
b=1
t=1
for i in range(t,k+1):
    for j in range(1,b+1):
        print(b,end=" ")
    b+=1
    print()'''
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# --------------------

# k=5
# b=1
# t=1
# for i in range(t,k+1):
#     for j in range(1,i+1):
#         print(b,end=" ")
#         b+=1
#     print()

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

'''p=4
for i in range(1,p+1):
    for j in range(1,p+2-i):
        print(j,end=" ")
        j+=1
    print()'''

# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

'''
def is_leap(year):
    if year % 400 == 0:
        return "leap year"
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return "leap year"
    else:
        return "not leap year"


year = int(input("Enter year: "))
print(is_leap(year))'''

import time

start = time.perf_counter()   # start timer

# ---- YOUR CODE STARTS HERE ----
p = 4
for i in range(1, p+1):
    for j in range(1, p+2-i):
        print(j, end=" ")
    print()
# ---- YOUR CODE ENDS HERE ----

end = time.perf_counter()     # end timer

print("\nRuntime:", end - start, "seconds")

