import pytest
from src.shell_emulator import Shell

def test_uname():
    shell = Shell()
    result = shell.uname()
    assert result is not None
