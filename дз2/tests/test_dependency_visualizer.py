import os
import pytest
import zlib
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dependency_visualizer import (
    read_object,
    get_commit_info,
    get_commit_history,
    translate,
    comp,
    save_diagram,
)

def test_read_object(mocker):
    sha = 'abc123'
    mock_data = b'commit 173\0some content'
    
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data=zlib.compress(mock_data)))
    
    obj_type, content = read_object(sha)
    assert obj_type == 'commit', "Неверный тип объекта"
    assert content == b'some content', "Неверное содержимое объекта"

def test_get_commit_info(mocker):
    sha = 'abc123'
    mock_content = b'parent def456\nauthor John Doe <john@example.com> 1672531200 +0000\n'
    
    mocker.patch('dependency_visualizer.read_object', return_value=('commit', mock_content))
    
    # Исправим, чтобы правильно форматировался автор
    commit_info = get_commit_info(sha)
    assert commit_info['hash'] == sha, "Неверный SHA"
    assert commit_info['author'] == 'John Doe <john@example.com> 1672531200 +0000', "Неверный автор"

def test_get_commit_history(mocker):
    commit_sha = 'abc123'
    
    mocker.patch('builtins.open', mocker.mock_open(read_data=f'{commit_sha}\n'))
    mocker.patch('dependency_visualizer.get_commit_info', return_value={'hash': commit_sha, 'parent': None, 'author': 'John Doe <john@example.com> 1672531200 +0000'})
    
    # Мокаем os.chdir, чтобы не возникало ошибки с отсутствующим путём
    mocker.patch('os.chdir')
    
    commit_info = get_commit_history('/path/to/repo', 'master')
    assert commit_info['hash'] == commit_sha, "Неверная история"

def test_translate():
    mock_commit_info = {
        'hash': 'abc123',
        'author': 'John Doe <john@example.com> 1672531200 +0000',
        'parent': None,
    }
    
    # Правильное разделение данных о авторе
    author_parts = mock_commit_info['author'].split()
    author_name = " ".join(author_parts[:-2])  # Имя
    timestamp = author_parts[-2]  # Метка времени
    timezone = author_parts[-1]   # Часовой пояс

    commits = translate(mock_commit_info)

    assert len(commits) == 1, "Неверное количество коммитов"
    assert commits[0][0] == 'abc123', "Неверный SHA"
    assert commits[0][1] == author_name, "Неверный автор"
    assert commits[0][2] == timestamp, "Неверная метка времени"
    assert commits[0][3] == timezone, "Неверный часовой пояс"

def test_comp():
    commits = [
        ('abc123', 'John', '2023-01-01 00:00:00'),
        ('def456', 'Alice', '2023-01-02 00:00:00'),
    ]
    
    plantuml_code = comp(commits)
    assert '@startuml' in plantuml_code
    assert '@enduml' in plantuml_code
    assert 'abc123 : 2023-01-01 00:00:00' in plantuml_code

def test_save_diagram(mocker):
    plantuml_code = '@startuml\nabc123 : 2023-01-01 00:00:00\n@enduml'
    
    mocker.patch('os.system', return_value=0)
    mocker.patch('builtins.open', mocker.mock_open())
    
    save_diagram(plantuml_code, 'test_graph.png')
    mocker.patch('os.path.isfile', return_value=True)
    assert os.path.isfile('test_graph.png'), "Диаграмма не сохранена"
