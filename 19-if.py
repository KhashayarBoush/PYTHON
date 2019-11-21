
number = int(input("Insert number : "))
if number > 100 :
    print(" number is over 100 ",number)
elif number <= 100 :
    print(" number is down of 100 ", number)

if number%2 == 0 :
    print(" number is odd 2  ")
    if number%3 == 0 :
        print(" number odd 2 and 3")
    else:
        print(" number is odd 2 Just")
else:
    print("number is out of renge")