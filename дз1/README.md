
---

# Shell Emulator  

## Описание  
Этот проект представляет собой эмулятор командной строки с базовыми командами Unix, такими как `cd`, `ls`, `tac`, `uniq`, `uname`, `exit`. Проект построен на Python и включает графический интерфейс для работы с виртуальной файловой системой, реализованной на основе tar-архива.  

Эмулятор поддерживает:  
- Перемещение по директориям (`cd`).  
- Отображение содержимого директорий (`ls`).  
- Отображение содержимого файла в обратном порядке (`tac`).  
- Удаление дубликатов строк в файле (`uniq`).  
- Вывод имени компьютера из конфигурационного файла (`uname`)
- Выход из эмулятора (`exit`).  

Тестирование всех функций осуществляется через модульные тесты.  

---

## Функции и настройки  

### Основные команды  
1. **`cd [path]`**  
   Переход в указанную директорию.  
   - Аргумент `path` может быть абсолютным (`/home`) или относительным (`../`).  
   - Пример использования:  
     ```bash
     /$ cd /home
     Текущая директория: /home
     ```

2. **`ls`**  
   Отображение списка файлов и поддиректорий в текущей директории.  
   - Пример использования:  
     ```bash
     /home$ ls
     file1.txt
     dir1
     ```

3. **`tac [file_path]`**  
   Отображение содержимого файла в обратном порядке.  
   - Аргумент `file_path`: путь к файлу.  
   - Пример использования:  
     ```bash
     /home$ tac file1.txt
     Строка 3
     Строка 2
     Строка 1
     ```

4. **`uniq [file_path]`**  
   Удаление дубликатов строк в файле.  
   - Аргумент `file_path`: путь к файлу.  
   - Пример использования:  
     ```bash
     /home$ uniq file_with_duplicates.txt
     Строка 1
     Строка 2
     ```

5. **`uname`**  
   Вывод имени компьютера из конфигурационного файла `config.toml`.  
   - Пример использования:  
     ```bash
     /$ uname
     MyComputer
     ```

6. **`exit`**  
   Выход из эмулятора.  
   - Пример использования:  
     ```bash
     /$ exit
     ```

### Настройки  
- Конфигурационный файл `config/config.toml` содержит имя компьютера, которое используется в команде `uname`.  
- Виртуальная файловая система загружается из tar-архива, указанного при запуске программы.  

---

## Сборка проекта  

### Зависимости  
Перед началом работы необходимо установить зависимости:  
```bash
pip install -r requirements.txt
```

### Команды сборки  
1. **Запуск программы с GUI:**  
   ```bash
   python shell_emulator.py [path_to_tar_archive]
   ```  

2. **Запуск тестов:**  
   ```bash
   python -m unittest discover -s tests -p "test_*.py"
   ```

---

## Результаты тестирования  

Результаты успешного прогона тестов:  
```bash
$ python -m unittest discover -s tests -p "test_*.py"
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

## Графический интерфейс

![графический интерфейс](дз1/image/emulator.png)


## Ссылка на репозиторий
https://github.com/riakkka/konfig.homeworks.git
