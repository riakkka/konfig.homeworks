echo "Сборка проекта и запуск тестов..."

# Добавляем корневую папку проекта в PYTHONPATH
export PYTHONPATH=$(pwd)

# Проверка на наличие pytest
if ! command -v pytest &> /dev/null
then
    echo "Ошибка: pytest не установлен. Установите его с помощью 'pip install pytest'."
    exit 1
fi

# Запуск тестов
pytest tests

# Сообщение об успешном завершении
if [ $? -eq 0 ]; then
    echo "Сборка и тесты завершены успешно."
else
    echo "Ошибка при выполнении тестов."
    exit 1
fi
