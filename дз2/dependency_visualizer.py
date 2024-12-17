import subprocess
import json
import os

def get_commit_graph(repo_path, branch_name):
    """Получаем граф зависимостей коммитов для ветки Git через git-команды"""
    
    # Выполним команду git rev-list для получения хешей коммитов в ветке
    command = ['git', 'rev-list', branch_name]
    result = subprocess.run(command, cwd=repo_path, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise Exception(f"Git error: {result.stderr}")
    
    commits = result.stdout.strip().split('\n')
    
    graph = "@startuml\n"
    
    for commit in commits:
        # Получаем родительские коммиты для текущего коммита
        command_parents = ['git', 'log', '--pretty=%P', '-n', '1', commit]
        result_parents = subprocess.run(command_parents, cwd=repo_path, capture_output=True, text=True)
        
        if result_parents.returncode != 0:
            raise Exception(f"Git error: {result_parents.stderr}")
        
        parents = result_parents.stdout.strip().split()
        
        for parent in parents:
            graph += f'"{commit}" --> "{parent}"\n'
    
    graph += "@enduml"
    return graph

def generate_uml_image(puml_content, output_image_path):
    """Генерируем изображение из текста PlantUML с помощью PlantUML"""
    
    # Сохранение текстового представления в файл .puml
    puml_file = "temp_graph.puml"
    with open(puml_file, "w") as f:
        f.write(puml_content)
    
    # Указываем правильный путь к plantuml.jar
    plantuml_jar_path = '/opt/homebrew/Cellar/plantuml/1.2024.8/libexec/plantuml.jar'  # Укажи свой путь
    
    # Запускаем PlantUML для генерации PNG
    command = ['java', '-jar', plantuml_jar_path, puml_file]
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise Exception(f"PlantUML error: {result.stderr}")
    
    # Перемещаем полученное изображение в нужный путь
    os.rename(puml_file.replace('.puml', '.png'), output_image_path)
    print(f"Изображенеи графа было сохранено в {output_image_path}")
    
    # Удаляем временные файлы
    os.remove(puml_file)

def main(config_path):
    # Чтение конфигурационного файла
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Получаем граф зависимостей
    graph = get_commit_graph(config['repo_path'], config['branch_name'])
    
    # Генерируем изображение из графа
    generate_uml_image(graph, config['output_image_path'])
    
    print("Граф был успешно создан")

if __name__ == "__main__":
    main('config.json')
