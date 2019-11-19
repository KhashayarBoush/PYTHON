

dic1 = {"name":"khashayar",
        "family" : "boush",
        "age" : 21,
        "city" : "Tehran",
        "phone" : 123456789
        }

dic1.get("sex","none")
print(dic1)

print("=" * 20 )
dic1 ["level"]="A" # add Data to dict
print(dic1)
print("/" * 20)
print("phone is --> : ",dic1["phone"])
print("&" * 20)
print("Keys is --> " , dic1.keys())
print("+" * 20)
print("Valus is --> ",dic1.values())
print("_-" * 20 )
items = dic1.items()
print(items)

#print("change an item to ttupel --> ",dic1.items())

dic2 = dic1.copy()
print("this is copy of dic 1 --> ",dic2)