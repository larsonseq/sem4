class RabinKarp:
    def __init__(self, text, pattern, radix, prime):
        self.text = text
        self.pattern = pattern
        self.radix = radix
        self.prime = prime
        self.text_len = len(text)
        self.pattern_len = len(pattern)
        self.radix_power = pow(radix, self.pattern_len - 1, prime)   # (radix**(pattern_length-1))%prime
        self.pattern_hash = self.calculate_hash(pattern)
        self.matches = []

    def calculate_hash(self, s):
        hash_value = 0
        for char in s:
            hash_value = (hash_value * self.radix + ord(char)) % self.prime
        return hash_value

    def check_equal(self, i):
        return self.pattern == self.text[i:i+self.pattern_len]

    def search(self):
        valid_shifts = []
        text_hash = self.calculate_hash(self.text[:self.pattern_len])
        if text_hash == self.pattern_hash and self.check_equal(0):
            self.matches.append(0)
        
        for i in range(1, self.text_len - self.pattern_len + 1):
            text_hash = (text_hash - ord(self.text[i - 1]) * self.radix_power) % self.prime
            text_hash = (text_hash * self.radix + ord(self.text[i + self.pattern_len - 1])) % self.prime
            if text_hash == self.pattern_hash and self.check_equal(i):
                self.matches.append(i)
                valid_shifts.append(i)
        
        return self.matches, valid_shifts

# Ask user for input
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")
radix = 256  # ASCII radix
prime = 101  # A prime number

# Perform Rabin-Karp string matching
rk = RabinKarp(text, pattern, radix, prime)
indices, valid_shifts = rk.search()
if indices:
    # print(f"Pattern found at indices: {indices}")
    print(f"Valid shifts: {valid_shifts}")
else:
    print("Pattern not found.")
