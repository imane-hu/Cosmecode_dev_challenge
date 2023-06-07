def count_file_stats(filename):
    line_count = 0
    word_count = 0
    char_count = 0

    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)
            char_count += len(line)

    return line_count, word_count, char_count
    