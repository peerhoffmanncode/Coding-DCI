import requests


def give_me_some_horror(sign):
    try:
        response = requests.get(f"https://ohmanda.com/api/horoscope/{sign}").json()
    except:
        response = {"Message": f"ERROR !"}

    return response


# print the data
print(give_me_some_horror(sign))
