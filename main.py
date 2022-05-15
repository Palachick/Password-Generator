import random


def concatenate_list(first_word, second_word, punctuation_symbols, number):
    if random.choice([1, 2]) == 1:
        concatenation = list(first_word.upper() + second_word.lower() + number + punctuation_symbols)
    else:
        concatenation = list(first_word.lower() + second_word.upper() + number + punctuation_symbols)
    return concatenation


def assembling_password(first_word, second_word, punctuation_symbols, number):
    list_after_concatenation = concatenate_list(first_word, second_word, punctuation_symbols, number)
    random.shuffle(list_after_concatenation)
    password = "".join(list_after_concatenation)
    print(f"Your password - {password}")

if __name__ == '__main__':
    choice = None
    while choice != "0":
        print """
        0 - Exit
        1 - Create a password manually
        2 - Сreate a password automatically
        """
        choice = input("Сhoose one of the options:")
        if choice == "1":
            first_word = input("Enter your first word:")
            second_word = input("Enter your second word:")
            number = int(input("Enter your number:"))
            punctuation_symbols = input("Enter any punctuation symbols:")
            assembling_password(first_word, second_word, punctuation_symbols, number)


