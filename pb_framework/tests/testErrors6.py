import pytest

class TestErrors6:

    def test_TS_025(self):
        # TC_025: Calculate list average
        values = []
        avg = sum(values) / len(values)   # Runtime Error

    def test_TS_026(self):
        # TC_026: Validate subtraction logic
        result = 10 - 3
        assert result == 10   # Logical Error

    def test_TS_027(self)
        # TC_027: Display success message
        print("Success")   # Syntax Error

    def test_TS_028(self):
        # TC_028: Access tuple index
        data = (1, 2, 3)
        print(data[10])   # Runtime Error

    def test_TS_029(self):
        # TC_029: Verify user role
        role = "user"
        assert role == "admin"   # Logical Error

    def test_TS_030(self):
        # TC_030: Read non-existing file
        file = open("missing.txt")   # Runtime Error
