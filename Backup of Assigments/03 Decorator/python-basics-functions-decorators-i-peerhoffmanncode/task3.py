#### Task 3 ##########################
print()
print()
print("#### Task 3 ##########################")
print()

def make_italics(func):
    def inner(*args, **kwargs):
        return f"<em>{func(*args, **kwargs)}</em>"
    return inner

def make_paragraph(func):
    def inner(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}</p>"
    return inner

def make_bold(func):
    def inner(*args, **kwargs):
        return f"<strong>{func(*args, **kwargs)}</strong>"
    return inner

@make_bold
def get_html_greeting():
    return "Hello, World"

@make_bold
def get_full_name(*args, **kwargs):
    if len(args):
            first = args[0]
            last = args[1]
    if len(kwargs):
            first = kwargs["first"]
            last = kwargs["last"]
    return f"{first} {last}"

@make_paragraph
@make_italics
def get_custom_html_greeting(*args, **kwargs):
    return f"Hello, {get_full_name(*args, **kwargs)}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))