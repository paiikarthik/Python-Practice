def mult(a, b):
    print(a * b)
    
def mult(a, b, c):
    
    print(a * b * c)
    
    
mult(2, 4, 3)
#mult(2, 7)

#In the above code, there are two mult() methods, but the python compiler can only see the last i.e the one with 3 parameters. 
# #Therefore, even though we can define multiple methods with the same name and different arguments, but only the last method of
#  them can be used. Calling any of the other methods will produce an error. Like here calling will mult(2,3) an error.

