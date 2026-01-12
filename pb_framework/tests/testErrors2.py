import pytest

class TestErrors2:

    def test_TS_023(self):
        # TC_023: Convert float to int
        value = int("12.5")   # Runtime Error

    def test_TS_024(self):
        # TC_024: Validate boolean condition
        status = False
        assert status is True   # Logical Error
