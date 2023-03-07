#!/usr/bin/env python
from typing import Union, Callable


def compare_to_seven(input_number: Union[int, str, Callable]) -> str:
    compared_to: int = 7
    if isinstance(input_number, int):
        if input_number > compared_to:
            return f"{input_number} is higher than {compared_to}."
        elif input_number < compared_to:
            return f"{input_number} is lower than {compared_to}."
        else:
            return f"{input_number} is {compared_to}."

    elif isinstance(input_number, str):
        # wired special corner case as requested // should actually be an error!
        if not input_number.isnumeric() and not input_number.isalpha():
            return f"{input_number} is lower than {compared_to}."
        elif input_number > str(compared_to):
            return f"{input_number} is higher than {compared_to}."
        elif input_number < str(compared_to):
            return f"{input_number} is lower than {compared_to}."
        else:
            return f"{input_number} is {compared_to}."

    elif isinstance(input_number, Callable):
        return f"you want it, you get it - da str!"

    else:
        raise TypeError("unsupported type!")


if __name__ == "__main__":
    compare_to_seven(8)
