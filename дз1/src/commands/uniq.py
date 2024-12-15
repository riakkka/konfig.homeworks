def uniq(shell, current_path, *args):
    if not args:
        return "Укажите файл для команды uniq."

    file_path = os.path.normpath(os.path.join(current_path, args[0]))

    try:
        file_member = next(member for member in shell.vfs.getmembers() if member.name == file_path.lstrip("/"))
        with shell.vfs.extractfile(file_member) as f:
            lines = f.readlines()
        unique_lines = list(dict.fromkeys([line.decode("utf-8") for line in lines]))
        return "".join(unique_lines)
    except StopIteration:
        return f"Файл '{args[0]}' не найден."
    except Exception as e:
        return f"Ошибка обработки файла '{args[0]}': {str(e)}"
