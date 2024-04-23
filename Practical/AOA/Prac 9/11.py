class Rabin():
    def __init__(self, text, pattern, radix, prime):
        self.text = text
        self.patt = pattern
        self.radix = radix
        self.prime = prime
        self.tl = len(text) 
        self.pl = len(pattern)
        self.phash = self.calculatehash(pattern)
        self.radixpow = pow(radix, self.pl - 1, self.prime)
        print(f"Radixpow is {self.radixpow}")
    
    def calculatehash(self, str1):
        shash = 0
        for s in str1:
            shash = (shash * self.radix + ord(s)) % self.prime
            print(shash, end=" ")
        print('')
        return shash
    
    def checkequal(self, i):
        return self.patt == self.text[i : i + self.pl]

    def search(self):
        valid = []
        texthash = self.calculatehash(self.text[0 : self.pl])
        if texthash == self.phash and self.checkequal(0):
            valid.append(0)
        for i in range(1, self.tl - self.pl + 1):
            texthash = (texthash - ord(self.text[i-1])*self.radixpow) % self.prime
            texthash = (texthash * self.radix +ord(self.text[i + self.pl - 1])) % self.prime
            if texthash == self.phash and self.checkequal(i):
                valid.append(i)
        return valid

# Ask user for input
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")
radix = 256  # ASCII radix
prime = 101  # A prime number

# Perform Rabin-Karp string matching
rk = Rabin(text, pattern, radix, prime)
indices = rk.search()
if indices:
    # print(f"Pattern found at indices: {indices}")
    print(f"Valid shifts: {indices}")
else:
    print("Pattern not found.")
