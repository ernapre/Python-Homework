text = "Python is simple and powerful because python is widely used"
text = text.lower()
words = text.split()

words_count = {}

for i in words:
    if i in words_count:
        words_count[i] += 1
    else:
        words_count[i] = 1

for i in words:
    print(i, ":", words_count[i])
