import unittest
from shell_emulator import Shell

class TestUniq(unittest.TestCase):
    def setUp(self):
        self.shell = Shell("config/config.toml", "virtual_fs/example.tar", None)

    def test_remove_duplicates(self):
        content = self.shell.execute_command("uniq", "/home/file_with_duplicates.txt")
        self.assertIsInstance(content, str)  # Проверяем, что результат является строкой
