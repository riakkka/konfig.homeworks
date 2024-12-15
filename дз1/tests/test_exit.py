import pytest
from src.shell_emulator import Shell
import sys

def test_exit(monkeypatch):
    shell = Shell()

    with pytest.raises(SystemExit):
        monkeypatch.setattr(sys, 'exit', lambda code: (_ for _ in ()).throw(SystemExit))
        shell.execute_command("exit")
