import re
import desSubKeys
import standardMethods
from random import choice
from string import ascii_lowercase
import main


def des_encryption_init():
    standardMethods.sleep_message("Encryption of text using DES Algorithm\n")

    plain_text = standardMethods.get_input("\nEnter the text you want to encrypt....", "(It can't be empty)", 0)
    standardMethods.sleep_message(f"Your entered text is: \n{plain_text}\n")

    des_encryption(plain_text)

    main.inquire_ciphering_type()


def des_encryption(text):
    standardMethods.sleep_message(f"Converting text into binary\n")
    plain_text_binary = list(map(int, "".join(format(ord(char), '08b') for char in text)))
    standardMethods.sleep_message(f"Text: {plain_text_binary}\n")

    standardMethods.sleep_message(
        f"\nChecking the binary length of the entered text and converting them in format of 64\n")
    standardMethods.sleep_message(f"Length of the binary text = {len(plain_text_binary)}\n")

    plain_text_binary_checked = standardMethods.check_and_adjust_text_size(plain_text_binary)
    standardMethods.sleep_message(f"New Text: {plain_text_binary_checked}\n")
    standardMethods.sleep_message(f"Now the Length of the Text: {len(plain_text_binary_checked)}\n")

    standardMethods.sleep_message(f"\nConverting text in modulus of 64\n")
    plain_text_binary_list = list(standardMethods.divide_list(plain_text_binary_checked, 64))
    standardMethods.sleep_message(f"{plain_text_binary_list}\n")

    standardMethods.sleep_message(f"\nGenerating Random key..\n")
    key_string = "".join(choice(ascii_lowercase) for char in range(8))
    standardMethods.sleep_message(f"\nKey generated is: {key_string}\n\n")

    standardMethods.sleep_message(f"\n Converting Key into bits\n")
    key = list(map(int, "".join(format(ord(char), '08b') for char in key_string)))
    standardMethods.sleep_message(f"{key}\n")
    temp_text = "".join(map(str, key))
    standardMethods.sleep_message(f"{temp_text}\n")

    encryption_confirmation = standardMethods.inquirer_selector("Continue to encrypt", ["Yes", "No"])
    if encryption_confirmation == "Yes":
        standardMethods.sleep_message(f"\n Creating sub keys for encryption\n")
        keys_list = desSubKeys.des_sub_keys(key)
        standardMethods.sleep_message(f"\n\n Keys Created Successfully\n\n")

        text_list = []
        for value in plain_text_binary_list:
            cipher_text = standardMethods.text_encryption_decryption(value, keys_list, "Plain Text", "Encryption")
            text_list.append(cipher_text)

        cipher_text = "".join(re.escape(char) for char in text_list)
        standardMethods.sleep_message(f"\n\n{cipher_text}\n\n")

    return cipher_text
