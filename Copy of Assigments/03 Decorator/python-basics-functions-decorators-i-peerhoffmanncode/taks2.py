#### Task 2 ##########################
print()
print()
print("#### Task 2 ##########################")
print()

def make_bold(func):
    def inner(*args, **kwargs):
        return f"<strong>{func(*args, **kwargs)}</strong>"
    return inner

@make_bold
def get_html_greeting():
    return "Hello, World"

@make_bold
def get_custom_html_greeting(*args, **kwargs):
    if len(args):
            first = args[0]
            last = args[1]
    if len(kwargs):
            first = kwargs["first"]
            last = kwargs["last"]
    return f"Hello, {first} {last}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_custom_html_greeting(first="Olaf", last="Scholz"))
print(get_html_greeting())