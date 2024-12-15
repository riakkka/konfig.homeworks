import pytest
from src.shell_emulator import Shell

def test_uniq(tmp_path):
    shell = Shell()
    test_file = tmp_path / "test.txt"
    test_file.write_text("line1\nline2\nline1\nline3")

    result = shell.uniq(str(test_file))
    assert result == "line1\nline2\nline3"
