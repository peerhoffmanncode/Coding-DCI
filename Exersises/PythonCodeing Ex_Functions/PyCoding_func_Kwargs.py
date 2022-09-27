
def my_funny_func(*args, **kwargs):
    print("args -->", args)
    print("kwargs -->", args)
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    location = args[0]
    return f"{first_name} {last_name} in {location}"


print(my_funny_func("Mainz", first_name="Peer", last_name="Hoffmann"))