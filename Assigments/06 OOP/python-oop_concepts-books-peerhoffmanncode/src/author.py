from gender import Gender


class Author:
    def __init__(self, _name: str, _email: str, _gender: Gender):
        self._name = _name
        self._email = _email
        self._gender = _gender

    def __str__(self) -> str:
        return (
            f"Author [name={self._name}, [email={self._email}, gender={self._gender}]"
        )

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def set_email(self, email) -> None:
        # email would be set
        self._email = email

    def get_gender(self) -> str:
        return f"{self._gender}"
