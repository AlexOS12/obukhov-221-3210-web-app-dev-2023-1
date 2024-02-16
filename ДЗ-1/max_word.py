with open("example.txt", encoding="utf-8") as file:
    text = file.read().lower()

# Удаление символов пунктуации
for p in "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~":
    text = text.replace(p, '')

# Слово : сколько раз встретилось в тексте
words = {}
mxLen = 0 

for word in text.split():
    if len(word) > mxLen:
        mxLen = len(word)
        words = {word : 1}
    elif len(word) == mxLen:
        if word in words:
            words[word] += 1
        else:
            words.update({word : 1})

for word in sorted(words, key=lambda x: words[x]):
    print(word)
