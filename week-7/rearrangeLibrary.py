from Stack import Stack

def rearrangeLibrary(string):
    if s[0] != '/' or s[-1] != '\\':
        return("Invalid input: The first character should be '/' and the last character should be '\\'.")
    characters=Stack()
    charactersReverse=Stack()
    for i in string:
        if i =="/":
            characters.push(i)
        if i.isalpha():
            characters.push(i)
        if i=="\\":
                temp=""
                while not characters.peek()=="/":
                   
                    temp+=characters.pop()
                characters.pop()
                for i in temp:
                    characters.push(i)
        # print(characters)
    while not characters.is_empty():
        charactersReverse.push(characters.pop())
    final_string=""
    while not charactersReverse.is_empty():
        final_string+=charactersReverse.pop()
    return final_string


s = "/ books / love \ i \\"
words = rearrangeLibrary(s)
print(words)

s2="/ /abc\ /de\ \\"
words2 = rearrangeLibrary(s2)
print(words2)