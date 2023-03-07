#### Task 3 ###


def log(*args):
    result = ""
    message = list(*args)
    for word in message:
        print(word)
        if word[-1] == ".":
            word += "\n"
        elif word[-1] == "!":
            word += "\n\n"
        else:
            word += " "
        result += word

    with open("messages.log", "a") as filename:
        print(result, file=filename)


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

log(message)
