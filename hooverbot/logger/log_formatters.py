from hooverbot.logger.console import COLORS, contextualize

offset = 0
offset_space = " " * offset


def log_response(channel_name, user, response):
    x = f"{offset_space}{contextualize('<-', COLORS.Yellow)} {contextualize(channel_name, COLORS.Yellow)} {contextualize(user, COLORS.Magenta)}"
    y = f"{offset_space}{contextualize('|', COLORS.Yellow)} {contextualize(response, COLORS.Magenta)}"
    return f"\n{x}\n{y}"


def log_incoming(channel_name, user, msg):
    x = f"{contextualize(user, COLORS.Blue)} {contextualize(channel_name, COLORS.Green)} {contextualize('->', COLORS.Green)}"
    y = f"{contextualize('|', COLORS.Green)} {contextualize(msg, COLORS.Blue)}"
    return f"\n{x}\n{y}"
