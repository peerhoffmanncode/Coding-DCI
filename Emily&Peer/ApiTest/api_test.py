import tmdbsimple as tmdb
import json
from pprint import pprint

tmdb.API_KEY = "27a100afa3b8b345ef46e716db51fbc4"
tmdb.REQUESTS_TIMEOUT = (2, 5)  # seconds, for connect and read specifically


# test

# movie = tmdb.Movies(603)
# response = movie.info()
# pprint(movie.title)
search = tmdb.Search()
response = search.tv(query="Silicon Valley")
for element in response["results"]:
    print(element["name"], element["id"])
    identity = tmdb.TV_Episodes(tv_id=element["id"], season_number=1, episode_number=1)
    tmdb.Discover()
    response = identity.info()
    pprint(response)
    input("#" * 50)
