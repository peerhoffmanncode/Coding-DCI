# please fill the two lists with the data from the "emails" list. Use string slicing and methods for extracting what you need
# example:
# test@mail.com
# usernames = ["test"]
# email_provider = ["mail.com"]

emails = [
    "123whatever@gmail.com",
    "456idontcare@gmail.com",
    "789istilldontmind@hotmail.de",
    "forrealbruvwhatever@gmx.de",
    "123whatever@gmail.com",
    "456idontcare@gmail.com",
    "789istilldontmind@hotmail.de",
    "forrealbruvwhatever@gmx.de",
    "123whatever@gmail.com",
    "456idontcare@gmail.com",
    "789istilldontmind@hotmail.de",
    "forrealbruvwhatever@gmx.de",
    "123whatever@gmail.com",
    ]

usernames = []
email_provider = []

for item in emails:
  # Loop start   
    usernames.append( item[ :item.index("@")])
    email_provider.append( item[item.index("@")+1: ])
  # loop end
  
print(usernames)
print(email_provider)