import re

class PhoneNumberConverter:
    regex = r"\(?\+?[49]+([0-9]|\/|\(|\)|\-| ){10,}"

    def to_python(self, value):
        value = value.strip().rstrip("/")

        second_check = re.sub(r'\D', '', value)
        if 3 < len(second_check) < 13:
            return value

        raise ValueError

    def to_url(self, value):
        return value
