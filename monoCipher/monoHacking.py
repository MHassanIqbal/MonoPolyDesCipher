import standard

common = "Common Letter Frequency Analysis"
bigrams = "Bigrams Frequency Analysis"
trigram = "Trigram Frequency Analysis"


def mono_hacking():
    standard.sleep_message("\n\nHacking of Cipher text using Mono-Alphabetic Cipher\n")
    init_cipher_text()


def init_cipher_text():
    cipher_text = standard.get_input("Enter the cipher text you want to decrypt....", "(It can't be empty)", 0)
    print(f"Your text is: \n{cipher_text}\n")

    selection_analysis_type(cipher_text)


def selection_analysis_type(cipher_text):
    analysis_type = standard.inquirer_selector("Select the analysis you want to perform to decipher the text",
                                               [common, bigrams, trigram, "Enter Cipher Text"])
    if analysis_type == common:
        common_letter_frequency_analysis(cipher_text)
    elif analysis_type == bigrams:
        bigrams_analysis(cipher_text)
    elif analysis_type == trigram:
        trigrams_analysis(cipher_text)
    elif analysis_type == "Enter Cipher Text":
        init_cipher_text()


def common_letter_frequency_analysis(cipher_text):
    standard.sleep_message("Attempting Hacking though Common letter frequency analysis...\n\n")

    temp_frequency = {}
    standard.sleep_message("Checking number of times a character is repeated in the cipher text...\n")
    for char in cipher_text.lower():
        if char.isalpha():
            if char in temp_frequency:
                temp_frequency[char] += 1
            else:
                temp_frequency[char] = 1
    standard.sleep_message(f"{temp_frequency}\n\n")

    standard.sleep_message("Calculation percentage of the characters...\n")
    for key, value in temp_frequency.items():
        percentage = round(value * 100.0 / len(cipher_text), 1)
        temp_frequency.update({key: percentage})
    standard.sleep_message(f"{temp_frequency}\n\n")

    standard.sleep_message("Getting common letter frequency from the database...\n")
    standard.sleep_message(f"{standard.common_letter_frequency}\n\n")

    standard.sleep_message("\nAnalysing common letter frequency table and comparing them with cipher characters to "
                           "extract potiential text...\n\n")

    text_potential = ""
    for char in cipher_text:
        if char.isalpha():
            if char in temp_frequency.keys():
                temp_value = min(standard.common_letter_frequency.values(),
                                 key=lambda x: abs(x - temp_frequency.get(char)))
                temp_key = list(standard.common_letter_frequency)[
                    list(standard.common_letter_frequency.values()).index(temp_value)]
                text_potential += "".join(temp_key)
        else:
            text_potential += char

    standard.sleep_message(f"Possible Text is: \n{text_potential}\n\n")

    return text_potential


def bigrams_analysis(cipher_text):
    standard.sleep_message("Attempting Hacking though Bigrams frequency analysis...\n\n")

    cipher_text = cipher_text.lower()

    standard.sleep_message("Converting cipher text in pairs... \n\n")
    cipher_bigrams = [cipher_text[char:char + 2] for char in range(len(cipher_text) - 1) if cipher_text[char:char + 2].isalpha()]
    standard.sleep_message(f"Cipher Bigrams: \n {cipher_bigrams}\n")

    bigrams_characters = []
    standard.sleep_message("\nGetting most common bigrams characters from the database... \n")
    for key in standard.bigrams_letter_frequency.keys():
        bigrams_characters.append(key)
    standard.sleep_message(f"{bigrams_characters}\n\n")

    temp_frequency = {}
    standard.sleep_message("Checking number of times a bigrams character is repeated in the cipher text...\n")
    for char in cipher_bigrams:
        if char.isalpha():
            if char in temp_frequency:
                temp_frequency[char] += 1
            else:
                temp_frequency[char] = 1
    standard.sleep_message(f"{temp_frequency}\n\n")

    standard.sleep_message("Calculation percentage of the bigrams characters...\n")
    for key, value in temp_frequency.items():
        percentage = round(value * 100.0 / len(cipher_bigrams), 1)
        temp_frequency.update({key: percentage})
    standard.sleep_message(f"{temp_frequency}\n\n")

    standard.sleep_message("Getting bigrams letter frequency from the database...\n")
    standard.sleep_message(f"{standard.bigrams_letter_frequency}\n\n")

    standard.sleep_message("\nAnalysing bigrams table and comparing them with cipher bigrams to extract potiential text...\n\n")

    text_potential = ""
    for char in cipher_bigrams:
        if char.isalpha():
            if char in temp_frequency.keys():
                temp_value = min(standard.bigrams_letter_frequency.values(),
                                 key=lambda x: abs(x - temp_frequency.get(char)))
                temp_key = list(standard.bigrams_letter_frequency)[
                    list(standard.bigrams_letter_frequency.values()).index(temp_value)]
                text_potential += "".join(temp_key)
        else:
            text_potential += char

    standard.sleep_message(f"Possible Text is: \n{text_potential}\n\n")

    return text_potential


def trigrams_analysis(cipher_text):
    standard.sleep_message("Attempting Hacking though Trigram frequency analysis...\n\n")

    cipher_text = cipher_text.lower()

    standard.sleep_message("Converting cipher text in group of 3 characters... \n\n")
    cipher_trigrams = [cipher_text[char:char + 3] for char in range(len(cipher_text) - 1) if cipher_text[char:char + 2].isalpha()]
    standard.sleep_message(f"Cipher Trigram: \n {cipher_trigrams}\n")

    trigrams_characters = []
    standard.sleep_message("\nGetting most common trigrams characters from the database... \n")
    for key in standard.bigrams_letter_frequency.keys():
        trigrams_characters.append(key)
    standard.sleep_message(f"{trigrams_characters}\n\n")

    temp_frequency = {}
    standard.sleep_message("Checking number of times a trigrams character is repeated in the cipher text...\n")
    for char in cipher_trigrams:
        if char.isalpha():
            if char in temp_frequency:
                temp_frequency[char] += 1
            else:
                temp_frequency[char] = 1
    standard.sleep_message(f"{temp_frequency}\n\n")

    standard.sleep_message("Calculation percentage of the trigrams characters...\n")
    for key, value in temp_frequency.items():
        percentage = round(value * 100.0 / len(cipher_trigrams), 1)
        temp_frequency.update({key: percentage})
    standard.sleep_message(f"{temp_frequency}\n\n")

    standard.sleep_message("Getting Trigrams letter frequency from the database...\n")
    standard.sleep_message(f"{standard.trigram_letter_frequency}\n\n")

    standard.sleep_message("\nAnalysing Trigrams table and comparing them with cipher bigrams to extract potiential text...\n\n")

    text_potential = ""
    for char in cipher_trigrams:
        if char.isalpha():
            if char in temp_frequency.keys():
                temp_value = min(standard.bigrams_letter_frequency.values(),
                                 key=lambda x: abs(x - temp_frequency.get(char)))
                temp_key = list(standard.bigrams_letter_frequency)[
                    list(standard.bigrams_letter_frequency.values()).index(temp_value)]
                text_potential += "".join(temp_key)
        else:
            text_potential += char

    standard.sleep_message(f"Possible Text is: \n{text_potential}\n\n")

    return text_potential
