def cd(shell, current_path, *args):
    if not args:
        return "/"

    target_path = args[0]
    full_path = os.path.normpath(os.path.join(current_path, target_path))

    if full_path == "/" or any(member.name.startswith(full_path.lstrip("/")) for member in shell.vfs.getmembers()):
        return full_path

    return f"Директория '{target_path}' не найдена. Текущая директория осталась: {current_path}"
