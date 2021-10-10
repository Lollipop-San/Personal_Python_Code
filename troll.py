def user_directory():
    'Just modify the input below to the directory of the file'
    return input(r"""
C:\Users\userdirectory\>""")


def troll_help():
    'This function will sort of troll the user if he/she typed "help"'
    response = user_directory()
    if response == 'help':
        return "No fuck you, learn things by yourself and dont ask help from me anymore"
    elif 'hlep' or 'hepl' in response:
        return f"""'{response}' is not recognized as an internal or external command,
operable program or batch file. Did you mean 'help'?"""
    return f"""'{response}' is not recognized as an internal or external command,
operable program or batch file."""


while True:
    e = print(troll_help())
    if e == 'help':
        break
