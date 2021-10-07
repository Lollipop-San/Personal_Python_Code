import random
import string



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
