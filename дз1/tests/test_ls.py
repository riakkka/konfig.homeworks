import os
import pytest
from src.shell_emulator import Shell

def test_ls(tmp_path):
    shell = Shell()
    shell.current_path = str(tmp_path)
    (tmp_path / "file1.txt").touch()
    (tmp_path / "file2.txt").touch()

    result = shell.ls()
    assert "file1.txt" in result
    assert "file2.txt" in result
