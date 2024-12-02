import os
import tomli
from pathlib import Path

class ShellEmulator:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.computer_name = self.config["computer_name"]
        self.tar_path = Path(self.config["tar_path"])
    
    def load_config(self, config_path):
        with open(config_path, "rb") as file:
            return tomli.load(file)
    
    def start(self):
        if not self.tar_path.exists():
            print(f"Ошибка: файл {self.tar_path} не найден.")
            return
        print(f"Добро пожаловать в {self.computer_name}! Введите 'exit' для выхода.")
        while True:
            try:
                command = input(f"{self.computer_name}$ ")
                if command == "exit":
                    print("Выход из эмулятора.")
                    break
                else:
                    print(f"Команда '{command}' пока не поддерживается.")
            except KeyboardInterrupt:
                print("\nВыход из эмулятора.")
                break

if __name__ == "__main__":
    config_path = Path(__file__).parent.parent / "config" / "config.toml"
    emulator = ShellEmulator(config_path)
    emulator.start()
