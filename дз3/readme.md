
---

# Конфигурационный инструмент командной строки для учебного конфигурационного языка

## 1. Общее описание  
В данной работе был создан инструмент для обработки и трансформации данных в пользовательский конфигурационный язык.  
Он позволяет:  
- Валидировать входные XML-данные.  
- Трансформировать XML-структуру в специализированный конфигурационный формат.  
- Проверять результаты трансформации через встроенные тесты.

Этот инструмент создан для упрощения работы с конфигурациями в различных предметных областях, таких как управление складом или развертывание IT-систем.

---

## 2. Описание функций и настроек  

### Функции  

#### 2.1. Валидатор (validator.py)  
- **Функция:** `validate_xml(xml_data: str) -> bool`  
  Проверяет, корректен ли входной XML.  
  - **Входные данные:** строка XML.  
  - **Выходные данные:** `True` (корректно) или `False` (ошибка).  
  - **Пример использования:**  
    ```python
    from validator import validate_xml
    result = validate_xml("<root><item>10</item></root>")
    print(result)  # True
    ```

#### 2.2. Парсер (parser.py)  
- **Функция:** `parse_xml(xml_data: str) -> ElementTree`  
  Разбирает входной XML в дерево элементов.  
  - **Входные данные:** строка XML.  
  - **Выходные данные:** объект `ElementTree` (или выбрасывает исключение `ET.ParseError` при ошибке).  
  - **Пример использования:**  
    ```python
    from parser import parse_xml
    tree = parse_xml("<root><item>10</item></root>")
    print(tree.getroot().tag)  # root
    ```

#### 2.3. Трансформер (transformer.py)  
- **Функция:** `transform_to_config_language(tree: ElementTree) -> str`  
  Преобразует дерево элементов в пользовательский конфигурационный язык.  
  - **Входные данные:** объект `ElementTree`.  
  - **Выходные данные:** строка в формате конфигурационного языка.  
  - **Пример использования:**  
    ```python
    from transformer import transform_to_config_language
    from xml.etree.ElementTree import ElementTree, fromstring
    tree = ElementTree(fromstring("<root><item>10</item></root>"))
    result = transform_to_config_language(tree)
    print(result)  # [ 10 ]
    ```

---

## 3. Описание команд для сборки проекта  

1. **Требования:**  
   Убедитесь, что у вас установлен Python 3.10+ и активирован виртуальный окружение.  

2. **Запуск тестов:**  
   Для проверки функциональности используйте команду:  
   ```bash
   python -m unittest discover -s tests
   ```

3. **Запуск инструментов:**  
   - **Валидация XML:**  
     ```bash
     python validator.py example.xml
     ```
   - **Парсинг и трансформация:**  
     ```bash
     python transformer.py example.xml
     ```

---


## 4. Результаты прогона тестов  

### Команда для запуска:  
```bash
python -m unittest discover -s tests
```

### Лог выполнения:  
```
Ran 11 tests in 0.002s

OK
```

### Отчёт об успешности тестов:  
- Всего тестов: 11.  
- Успешно: 11.  

---

## 5. Ссылка на репозиторий  

[ConfigLang Tool на GitHub](https://github.com/riakkka/konfig.homeworks.git)

---
