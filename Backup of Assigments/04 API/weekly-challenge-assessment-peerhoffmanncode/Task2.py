import os
import time
import requests
import pprint as pprint
import psycopg2


def write_file(filename: str, data: list, sortlist = False) -> None:
    """ function to write data to a file """
    if not data:
        # not data no file
        return
    if sortlist:
        #sort data if forced
        data.sort()
    with open(filename, "w") as f:
        f.write("\n".join(data))


def get_pokemon_names(throttle: float = 0, url: str = "") -> list:
    """ get names of pokemons form pokeapi """
    
    # Terminator string to indicate end of list
    TERMINATOR = ["!$_$!"]

    # fail safe case!
    if not url:
        return TERMINATOR

    # throttle requests
    if throttle:
        time.sleep(throttle)

    # read from the API
    print(f"Requesting from API [{url}]{' ' * (80-len(url))}", end="\r")
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

    all_found_pokemons = get_pokemon_names(throttle=MAIN_THROTTLE, url=url)
    all_found_pokemons.pop()
    # deprecated because of postgres integration
    # write_file("pokemon_list.txt", all_found_pokemons, sortlist = True)


if __name__ == "__main__":
    
    # connect to the postgres db
    pgsql = psycopg2.connect(
        host = "localhost"
        database = ">>fill<<"
        user = "postgres"
        password = "")
    
    # create cursor for the postgres database
    pgsql_cursor = pgsql.cursor()
    
    # execute query at cursor
    pgsql_cursor.execute("select * from ...")
    
    # fetch all data from the postgres cursor
    pgsql_rows = pgsql_cursor.fetchall()
    
    # close pgsql cursor
    pgsql_cursor.close()
    
    main("https://pokeapi.co/api/v2/pokemon")
    
    # close the postgres database connection
    pgsql.close()
