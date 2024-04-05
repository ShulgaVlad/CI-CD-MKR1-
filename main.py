def comparing(file1_path, file2_path, same_path, diff_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        # Зчитування рядків кожного файлу і видалення пробільних символів на початку та кінці рядків
        file1_lines = set(line.strip() for line in file1.readlines())
        file2_lines = set(line.strip() for line in file2.readlines())

    # Визначення спільних та унікальних рядків
    same_lines = file1_lines.intersection(file2_lines)
    diff_lines = file1_lines.symmetric_difference(file2_lines)

    # Запис спільних рядків у файл "same.txt"
    with open(same_path, 'w', encoding='utf-8') as same_file:
        for line in same_lines:
            same_file.write(line + '\n')

    # Запис унікальних рядків у файл "diff.txt"
    with open(diff_path, 'w', encoding='utf-8') as diff_file:
        for line in diff_lines:
            diff_file.write(line + '\n')

