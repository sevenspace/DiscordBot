from webbrowser import get
from nrclex import NRCLex


def get_emotion(text):

    text = NRCLex(text)

    hCount = 0
    sCount = 0

    for i in range(len(text.top_emotions)):
        if text.top_emotions[i][0] == "positive" or text.top_emotions[i][0] == "joy":
            hCount += 1
        elif text.top_emotions[i][0] == "negative" or text.top_emotions[i][0] == "sadness" or text.top_emotions[i][0] == "fear":
            emotion = "sad"
            sCount += 1
        else:
            emotion = "neutral"

    if hCount > sCount:
        emotion = "happy"
    elif sCount > hCount:
        emotion = "sad"
    else:
        emotion = "neutral"

    return emotion
