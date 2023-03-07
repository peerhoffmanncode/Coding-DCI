# Global scope var
settings = {"title": "my awesome string"}
print(f"global scope, original state: {settings}")

def change_site_title(text_to_change: str):
    ''' function to change a dictionary from the global scope'''
    settings["title"] = text_to_change
    
change_site_title("my_change!!!")
print(f"global scope, changed state: {settings}")
