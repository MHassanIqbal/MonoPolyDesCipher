from time import sleep
import inquirer


def sleep_message(message):
    for char in message:
        sleep(0.005)
        print(char, end='', flush=True)
    return


def inquirer_selector(message, choices):
    options_selection = [
        inquirer.List('code', message, choices),
    ]
    selection = inquirer.prompt(options_selection)
    return selection['code']


def get_input(message, warning, limit):
    temp_text = []
    while len(temp_text) == limit:
        print("\n" + message + warning + "\n")
        for line in iter(input, ''):
            temp_text.append(line)
    text = "\n".join(temp_text)
    return text


common_letter_frequency = {
    "a": 7.9, "b": 1.4, "c": 2.7, "d": 4.1, "e": 12.2, "f": 2.1, "g": 1.9, "h": 5.9, "i": 6.8, "j": 0.2, "k": 0.8,
    "l": 3.9, "m": 2.3, "n": 6.5, "o": 7.2, "p": 1.8, "q": 0.1, "r": 5.8, "s": 6.1, "t": 8.8, "u": 2.7, "v": 1.0,
    "w": 2.3, "x": 0.2, "y": 1.9, "z": 1.0
}


bigrams_letter_frequency = {
    "th": 2.72, "he": 2.33, "in": 2.03, "er": 1.78, "an": 1.61, "re": 1.41, "es": 1.32, "on": 1.32, "st": 1.25,
    "nt": 1.17, "en": 1.13, "at": 1.12, "ed": 1.08, "nd": 1.07, "to": 1.07, "or": 1.06, "ea": 1.00, "tt": 0.99,
    "ar": 0.98, "te": 0.98, "ng": 0.89, "al": 0.88, "it": 0.88, "as": 0.87, "is": 0.86, "ha": 0.83, "et": 0.76,
    "se": 0.73, "ou": 0.72, "of": 0.71
}


trigram_letter_frequency = {
    "the": 1.81, "and": 0.73, "ing": 0.72, "ent": 0.42, "ion": 0.42, "her": 0.36, "for": 0.34, "tha": 0.33,
    "nth": 0.33, "int": 0.32, "ere": 0.31, "tio": 0.31, "ter": 0.30, "est": 0.28, "ers": 0.28, "ati": 0.26,
    "hat": 0.26, "ate": 0.25, "all": 0.25, "eth": 0.24, "hes": 0.24, "ver": 0.24, "his": 0.24, "oft": 0.22,
    "ith": 0.21, "fth": 0.21, "sth": 0.21, "oth": 0.21, "res": 0.21, "ont": 0.20
}
