import random
import string

import main
import standard


english = "English"
german = "German"


def poly_encryption():
    standard.sleep_message("Encryption of text using Poly-Alphabetic Cipher\n")

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
    alphabets = string.ascii_lowercase
    key = ""
    if language == english:
        key = "".join(random.choice(alphabets) for _ in range(26))
    elif language == german:
        german_alphabets = alphabets + "äöüß"
        key = "".join(random.choice(german_alphabets) for _ in range(30))

    return key


def text_encryption(text, key, language):
    key = key.lower()
    plain_text = text.lower().replace("", "")
    cipher_text_list = []
    for i, char in enumerate(plain_text):
        if char.isalpha():
            key_char = key[i % len(key)]
            alphabets = ""
            total_alphabets = 0
            if language == english:
                alphabets = string.ascii_lowercase
                total_alphabets = 26
            elif language == german:
                alphabets = string.ascii_lowercase + "äöüß"
                total_alphabets = 30
            shift = alphabets.index(key_char)
            encrypted_char = alphabets[(alphabets.index(char) + shift) % total_alphabets]
            cipher_text_list.append(encrypted_char)
        else:
            cipher_text_list.append(char)

    cipher_text = "".join(cipher_text_list)
    return cipher_text

