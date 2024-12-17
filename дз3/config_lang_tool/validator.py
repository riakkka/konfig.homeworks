import xml.etree.ElementTree as ET

def validate_xml(xml_data):
    """
    Валидирует синтаксис XML, проверяя его корректность.
    """
    try:
        tree = ET.ElementTree(ET.fromstring(xml_data))
        root = tree.getroot()

        # Проверка корректности структуры: корневой элемент должен быть <root>
        if root.tag != "root":
            raise ValueError("Корневой элемент должен быть <root>")

        # Дополнительные проверки на содержание элементов, их типы и структуру
        validate_element(root)

        return True
    except (ET.ParseError, ValueError) as e:
        print(f"Ошибка: {e}")
        return False

def validate_element(element):
    """
    Рекурсивная проверка элементов XML на корректность.
    Проверяем типы данных и наличие нужных элементов.
    """
    if len(element) > 0:  # если у элемента есть дочерние элементы
        for child in element:
            validate_element(child)
    else:
        # Проверка содержимого листовых элементов
        if element.tag == "item" and not element.text.isdigit():
            raise ValueError(f"Неверное значение в элементе <{element.tag}>: должно быть числом.")
        if element.tag == "setting" and element.text not in ["True", "False"]:
            raise ValueError(f"Неверное значение в элементе <{element.tag}>: должно быть 'True' или 'False'.")
