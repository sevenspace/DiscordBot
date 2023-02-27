import re
import random

# random happy emoji


def happy():
    happy_emoji = [
        ":grin:",
        ":smiley:",
        ":smile:",
        ":grinning:",
        ":slight_smile:",
        ":relaxed:",
        ":blush:",
        ":hugging:"][random.randrange(8)]
    return happy_emoji
