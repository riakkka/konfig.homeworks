import unittest
import xml.etree.ElementTree as ET
from parser import parse_xml  # Импорт функции parse_xml

class TestParser(unittest.TestCase):

    def test_parse_valid_xml(self):
        valid_xml = "<root><child>Test</child></root>"
        result = parse_xml(valid_xml)
        # Убедимся, что возвращается корневой элемент
        self.assertEqual(result.tag, 'root')  # Проверяем тег корневого элемента
        self.assertEqual(result[0].tag, 'child')  # Проверяем тег первого дочернего элемента

    def test_parse_empty_xml(self):
        empty_xml = ""  # Пустая строка
        with self.assertRaises(ET.ParseError):  # Пустой XML должен вызывать ошибку
            parse_xml(empty_xml)

    def test_parse_invalid_xml(self):
        invalid_xml = "<root><child>Test</root>"  # Некорректный XML
        with self.assertRaises(ET.ParseError):  # Ожидаем ошибку
            parse_xml(invalid_xml)
