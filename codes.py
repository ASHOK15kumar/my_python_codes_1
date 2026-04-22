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
        

num=int(input('enter num: '))
if num<1:
    print("enter a valid num")
elif num<2:
    print('its not a prime')
else:
    for i in range(2,num):
        if num%i==0:
            print('not prime')
            break
    else:
        print("its a prime")


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
