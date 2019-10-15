# operator use for Change Variables

# we have 7 operators
#||||||||||||||||||||||||
# 1 : arithmetic Operator
# 2 : Relational Operator
# 3 : assignment Operatos
# 4 : Logical    Operatos
# 5 : Bitwise    Operatos
# 6 : Membership Operatos
# 7 : Identy     Operatos
#|||||||||||||||||||||||||
#---------------------------------
# variables
a = 5
b = 10 
#---------------------------------
# 1 : Arithmatic Operatos
a + b  |  a ** b  | a % b   
a - b  |  a // b  | 
a * b  |  a /  b  |
#---------------------------------
# 2 : relational operator
a == b |  a != b  | 
a <  b |  a >  b  |
a <= b |  a >= b  | 
#---------------------------------
# 3 : assignment Operatos
a += b
a = a + b
print(a)

b -= a
b = b - a
print (b)
#---------------------------------
# 6 : Membership Operatos
a = [ 1 , 2 , 3 , 4]
print (1 in a)
print ( 1 not in a)

c = 5 
d = 10 
print (a is b) # False
print ( a is a ) # True