import string

import standard
import polyDecryption
import polyEncryption
import polyHacking


encryption = "Encryption"
decryption = "Decryption"
hacking = "Hacking"
exit_program = "Exit"


def inquire_ciphering_type():
    ciphering_type = standard.inquirer_selector("Welcome to Poly-Alphabetic Ciphering.Select the option.", [encryption, decryption, hacking, exit_program])
    if ciphering_type == encryption:
        polyEncryption.poly_encryption()
    elif ciphering_type == decryption:
        polyDecryption.poly_decryption()
    elif ciphering_type == hacking:
        polyHacking.poly_hacking()
    elif ciphering_type == exit_program:
        standard.sleep_message("Exiting program.... Thank you.")
        exit()


if __name__ == '__main__':
    inquire_ciphering_type()
