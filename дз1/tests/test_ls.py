import unittest
from shell_emulator import Shell

class TestLs(unittest.TestCase):
    def setUp(self):
        self.shell = Shell("config/config.toml", "virtual_fs/example.tar", None)

    def test_list_files(self):
        self.shell.execute_command("cd", "/home")
        result = self.shell.execute_command("ls")
        self.assertIsInstance(result, str)  # Проверяем, что результат является строкой
