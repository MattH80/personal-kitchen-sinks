from enum import Enum 


class print_colours(Enum):
    BLACK = str(30)
    RED = str(31)
    GREEN = str(32)
    YELLOW = str(33)
    BLUE = str(34)
    PURPLE = str(35)
    CYAN = str(36)
    WHITE = str(37)

class print_style(Enum):
    NONE = str(0)
    BOLD = str(1)
    UNDERLINE = str(2)
    NEGATIVE1 = str(3)
    NEGATIVE2 = str(5)

class background_colours(Enum):
    BLACK = '40m'
    RED = '41m'
    GREEN = '42m'
    YELLOW = '43m'
    BLUE = '44m'
    PURPLE = '45m'
    CYAN = '46m'
    WHITE = '47m'

def colour_code(style=print_style.NONE, print_colour=print_colours.WHITE, background_colour=background_colours.BLACK) -> str:
    ansi_escape_code = "\033["
    return str(ansi_escape_code + style.value + ";" + print_colour.value + ";" + background_colour.value)

if __name__ == '__main__':
    print(colour_code() + "Hi")