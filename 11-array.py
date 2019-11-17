# we can use Array For keep data

arr = [" khashayar ", " boush ", " 21 ", "Programmer"]
print("my name is : " + arr[0] + "... and my Fmaily is " + arr[1])

l1 = [100,200,300,400] # new array list
l2 = [500,600,700,800]

l1 [1:1] = [110,220] # add 110, 220 to list

l1 [0:1] = [] # delete 100 or index 0

print("List Indexs Length --> : ",len(l1))

l3 = l1 + l2

print("L3 Duplicate --> " ,l3 * 2 ) # copy L3 Not *

print("L3 = " , l3)

print("L1 --> " , l1)

# or we can use array

print(["a"] * 10 )

# empty array

l1 [:] = []
print("empty L1 -->",l1)
