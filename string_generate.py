import random
import string 

class generate:
    """This class can contains functions that can randomly generate characters that are defined in ASCII.
The user can choose on how many number of characters to generate."""
    def string_letter(size):
        """Takes the argument inside the parenthesis (integer) as the number of the randomly generated characters.
Returns a string that contains only letters may it be uppercase or lowercase."""
        chars = string.ascii_uppercase + string.ascii_lowercase
        return ''.join(random.choice(chars) for _ in range(size))

    def string_number(size):
        """Takes the argument inside the parenthesis (integer) as the number of the randomly generated characters.
Returns only numbers (integers) in the form of strings."""
        chars = string.digits
        return ''.join(random.choice(chars) for _ in range(size))

    def string_specialchar(size):
        """Takes the argument inside the parenthesis (integer) as the number of the randomly generated characters.
Returns only special characters (eg. <, =, >, ?, @) in the form of strings."""
        chars = string.punctuation
        return ''.join(random.choice(chars) for _ in range(size))

    def string_letter_number(size):
        """Takes the argument inside the parenthesis (integer) as the number of the randomly generated characters.
Returns letters (uppercase and lowercase) and numbers (integers) in the form of strings.
Please take note that it may not always return a string with a number."""
        chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
        return ''.join(random.choice(chars) for _ in range(size))

    def string_ascii(size):
        """Takes the argument inside the parenthesis (integer) as the number of the randomly generated characters.
Returns letters (uppercase and lowercase), numbers (integers) and special characters (eg. <, =, >, ?, @) in the form of strings."""
        chars = string.ascii_lowercase + string.ascii_uppercase + \
            string.punctuation + string.digits
        return ''.join(random.choice(chars) for _ in range(size))


class generate_string2:
    # this class is buggy for now due to the inability to customize the number of characters
    """This class has a string generator which a user can customize by modifying the characters list.
But the number of characters generated cannot be customized.
(returns a string) Note: this is just for experiment so expect a lot of errors while using it."""
    def generate():
        characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                      "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "y", "x", "y", "z",
                      "A", "B", "C", "D", "E", "F",
                      "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@", "#", ]

        for char in characters:
            print(random.choice(characters), end='')
