import main
import standard
import random
import string

english = "English"
german = "German"


def mono_encryption():
    standard.sleep_message("Encryption of text using Mono-Alphabetic Cipher\n")

    plain_text = standard.get_input("Enter the text you want to encrypt....", "(It can't be empty)", 0)
    print(f"Your text is: \n{plain_text}\n")

    language = standard.inquirer_selector("Select the language...", [english, german])
    standard.sleep_message(f"Language Selected: {language}\n")

    standard.sleep_message(f"\nGenerating random {language} key..\n")
    key = generate_random_key(language)
    standard.sleep_message(f"\nKey: {key}\n")

    standard.sleep_message(f"\nEncrypting entered {language} text with key generated...\n")
    text_encrypted = text_encryption(plain_text, key, language)
    standard.sleep_message(f"\n{text_encrypted}\n")
    standard.sleep_message(f"\n\nEncryption done successfully\n\n")

    main.inquire_ciphering_type()


def generate_random_key(language):
    alphabets = ""
    if language == english:
        alphabets = list(string.ascii_lowercase)
    elif language == german:
        alphabets = list(string.ascii_lowercase + "ÄäÖöÜüß")
    random.shuffle(alphabets)
    key = "".join(alphabets)
    return key


def text_encryption(text, key, language):
    text_encrypted = ""
    temp_key = ""
    if language == english:
        temp_key = dict(zip(list(string.ascii_lowercase), key))
    elif language == german:
        temp_key = dict(zip(list(string.ascii_lowercase + "ÄäÖöÜüß"), key))
    for char in text:
        if char.isalpha():
            if char in temp_key:
                text_encrypted += temp_key[char]
        else:
            text_encrypted += char
    return text_encrypted
