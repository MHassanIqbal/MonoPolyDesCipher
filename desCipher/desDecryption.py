import desSubKeys
import main
import standardMethods
import re


def des_decryption_init():
    standardMethods.sleep_message("Decrypting of cipher text using DES Algorithm\n")

    cipher_text = standardMethods.get_input("\nEnter the cipher text you want to decrypt....", "(It can't be empty)", 0)
    standardMethods.sleep_message(f"Your entered text is: \n{cipher_text}\n")

    des_decryption(cipher_text)

    main.inquire_ciphering_type()


def des_decryption(text):
    standardMethods.sleep_message(f"Converting cipher text into binary\n")
    cipher_text_binary = list(map(int, "".join(format(ord(char), '08b') for char in text)))
    standardMethods.sleep_message(f"Cipher Text: {cipher_text_binary}\n")
    temp_text = "".join(map(str, cipher_text_binary))
    standardMethods.sleep_message(f"{temp_text}\n")

    cipher_text_binary_text_binary_checked = standardMethods.check_and_adjust_text_size(cipher_text_binary)

    standardMethods.sleep_message(f"New Cipher Text: {cipher_text_binary_text_binary_checked}\n")
    standardMethods.sleep_message(f"Now the Length of the Text: {len(cipher_text_binary_text_binary_checked)}\n")

    standardMethods.sleep_message(f"\nConverting text in modulus of 64\n")
    cipher_text_binary_list = list(standardMethods.divide_list(cipher_text_binary_text_binary_checked, 64))
    standardMethods.sleep_message(f"{cipher_text_binary_list}\n")

    key = get_and_check_key()
    key_binary = list(map(int, "".join(format(ord(char), '08b') for char in key)))
    standardMethods.sleep_message(f"{key_binary}\n")
    temp_text = "".join(map(str, key_binary))
    standardMethods.sleep_message(f"{temp_text}\n")

    decryption_confirmation = standardMethods.inquirer_selector("Continue to decrypt", ["Yes", "No"])
    if decryption_confirmation == "Yes":
        standardMethods.sleep_message(f"\nGenerating Sub keys..\n")
        keys_list = desSubKeys.des_sub_keys(key_binary)
        standardMethods.sleep_message(f"\n\n Sub Keys Created Successfully\n\n")
        standardMethods.sleep_message(f"\nReversing keys generated...\n")
        key_list_reversed = list(reversed(keys_list))

        text_list = []
        for value in cipher_text_binary_list:
            plain_text = standardMethods.text_encryption_decryption(value, key_list_reversed, "Cipher Text", "Decryption")
            text_list.append(plain_text)

        plain_text = "".join(re.escape(char) for char in text_list)
        standardMethods.sleep_message(f"\n\n{plain_text}\n\n")

    return


def get_and_check_key():

    text = standardMethods.get_input("Enter the key of exact 8 characters....", "(It can't be empty)", 0)
    if len(text) == 8 and text.isalpha():
        return text
    else:
        get_and_check_key()
    return text
