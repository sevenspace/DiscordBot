from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot("Pani")
chatbot.storage.drop()
trainer = ListTrainer(chatbot)

# Dictionary of list inputs and responses
questions = [
    ("can you help me", "What help would you like? For information on how to use the chatbot use !bot_info"),
    ("can you describe",
     "You can use the command !health_info to get more information on this"),
    ("how are you", "I am good :smile: How are you feeling?"),
    ("what mental illnesses are there",
     "You can use the command !health_info to get more information on this")
]

positive = [
    ("happy", "I'm glad you're happy"),
    ("great", "That's good to hear"),
    ("amazing", "Good for you!"),
    ("doing good", "Nice!"),
    ("love", "Amazing! ")
]

dep_Ad = [
    ("depressed", "Try going out for a walk or jog to help lift your mood"),
    ("advice on depression",
     "Stay in touch with friends and family and talk to them when you feel down"),
    ("help with depression",
     "Try relaxation techniques like, yoga, deep breathing, or meditation"),
    ("sad", "I'm sorry to hear that. How about trying to write down your feelings in a journal and the challenges you face when feeling depressed")
]

anx_Ad = [
    ("help with anxiety", "Try to figure out what triggers your anxiety. Jot down in a diary whenver you feel anxious to help see the patterns"),
    ("advice for anxiety", "Try counting to 10 slowly and repeat, until you feel more calm"),
    ("anxious", "Take some time to relax, listen to music, or meditate"),
    ("restless", "Try counting to 10 slowly and repeat, until you feel more calm")
]

stress_Ad = [
    ("stressed", "Practice meditation or mindfulness"),
    ("help with stress", "Talk to good friends and family who are good listeners"),
    ("advice for stress", "Try to find some time to do any hobbies you enjoy"),
    ("stressful", "Practice meditation or mindfulness")
]

adhd_Ad = [
    ("help with adhd", "Try changing your lifestyle by eating more healthy, exercising more"),
    ("advice for adhd", "Practice meditation or relaxation techniques"),
    ("can't concentrate",
     "Try putting your phone down and stay away from social media to help settle your mind")
]

greeting = [
    ("hi", "Hi I am Pani the mental health assistant chatbot :slight_smile:"),
    ("hello", "Hello I am Pani the chatbot"),
    ("hey", "It's nice to meet you I am Pani")
]

gratitude = [
    ("thank you", "You're welcome"),
    ("thanks", "Glad I could help")
]

guidance = [
    ("wasn't useful"),
    ("useless"),
    ("does not make sense")
]

emergency = [
    ("kill myself"),
    ("want to die"),
    ("hurt myself")
]

# training for the response set
for dep, advice1 in dep_Ad:
    trainer.train([
        f"{dep}",
        f"{advice1}"
    ])

for anx, advice2 in anx_Ad:
    trainer.train([
        f"{anx}",
        f"{advice2}"
    ])

for stress, advice3 in stress_Ad:
    trainer.train([
        f"{stress}",
        f"{advice3}"
    ])

for adhd, advice4 in adhd_Ad:
    trainer.train([
        f"{adhd}",
        f"{advice4}"
    ])

for quest, ans in questions:
    trainer.train([
        f"{quest}",
        f"{ans}"
    ])

for emerge in emergency:
    trainer.train([
        f"{emerge}",
        f"This seems serious and Pani thinks you should contact someone urgently I recommend\nSamaritans: 116 123\nNational Suicide Prevention: 0800 689 5652\nSANEline: 0300 304 7000"
    ])

for happy, posi in positive:
    trainer.train([
        f"{happy}",
        f"{posi}"
    ])
for greet, ans in greeting:
    trainer.train([
        f"{greet}",
        f"{ans}"
    ])

for thank, grat in gratitude:
    trainer.train([
        f"{thank}",
        f"{grat}"
    ])

for guide in guidance:
    trainer.train([
        f"{guide}",
        f"Sorry about that, if you want to talk to a real person to give better advice try\nhttps://www.samaritans.org/how-we-can-help/contact-samaritan/"
    ])

trainer.export_for_training("paniBot.json")
