conversions = {"length" : {"centimeters":0.3937, "meters": 39.3701, "inches": 1, "feet": 12}, "volume" : {"liters": 1.05669, "quarts": 1}, "mass" : {"grams": 0.00220462, "pounds": 1, "kilograms": 2.20462}}

def solve_prob(problem):
    words = problem.split(" ")
    metric_unit = words[-1]
    metric_unit = metric_unit[0:len(metric_unit)-1]
    english_unit = words[2]
    metric_value = float(words[-2])
    category = ""
    can_convert = False
    for key in conversions.keys():
        if (english_unit in conversions[key]) and (metric_unit in conversions[key]):
            can_convert = True
            category = key
    if can_convert:
        factor = conversions[category][metric_unit] / conversions[category][english_unit]
        english_value = metric_value * factor
        print(english_value)
    else:
        print("Invalid question")

word_problem = input("Enter your desired conversion from metric-to-english units: ")
solve_prob(word_problem)