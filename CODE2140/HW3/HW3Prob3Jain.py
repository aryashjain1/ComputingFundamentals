def math_word(problem):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    words = problem.lower().split(" ")
    if words[1] == "plus":
        return nums.index(words[0]) + nums.index(words[-1])
    if words[1] == "minus":
        return nums.index(words[0]) - nums.index(words[-1])
    if words[1] == "times":
        return nums.index(words[0]) * nums.index(words[-1])
    if words[1] == "divided" and words[-2] == "by":
        return nums.index(words[0]) / nums.index(words[-1])
    if words[1] == "raised" and words[-2] == "to":
        return nums.index(words[0]) ** nums.index(words[-1])
    return "invalid problem. Try again"

print(math_word("one plus two"))
print(math_word("five raised to three"))
print(math_word("three to the fifth"))