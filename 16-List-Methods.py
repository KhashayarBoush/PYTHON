

L1 = [1,2,5,4,8,9,64,1,65464,4,974,9,6546,123]

L1.append(1000) # add new argumunt to list
print(L1)
print("=" * 20)
print(L1.index(5)) # 5 address in List is 2
print("=" * 20)
print(L1)
L1.remove(1000)
print("=" * 20)
print("How much 1 in array --> : ",L1.count(1))
print("=" * 20)
L1.extend(["this is new extend"])
# L1.extend(L1)
print(L1)
print("=" * 20)
L1.insert(0,"this is insert new item")
print(L1)
print("#" * 20)
L2 = [10,654,234,8234,65464,544,23,0,234,545,0,5456,652434]
soretd = L2.sort()
print("L2 Sorted --> : ",L2)
print("=" * 20)