
str1 = input("please inter your word : -->  ")
def myapp(str1):
    var = str1
    print("+" * 20)
    print(" Length of Word : " , len(str(var)))
    print("+" * 20)
    print( "Last Word is --> :  " , var[len(var) - 1])
    print("=" * 20)
    var2 = input(" do you need to find a Word : ")
    if var2 == "y":
        var3 = input("please insert your word : ")
        print(var.count(var3))
    else:
        print("Have a good day")


myapp(str1)