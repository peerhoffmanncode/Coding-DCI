dictionary = {
    "next": "a link",
    "results": [
        {"name": "A", "items": ["Shaban"]},
        {"name": "B", "items": ["Peer"]},
        {"name": "C", "items": ["Jacques"]},
        {"name": "D", "items": ["Muhannad"]},
    ]
}

for element in dictionary["results"]:
    print(element["items"][0])