# TODO:
# - Write a function to make two names titlezed e.g. title_name(name1, name1)
# - write a function, when given a list of names, it creates one name (test it too) e.g. join_names([‘name1’, ‘name2’, ‘name3’])


def make_title(input_string1: str, input_string2: str) -> tuple:
    return input_string1.title(), input_string2.title()


def make_full_name(names: list[str]) -> str:
    return " ".join(names)
