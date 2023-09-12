def is_palindrome(word):
    copy1 = word.upper()
    for i in range(len(copy1)-1, -1, -1):
        if ord(copy1[i]) < 65 or ord(copy1[i]) > 90 and len(copy1) >= 0:
            copy1 = copy1.replace(copy1[i], "", 1)
    copy2 = ""
    for i in range(len(copy1)-1, -1, -1):
        copy2 += copy1[i]
    return copy1 == copy2
    
print(is_palindrome("taCO      Cat"))
