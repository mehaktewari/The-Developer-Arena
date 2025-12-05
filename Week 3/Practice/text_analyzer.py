def text_analyzer(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    
    return num_words, num_chars

# Test
text = "Python is amazing!"
words, chars = text_analyzer(text)

print("Words:", words)
print("Characters:", chars)
