# number_to_ordinal_word.py

ones = {
    0: "",
    1: "one",     2: "two",      3: "three",
    4: "four",    5: "five",     6: "six",
    7: "seven",   8: "eight",    9: "nine",
    10: "ten",    11: "eleven",  12: "twelve",
    13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen"
}

tens = {
    20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty",  60: "sixty",  70: "seventy",
    80: "eighty", 90: "ninety"
}

# Special ordinal endings
ordinal_exceptions = {
    "one": "first",
    "two": "second",
    "three": "third",
    "five": "fifth",
    "eight": "eighth",
    "nine": "ninth",
    "twelve": "twelfth"
}

def make_ordinal(word):
    if word in ordinal_exceptions:
        return ordinal_exceptions[word]
    if word.endswith("y"):
        return word[:-1] + "ieth"
    return word + "th"

def number_to_words(n):
    if n < 20:
        return ones[n]
    if n < 100:
        if n in tens:
            return tens[n]
        return tens[n // 10 * 100 // 10] + "-" + ones[n % 10]
    if n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + " hundred"
        return ones[n // 100] + " hundred " + number_to_words(n % 100)
    if n < 1000000:
        if n % 1000 == 0:
            return number_to_words(n // 1000) + " thousand"
        return number_to_words(n // 1000) + " thousand " + number_to_words(n % 1000)

    return "number too big lol"

def number_to_ordinal_word(n):
    words = number_to_words(n).split()
    last = words[-1]

    # Convert last word to ordinal
    ordinal_last = make_ordinal(last)

    # Replace last word
    words[-1] = ordinal_last

    return " ".join(words)

