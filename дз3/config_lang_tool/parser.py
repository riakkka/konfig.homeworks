import xml.etree.ElementTree as ET

def parse_xml(xml_data):
    """
    Парсит XML-данные и возвращает дерево элементов.
    """
    try:
        tree = ET.ElementTree(ET.fromstring(xml_data))
        return tree
    except ET.ParseError as e:
        print(f"Ошибка при разборе XML: {e}")
        return None

def validate_xml(xml_data):
    """
    Валидирует синтаксис XML.
    Возвращает True, если XML корректен, иначе False.
    """
    return parse_xml(xml_data) is not None
