import standard
import monoDecryption
import monoEncryption
import monoHacking


encryption = "Encryption"
decryption = "Decryption"
hacking = "Hacking"
exit_program = "Exit"


def inquire_ciphering_type():
    ciphering_type = standard.inquirer_selector("Welcome to Mono-Alphabetic Ciphering.Select the option.", [encryption, decryption, hacking, exit_program])
    if ciphering_type == encryption:
        monoEncryption.mono_encryption()
    elif ciphering_type == decryption:
        monoDecryption.mono_decryption()
    elif ciphering_type == hacking:
        monoHacking.mono_hacking()
    elif ciphering_type == exit_program:
        standard.sleep_message("Exiting program.... Thank you.")
        exit()


if __name__ == '__main__':
    inquire_ciphering_type()
