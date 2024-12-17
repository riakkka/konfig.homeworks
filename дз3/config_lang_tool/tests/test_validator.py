import unittest
from validator import validate_xml

class TestValidator(unittest.TestCase):
    def test_valid_xml(self):
        valid_xml = """<root><item>10</item><item>20</item></root>"""
        self.assertTrue(validate_xml(valid_xml))

    def test_invalid_xml(self):
        invalid_xml = "<root><item>10<item></root>"
        self.assertFalse(validate_xml(invalid_xml))

    def test_empty_xml(self):
        empty_xml = ""
        self.assertFalse(validate_xml(empty_xml))  # Пустой XML считается некорректным
