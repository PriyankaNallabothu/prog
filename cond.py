n=22
if n%2==0:
    print('even')

s = 'Priya'
if s[-1].lower() in 'aeiou':
    print('last char is vowel')


p = 'mom'
if p[::-1]:
    print('Palindrome')


# wap to check whether the given number is even or odd
num=27
if num%2==0:
    print('even')
else:
    print('odd')

# s = input('enter the string:')
# if s[0].islower():
#    print(s[0].upper())
# else:
#    print(s[0].lower())

# wap to check whether two strings are Anagrams or not
# s = 'car'
# s1 = 'arc'
# res = list(s)
# res1 = list(s1)
# res.sort()
# res1.sort()
# s2 = ''.join(res)
# s3 = ''.join(res1)
# if s2 == s3:
#    print('anagram')
# else:
#    print('not anagram')

# wap to validate pan card number
# n=input()
# if len(n) == 10 and n[0:5].isupper() and n[5:9].isnumeric() and n[-1].isupper():
#     print('valid')
# else:
#     print('not valid')





# wap to print first largest number
n1=23
n2=17
n3=2
if n1>n2 and n1>n3:
    print(f'n1 {n1} is largest')
elif n2>n3 and n2>n1:
    print('n2 is largest')
else:
    print('n3 is largest')

# wap to print smallest number
n1=23
n2=17
n3=2
if n1<n2 and n1<n3:
    print(f'n1 {n1} is smallest')
elif n2<n3 and n2<n1:
    print('n2 is smallest')
else:
    print('n3 is smallest')
# wap to find positive,negative and netural number
n=eval(input('enter the number:'))
if n>0:
    print('Positive number')
elif n<0:
    print('Negative number')
else:
    print('Netural number')


# wap to return second largest number among 3 numbers
n1=17
n2=2
n3=22
if n1>n2 and n1>n3:
    if n2>n3:
        print('n2 is second largest')
    else:
        print('n3 is second largest')
elif n2>n3 and n2>n1:
    if n3>n1:
        print('n3 is second largest')
    else:
        print('n1 is second largest')
else:
    if n1>n2:
        print('n1 is second largest')
    else:
        print('n2 is second largest')



# wap to check the length of the list is even or odd and check whether middle element is string convert it into uppercase,suppose if it is list add an element at 0th position,suppose if it is an individual datatype and add the same data to it,suppose if it is in tuple,set,dictionary have length of it.
n=list(input())




# wap to print numbers from 1-5
i=1
while i <= 5:
    print(i,end=' ')
    i+=1

# wap to print numbers from 5-1
i=5
while i>0:
    print(i,end=' ')
    i-=1





























