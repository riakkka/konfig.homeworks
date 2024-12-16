import unittest
from shell_emulator import Shell

class TestTac(unittest.TestCase):
    def setUp(self):
        self.shell = Shell("config/config.toml", "virtual_fs/example.tar", None)

    def test_reverse_file_content(self):
        content = self.shell.execute_command("tac", "/home/file1.txt")
        self.assertIsInstance(content, str)  # Проверяем, что результат является строкой
