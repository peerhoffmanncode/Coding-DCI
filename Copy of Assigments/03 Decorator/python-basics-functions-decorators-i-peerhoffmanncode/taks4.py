#### Task 4 ##########################
print()
print()
print("#### Task 4 ##########################")
print()

def wrap_with(tag="strong"):
    def decorator(func):
        def inner(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return inner
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

### Tests
print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))