import pytest

class TestErrors4:

    def test_TS_019(self):
        # TC_019: Divide two numbers
        result = 20 / 2   # Fixed: avoid division by zero

    def test_TS_020(self):
        # TC_020: Validate multiplication result
        value = 3 * 3
        assert value == 9   # Fixed: corrected logical assertion

    def test_TS_021(self):
        # TC_021: Print user name
        name = "Admin"
        print(name)   # Fixed: added missing colon in method definition

    def test_TS_022(self):
        # TC_022: Access dictionary key
        data = {"id": 1, "name": "Admin"}
        print(data["name"])   # Fixed: key now exists
