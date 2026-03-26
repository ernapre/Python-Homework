try:
    file = open("C:/Users/preka/Homework/Python-Homework/hello.txt", "r")
    lines = file.readlines()

    if len(lines) == 0:
        print("Empty file!")
    else:
        total_words = 0

        for i in lines:
            words = i.split()
            total_words += len(words)

        shortest_line = min(lines, key=len)

        print("Total number of words: ", total_words)
        print("Shortest line:", shortest_line)
    file.close()


except FileNotFoundError:
    print("Error: File not found")
