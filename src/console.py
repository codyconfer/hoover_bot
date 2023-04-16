class Colors:
    Black = "\u001b[30m"
    Red = "\u001b[31m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta = "\u001b[35m"
    Cyan = "\u001b[36m"
    White = "\u001b[37m"
    Bright_Black = "\u001b[30;1m"
    Bright_Red = "\u001b[31;1m"
    Bright_Green = "\u001b[32;1m"
    Bright_Yellow = "\u001b[33;1m"
    Bright_Blue = "\u001b[34;1m"
    Bright_Magenta = "\u001b[35;1m"
    Bright_Cyan = "\u001b[36;1m"
    Bright_White = "\u001b[37;1m"
    Reset = "\u001b[0m"


class Backgrounds:
    Black = "\u001b[40m"
    Red = "\u001b[41m"
    Green = "\u001b[42m"
    Yellow = "\u001b[43m"
    Blue = "\u001b[44m"
    Magenta = "\u001b[45m"
    Cyan = "\u001b[46m"
    White = "\u001b[47m"
    Bright_Black = "\u001b[40;1m"
    Bright_Red = "\u001b[41;1m"
    Bright_Green = "\u001b[42;1m"
    Bright_Yellow = "\u001b[43;1m"
    Bright_Blue = "\u001b[44;1m"
    Bright_Magenta = "\u001b[45;1m"
    Bright_Cyan = "\u001b[46;1m"
    Bright_White = "\u001b[47;1m"
    Reset = "\u001b[0m"


class TextStyles:
    Bold = "\u001b[1m"
    Underline = "\u001b[4m"
    Reversed = "\u001b[7m"
    Reset = "\u001b[0m"


COLORS = Colors()
BACKGROUNDS = Backgrounds()
TEXT_STYLES = TextStyles()


def contextualize(msg: str, color: str):
    return f"{color}{msg}{COLORS.Reset}"
