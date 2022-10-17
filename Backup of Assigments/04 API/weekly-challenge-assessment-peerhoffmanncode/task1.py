import os
import time
import requests


def write_file(filename: str, data: list, sortlist = False) -> None:
    """write data to a file"""
    if not data:
        # not data no file
        return
    if sortlist:
        #sort data if forced
        data.sort()
    with open(filename, "w") as f:
        f.write("\n".join(data))


def get_pokemon_names(throttle: float = 0, url: str = "") -> list:
    """get the names of the pokemons"""
    TERMINATOR = ["!$_$!"]

    # fail safe case!
    if not url:
        return TERMINATOR

    # throttle requests
    if throttle:
        time.sleep(throttle)

    # read from the API
    #print(f"Requesting from API [{url}]{' ' * (80-len(url))}", end="\r")
    pokemon_name = requests.get(url).json()
    # get next url
    next_url = pokemon_name["next"]
    if not next_url or next_url == "null":
        # base case!
        if pokemon_name:
            # return left overs
            return [
                pokemon_name["results"][pokemon]["name"]
                for pokemon in range(len(pokemon_name["results"]))
            ] + TERMINATOR
        else:
            return TERMINATOR

    # List comprehension & recursion
    # possible memory optimization, store data to file/database instead of memory!
    return [
        pokemon_name["results"][pokemon]["name"]
        for pokemon in range(len(pokemon_name["results"]))
    ] + get_pokemon_names(throttle=throttle, url=next_url)


def main(url):
    """main programm"""
    MAIN_THROTTLE = 0
    # os.system("clear")
    # print("Accessing API of Pokemon")
    # print(f"[{url}]")
    all_found_pokemons = get_pokemon_names(throttle=MAIN_THROTTLE, url=url)
    all_found_pokemons.pop()
    # print()
    # print(f"Found [{len(all_found_pokemons)}] Pokemons")
    write_file("pokemon_list.txt", all_found_pokemons, sortlist = True)


if __name__ == "__main__":
    main("https://pokeapi.co/api/v2/pokemon")
