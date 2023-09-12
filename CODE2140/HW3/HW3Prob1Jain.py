def pig_latin(phrase):
    words = phrase.split(" ")
    new_phrase = words[0][1:len(words[0])] + words[0][0].lower() + "ay"
    for i in range(1, len(words)):
        word = words[i]
        if word[-1] in ('a', 'e', 'i', 'o', 'u'):
            new_phrase += " " + word + "ay"
        else:
            new_phrase += " " + word[1:len(word)] + word[0] + "ay"
    return new_phrase

print(pig_latin("Hello this are billy"))