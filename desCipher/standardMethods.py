import binascii
from time import sleep
import inquirer
import standardTables


def sleep_message(message):
    for char in message:
        sleep(0)
        print(char, end='', flush=True)
    return


def inquirer_selector(message, choices):
    options_selection = [
        inquirer.List('code', message, choices),
    ]
    selection = inquirer.prompt(options_selection)
    return selection['code']


def get_input(message, warning, limit):
    temp_text = []
    while len(temp_text) == limit:
        print("\n" + message + warning + "\n")
        for line in iter(input, ''):
            temp_text.append(line)
    text = "\n".join(temp_text)
    return text


def permutation(text, table):
    key_permuted = []
    for value in table:
        key_permuted.append(text[value - 1])
    return key_permuted


def text_encryption_decryption(text, keys_list, text_type, action_type):
    sleep_message(f"Starting {action_type} of the 64 bit text....\n\n")
    sleep_message(f"Initial {text_type}: {text}\n\n")

    text_binary = list(map(int, text))

    sleep_message(f"Performing Initial permutation on the {text_type}\n")
    text_initial_permuted = permutation(text_binary, standardTables.initial_permutation_table)
    sleep_message(f"{text_type} IP: {text_initial_permuted}\n\n")

    sleep_message(f"Slicing Permuted {text_type} into 2 equal parts of 32 bits as L0 and R0.\n")
    text_left_0 = text_initial_permuted[:len(text_initial_permuted) // 2]
    text_right_0 = text_initial_permuted[len(text_initial_permuted) // 2:]
    sleep_message(f"L0: {text_left_0}\n")
    sleep_message(f"R0: {text_right_0}\n")

    sleep_message("\nPerforming Rounds operations on the L0 and R0 to get final L16 and R16 after 16 rounds\n")
    round_num = 1
    text_list_left = [text_left_0]
    text_list_right = [text_right_0]
    while round_num <= 16:
        text_left, text_right = text_round_operations(text_list_left[round_num - 1], text_list_right[round_num - 1],
                                                      round_num, keys_list[round_num - 1])
        text_list_left.append(text_left)
        text_list_right.append(text_right)
        round_num += 1

    sleep_message(f"Performing Swapping to converter L16 to R16 and R16 to LR and combining them in one text to get "
                  f"{text_type} of 64 bits\n")
    text_r16_l16 = text_list_right[len(text_list_right) - 1] + text_list_left[len(text_list_right) - 1]
    sleep_message(f"{text_type} R16L16: {text_r16_l16}\n")

    sleep_message(f"\nApplying final permutation on {text_type} R16L16 to get {text_type} in binary.\n")
    text_cipher_binary = permutation(text_r16_l16, standardTables.final_permutation_table)
    sleep_message(f"Text (Binary): {text_cipher_binary}\n")
    text_cipher_binary_string = "".join(map(str, text_cipher_binary))
    sleep_message(f"{text_cipher_binary_string}\n")

    sleep_message(f"\nConverting Binary to Text\n")
    text_final = ""
    for char in range(0, len(text_cipher_binary_string), 8):
        text_final += format(chr(int(text_cipher_binary_string[char:char + 8], 2)))

    return text_final


def expansion(text):
    text_expanded = []
    for value in standardTables.text_expansion_table:
        text_expanded.append(text[value - 1])
    return text_expanded


def text_round_operations(text_left, text_right, round_num, key):
    sleep_message(f"\n \n **Round: {round_num}** \n\n")

    sleep_message(f"L{round_num - 1}: {text_left}\n")
    sleep_message(f"R{round_num - 1}: {text_right}\n")

    sleep_message(f"\nPerforming expansion on R{round_num - 1} to expand from 32 bits to 48 bits\n")
    text_expanded = expansion(text_right)
    sleep_message(f"E(R{round_num - 1}): {text_expanded}\n")

    sleep_message(f"\nPerforming XOR to Key{round_num} of 48 bits with expanded R{round_num - 1} of 48 bits.\n")
    text_expanded_xor = [x ^ y for x, y in zip(key, text_expanded)]
    sleep_message(f"K{round_num} + E(R{round_num - 1}): {text_expanded_xor}\n")

    sleep_message(f"\nSplitting K{round_num} + E(R{round_num - 1}) into 8 parts 6 bits each..\n")
    text_bits_list = []
    temp_num = 1
    for bits in range(0, len(text_expanded_xor), 6):
        text_bits = text_expanded_xor[bits:bits + 6]
        text_bits_list.append(text_bits)
        print(f"B{temp_num}: {text_bits}")
        temp_num += 1

    sleep_message(
        f"\nPerforming Substitution Algorithm S-Box to the R{round_num - 1} to get 32 bits text from 48 bits text\n")
    s_box_tables_list = [standardTables.s1_box_table, standardTables.s2_box_table, standardTables.s3_box_table,
                         standardTables.s4_box_table, standardTables.s5_box_table, standardTables.s6_box_table,
                         standardTables.s7_box_table, standardTables.s8_box_table]
    s_box_value = []
    temp_num = 1
    while temp_num <= 8:
        temp_s_box_bit = s_box(text_bits_list[temp_num - 1], s_box_tables_list[temp_num - 1], temp_num)
        s_box_value += temp_s_box_bit
        temp_num += 1

    sleep_message(f"\nS(E1 + E (R{round_num})): {s_box_value}\n")

    sleep_message(f"\nPerforming permutation on S (E{round_num} + E(R{round_num - 1}))\n")
    s_box_value_permuted = permutation(s_box_value, standardTables.s_box_permutation_table)
    sleep_message(f"{s_box_value_permuted}\n")

    sleep_message(f"\nPerforming XOR to L{round_num - 1} of 32 bits with S (E{round_num} + E(R{round_num - 1})) of 32 "
                  f"bits. and converting R{round_num - 1} at the start of the round{round_num} to L{round_num}\n")
    text_final_right = [x ^ y for x, y in zip(text_left, s_box_value_permuted)]
    text_final_left = text_right
    sleep_message(f"L{round_num}: {text_final_left}\n")
    sleep_message(f"R{round_num}: {text_final_right}\n")
    sleep_message(f"\n\nRound{round_num} completed successfully.\n\n")

    return text_final_left, text_final_right


def s_box(text, table, num):
    sleep_message(f"\nGet First and Last bit of B{num}\n")
    bit_1 = str(text[0])
    bit_2 = str(text[5])
    sleep_message(f"First Bit of B{num}: {bit_1}\n")
    sleep_message(f"Last Bit of B{num}: {bit_2}\n")

    sleep_message(f"Adding first and last bit and convert to integer to get row for S{num} table\n")

    bit_row = int((bit_1 + bit_2), 2)
    sleep_message(f"Row to check of S{num} is {bit_row}\n")

    sleep_message(f"Converting rest of the bits to integer to get column for S{num} table\n")
    bit_col = ""
    for value in text[1:5]:
        bit_col += str(value)
    bit_col = int(bit_col, 2)
    sleep_message(f"Colum to check of S{num} is {bit_col}\n")

    row_num = table.get(bit_row)
    value_int = row_num.get(bit_col)
    s_box_bit_value_string = "{0:04b}".format(value_int)
    sleep_message(
        f"Value at row{bit_row} and column{bit_col} of table S{num} is: {s_box_bit_value_string}\n")

    s_box_bit_value = list(map(int, s_box_bit_value_string))
    sleep_message(f"S(B{num}): {s_box_bit_value}\n")

    return s_box_bit_value


def check_and_adjust_text_size(text):
    if len(text) < 64:
        while True:
            text.insert(0, 0)
            if len(text) == 64:
                break
    elif len(text) > 64:
        while True:
            text.insert(0, 0)
            if len(text) % 64 == 0:
                break
    return text


def divide_list(text_list, num):
    for char in range(0, len(text_list), num):
        yield text_list[char:char + num]
