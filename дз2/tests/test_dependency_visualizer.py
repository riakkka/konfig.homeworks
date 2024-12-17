import os
import pytest
from dependency_visualizer import (
    read_object,
    get_commit_info,
    get_commit_history,
    translate,
    comp,
    save_diagram,
)

def test_read_object():
    sha = 'abc123'  # Пример SHA для теста
    obj_type, content = read_object(sha)
    assert obj_type is not None, "Объект Git не найден"
    assert content is not None, "Содержимое объекта Git не найдено"

def test_get_commit_info():
    sha = 'abc123'
    commit_info = get_commit_info(sha)
    assert commit_info is not None, "Информация о коммите не получена"
    assert commit_info['hash'] == sha, "Неверный SHA коммита"
    assert 'author' in commit_info, "Отсутствует информация об авторе коммита"

def test_get_commit_history():
    repo_path = '/Users/riakka/Desktop/Konfig'  
    branch_name = 'master'  
    try:
        commit_info = get_commit_history(repo_path, branch_name)
        assert commit_info is not None, "История коммитов не получена"
    except FileNotFoundError:
        pytest.fail(f"Не найдена ветка {branch_name} или репозиторий по пути {repo_path}")

def test_translate():
    mock_commit_info = {
        'hash': 'abc123',
        'author': 'John Doe 1672531200 +0000',
        'parent': None,
    }
    commits = translate(mock_commit_info)
    assert len(commits) == 1, "Неверное количество коммитов"
    assert commits[0][0] == 'abc123', "Неверный SHA коммита в списке"
    assert commits[0][1] == 'John', "Неверный автор коммита"

def test_comp():
    # Тестирование генерации PlantUML
    commits = [
        ('abc123', 'John', '2023-01-01 00:00:00'),
        ('def456', 'Alice', '2023-01-02 00:00:00'),
    ]
    plantuml_code = comp(commits)
    assert '@startuml' in plantuml_code, "PlantUML код должен начинаться с @startuml"
    assert '@enduml' in plantuml_code, "PlantUML код должен заканчиваться @enduml"
    assert 'abc123 : 2023-01-01 00:00:00' in plantuml_code, "Отсутствует информация о коммите"

def test_save_diagram():
    plantuml_code = '@startuml\nabc123 : 2023-01-01 00:00:00\n@enduml'
    image_path = 'test_graph.png'
    try:
        save_diagram(plantuml_code, image_path)
        assert os.path.isfile(image_path), "Файл диаграммы не создан"
    finally:
        if os.path.isfile(image_path):
            os.remove(image_path)
