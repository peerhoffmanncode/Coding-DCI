""" TOLLES PROGRAMM !!"""

import unittest
from unittest.mock import patch

from app import rm

### Mocking approach !! ###
### UNITTEST MOCK MODUL !!

print("global: ", dir())


class Test(unittest.TestCase):
    def test_remove(self):
        # simulate a actual remove
        # function needs to be inline to the actual remove function!!
        print("class", dir(self))
        with patch("os.path.isfile"):
            with patch("os.remove"):
                print("context manager", dir(self))
                self.assertEqual(rm("delete.me"), True)


if __name__ == "__main__":
    unittest.main()
