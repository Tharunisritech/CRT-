'''
Docstring for CRT.IV-SEM.Python.Practice.M01_Language_&_Programming_Basics.S04.PS07_Debugging
Debugging

try:
    a=int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("Can not be divisible by Zero")
except ValueError:
    print("Invalid input")
    
    pdb Commands:
    1)n ==> to execute the output in a next line
    2)p variable ==> to get the value of the variable
    3)l ==> list nearby code 
    4)c ==> continue the execution
    5)s ==>to start a function
    6)r ==> return from the function 
    7)h ==>help 
    8)q ==> quit the execution

    '''
import pdb 

def add(a, b):
    pdb.set_trace() #set the breakpoint 
    return a+b 
a=int(input("Enter first number: "))
b=int(input("Enter second number:"))
print(add(a,b))
       
          