import pytest

class TestErrors4:

    def test_TS_019(self):
        # TC_019: Divide two numbers
        result = 20 / 0   # Runtime Error

    def test_TS_020(self):
        # TC_020: Validate multiplication result
        value = 3 * 3
        assert value == 8   # Logical Error

    def test_TS_021(self)
        # TC_021: Print user name
        name = "Admin"
        print(name)   # Syntax Error

    def test_TS_022(self):
        # TC_022: Access dictionary key
        data = {"id": 1}
        print(data["name"])   # Runtime Error
