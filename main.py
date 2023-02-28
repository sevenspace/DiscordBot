import discord
from discord.ext import commands
import bot2 as b

#bot = commands.Bot(command_prefix="!")
client = discord.Client()

# shows bot has gone online


@client.event
async def on_ready():
    print("You have logged on as {0.user}".format(client))

# get's user's username


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

# general greetings/information section
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}! My name is Pani :grinning:')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Goodbye {username}')
            return
        elif user_message.lower() == '!bot_info':
            await message.channel.send("Pani the chatbot is made to help you answer your questions and queries on mental health and help you learn more about them.\nTo get information on different mental illnesses use the !health_info command\nOtherwise type in a query and Pani will do her best to answer you!")
            return


# mental health resources section
    if user_message.lower() == '!health_info':
        await message.channel.send("These commands provide resources: ")
        await message.channel.send("!depression\n !anxiety\n !stress\n !adhd\n !trauma\n !eating_disorder")
        return
    if user_message.lower() == '!depression':
        await message.channel.send('Depression\nDefinition: Depression is a mental disorder, which is identified by persistent sadness, feelings of unhappiness, losing interest in activities you enjoy and feeling hopeless. \nStatistics: There is an estimation of 280 million people worldwide that have depression. There are many effective treatments for depression and can be treated by a medical professional if severe. \nResources: https://www.nhs.uk/mental-health/conditions/clinical-depression/overview/, https://www.helpguide.org/articles/depression/coping-with-depression.html \n')
    elif user_message.lower() == '!anxiety':
        await message.channel.send('Anxiety \nDefinition: Anxiety is a feeling or unease, worry or fear. This feeling can range from being mild or severe. Everyone has some sense of anxiety and it is normal to feel anxious during certain times. However, for others they may have more severe symptoms where they have trouble controlling their worries, which can affect their daily lives. \nStatistics: 62 % of people have reported to experience some degree of anxiety \nResources: https://www.mind.org.uk/information-support/types-of-mental-health-problems/anxiety-and-panic-attacks/about-anxiety /, https://www.healthline.com/health/mental-health/how-to-cope-with-anxiety  # quick-coping-methods \n')
    elif user_message.lower() == '!stress':
        await message.channel.send('Stress \nDefinition: Stress is a reaction from your body when you feel overwhelmed, threatened or under pressure. It is a common feeling and that can happen in certain situations can affect our mood and our body. \nStatistics: Everyone experiences stress and will occur at some points in our lives \nResources: https://www.mentalhealth.org.uk/a-to-z/s/stress, https://www.cdc.gov/violenceprevention/about/copingwith-stresstips.html \n')
    elif user_message.lower() == '!eatingdis':
        await message.channel.send('Eating Disorder \nDefinition: An eating disorder is a mental condition that makes your control of food is used to cope with feelings or other situations. Anyone can get an eating disorder and can involve unhealthy thoughts to towards food, their body and eating. \nStatistics: Eating disorders affect at least 9 % of people worldwide. They’re deemed one of the deadliest mental illnesses after opioid overdose \nResources: https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/eating-disorders/overview /, https://www.beateatingdisorders.org.uk/ \n')
    elif user_message.lower() == '!adhd':
        await message.channel.send('ADHD \nDefinition: AHD stands for Attention Hyperactivity Disorder and affects people’s behaviour. It is a mental disorder that can include inattention, hyperactivity and impulsivity. \nStatistics: It is estimated 8.4 % of children and 2.5% of adults have ADHD \nResources: https://www.cdc.gov/ncbddd/adhd/facts.html, https://www.nhs.uk/conditions/attention-deficit-hyperactivity-disorder-adhd/living-with / \n')
    elif user_message.lower() == '!trauma':
        await message.channel.send('Trauma \nDefinition: Trauma is when you go through something that may be extremely stressful, distressing or frightening. It can have long-lasting effects and everyone has a different reaction to trauma. \nStatistics: Over 70 % of people have experiences at least one traumatic event in their lifetime \nResources: https://www.mind.org.uk/information-support/types-of-mental-health-problems/trauma/about-trauma /, https://www.apa.org/topics/trauma/stress \n')
    else:
        await message.channel.send(b.escalation(user_message.lower()))
        await message.channel.send(b.emoji_res(user_message.lower()))

# put your bot discord token here replacing text
client.run("insert Discord bot token here")
