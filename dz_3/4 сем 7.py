import string

file_path = '/usr/share/licenses/python/LICENSE'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

for char in string.punctuation:
    text = text.replace(char, ' ')

text = text.lower()
words = text.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

print("10 самых часто употребляемых слов:")

for i in range(10):
    max_word = max(word_counts, key=word_counts.get)
    max_value = word_counts[max_word]
    print(i + 1, max_word, "-", max_value, "раз(а)")

    word_counts.pop(max_word)