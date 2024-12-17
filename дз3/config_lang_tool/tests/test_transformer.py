import unittest
from transformer import transform_to_config_language

class TestTransformer(unittest.TestCase):
    def test_transform_array(self):
        xml_data = """<root><array>[ 10, 20, 30 ]</array></root>"""
        transformed = transform_to_config_language(xml_data)
        self.assertEqual(transformed, "[10, 20, 30]")

    def test_transform_dict(self):
        xml_data = """<root><dictionary>dict(имя1 = 10, имя2 = 20)</dictionary></root>"""
        transformed = transform_to_config_language(xml_data)
        self.assertEqual(transformed, "dict(имя1 = 10, имя2 = 20)")

if __name__ == '__main__':
    unittest.main()
