def tac(shell, current_path, *args):
    if not args:
        return "Укажите файл для команды tac."

    file_path = os.path.normpath(os.path.join(current_path, args[0]))

    try:
        file_member = next(member for member in shell.vfs.getmembers() if member.name == file_path.lstrip("/"))
        with shell.vfs.extractfile(file_member) as f:
            lines = f.readlines()
        return "".join(reversed([line.decode("utf-8") for line in lines]))
    except StopIteration:
        return f"Файл '{args[0]}' не найден."
    except Exception as e:
        return f"Ошибка чтения файла '{args[0]}': {str(e)}"
