with open("input.txt", "r") as f:
    text = f.read()
print(text.count('. ') + text.count('! ') + text.count('? ')+text.count('.\n') + text.count('!\n') + text.count('?\n'))