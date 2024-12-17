import unittest
from validator import validate_xml

class TestValidator(unittest.TestCase):
    def test_valid_xml(self):
        valid_xml = """<root><item>10</item><item>20</item></root>"""
        result = validate_xml(valid_xml)
        self.assertTrue(result)

    def test_invalid_xml(self):
        invalid_xml = "<root><item>10<item></root>"
        result = validate_xml(invalid_xml)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
