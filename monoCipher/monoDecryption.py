import standard
import string
import main

english = "English"
german = "German"


def mono_decryption():
    standard.sleep_message("Encryption of cipher text using Mono-Alphabetic Cipher\n")

    cipher_text = standard.get_input("Enter the cipher text you want to decrypt....", "(It can't be empty)", 0)
    print(f"Your text is: \n{cipher_text}\n")

    language = standard.inquirer_selector("Select the language...", [english, german])
    standard.sleep_message(f"Language Selected: {language}\n")

    key_limit = 0
    if language == english:
        key_limit = 52
    elif language == german:
        key_limit = 59

    key = input(f"\nEnter key. Minimum chars for {language} should be {key_limit}\n")
    print(f"\nKey Entered: {key}\n")

    standard.sleep_message("Decrypting text...\n")
    cipher_text = cipher_decryption(cipher_text, key, language)
    standard.sleep_message(f"{cipher_text}\n")
    standard.sleep_message(f"\nDecryption done successfully\n\n")

    main.inquire_ciphering_type()


def cipher_decryption(text, key, language):
    cipher_decrypted = ""
    temp_text = ""
    if language == english:
        temp_text = dict(zip(key, list(string.ascii_lowercase)))
    elif language == german:
        temp_text = dict(zip(key, list(string.ascii_lowercase + "ÄäÖöÜüß")))
    for char in text:
        if char.isalpha():
            if char in temp_text:
                cipher_decrypted += temp_text[char]
        else:
            cipher_decrypted += char
    return cipher_decrypted
