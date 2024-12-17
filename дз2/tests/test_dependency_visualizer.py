import pytest
import os
from unittest.mock import patch, mock_open, MagicMock
from dependency_visualizer import load_config, get_commit_graph, create_image

# Тест для load_config
def test_load_config():
    mock_config = """
    {
        "repo_path": "/fake/repo",
        "branch_name": "main",
        "plantuml_path": "/fake/plantuml.jar",
        "output_image_path": "output.png"
    }
    """
    with patch("builtins.open", mock_open(read_data=mock_config)):
        config = load_config("config.json")
        assert config["repo_path"] == "/fake/repo"
        assert config["branch_name"] == "main"
        assert config["plantuml_path"] == "/fake/plantuml.jar"
        assert config["output_image_path"] == "output.png"

# Тест для get_commit_graph
@patch("dependency_visualizer.Repo")
def test_get_commit_graph(mock_repo):
    # Подготовка мока для коммита
    mock_commit = MagicMock()
    mock_commit.hexsha = "abc123"
    mock_repo.return_value.iter_commits.return_value = [mock_commit]

    repo_path = "/fake/repo"
    branch_name = "main"
    graph = get_commit_graph(repo_path, branch_name)

    # Проверка, что граф содержит ожидаемые данные
    assert "@startuml" in graph
    assert "@enduml" in graph
    assert "abc123" in graph  # Хэш коммита должен присутствовать

# Тест для create_image
@pytest.mark.skip(reason="Requires PlantUML installed")
def test_create_image():
    graph = "@startuml\nA --> B\n@enduml"
    plantuml_path = "/fake/plantuml.jar"
    output_image_path = "output.png"

    with patch("subprocess.run") as mock_run:
        create_image(graph, plantuml_path, output_image_path)

        # Проверяем, что subprocess.run вызван с правильными аргументами
        mock_run.assert_called_with(
            ["java", "-jar", plantuml_path, "-p"],
            input=graph.encode(),
            stdout=pytest.mock.ANY,
            stderr=pytest.mock.ANY,
            check=True
        )
