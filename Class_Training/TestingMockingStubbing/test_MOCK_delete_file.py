""" TOLLES PROGRAMM !!"""

import unittest
from unittest.mock import patch

from app import rm

### Mocking approach !! ###
### UNITTEST MOCK MODUL !!


class Test(unittest.TestCase):
    def test_remove(self):
        # simulate a actual remove
        # function needs to be inline to the actual remove function!!
        with patch("os.path.isfile"):
            with patch("os.remove"):
                self.assertEqual(rm("delete.me"), "not to compare with!")


if __name__ == "__main__":
    unittest.main()
