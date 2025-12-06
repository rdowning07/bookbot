def word_count(text):
    words = text.split()
    count = len(words)
    return count

def char_count(text):
    counts = {}

    for char in text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts