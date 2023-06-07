import file_stats
filename = 'test_file.txt'
lines, words, characters = file_stats.count_file_stats(filename)

print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
print(f"Number of characters: {characters}")