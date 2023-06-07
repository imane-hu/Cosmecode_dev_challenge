import sys, rev_alpha
# Get the arguments from the command line
arguments = sys.argv[1:]

# Merge the arguments into a single string separated by spaces
merged_string = ' '.join(arguments)

# Check if any argument is provided
if merged_string:
    result = rev_alpha.reverse_swap_case(merged_string)
    print(result)