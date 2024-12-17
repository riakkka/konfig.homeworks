import xml.etree.ElementTree as ET
from transformer import transform_to_config_language

def main():
    # Читаем XML с стандартного ввода
    xml_data = input().strip()  # Убираем возможные лишние пробелы и символы новой строки

    # Разбираем XML
    root = ET.fromstring(xml_data)

    # Преобразуем данные в конфигурационный язык
    transformed_data = transform_to_config_language(root)

    # Выводим результат на стандартный вывод
    print(transformed_data)  # Проверяем результат

if __name__ == "__main__":
    main()
