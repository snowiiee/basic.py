a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
op = input('Enter an Valid Arithmetic operations(i.e., +,-,/,*,//,**: ')

if op=='+':
    result=a+b
elif op=='-':
    result=a-b
elif op=='/':
    result=a/b
elif op=='%':
    result=a%b
elif op=='//':
    result=a//b
elif op=='**':
    result=a**b
else:
    result='Invalid'

print(result)
