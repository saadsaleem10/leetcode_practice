def reverseWords(s):
    stack = []
    
    words = s.split()
    print(words)

    stack = []

    for word in words:
        stack.append(word)

    print(stack)


    newString = ""

    while stack:
        newString +=stack.pop()+" "

    print(newString)

    newString = newString.rstrip()

    return newString


reverseWords(s = "hello world saad saleem")