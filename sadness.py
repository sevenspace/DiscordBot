import re
import random

# random sad emoji


def sad():
    sad_emoji = [
        ":cry:",
        ":slight_frown:",
        ":frowning:",
        ":disappointed:",
        ":sob:",
        ":pensive:",
        ":persevere:",
        ":confused:"][random.randrange(8)]
    return sad_emoji
