with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

words = len(file_contents.lower().split())

def word_count(string):
    return len(string.lower().split())

def char_map(string):
    chars = {}
    for char in string.lower():
        if char not in "abcdefghijklmnopqrstuvwxyz":
            continue
        if char in chars:
            chars[char] += 1
            continue
        chars[char] = 1
    return chars

chars = char_map(file_contents)
print("--- Begin report of books.frankenstein.txt ---")
print(f"{word_count(file_contents)} words found in the document")
for char, count in chars.items():
    print(f"The {char} character was found {count} times")
print("--- End report ---")
