import csv


def get_csv(filename: str):
    columns = int(filename.split('_')[-1])

    with open(f'{filename}.txt', encoding='UTF-8') as f:
        lines = f.readlines()

    new_lines = []
    new_line = []
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip().replace(',', '.')
        if len(new_line) < columns:
            new_line.append(lines[i])
        elif len(new_line) >= columns:
            new_lines.append(new_line)
            new_line = [lines[i]]

    with open(f'{filename}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_lines)


get_csv('filename_col')  # edit filename_col
