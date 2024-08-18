import standardMethods
import standardTables


def des_sub_keys(key):
    standardMethods.sleep_message(f"\n\nStarting encryption of the 64 bit key....\n\n")
    standardMethods.sleep_message(f"Initial Key: {key}\n\n")

    key_binary = list(map(int, key))

    standardMethods.sleep_message(f"Performing permutation 1 on the key. Key of 64 bits will be converted to 56 bits\n")
    key_permuted_1 = standardMethods.permutation(key_binary, standardTables.permutation_table_1)
    standardMethods.sleep_message(f"Key PC-1: {key_permuted_1}\n")

    standardMethods.sleep_message(f"Splitting Key-PC-1 in half. we'll get C0 and D0\n")
    key_c0 = key_permuted_1[:len(key_permuted_1) // 2]
    key_d0 = key_permuted_1[len(key_permuted_1) // 2:]
    standardMethods.sleep_message(f"Key-C0: {key_c0}\n")
    standardMethods.sleep_message(f"Key-D0: {key_d0}\n")

    standardMethods.sleep_message(f"Performing left shift on key to get C0-D0, C1-D1, C2-D2, ...., C16-D16. \n")
    standardMethods.sleep_message(f"Performing left shift of 1 iteration for round 1, 2, 9 and 16 while 2 iterations "
                                  f"for remaining rounds\n")
    keys_list = []
    round_num = 1
    while round_num <= 16:
        key = key_left_shift(key_c0, key_d0, round_num)
        keys_list.append(key)
        round_num += 1

    standardMethods.sleep_message(f"\nMerging C and D sub keys C0D0, C1D1, ..., C16D16 and performing Permutation "
                                  f"PC-2 on the the sub keys to get K1, K2, ...., K16.\n")
    key_list_final = []
    round_num = 1
    while round_num <= 16:
        key = standardMethods.permutation(keys_list[round_num-1], standardTables.permutation_table_2)
        key_list_final.append(key)
        standardMethods.sleep_message(f"Key{round_num}: {key}\n")
        round_num += 1

    return key_list_final


def key_left_shift(key1, key2, round_num):
    if round_num == 1 or round_num == 2 or round_num == 9 or round_num == 16:
        value = key1.pop(0)
        key1.append(value)

        value = key2.pop(0)
        key2.append(value)
    else:
        value1 = key1.pop(0)
        value2 = key1.pop(0)
        key1.append(value1)
        key1.append(value2)

        value1 = key2.pop(0)
        value2 = key2.pop(0)
        key2.append(value1)
        key2.append(value2)

    standardMethods.sleep_message(f"C{round_num}: {key1}\n")
    standardMethods.sleep_message(f"D{round_num}: {key2}\n")

    key = key1 + key2

    return key
