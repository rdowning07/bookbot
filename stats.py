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

def sort_on(item):
  return item["num"]

def sort_on(item):
    return item["num"]

def sort_chars(char_counts):
    char_list = []
    
    for char, num in char_counts.items():
        if not char.isalpha():
            continue
        char_list.append({"char": char, "num": num})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

