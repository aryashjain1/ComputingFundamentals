def summarize_letters(word):
    word = word.upper()
    freqs = [0] * 26
    letters_dict = {}
    letters_list = []
    for i in range(len(word)-1, -1, -1):
        if ord(word[i]) < 65 or ord(word[i]) > 90 and len(word) >= 0:
            word = word.replace(word[i], "", 1)
    for j in range(len(word)):
        freqs[ord(word[j]) - 65] += 1
        if word[j] in letters_dict:
            letters_dict[word[j]] += 1
        else:
            letters_dict[word[j]] = 1
    for k in range(len(freqs)):
        if freqs[k] != 0:
            letters_list.append((chr(k + 65), freqs[k]))
    if len(letters_dict) == 26:
        print("You have all the alphabet!")
    return (letters_dict, letters_list)

word_in = 'aaqwertyuioplkjhgfdsazxcvbnmq12345.,.'
word_dict, word_tuple = summarize_letters(word_in)
print(word_dict)
print(word_tuple)