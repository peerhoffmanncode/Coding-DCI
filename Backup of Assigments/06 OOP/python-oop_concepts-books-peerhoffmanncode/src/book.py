from author import Author


class Book:
    def __init__(self, _name: str, _author: Author, _price: float, _qty: int = 1):
        self._name = _name
        self._author = _author
        self._price = _price
        self._qty = _qty

    def __str__(self):
        return f"Book [name={self._name},Author[name={self._author.get_name()},email={self._author.get_email()},gender={self._author.get_gender()}],price={self._price},qty={self._qty}"

    def get_name(self) -> str:
        return self._name

    def get_author(self) -> Author:
        return self._author

    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float) -> None:
        self._price = price

    def get_qty(self) -> int:
        return self._qty

    def set_qty(self, qty: int) -> None:
        self._qty = qty
