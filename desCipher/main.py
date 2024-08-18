import standardMethods
import desEncryption
import desDecryption
import desBitmap

encryption = "Encryption"
decryption = "Decryption"
bitmap = "Bitmap"
exit_program = "Exit"


def inquire_ciphering_type():
    ciphering_type = standardMethods.inquirer_selector("Welcome to DES Ciphering.Select the option.",
                                                       [encryption, decryption, bitmap, exit_program])
    if ciphering_type == encryption:
        desEncryption.des_encryption_init()
    elif ciphering_type == decryption:
        desDecryption.des_decryption_init()
    elif ciphering_type == bitmap:
        desBitmap.des_bitmap()
    elif ciphering_type == exit_program:
        standardMethods.sleep_message("Exiting program.... Thank you.")
        exit()


if __name__ == '__main__':
    inquire_ciphering_type()
