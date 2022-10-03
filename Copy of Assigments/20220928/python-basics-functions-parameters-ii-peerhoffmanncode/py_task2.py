# Global scope var
settings = {"title": "My original title"}
default_settings = {"title": "My original title"}

def change_site_title(text_to_change: str):
    ''' function to change a dictionary from the global scope'''
    settings["title"] = text_to_change

def get_title(settings = default_settings):
    ''' function to return a title from the settings dictionary'''
    return settings["title"]


print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())
