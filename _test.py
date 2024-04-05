import pytest
from main import comparing
# Фікстура для створення тестових файлів
@pytest.fixture
def create_test_files(tmp_path):
    # Шляхи до тестових файлів
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    same = tmp_path / "same.txt"
    diff = tmp_path / "diff.txt"

    # Створення тестового вмісту для файлів
    file1_content = "line1 anyline cntrl\ndifferent line2\nline3 notline str"
    file2_content = "line1 anyline cntrl\ndiff line41\nline3 notline str"

    # Запис тестового вмісту в файли
    file1.write_text(file1_content)
    file2.write_text(file2_content)

    # Повертаємо шляхи до тестових файлів
    return file1, file2, same, diff

# Тест, який використовує фікстуру для створення тестових файлів і перевірки результатів порівняння
def test_comparing(create_test_files):
    file1, file2, same, diff = create_test_files
    comparing(file1, file2, same, diff)

    same_contents = same.read_text().strip().split('\n')
    diff_contents = diff.read_text().strip().split('\n')

    # Sort the contents before asserting
    assert sorted(same_contents) == sorted(["line1 anyline cntrl", "line3 notline str"])
    assert sorted(diff_contents) == sorted(["different line2", "diff line41"])

# Виклик pytest для запуску тесту
# pytest test_comparing.py