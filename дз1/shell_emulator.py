import os
import sys
import tarfile
import tomllib
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog


class Shell:
    def __init__(self, config_path, archive_path, output_widget):
        self.config_path = config_path
        self.current_path = "/" 
        self.vfs = self.load_virtual_fs(archive_path)
        self.output_widget = output_widget
        self.computer_name = self.load_computer_name()

    def load_computer_name(self): 
        try:
            with open(self.config_path, "rb") as file:
                config = tomllib.load(file)
                return config["computer_name"]
        except Exception as e:
            return f"Ошибка чтения config.toml: {e}"

    def load_virtual_fs(self, archive_path):
        vfs = {}
        try:
            with tarfile.open(archive_path, "r") as archive:
                for member in archive.getmembers():
                    if member.isfile():  # Загружаем только файлы
                        normalized_path = "/" + member.name  # Добавляем начальный слэш
                        file_content = archive.extractfile(member).read().decode("utf-8")
                        vfs[normalized_path] = file_content
            return vfs
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузки архива: {e}")
            sys.exit(1)

    def execute_command(self, command, *args):
        commands = {
            "cd": self.cd,
            "ls": self.ls,
            "tac": self.tac,
            "uniq": self.uniq,
            "uname": self.uname,
            "exit": self.exit,
        }
        if command in commands:
            return commands[command](*args)
        return f"Неизвестная команда: {command}"

    def cd(self, path):
        if path == "/":
            self.current_path = "/"
            return f"Текущая директория: {self.current_path}"
        
        full_path = os.path.normpath(os.path.join(self.current_path, path))
        full_path = full_path + "/" if not full_path.endswith("/") else full_path  # Убедимся, что путь заканчивается на /

        # Проверяем, есть ли файлы в архиве, начинающиеся с указанного пути
        is_valid_directory = any(file_path.startswith(full_path) for file_path in self.vfs)
        if is_valid_directory:
            self.current_path = full_path
            return f"Текущая директория: {self.current_path}"
        return f"Директория не найдена: {path}"

    def ls(self, *args):
        current_dir = self.current_path if self.current_path.endswith("/") else self.current_path + "/"
        entries = set()

        for path in self.vfs:
            if path.startswith(current_dir):
                relative_path = path[len(current_dir):]
                first_part = relative_path.split("/")[0]
                entries.add(first_part)

        if not entries:
            return "Пусто"

        return "\n".join(sorted(entries))


    def tac(self, file_path):
        full_path = os.path.normpath(os.path.join(self.current_path, file_path))
        if full_path in self.vfs:
            return "\n".join(reversed(self.vfs[full_path].splitlines()))
        return f"Файл не найден: {file_path}"

    def uniq(self, file_path):
        full_path = os.path.normpath(os.path.join(self.current_path, file_path))
        if full_path in self.vfs:
            lines = self.vfs[full_path].splitlines()
            return "\n".join(sorted(set(lines), key=lines.index))
        return f"Файл не найден: {file_path}"

    def uname(self, *args):
        return self.computer_name
    
    def exit(self, *args):
        sys.exit("Выход из эмулятора Shell")



class ShellGUI:
    def __init__(self, root, config_path, archive_path):
        self.root = root
        self.shell = Shell(config_path, archive_path, self.create_output_widget())
        self.root.title("Эмулятор Shell")
        
        # Текстовое поле для вывода результатов
        self.output = scrolledtext.ScrolledText(self.root, width=80, height=20, wrap=tk.WORD)
        self.output.pack(pady=10)

        # Поле для ввода команды
        self.command_entry = tk.Entry(self.root, width=80)
        self.command_entry.pack(pady=5)
        self.command_entry.bind("<Return>", self.execute_command)

        # Кнопка выполнения
        self.run_button = tk.Button(self.root, text="Выполнить", command=self.run_command)
        self.run_button.pack(pady=5)

        # Начальный вывод
        self.show_output("Эмулятор Shell запущен. Текущая директория: /")

    def create_output_widget(self):
        """
        Создаёт виджет для вывода сообщений.
        """
        output_widget = scrolledtext.ScrolledText(self.root, width=80, height=20, wrap=tk.WORD)
        output_widget.config(state=tk.DISABLED)  # Запрещаем редактирование
        return output_widget

    def execute_command(self, event=None):
        self.run_command()

    def run_command(self):
        command_input = self.command_entry.get().strip()
        if not command_input:
            return

        parts = command_input.split()
        cmd, args = parts[0], parts[1:]
        result = self.shell.execute_command(cmd, *args)
        self.show_output(f"{self.shell.current_path}$ {command_input}\n{result}")
        self.command_entry.delete(0, tk.END)

    def show_output(self, text):
        """
        Выводит текст в виджет для вывода в графическом интерфейсе.
        """
        self.output.config(state=tk.NORMAL)  # Включаем редактирование
        self.output.insert(tk.END, text + "\n")
        self.output.yview(tk.END)
        self.output.config(state=tk.DISABLED)  # Запрещаем редактирование

def main():
    # Определяем путь к config.toml относительно текущего файла
    config_path = os.path.join(os.path.dirname(__file__), "../config/config.toml")
    
    if len(sys.argv) != 2:
        archive_path = filedialog.askopenfilename(
            title="Выберите tar-архив",
            filetypes=[("Tar Archive", "*.tar")]
        )
        if not archive_path:
            messagebox.showerror("Ошибка", "Архив не выбран. Завершение программы.")
            return
    else:
        archive_path = sys.argv[1]

    root = tk.Tk()
    app = ShellGUI(root, config_path, archive_path)
    root.mainloop()


if __name__ == "__main__":
    main()
