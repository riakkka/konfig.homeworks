import unittest
import xml.etree.ElementTree as ET
from transformer import transform_to_config_language

class TestTransformer(unittest.TestCase):
    def test_transform_single_item(self):
        xml_data = "<root><item>10</item></root>"
        root = ET.fromstring(xml_data)
        result = transform_to_config_language(root)
        self.assertEqual(result, "[ 10 ]")

    def test_transform_multiple_items(self):
        xml_data = "<root><item>10</item><item>20</item><item>30</item></root>"
        root = ET.fromstring(xml_data)
        result = transform_to_config_language(root)
        self.assertEqual(result, "[ 10, 20, 30 ]")

    def test_transform_dict(self):
        xml_data = "<root><dict><key1>value1</key1><key2>value2</key2></dict></root>"
        root = ET.fromstring(xml_data)
        result = transform_to_config_language(root)
        self.assertEqual(result, "dict(key1 = value1, key2 = value2)")

    def test_transform_calculate(self):
        xml_data = "<root><calculate>MY_CONST</calculate></root>"
        root = ET.fromstring(xml_data)
        result = transform_to_config_language(root)
        self.assertEqual(result, "{ MY_CONST }")

    def test_transform_def(self):
        xml_data = "<root><def><name>MY_CONST</name><value>42</value></def></root>"
        root = ET.fromstring(xml_data)
        result = transform_to_config_language(root)
        self.assertEqual(result, "def MY_CONST = 42")
