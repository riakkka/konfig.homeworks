import sys
import os
import unittest
from src.shell_emulator import Shell

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # Пути к файлам в проекте
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.config_path = os.path.join(project_root, 'config', 'config.toml')
        self.archive_path = os.path.join(project_root, 'virtual_fs', 'example.tar')
        self.output_widget = None

        # Инициализация оболочки
        self.shell = Shell(self.config_path, self.archive_path, self.output_widget)
