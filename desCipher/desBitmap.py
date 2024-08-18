import base64
import desDecryption
import desEncryption
import main
import standardMethods
from PIL import Image


def des_bitmap():
    standardMethods.sleep_message("Encryption of bitmap using DES Algorithm\n\n")

    encryption_confirmation = standardMethods.inquirer_selector("Select yes to start encryption...", ["Yes", "No"])
    if encryption_confirmation == "Yes":

        standardMethods.sleep_message(f"\nLoading Image.....\n")
        image = Image.open("logo.png")
        image.show()

        standardMethods.sleep_message(f"\nReading image data...\n")
        with open("logo.png", "rb") as img:
            image_data = base64.b64encode(img.read())
        standardMethods.sleep_message(f"Image Data: {image_data}\n")

        image_date_encrypted = desEncryption.des_encryption(image_data)

        image_date_encrypted_binary = b"".join([bytes(chr(int(image_date_encrypted[x:x + 8], 2)), "utf-8")
                                                for x in range(0, len(image_date_encrypted), 8)])

        standardMethods.sleep_message(f"Showing encrypted image....\n")
        with open("logo_encrypted.png", "wb") as img_encrypted:
            img_encrypted.write(base64.b64encode(image_date_encrypted_binary))
        temp_image = Image.open("logo_encrypted.png")
        temp_image.show()

        decryption_confirmation = standardMethods.inquirer_selector("Select yes to start decryption...", ["Yes", "No"])
        if decryption_confirmation == "Yes":
            standardMethods.sleep_message(f"\nLoading Image.....\n")
            image = Image.open("logo_encrypted.png")
            image.show()

            standardMethods.sleep_message(f"\nReading encrypted image data...\n")
            with open("logo_encrypted.png", "rb") as img_encrypted:
                image__encrypted_data = base64.b64encode(img_encrypted.read())
            standardMethods.sleep_message(f"Encrypted Image Data: {image__encrypted_data}\n")

            image_date_decrypted = desDecryption.des_decryption(image_data)

            image_date_decrypted_binary = b"".join([bytes(chr(int(image_date_decrypted[x:x + 8], 2)), "utf-8") for x in
                                                    range(0, len(image_date_decrypted), 8)])

            standardMethods.sleep_message(f"Showing Decrypted image....\n")

            with open("logo_Decrypted.png", "wb") as img_decrypted:
                img_decrypted.write(base64.b64encode(image_date_decrypted_binary))

    main.inquire_ciphering_type()

    return
