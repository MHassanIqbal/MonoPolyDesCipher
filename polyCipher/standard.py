from time import sleep
import inquirer


def sleep_message(message):
    for char in message:
        sleep(0.005)
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
