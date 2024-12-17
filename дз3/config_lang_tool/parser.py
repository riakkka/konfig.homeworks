import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    if not xml_string.strip():  # Проверка на пустую строку
        raise ET.ParseError("XML string is empty")
    
    try:
        return ET.fromstring(xml_string)
    except ET.ParseError as e:
        print(f"Ошибка при разборе XML: {e}")
        raise  # Повторное выбрасывание исключения, чтобы тесты могли его поймать
