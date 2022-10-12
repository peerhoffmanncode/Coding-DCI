#### Task 4 ##########################
print()
print()
print("#### Task 4 ##########################")
print()

def wrap_with(tag="strong"):
    def decorator(func):
        def strong(*args, **kwargs):
                return f"<strong>{func(*args, **kwargs)}</strong>"
        def em(*args, **kwargs):
                return f"<em>{func(*args, **kwargs)}</em>"
        def p(*args, **kwargs):
                return f"<p>{func(*args, **kwargs)}</p>"
        if tag == "strong":
            return strong
        elif tag == "em":
            return em
        elif tag == "p":
            return p
    return decorator
    

@wrap_with(tag="strong")
def get_html_greeting():
    return "Hello, World"

@wrap_with(tag="strong")
def get_full_name(*args, **kwargs):
    if len(args):
            first = args[0]
            last = args[1]
    if len(kwargs):
            first = kwargs["first"]
            last = kwargs["last"]
    return f"{first} {last}"

@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(*args, **kwargs):
    return f"Hello, {get_full_name(*args, **kwargs)}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))