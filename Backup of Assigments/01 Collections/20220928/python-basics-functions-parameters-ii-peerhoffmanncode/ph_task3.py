# Global scope var
settings = {"title": "My original title",
            "pages": []}
default_settings = {"title": "My original title",
                    "pages": []}

def change_site_title(text_to_change: str):
    ''' function to change a dictionary from the global scope'''
    settings["title"] = text_to_change

def get_title(settings = default_settings):
    ''' get the title '''
    return settings["titles"]

def get_pages(settings = default_settings):
    ''' get the pages '''
    return settings["pages"]

def add_page(pages_to_add, settings = default_settings):
    ''' add the pages '''
    settings["pages"].append(pages_to_add)
    return


home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))