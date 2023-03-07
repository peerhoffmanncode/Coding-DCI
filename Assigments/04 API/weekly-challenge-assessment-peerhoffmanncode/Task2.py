import os
import time
import requests
import psycopg2


# "host = localhost dbname = pokemon user = postgres password = "
def write_to_db(connection_str: str, db_table: str, data: list) -> None:
    # connect to the postgres db
    database = psycopg2.connect(connection_str)
    # create cursor for the postgres database
    pgsql_cursor = database.cursor()
    for idx, element in enumerate(data, start = 1):
        # execute query at cursor
        # table = should be pokemons for this example
        print(f"INSERT INTO {db_table} VALUES ({idx}, '{element}');")
        pgsql_cursor.execute(f"INSERT INTO {db_table} (id, name) VALUES ({idx}, '{element}');")
                                INSERT INTO pokemon (name, id) VALAUES ('pokemon34', 55)
    database.commit()
    # fetch all data from the postgres cursor
    # pgsql_rows = pgsql_cursor.fetchall()
    # close pgsql cursor
    pgsql_cursor.close()
    # close the postgres database connection
    database.close()


def write_file(filename: str, data: list, sortlist=False) -> None:
    """function to write data to a file"""
    if not data:
        # not data no file
        return
    if sortlist:
        # sort data if forced
        data.sort()
    with open(filename, "w") as f:
        f.write("\n".join(data))


def get_pokemon_names(throttle: float = 0, url: str = "") -> list:
    """get names of pokemons form pokeapi"""

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

    # write to PostgreSQL database
    # "host = localhost dbname = pokemon user = postgres password = "
    write_to_db(
        "host=localhost dbname=pokemon user=postgres",
        "pokemons",
        all_found_pokemons,
    )

if __name__ == "__main__":
    main("https://pokeapi.co/api/v2/pokemon")
