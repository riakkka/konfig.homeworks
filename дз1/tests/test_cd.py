import pytest
from src.shell_emulator import Shell

def test_cd():
    shell = Shell()
    assert "Текущая директория" in shell.cd("/")
    assert "Директория не найдена" in shell.cd("/неизвестная_папка")
