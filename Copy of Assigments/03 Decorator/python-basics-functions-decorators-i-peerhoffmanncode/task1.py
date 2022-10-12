#### Task 1 ##########################
print()
print()
print("#### Task 1 ##########################")
print()

def make_bold(func):
    def inner():
        return f"<strong>{func()}</strong>"
    return inner

@make_bold
def get_html_greeting():
    return "Hello, World"

print(get_html_greeting())
