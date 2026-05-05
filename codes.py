'''----------------reversed str------------------'''
# a = 9827463478
# rev = 0
# while a !=0:
#     rev = rev*10+(a % 10)
#     a=a//10
# print(rev)


# def reversed (str):
#     rev=0
#     while str !=0:
#         rev=rev*10+str%10
#         str=str//10
#     return rev
# k=reversed(123456)
# print(k)



'''------------------------multiplication of all digits in a number-----------------'''

# val=int(input("enter a num: "))
# mult=1
# while val>=1:
#     mult= (val % 10)*mult
#     val=val//10
# print(mult)


# def mult(val):
#     value=1
#     while val>=1:
#         value=(val % 10)*value
#         val=val//10
#     return value
# userinput=int(input('enter a value: '))
# print(mult(userinput))

'''------------------factorial-----------'''

# input=int(input('enter a num: '))
# value=1
# for i in range(input+1):
#     if i != 0 :
#         value = value * i
#     else:
#         pass # u can do without else block
# print(value)


# def factorial(num):
#     val=1
#     for i in range(num+1):
#         if i !=0:
#             val=val*i
#         else:
#             print('i am from else block and iam optional for this code')
#     return val
# input=int(input('enter a num: '))
# print(factorial(input))



'''----------------print a fibonacci number of n------------'''

# def fibonacci(n ):
#     val=0
#     for i in range(n +1):
#         if i != 0:
#             val=val+i
#     return val
# input=int(input('enter a value of  n : '))
# print(fibonacci(input))

'''----------------wap to print a fibonacci all numbers of n------------'''

# input=int(input('enter a value : '))
# val=0
# for i in range(input +1):
#     if i != 0:
#         print(val)
#         val=val+i


# def fibonacci(n):
#     val=0
#     for i in range(n +1):
#         if i != 0:
#             print(val)
#             val=val+i
# input=int(input('enter a value of  n : '))
# fibonacci(input)


# def fibonacci(n):
#     a,b=0,1
#     for i in range (n):
#         print(a)
#         a,b=b,a+b
# input=int(input('enter a value of  n : '))
# fibonacci(input)


'''---------------chek a num is prime num or not---------------'''

# num=int(input('enter num: '))
# if num<2:
#     print('its nor a prime')
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print('not prime')
#             break
#     else:
#         print("its a prime")
        

# num=int(input('enter num: '))
# if num<1:
#     print("enter a valid num")
# elif num<2:
#     print('its not a prime')
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print('not prime')
#             break
#     else:
#         print("its a prime")


# def prime(val):
#     if val>2:
#         for i in range(2,val):
#             if val%i==0:
#                 print('not a prime num')
#                 break
#         else:
#             print('yes it is a prime num')
#     else:
#         print('enter valid num')
# userinput=int(input('enter a num: '))
# prime(userinput)

# a=67
# if a<1:
#     print('not prime')
# else:
#     for i in range(2,a):
#         if a % i == 0 :
#             print('not prime')
#             break
#     else:
#         print('prime')

'''--------to find the range of prime numbers-----------'''
# inr=10
# ine=22
# primes=[]
# for j in range(inr,ine+1):
#     isprime=True
#     for i in range(2,int(j**0.5)+1):
#         if j % i == 0 :
#             isprime=False
#             break
#     if isprime==True:
#         primes.append(j)
# print(primes)

# def find_primes(a,b):
#     primes=[]
#     for j in range(a,b+1):
#         isprime=True
#         for i in range(2,int(j**0.5)+1):
#             if j % i == 0 :
#                 isprime=False
#                 break
#         if isprime:
#             primes.append(j)
#     return primes
# k=find_primes(10,20)
# print(k)


'''------------------------ simple interest -------------------'''

# A=int(input('enter your money: '))
# B=int(input('enter interest_percentage rate per year: '))
# C=int(input('enter C in years: '))
# interest=A*(B/100)*C # or A*B*C/100    # because 5*10/100*20 =  5/1*10/100*20/1   think about this line for better understanding
# print(f'simple interest {interest}')
# print(f'your money with simple interest is: {interest}')


# print((5*10*20/100)==5*(10/100)*20)

'''------------------------ compound interest -------------------'''

# import time
# start = time.perf_counter() 
# # WAP to calculate COMPOUND interest of 1000 for 2years with 10% interest rate   (EXAMPLE QUESTION)
# def compound_interest(A,B,C):
#     num=1
#     C_interest=(A*(B/100)*1)
#     for i in range (C-1):
#         C_interest+=(A*(B/100))+(C_interest*(B/100))
#         num+=1
#     return (f'coumpound interest per {C} years is {C_interest}') 

# A=int(input('enter your money: '))
# B=int(input('enter interest_percentage rate per year: '))
# C=int(input('enter for years: '))
# print(compound_interest(A,B,C))

# end = time.perf_counter() 
# print("\nRuntime:", end - start, "seconds")


'''----------------------list comprehension----------------------------'''

# squares = [i ** 2 for i in range(10)]
# print("Squares:", squares)

'''-----------------------multiplication tables-------------------------'''

# val=int(input('enter num: '))
# for i in range(1,11):
#     res=val*i
#     print(f"{val}*{i}={res}")

'''-----------------------Bubble sort------------------------------------'''

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(arr)
# print("Sorted array:", arr)




'''--------------------------------------------------------------------------you have some questions here----------------'''


# def bubble_sort(num):
#     le=len(num)
#     for i in range(le-1):
#         for j in range(0,le-i-1):
#             if  num[j] > num[j+1]:
#                 num[j+1],num[j]=num[j],num[j+1]
#     return num

# var=[3,4,32,6,0,9]
# bubble_sort(var)
# print('sorted array: ',var)



# def bubble_sort(num):
#     le=len(num)
#     for i in range(le-1):
#         for j in range(0,le-i):
#             if num[i] > num[j+i]:
#                 num[j+i],num[i]=num[i],num[j+i]

#     return num

# var=bubble_sort([3,4,32,6,0,9])
# print('sorted array: ',var)

'''------------------------------count vowels--------------------'''

# str='aifjoeijf0j03i0ir04i04i'
# vov='aeiouAEIOU'
# cnt=0
# for i in range(len(str)):
#     if str[i] in vov:
#         cnt +=1
# print(cnt)



# def vovels(str='uhiuhihuihuhkj'):
#     vov='aeiouAEIOU'
#     cnt=0
#     for i in range(len(str)):
#         if str[i] in vov:
#             cnt +=1
#     return cnt
# k=vovels('lsajifij3f3h44 0q0i409')
# print(k)

'''-------------------------------lcm-----page no 8 question no 9 you have a doubt overe here-------------------------------------'''

# def compute_lcm(x, y):
#     if x == 0 or y == 0:
#         return 0

#     if x > y:
#         greater = x
#     else:
#         greater = y

#     while True:
#         if greater % x == 0 and greater % y == 0:
#             return greater
#         greater += 1


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print("LCM:", compute_lcm(num1, num2))


'''--------------------------------------anagram-------------------------------'''
# You need 2 strings. They’re just rearranged versions of each other. Same letters, same count.
# night ↔ thing 
# debit card ↔ bad credit → spaces don’t matter if you ignore them  
# astronomer ↔ moon starer
# Notice: Both words have identical letters. If you sort them, they become the same: eilnst = eilnst


# input1=str(input('enter a string: '))
# # input2=str(input('enter a string: '))

# # rep=input1.replace(' ','')
# # rep2=input2.replace(' ','')
# input1.sort()
# print (input1)


# s = "python" 
# sorted_s = "   ".join(sorted(s)) 
# print(sorted_s)

'''---'''

# def prime_num(num):
#     if num>0:
#         primes=[2]
#         val=2
#         for i in range(2,val+1):
#             for j in range(2,num):
#                 if val % j == 0 and val % 2 ==0:
#                     val = val+1
#                 else:
#                     primes=primes.append(val)
#                     val +=1    
#         return primes

# value=prime_num(10)
# print(value)




# def prime_num(num):
#     if num < 2:
#         return []
    
#     primes = []
#     for val in range(2, num + 1):  # check each number from 2 to num
#         is_prime = True
#         for j in range(2, int(val**0.5) + 1):  # only check up to sqrt(val)
#             if val % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(val)
#     return primes
# value = prime_num(10)
# print(value)  # [2, 3, 5, 7]



# inr=69
# if inr<1:
#     print('not prime')
# else:
#     for i in range(2,int(inr**0.5)+1):
#         if inr % i == 0 :
#             print('not prime')
#             break
#     else:
#         print('prime')

'''----------------------------------FIND LCM BETWEEN 2 NUMS -----------------------------'''

# x=6
# y=8
# if x==y:
#     lcm=x
# elif x > y :
#     greater =x
# else:
#     greater=y
# while True:
#     if greater % y ==0 and greater % x ==0 :
#         lcm =greater
#         break
#     greater +=1
# print(lcm)

# def find_lcm(x,y):
#     if x==y:
#         lcm=x
#     elif x > y :
#         greater =x
#     else:
#         greater=y
#     while True:
#         if greater % y ==0 and greater % x ==0 :
#             lcm =greater
#             break
#         greater +=1
#     return lcm
# a=int(input('enter num: '))
# b=int(input('enter num: '))

# vals=find_lcm(a,b)
# print(vals)


'''----------------------------leap year------------------------'''

# def leap_year(x):
#     if x<=0:
#         return 'enter valid num'
#     elif x>=0:
#         if x % 400 == 0 or (x % 4 ==0 and x % 100 !=0) :
#             return 'leap year'
#         else:
#             return 'not leap year'
# val=int(input('enter year: '))
# print(leap_year(val))

# k=[12,122,4,43,532]
# k.sort()
# print(k)
'''---------------------------------palindrome--------------------------------------'''
# ----normal approach-------------
# def palindrome(stringu):
#     if stringu == stringu[::-1]:
#         return 'yes'
# k=str(input('enter string:')) 
# print(palindrome(k))

# def palin(value):
#     val=value.replace(" ","")
#     if val==val[::-1]:
#         return 'True'
#     else:
#         return 'False'
# k=str(input('value: '))
# print(palin(k))

# ---------the best approaches--------------

# def palin(s):
#     s = s.replace(" ", "").lower()  # note spaces shoul not count in palindrome string   (h ell o = he llo)
#     return s == s[::-1]
# value=str(input('enter a value: '))
# if palin:
#     print('its a palindrome string')
# else:
#     print('its a palindrome string')

# -----sometime they ask like ignore special characters and numerics-----

# def is_palindrome(s):
#     cleaned = ""

#     for ch in s:
#         if ch.isalpha():     # keep only letters
#             cleaned += ch.lower()

#     return cleaned == cleaned[::-1]

# -----sometime they ask like ignore special characters only and check -----

# def is_palindrome(s):
#     cleaned = ""

#     for ch in s:
#         if ch.isalnum():   # letters + numbers only
#             cleaned += ch.lower()

#     return cleaned == cleaned[::-1]


# --------------------------    (or)---

# def is_palindrome(s):
#     cleaned = ""

#     for ch in s:
#         if ch.isalnum():   # keeps letters + numbers, removes special chars
#             cleaned += ch.lower()

#     return cleaned == cleaned[::-1]

'''------------------frequency of each character in a string-----------'''

# def char_frequency(s):
#     freq = {}
    
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1
    
#     return freq

'''-------------------------------------------reverse a string withot slicing--------------------'''

# def reverse_string(s):
#     rev = ""
#     for ch in s:
#         rev = ch + rev
#     return rev

# print(reverse_string('akhf'))

'''---------------------------------------------------reverese a number----------------------'''
# def sum_of(digits):
#     sum=0
#     while digits>0:
#         sum += digits %  10
#         digits = digits // 10
#     return sum
# print(sum_of(1234))
        

'''-----------------------------vowels cout------------------------------'''
# def vowels_count(word):
#     cnt=0
#     for i in range (len(word)):
#         if word[i] in 'aeiouAeiou':
#             cnt+=1
#     return cnt
# val=str(input('enter a string: '))
# print(vowels_count(val))

'''# -----------------                doubt  ------------------'''

# def rm_dupli(dupli):
#     res=set(dupli)
#     lis=list(res)
#     return lis
# val = list(map(int, input("Enter numbers: ").split(",")))
# print(rm_dupli(val))




    
