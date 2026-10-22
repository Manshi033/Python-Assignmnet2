# Accept a sentence from the user
s = input("Enter a sentence: ")

# Remove spaces
print("Left strip:", s.lstrip())
print("Right strip:", s.rstrip())
print("Strip:", s.strip())

# a) Search for a substring
sub = input("Enter substring to search: ")
print("Using find():", s.find(sub))

try:
    print("Using index():", s.index(sub))
except ValueError:
    print("Substring not found")

# b) Count a word
word = input("Enter word to count: ")
print("Count:", s.count(word))

# c) Replace a word
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("Replace:", s.replace(old, new))

# d) Split and join
words = s.split()
print("Split:", words)
print("Join:", " ".join(words))

# e) String immutability
try:
    s[0] = 'A'
except TypeError:
    print("Strings are immutable")

# f) Sort words alphabetically
print("Sorted words:", sorted(words))