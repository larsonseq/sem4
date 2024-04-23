def prefix_function(pattern):
    m = len(pattern)
    prefix = [0] * m
    prefix[0] = 0
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        prefix[q] = k
    return prefix

def kmp_match(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix = prefix_function(pattern)
    valid_shifts = []
    matches = []
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = prefix[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = prefix[q - 1]
            valid_shifts.append(i - m + 1)
    return matches, valid_shifts, prefix

# Ask user for input
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

# Perform Knuth-Morris-Pratt string matching
indices, valid_shifts, prefix_array = kmp_match(text, pattern)
if indices:
    print(f"Pattern found at indices: {indices}")
    print(f"Valid shifts: {valid_shifts}")
    print(f"Prefix array: {prefix_array}")
else:
    print("Pattern not found.")
