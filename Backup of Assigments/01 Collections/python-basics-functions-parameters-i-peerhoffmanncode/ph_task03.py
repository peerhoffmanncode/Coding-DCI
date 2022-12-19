import datetime

def greet(name = "", date = datetime.datetime.now()):
    ''' function to greet a person
        in respect of the time.
    '''
    hour = int(date.strftime("%H"))
    if hour < 12:
        return(f"Good Morning, {name}!")
    elif 12 <= hour < 20:
        return(f"Good Afternoon, {name}!")
    else:
        return(f"Good Night, {name}!")

print(greet(
    name="John",
    date=datetime.datetime(2021, 5, 7, 11, 59, 59)
    ))
print(greet(
    date=datetime.datetime(2021, 5, 7, 12, 0, 1),
    name="John"
    ))