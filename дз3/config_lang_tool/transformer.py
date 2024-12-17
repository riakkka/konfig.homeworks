def transform_to_config_language(root):
    result = []
    items = []  # Список для хранения значений элементов <item>

    def process_element(element):

        if element.tag == 'def':
            name = element.find('name').text
            value = element.find('value').text
            result.append(f"def {name} = {value}")
        elif element.tag == 'calculate':
            name = element.text.strip()  # Убираем лишние пробелы и обрабатываем текст
            result.append(f"{{ {name} }}")  # Заключаем в фигурные скобки
        elif element.tag == 'item':
            items.append(element.text)  # Сохраняем элементы <item> в список
        elif element.tag == 'dict':
            dict_items = []
            for child in element:
                key = child.tag
                value = child.text
                dict_items.append(f"{key} = {value}")
            result.append(f"dict({', '.join(dict_items)})")
        elif len(element) == 0:
            result.append(element.text)
        else:
            pass

    # Обрабатываем дочерние элементы корня
    for child in root:
        process_element(child)

    # Если у нас есть элементы <item>, оборачиваем их в квадратные скобки
    if items:
        result.append(f"[ {', '.join(items)} ]")

    return " ".join(result)
