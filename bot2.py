from textblob import TextBlob

import stopwords as stopwords
import classifier as cl
from chatterbot import ChatBot
import json

import emotionClass as emo

# emoji files
import happy
import sadness as sadge
import affirmation as affirm

bot = ChatBot("Pani")

# opens training db
with open("paniBot.json", "r") as f:
    array = json.load(f)

CONVERSATION = array["conversations"]
BOT_NAME = "Pani"
STOP_WORDS = stopwords.stopwords_list
neg_distribution = []


# this function gets the sentiment score
def sentiment(U_input):
    blob_it = cl.trainer().prob_classify(U_input)
    score = round(blob_it.prob("neg"), 2)
    return score


# gets emotes
def emote(U_input):
    return emo.get_emotion(U_input)

# reads user input and checks if in the response DB if so return the bot response


def emoji_res(user_input):
    emotion = emote(user_input)
    if check_word(user_input, "thank") or check_word(user_input, "thanks"):
        return affirm.affirmation()
    elif emotion == "happy" and sentiment(user_input) < 0.3:
        return happy.happy()
    elif emotion == "sad" and sentiment(user_input) >= 0.55 and sentiment(user_input) < 0.85:
        return sadge.sad()
    else:
        return ""

# Checks if a word is in the user input


def check_word(user_input, word):
    words = user_input.split()
    if word in words:
        return True
    else:
        return False

# checks user response is in the set


def responseCheck(user_input):
    user_blob = TextBlob(user_input)
    # this normalises user input into lowercase
    lower_input = user_blob.lower()
    # we tokenize the object into words
    token_input = lower_input.words
    # creates list of words not in the stop word list
    filtered_input = [w for w in token_input if w not in STOP_WORDS]

    response_set = set()

    for con_list in CONVERSATION:
        for sentence in con_list:
            sentence_split = sentence.split()
            if set(filtered_input).intersection(sentence_split):
                response_set.update(con_list)

    if not response_set:
        return "Sorry I don't understand, please ask again, or phrase your sentence differently"
    else:
        return max(response_set, key=len)


# gets user input and responds and checks if the user needs more help depending on recent sentiment


def escalation(U_input):
    live_resp = "You seem like you need more professional help\nI recommend contacting these hotlines:\nSamaritans: 116 123 \nNational Suicide Prevention: 0800 689 5652 \nSANEline: 0300 304 7000 "

    neg_distribution.append(sentiment(U_input))
    list_len = len(neg_distribution)
    bot_response = responseCheck(U_input)

    if list_len > 3:
        last_3 = neg_distribution[-3:]
        if last_3[0] >= 0.55 and last_3[0] <= last_3[1] <= last_3[2]:
            last_3.clear()
            return live_resp
        else:
            return bot_response
    else:
        return bot_response


# testing for chatbot

# if __name__ == '__main__':
#     while True:
#         try:
#             user_input = input("You: ")
#             print('Bot: ', escalation(user_input))
#             print(emoji_res(user_input))
#             print(neg_distribution)
#         except (KeyboardInterrupt, EOFError, SystemExit):
#             break
