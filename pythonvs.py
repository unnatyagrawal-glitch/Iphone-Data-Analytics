# info = {
#     "key": "value",
#     "subjects": {
#         "phy": 97,
#         "chem": 98,
#         "math": 95
#     }
# }

# info["name"]="Unnaty"
# info["surname"]="Agrawal"
# print(info["subjects"]["phy"])

# print(len(list(info["subjects"].keys())))

# print(info.items())

# pairs=list(info.items())
# print(pairs[0])

#print(info["key1"]) #will give error
#print(info.get("key1")) #will return None

# new_dict= {"city": "delhi", "age": 16}
# info.update(new_dict)


# collection={1,2,2,"hello","world"}
# print(collection)


marks={}

x= int(input("enter phy:"))
marks.update({"phy":x})

x= int(input("ent chem:"))
marks.update({"chem":x})

print(marks)
