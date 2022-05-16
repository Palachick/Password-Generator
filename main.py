import random
import string


# creating a password manually
def concatenate_list(first_word, second_word, punctuation_symbols, number):
    """Concatenate and conversion in list"""

    if random.choice([1, 2]) == 1:
        concatenation = list(first_word.upper() + second_word.lower() + number + punctuation_symbols)
    else:
        concatenation = list(first_word.lower() + second_word.upper() + number + punctuation_symbols)
    return concatenation


def assembling_password_manually(first_word, second_word, punctuation_symbols, number):
    """Shuffling and assembling the password"""

    list_after_concatenation = concatenate_list(first_word, second_word, punctuation_symbols, number)

    # creating password
    random.shuffle(list_after_concatenation)
    password = "".join(list_after_concatenation)

    print(f"Your password - {password}")


# creating a password automatically
def creating_password_automatically(length):
    """Create a password using strings and random modules"""

    # initialization
    lower_symbols = string.ascii_lowercase
    upper_symbols = string.ascii_uppercase
    punctuation_symbols = string.punctuation
    numbers = string.digits

    # concatenate
    concatenate_symbols = lower_symbols + upper_symbols + punctuation_symbols + numbers

    # creating password
    temporary_sequence = random.sample(concatenate_symbols, length)
    password = "".join(temporary_sequence)

    print(f"Your password - {password}")


if __name__ == '__main__':
    choice = None
    while choice != "0":
        # creating menu
        print ("""
        0 - Exit
        1 - Create a password manually
        2 - Сreate a password automatically
        """)
        choice = input("Сhoose one of the options : ")
        # input processing
        if choice == "1":
            first_word = input("Enter your first word : ")
            second_word = input("Enter your second word : ")
            number = input("Enter your number : ")
            punctuation_symbols = input("Enter any punctuation symbols : ")
            assembling_password_manually(first_word, second_word, punctuation_symbols, number)
        elif choice == "2":
            length = int(input("Enter length your password : "))
            creating_password_automatically(length)

