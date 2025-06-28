# Preprocess Phase: Create the last occurrence table function
def last_occurrence_table(text, pattern):
    last = {}                       # Dictionary to store key, value (eg: 'a': value)
    n = len(text)                   # n: length of text
    m = len(pattern)                # m: length of pattern
    for i in range(n):              # Iterates through all character in text
        last[text[i]] = -1          # Set each character in text to -1
    for j in range(m):              # Iterates through all character in pattern
        last[pattern[j]] = j        # Rewrite value of character in pattern based on last occurrence
    return last

# Searching Phase: Boyer-Moore function (return -1 if no pattern is found, return index if found)
def BoyerMoore(text, pattern):
    n = len(text)           # n: length of text
    m = len(pattern)        # m: length of pattern
    if (m == 0 or n == 0 or m > n):  # Check if any of text or pattern has null value
        return -1, [], 0    # return -1 as it cannot be found, (index, character not compared, shift count)

    last = last_occurrence_table(text, pattern) # Function call: last occurrence table
    i = m - 1     # Index in text: for traverse and compare
    j = m - 1     # Index in pattern: for traverse and compare
    prev_i = i    # To store the previous i value and calculate the shift value
    shift = 0     # To store shift count
    compared_indices = set() # To store the indices that has been compared
    count = 0     # To store number of comparison done

    while (i < n):
        compared_indices.add(i)       # Add indices that has been compared
        count += 1                    # Increment count value
        if (text[i] == pattern[j]):   # Case: Character matched
            if j == 0:                 # Finish check: All characters in pattern match with text
                return i, (set(range(n)) - compared_indices), count
            else:                     # Didn't finish checking: check previous character
                i -= 1                # Decrement index of text: Looking-Glass Heuristic
                j -= 1                # Decrement index of pattern: Looking-Glass Heuristic
        else:                         # Case: Character mismatched
            shift += 1
            prev_i = (i + m - min(j, 1 + last.get(text[i]))) - prev_i   # Count how many position the pattern shift
            print(f"Shift {shift}: Mismatch at text[{i}] = '{text[i]}', shifting by {prev_i} characters")
            i += m - min(j, 1 + last.get(text[i]))  # Character-Jump Heuristic: jump step
            j = m - 1                               # Restart to the end of pattern
            prev_i = i                               # Reset shift value to the new i position

    return -1, (set(range(n)) - compared_indices), count

# Main
text = input("Enter the text: ").lower()
pattern = input("Enter the word you want to search: ").lower()
print("---------------------------------")
position, never_compared, compare_count = BoyerMoore(text, pattern)   # Function call: Boyer-Moore
                                                                      
if (position == -1):        # If pattern not found
    print("\nNo match.")
else:                       # If pattern found
    print(f'\nPattern "{pattern}" found at index: {position}')

# Additional Information:
print('\nTotal number of comparison:', compare_count)
print(f'Total characters never compared: {len(never_compared)} at indices {never_compared}')
