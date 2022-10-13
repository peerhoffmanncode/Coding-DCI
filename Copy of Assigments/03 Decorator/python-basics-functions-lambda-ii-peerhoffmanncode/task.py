#### Task 1 ##########################
print()
print()
print("#### Task 1 ##########################")
print()

subject_marks = [
    ("English", 88),
    ("Science", 90),
    ("Maths", 97),
    ("Social sciences", 82),
]

subject_marks.sort(key=lambda x: x[1])
print(subject_marks)


#### Task 2 ##########################
print()
print()
print("#### Task 2 ##########################")
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: not x % 2, numbers)))


#### Task 3 ##########################
print()
print()
print("#### Task 3 ##########################")
print()
pwd = "admin"
usr = "admin"


def protected(func):
    """decorator that validates a admin login"""

    def inner():
        given_pwd = input("Username: ")
        given_usr = input("Password: ")
        if given_pwd == pwd and given_usr == usr:
            return func()
        else:
            print("You are not authorized")
            return

    return inner


def public():
    print("Hello World!")


@protected
def private():
    print("Welcome, admin!")


public()
private()


#### Task 4 ##########################
print()
print()
print("#### Task 4 ##########################")
print()


def wrap_with(tag=""):
    """decorator factory"""
    def decorator(func):
        """decorator function for HTML tags"""
        if tag:
            return lambda *args, **kwargs: f"<{tag}>{func(*args, **kwargs)}</{tag}>"

        else: # added else for unknown tag!
            return lambda *args, **kwargs: f"{func(*args, **kwargs)}"

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
