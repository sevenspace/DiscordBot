from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

# training classifier with certain sentences and words


def trainer():
    train = [
        ("i am good", "pos"),
        ("i'm feeling happy", "pos"),
        ("fine thanks", "pos"),
        ("thank you", "pos"),
        ("doing ok", "pos"),
        ("i feel down", "neg"),
        ("i don't know", "neg"),
        ("i love that", "pos"),
        ("i like that", "pos"),
        ("i don't like you", "neg"),
        ("i don't understand", "neg"),
        ("i feel bad", "neg"),
        ("i hate myself", "neg"),
        ("i am sad", "neg"),
        ("i feel happy", "pos"),
        ("i am great", "pos"),
        ("feeling depressed", "neg"),
        ("i am very anxious", "neg"),
        ("it didn't answer my question", "neg"),
        ("you're amazing", "pos"),
        ("my life sucks", "neg"),
        ("everything has been good recently", "pos"),
        ("i want to die", "neg"),
        ("i want to kill myself", "neg"),
        ("i hate you", "neg"),
        ("thank you", "pos"),
        ("i want to hurt myself", "neg")
    ]

    return NaiveBayesClassifier(train)


# testing classifier section

# if __name__ == "__main__":
#     user_input = "I am feeling very happy"
#     classy = trainer().prob_classify(user_input)
#     print()
#     print(f'String:  {user_input}')
#     print(f'---------{len(user_input) * "-"}+')
#     print(f'Negative probability: {classy.prob("neg")}')
#     print(f'Positive probability: {classy.prob("pos")}')
