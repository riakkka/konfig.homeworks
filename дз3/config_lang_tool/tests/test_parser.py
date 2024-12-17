import unittest
from parser import parse_xml

class TestParser(unittest.TestCase):
    def test_parse_valid_xml(self):
        xml_data = """<root><item>10</item><item>20</item></root>"""
        result = parse_xml(xml_data)
        self.assertIsNotNone(result)
        self.assertEqual(result.tag, 'root')
        self.assertEqual(len(result), 2)
    
    def test_parse_invalid_xml(self):
        invalid_xml = "<root><item>10<item></root>"
        with self.assertRaises(Exception):
            parse_xml(invalid_xml)

if __name__ == '__main__':
    unittest.main()
