
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

## 2. Примеры описания конфигураций из разных предметных областей
### Пример 1: Конфигурация для управления складом
Предположим, что мы работаем с конфигурацией для системы управления складом. Конфигурация может описывать товары, их количество и расположение на складе. Пример XML-конфигурации:

xml
Копировать код
<warehouse>
    <item>
        <name>Product A</name>
        <quantity>100</quantity>
        <location>A1</location>
    </item>
    <item>
        <name>Product B</name>
        <quantity>200</quantity>
        <location>B1</location>
    </item>
</warehouse>
---

### Пример 2: Конфигурация для развертывания IT-системы
Для развертывания IT-системы может понадобиться описание серверов, их ролей и конфигураций. Пример XML-конфигурации:

xml
Копировать код
<deployment>
    <server>
        <hostname>server1</hostname>
        <role>web</role>
        <ip>192.168.0.1</ip>
    </server>
    <server>
        <hostname>server2</hostname>
        <role>database</role>
        <ip>192.168.0.2</ip>
    </server>
</deployment>

## 3. Описание функций и настроек  

### Функции  

#### 3.1. Валидатор (validator.py)  
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

#### 3.2. Парсер (parser.py)  
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

#### 3.3. Трансформер (transformer.py)  
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

## 4. Описание команд для сборки проекта  

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


## 5. Результаты прогона тестов  

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

## 6. Ссылка на репозиторий  

[ConfigLang Tool на GitHub](https://github.com/riakkka/konfig.homeworks.git)

---
