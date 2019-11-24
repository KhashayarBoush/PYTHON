

set1 = {1,2,9,"khashayar",64}
print(set1)

print("==" * 20 )
array = ["test1","test2","test3","test4"]
print(array[0])

print("==" * 20 )
List_to_Set = set(array)
print(List_to_Set)

print("==" * 20 )
# print(List_to_Set[0]) # a set has not Andis
set_copy = set1.copy()
print(set_copy)

print("==" * 20 )
set_discard = set1.remove("khashayar")
print(set1)

print("==" * 20 )
add = set1.add("Woow Add")
print(set1)

print("==" * 20 )
pop = set1.pop()
print(set1)

print("==" * 20 )
update = set1.update("123")
print(set1)

#############################################################
print("==" * 20 )
print("==" * 20 )
s1 = set([1,2,3,4])
s2 = {5,6,7,8}
s3 = {8,9,10,11}
print("==" * 20 )
print(" s1 - s2 # isdisjoint --> ",s1.isdisjoint(s2))
print(" s2 - s3 # isdisjoint --> ",s2.isdisjoint(s3))
print("==" * 20 )
s4 = s2.intersection(s3)
print("intersection --> s2 - s3 : ",s4)
print("=" * 20)
s5 = s2.difference(s3)
print("Set diffrence --> s2 - s3",s5)
print("*" * 20 )


