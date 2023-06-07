import data_stats

csv_file = "data.csv"
mean, median, std_dev = data_stats.data_info(csv_file)
# Print the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")