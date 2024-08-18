import string

import main
import standard


english = "English"
german = "German"


def poly_decryption():
    standard.sleep_message("Encryption of cipher text using Poly-Alphabetic Cipher\n")

    cipher_text = standard.get_input("Enter the cipher text you want to decrypt....", "(It can't be empty)", 0)
    print(f"Your text is: \n{cipher_text}\n")

    language = standard.inquirer_selector("Select the language...", [english, german])
    standard.sleep_message(f"Language Selected: {language}\n")

    key_limit = 0
    if language == english:
        key_limit = 26
    elif language == german:
        key_limit = 30

    key = input(f"\nEnter key. Minimum chars for {language} should be {key_limit}\n")
    print(f"\nKey Entered: {key}\n")

    standard.sleep_message("Decrypting text...\n")
    cipher_text = cipher_decryption(cipher_text, key, language)
    standard.sleep_message(f"{cipher_text}\n")
    standard.sleep_message(f"\nDecryption done successfully\n\n")

    main.inquire_ciphering_type()


def cipher_decryption(cipher_text, key, language):
    cipher_text = cipher_text.lower()
    plain_text_list = []
    for i, char in enumerate(cipher_text):
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
            decrypted_char = alphabets[(alphabets.index(char) - shift % total_alphabets)]
            plain_text_list.append(decrypted_char)
        else:
            plain_text_list.append(char)
    plain_text = "".join(plain_text_list)

    return plain_text
