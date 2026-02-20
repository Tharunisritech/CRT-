'''
* * * * 
* * * * 
* * * * 
* * * *

n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
    '''
'''
n = 4
* 
* *
* * *
* * * *

n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()
    
n = 4
* * * *
* * *
* * 
*
'''
# n = int(input())
# for i in range(n):
#     for j in range(n - i):
#         print("*", end=" ")
#     print()

# n = int(input())
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# k = 1
# n = int(input())
# for i in range(1, n+1):
#     for j in range(i):
#         print(k, end=" ")
#         k += 1
#     print()

# n = 4
# A 
# A B 
# A B C 
# A B C D
# print(ord('C'))

# n = int(input())
# for i in range(1, n+1):
#     for j in range(i):
#         print(chr(65+j), end=" ")
#     print()

# n = int(input())
# k = 65
# for i in range(1, n+1):
#     for j in range(i):
#         print(chr(k), end=" ")
#         k += 1
#     print()
# Hollow Square
# * * * *
# *     *
# *     *
# * * * * 

n = int(input())
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end =" ")
        else:
            print(" ", end=" ")
    print()
    

