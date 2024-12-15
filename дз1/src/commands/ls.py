def ls(shell, *args):
    path = shell.current_path if not args else args[0]
    try:
        files = shell.list_files(path)
        if not files:
            return f"В директории {path} нет файлов или папок."
        return "\n".join([file[len(path):].lstrip("/") for file in files if file != path])
    except Exception as e:
        return f"Ошибка доступа к директории {path}: {str(e)}"

