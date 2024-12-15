import pytest
from src.shell_emulator import Shell

def test_tac(tmp_path):
    shell = Shell()
    test_file = tmp_path / "test.txt"
    test_file.write_text("line1\nline2\nline3")

    result = shell.tac(str(test_file))
    assert result == "line3\nline2\nline1"
