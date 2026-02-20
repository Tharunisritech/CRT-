# li = [1, 2, 3, 4, 5]
# #output : [1, 4, 9, 16, 25]

# res = []
# for i in li:
#     if i%2 == 0:
#         res.append(i**2)
# print(res)

# li = ['a', 'b', 'c']
# # 'a, b, c
# res = ""
# for ch in li:
#     res = res + ch + " " 
# print(res)

# print(" ".join(li))

# print(*li)

''' Intermediate patterns
1. pyramid
n = 4
output:
   *   
  * *   
 * * * 
* * * *
'''
# n = int(input())
# for  i in range(1, n+1):
#     print(" "*(n-i)+ "* "*i)
# * * * *
#  * * * 
#   * * 
#    *
n = int(input())
for i in range(n,0, -1):
    print(" "*(n-i)+ "* "*i)

