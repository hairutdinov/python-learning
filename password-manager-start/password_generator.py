from random import choice, randint, shuffle

LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
MIN_LETTERS_COUNT = 8
MAX_LETTERS_COUNT = 10
MIN_SYMBOLS_COUNT = 2
MAX_SYMBOLS_COUNT = 4
MIN_NUMBERS_COUNT = 2
MAX_NUMBERS_COUNT = 4


class PasswordGenerator:
    @staticmethod
    def generate():
        nr_letters = randint(MIN_LETTERS_COUNT, MAX_LETTERS_COUNT)
        nr_symbols = randint(MIN_SYMBOLS_COUNT, MAX_SYMBOLS_COUNT)
        nr_numbers = randint(MIN_NUMBERS_COUNT, MAX_NUMBERS_COUNT)
        password = []

        password.extend([choice(LETTERS) for _ in range(0, nr_letters)])
        password.extend([choice(SYMBOLS) for _ in range(0, nr_symbols)])
        password.extend([choice(NUMBERS) for _ in range(0, nr_numbers)])

        shuffle(password)

        return "".join(password)
