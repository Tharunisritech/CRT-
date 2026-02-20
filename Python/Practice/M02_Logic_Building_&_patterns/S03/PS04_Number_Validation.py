'''Armstrong number 
n=123
1^3+2^3+3^3
=1+8+27
36!=123'''
'''n=int(input())
d=len(str(n))
res=0
for i in str(n):
    int(i) ** d
if res==n:
    print("Armstrong")
else:
    print("Not Armstrong")
print("Armstrong" if n==res else "Not Armstrong")'''
'''Perfect  number
n=6
1+2+3=6'''
n = int(input("Enter a number: "))

s = 0
for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print("Perfect number")
else:
    print("Not a perfect number")

'''Strong number
145
1!+4!+5!
1+24+120
145'''

def fact(n):
    if n<0:
        return "no Factorial for -ve"
    elif n==0 or n==1:
        return 1

    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
        return fact
s=0
n=int(input())
