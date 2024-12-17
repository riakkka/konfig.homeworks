import os
import json
import zlib
from datetime import datetime

# Функция для загрузки конфигурации из JSON
def load_config():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            print(f"Конфигурация успешно загружена: {config}")
            return config
    except Exception as e:
        print(f"Ошибка при загрузке конфигурации: {e}")
        raise

# Функция для чтения объекта из Git-репозитория
def read_object(sha):
    path = os.path.join('.git', 'objects', sha[:2], sha[2:])
    if not os.path.isfile(path):
        return None, None
    with open(path, 'rb') as f:
        data = f.read()
    data = zlib.decompress(data)
    size, obj_type, content = parse_git_object(data)
    return obj_type, content

# Функция для парсинга Git-объекта
def parse_git_object(data):
    header_end = data.index(b'\0')
    header = data[:header_end].decode()
    obj_type, size = header.split(' ')
    content = data[header_end + 1:]
    return size, obj_type, content

# Функция для получения информации о коммите
def get_commit_info(commit_sha):
    obj_type, content = read_object(commit_sha)
    if obj_type != 'commit':
        return None
    lines = content.decode().splitlines()
    commit_info = {}
    commit_info['hash'] = commit_sha
    commit_info['parent'] = None
    for line in lines:
        if line.startswith('parent'):
            hash = line.split()[1]
            commit_info['parent'] = get_commit_info(hash)
        elif line.startswith('author'):
            commit_info['author'] = line.split(' ', 2)[2]
    return commit_info

# Функция для получения истории коммитов
def get_commit_history(repo_path, branch_name):
    os.chdir(repo_path)  # Перемещаемся в каталог репозитория
    branch_path = os.path.join('.git', 'refs', 'heads', branch_name)
    with open(branch_path, 'r', encoding='utf-8') as f:
        commit_sha = f.read().strip()
        commit_info = get_commit_info(commit_sha)
        return commit_info

# Функция для преобразования информации о коммитах в список кортежей
def translate(commit_info):
    if commit_info is None:
        return []
    author, timestamp, _ = commit_info['author'].split()
    ts = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    return [(commit_info['hash'], author, ts)] + translate(commit_info['parent'])

# Функция для формирования диаграммы PlantUML
def comp(commits):
    output = ['@startuml']
    for hash, author, date in commits:
        output.append(f'{hash} : {date}')
        output.append(f'{hash} : {author}(author)')
    window_size = 2
    for i in range(len(commits) - window_size + 1):
        a, b = commits[i:i + window_size]
        output.append(f'{a[0]} <|-- {b[0]}')
    output.append('@enduml')
    return '\n'.join(output)

# Функция для сохранения диаграммы в формате PNG
def save_diagram(plantuml_code, image_path):
    try:
        # Сохраняем код диаграммы в файл
        with open('graph.puml', 'w') as f:
            f.write(plantuml_code)

        # Запускаем генерацию изображения с помощью PlantUML
        os.system(f'plantuml graph.puml -o {os.path.dirname(image_path)}')

        # Переименовываем и удаляем временный файл
        os.rename('graph.png', image_path)
        os.remove('graph.puml')
        print(f"Диаграмма сохранена в файл: {image_path}")
    except Exception as e:
        print(f"Ошибка при сохранении диаграммы: {e}")

# Основная функция
def main():
    try:
        # Загружаем конфигурацию
        config = load_config()
        visualization_path = config.get('visualization_path', '')
        repo_path = config.get('repo_path', '')
        image_path = config.get('image_path', '')
        branch_name = config.get('branch_name', '')

        if not all([visualization_path, repo_path, image_path, branch_name]):
            raise ValueError("Отсутствуют необходимые параметры в конфигурации.")

        # Получаем историю коммитов
        commit_info = get_commit_history(repo_path, branch_name)

        # Преобразуем историю в формат для визуализации
        commits = translate(commit_info)

        # Генерируем код для PlantUML
        plantuml_code = comp(commits)

        # Сохраняем диаграмму в файл
        save_diagram(plantuml_code, image_path)

        print("Процесс завершен успешно!")

    except Exception as e:
        print(f"Ошибка в процессе работы программы: {e}")

# Запуск основной функции
if __name__ == "__main__":
    main()
