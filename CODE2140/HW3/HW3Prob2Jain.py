def three_letter_combos(word):
    words_list = []
    for i in range(len(word)):
        for j in range(len(word)):
            for k in range(len(word)):
                words_list.append(word[i]+word[j]+word[k])
    return words_list

print(three_letter_combos('thing'))