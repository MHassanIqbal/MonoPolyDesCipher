import string

import main
import polyDecryption
import standard
from collections import Counter

english = "English"
german = "German"


def poly_hacking():
    standard.sleep_message("\n\nHacking of Cipher text using Mono-Alphabetic Cipher\n")

    cipher_text = standard.get_input("Enter the cipher text you want to decrypt....", "(It can't be empty)", 0)
    print(f"Your text is: \n{cipher_text}\n")

    language = standard.inquirer_selector("Select the language...", [english, german])
    standard.sleep_message(f"Language Selected: {language}\n")

    standard.sleep_message(f"Attempting to hack the cipher text....\n")

    standard.sleep_message(f"Formatting cipher text...\n")
    cipher_text = cipher_text.lower().replace("", "")
    standard.sleep_message(f"Cipher Text: {cipher_text}\n")

    standard.sleep_message(f"Checking length and alphabets in {language}\n")
    alphabets = ""
    if language == english:
        alphabets = string.ascii_lowercase
    elif language == german:
        alphabets = string.ascii_lowercase + "äöüß"
    standard.sleep_message(f"Alphabets: {alphabets} | {len(alphabets)}\n")

    standard.sleep_message(f"\nGetting Substrings.\n")
    substring = get_substrings(cipher_text, alphabets)
    standard.sleep_message(f"\nSubstrings: {substring}\n")

    standard.sleep_message(f"\nPerforming frequency analysis...\n")
    frequency = frequency_analysis(substring)
    standard.sleep_message(f"\nFrequency: {frequency}\n")

    standard.sleep_message(f"\nChecking possible keys...\n")
    possible_keys_all = check_possible_key(substring, frequency, alphabets)
    standard.sleep_message(f"\nAll Possible Keys are...\n")

    standard.sleep_message(f"\n\nTrying possible keys to decrypt the text...\n")
    for key in possible_keys_all:
        standard.sleep_message(f"\nPossible Key: {key}\n")
        plain_text = polyDecryption.cipher_decryption(cipher_text, key, language)
        standard.sleep_message(f"Possible Text: {plain_text}\n")

    main.inquire_ciphering_type()


def get_substrings(cipher_text, alphabets):
    substrings = ["" for _ in range(len(alphabets))]
    for i, char in enumerate(cipher_text):
        substrings[i % len(alphabets)] += char
    return substrings


def frequency_analysis(substrings):
    counter = Counter(substrings)
    total_characters = len(substrings)
    frequency = {char: count / total_characters for char, count in counter.items()}
    return frequency


def check_possible_key(substring, frequency, alphabets):
    possible_key_list = [[] for _ in range(len(alphabets))]

    for i, substring in enumerate(substring):
        guessed_key = guess_key_substring(frequency, alphabets)
        possible_key_list[i] = guessed_key

    standard.sleep_message(f"Combining all possible guess keys\n")
    possible_keys_all = ["".join(key_combination) for key_combination in cartesian_list(possible_key_list)]

    return possible_keys_all


def guess_key_substring(frequency, alphabets):
    standard.sleep_message(f"Sorting frequency...\n")
    frequency_sorted_characters = sorted(frequency, key=frequency.get, reverse=True)

    standard.sleep_message(f"Guessing key with frequencies...\n")
    guessed_key = []
    for char in frequency_sorted_characters:
        shift = (alphabets.index(char) - alphabets.index('e')) % len(alphabets)
        temp_key = guessed_key.append(alphabets[shift])
        standard.sleep_message(f"Key: {temp_key}\n")

    return guessed_key


def cartesian_list(possible_key_list):
    if not possible_key_list:
        return [[]]
    possible_key_list_updated = [[item] + rest for item in possible_key_list[0]
                                 for rest in cartesian_list(possible_key_list[1:])]
    return possible_key_list_updated
