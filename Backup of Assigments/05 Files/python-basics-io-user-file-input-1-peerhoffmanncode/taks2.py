#### Task 2 ###

message = [
    "Hello",
    "visitor!",
    "Welcome",
    "to",
    "our",
    "command",
    "line",
    "interface.",
    "Please,",
    "contact",
    "us",
    "if",
    "you",
    "have",
    "any",
    "questions.",
]

result = ""
message[1] = input("What is your name? ").capitalize() + "!"
for word in message:
    if word[-1] == ".":
        word += "\n"
    elif word[-1] == "!":
        word += "\n\n"
    else:
        word += " "
    result += word

print(result)
