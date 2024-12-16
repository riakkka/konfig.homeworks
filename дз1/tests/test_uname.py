import unittest
from shell_emulator import Shell

class TestUname(unittest.TestCase):
    def setUp(self):
        self.shell = Shell("config/config.toml", "virtual_fs/example.tar", None)

    def test_uname_output(self):
        result = self.shell.execute_command("uname")
        self.assertIsInstance(result, str)  # Проверяем, что результат является строкой
