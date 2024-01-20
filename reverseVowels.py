def reverseVowels(s):
    # print(s)
    temp = []

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    for i in s:
        if i in vowels:
            temp.append(i)
            
    temp.reverse()

    new_string = ""
    index = 0

    for i in s:
        if i in vowels:
            new_string+=temp[index]
            index+=1
        else:
            new_string+=i

    return new_string


    


reverseVowels("SATEOPD")
