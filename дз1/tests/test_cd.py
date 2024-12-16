import unittest
from shell_emulator import Shell

class TestCd(unittest.TestCase):
    def setUp(self):
        self.shell = Shell("config/config.toml", "virtual_fs/example.tar", None)

    def test_change_directory(self):
        result = self.shell.execute_command("cd", "/home")
        self.assertIn("/home", result)

    def test_invalid_directory(self):
        result = self.shell.execute_command("cd", "/invalid")
        self.assertIn("Директория не найдена", result)
