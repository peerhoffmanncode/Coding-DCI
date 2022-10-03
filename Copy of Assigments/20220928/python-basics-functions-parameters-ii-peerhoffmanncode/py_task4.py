
def print_user_profile(first = "", last = "Doe", pictures = None, gender: str = "female"):
    #import pdb; pdb.set_trace()
    ''' function to print user profile information'''
    
    if pictures == None:
        pictures = []
        
    if first == "":
        if gender == "female":
            first = "John"
        else:
            first = "Jane"
    if last == "":
        if gender == "female":
            last = "John"
        else:
            last = "Jane"
            
    # if pictures == []:
    #     pictures.append("common_header.png")

    pictures.insert(0,"common_header.png")
            
    return(f"The user {first} {last} has the following pictures: {pictures}")


test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
#print(print_user_profile(**test_data1))
# print("before 1. ", test_data2)
# print(print_user_profile(**test_data2))
# print("after 1. ", test_data2)
#print(print_user_profile(**test_data3))
# print(print_user_profile(**test_data2))
# print("after 2. ", test_data2)

list1 = [1,2,3]
list2 = []

#list2 = list1.copy()# copy list
list2 = list1[1:2]    # same thing

list1.append(5)
print(list1, list2)