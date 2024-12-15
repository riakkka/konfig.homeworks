import os
import sys
import tarfile

class Shell:
    def __init__(self, archive_path):
        self.current_path = "/"  #текущая виртуальная директория
        self.vfs = {}  #виртуальная файловая система: словарь {путь: содержимое файла}
        self.load_vfs_from_tar(archive_path)  #загружаем архив в VFS

    def load_vfs_from_tar(self, archive_path):
        """
        Загружает файлы из архива example.tar в виртуальную файловую систему.
        """
        try:
            with tarfile.open(archive_path, "r") as tar:
                for member in tar.getmembers():
                    if member.isfile():  #игнор директорий
                        file = tar.extractfile(member)
                        if file:
                            content = file.read().decode("utf-8")
                            self.vfs[os.path.normpath(f"/{member.name}")] = content
        except Exception as e:
            print(f"Ошибка загрузки архива: {e}")
            sys.exit(1)

    def run(self):
        """
        Главный цикл эмулятора командной строки.
        """
        while True:
            command_input = input(f"{self.current_path}$ ").strip()
            if command_input:
                command_parts = command_input.split()
                command = command_parts[0]
                args = command_parts[1:]
                result = self.execute_command(command, *args)
                if result is not None:  #команда что-то возвращает — выводим
                    print(result)

    def execute_command(self, command, *args):
        """
        Выполняет команду, переданную пользователем.
        """
        commands = {
            "cd": self.cd,
            "ls": self.ls,
            "exit": self.exit_shell,
            "tac": self.tac,
            "uniq": self.uniq,
            "uname": self.uname
        }
        if command in commands:
            return commands[command](*args)
        return f"Неизвестная команда: {command}"

    def cd(self, path):
        """
        Перемещает пользователя между виртуальными директориями.
        """
        new_path = os.path.normpath(os.path.join(self.current_path, path))
        #проверка существует ли путь в виртуальной файловой системе
        if any(file.startswith(new_path.rstrip("/") + "/") or file == new_path for file in self.vfs):
            self.current_path = new_path
            return f"Текущая директория: {self.current_path}"
        return f"Директория не найдена: {path}"

    def ls(self, *args):
        """
        Показывает файлы и папки в текущей виртуальной директории.
        """
        path_prefix = self.current_path.rstrip("/") + "/"
        files_in_dir = set()
        for file in self.vfs:
            if file.startswith(path_prefix):
                rel_path = file[len(path_prefix):].split("/", 1)[0]
                files_in_dir.add(rel_path)
        return "\n".join(sorted(files_in_dir)) if files_in_dir else "Пусто"

    def exit_shell(self, *args):
        """
        Завершает работу эмулятора.
        """
        print("Выход из эмулятора.")
        sys.exit(0)

    def tac(self, filename):
        """
        Показывает содержимое файла в обратном порядке.
        """
        file_path = os.path.normpath(os.path.join(self.current_path, filename))
        if file_path in self.vfs:
            lines = self.vfs[file_path].splitlines()
            return "\n".join(reversed(lines))
        return f"Файл не найден: {filename}"

    def uniq(self, filename):
        """
        Выводит уникальные строки из файла.
        """
        file_path = os.path.normpath(os.path.join(self.current_path, filename))
        if file_path in self.vfs:
            lines = self.vfs[file_path].splitlines()
            unique_lines = "\n".join(sorted(set(lines), key=lines.index))
            return unique_lines
        return f"Файл не найден: {filename}"

    def uname(self, *args):
        """
        Возвращает имя операционной системы.
        """
        return "Darwin"  #фиксируем "Darwin"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("чтобы все работало введите: python3 shell_emulator.py <путь_к_архиву>")
        sys.exit(1)
    archive_path = sys.argv[1]
    shell = Shell(archive_path)  #создаем объект эмулятора
    shell.run()  #запускаем заново основной цикл
