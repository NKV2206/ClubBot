import lightbulb
import hikari
import pymongo
from datetime import datetime,timedelta
import asyncio
current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
thirty_days_ago = (datetime.now() - timedelta(days=30)).replace(hour=0, minute=0, second=0, microsecond=0)
thirty_days_ago=thirty_days_ago.strftime("%Y-%m-%d")
current_date=current_date.strftime("%Y-%m-%d")

from pymongo import MongoClient
mongo_client =MongoClient("localhost", 27017)
db = mongo_client["WEC_BOT"]  
collection=db["WEC"]
collection2=db['WEC_NONTECH']
collection3=db['WEC_Members']


bot=lightbulb.BotApp(token='MTE2MjAwNTA4MjE1MDI3NzE0MQ.GhZHqw.umaEvikHFkkABnBBAA_-c6tPDMj-o85GbhRcHs',intents=hikari.Intents.ALL,default_enabled_guilds=(1162015150853861398))#instantiating a bot

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Bot is here")

@bot.command
@lightbulb.command('hi','Says Hi!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Hey There!')

@bot.command()
@lightbulb.command('events','Display\'s WEC events')
@lightbulb.implements(lightbulb.SlashCommand)
async def events(ctx):
    """A command to display information about club events from MongoDB."""
    wec_data = collection.find({"date": {"$gt": current_date}}).sort('date',pymongo.ASCENDING)  # Customize the query as per your data structure

    wec_info = "\U0001F4BB Upcoming Events: \U0001F4BB \n"
    for i in wec_data:
        wec_info += f"\n{i['sig'] }: {i['Name']}: {i['date']}"

    await ctx.respond(wec_info)

@bot.command()
@lightbulb.command('past-events','Display\'s WEC past events in different sigs')
@lightbulb.implements(lightbulb.SlashCommand)
async def events(ctx):
    """A command to display information about club events from MongoDB."""
    wec_data1 = collection.find( {"date": {"$gte": thirty_days_ago,"$lt": current_date}}).sort('date',pymongo.DESCENDING) # Customize the query as per your data structure

    wec_info = "\U0001F4BB Recently Concluded Events:\U0001F4BB \n"
    for i in wec_data1:
        wec_info += f"{i['sig'] }:    {i['Name']}:    {i['date']}\n"

    await ctx.respond(wec_info)

@bot.command()
@lightbulb.command('wec-core','Display\'s WEC\'s Core Team for the Year ')
@lightbulb.implements(lightbulb.SlashCommand)
async def events(ctx):
    """A command to display information about club events from MongoDB."""
    wec_data1 = collection3.find( ) # Customize the query as per your data structure

    wec_info = "\U0001F389 Our Core Team \U0001F389 \n"
    for i in wec_data1:
        wec_info += f"{i['Name'] }    :{i['Role']}\n"

    await ctx.respond(wec_info)
@bot.command()
@lightbulb.command('non-tech-events','Display\'s WEC\'s Upcoming Non Tech events')
@lightbulb.implements(lightbulb.SlashCommand)
async def events(ctx):
    """A command to display information about club events from MongoDB."""
    wec_data = collection2.find({"date": {"$gt": current_date}}).sort('date',pymongo.ASCENDING)  # Customize the query as per your data structure

    wec_info = "\U0001F600 Upcoming Non-Tech Events: \U0001F600 \n"
    for i in wec_data:
        wec_info += f"\n{i['Name']}: {i['date']}"

    await ctx.respond(wec_info)
@bot.command()
@lightbulb.command('past-nontech-events','Display\'s WEC past non-tech-events')
@lightbulb.implements(lightbulb.SlashCommand)
async def events(ctx):
    """A command to display information about club events from MongoDB."""
    wec_data1 = collection2.find( {"date": {"$gte": thirty_days_ago,"$lt": current_date}}).sort('date',pymongo.DESCENDING) # Customize the query as per your data structure

    wec_info = "\U0001F600 Recently Concluded Events:\U0001F600 \n"
    for i in wec_data1:
        wec_info += f"{i['Name']}  :  {i['date']}\n"

    await ctx.respond(wec_info)

@bot.command()
@lightbulb.command('development','Information about The Devolopment SIG')
@lightbulb.implements(lightbulb.SlashCommand)
async def events(ctx):
    """A command to display information about club events from MongoDB."""
    wec_data = collection.find({"$and":[{"sig":"Development"},{"date":{"$gt": current_date}}]}).sort('date',pymongo.ASCENDING)  # Customize the query as per your data structure

    wec_info = "About Us : We focus on helping students bridge the gap between theory and practice in software development. Students grow their knowledge in a peer-to-peer learning environment while building solutions to existing problems and helping the communities around through various projects and events. We have tried our hands on backend, frontend, mobile development and are now venturing into game development as well\n"
    try:
        next(wec_data)
        wec_data.rewind()
        wec_info+="Some of Our Upcoming Events are...\n"
        for i in wec_data:
            wec_info += f"{i['Name']}: {i['date']}\n"
    except:
        wec_info+="We Don\'t Have any Upcoming Events..\nStay Tuned as we will be back wih more events\n"
    wec_info+="Follow the WEC Insta page for Latest Updates on WEC events : https://www.instagram.com/wecnitk/"

    await ctx.respond(wec_info)

@bot.command()
@lightbulb.command('intelligence','Information about The Intelligence SIG')
@lightbulb.implements(lightbulb.SlashCommand)
async def events(ctx):
    """A command to display information about club events from MongoDB."""
    wec_data = collection.find({"$and":[{"sig":"Intelligence"},{"date":{"$gt": current_date}}]}).sort('date',pymongo.ASCENDING)  # Customize the query as per your data structure

    wec_info = "About Us : We focus on understanding human intelligence and applying it to machines for the benefit of humanity. We explore the domains of Machine Learning (ML) and Artificial Intelligence (AI), focusing on both research and applications. We research topics in ML theory, Deep Learning, Reinforcement Learning, Data Science, etc. and their applications in simulated and real worlds. We are also interested in competitive ML, primarily participating in Kaggle contests and applying ML techniques for software products\n"
    try:
        next(wec_data)
        wec_data.rewind()
        wec_info+="Some of Our Upcoming Events are...\n"
        for i in wec_data:
            wec_info += f"{i['Name']}: {i['date']}\n"
    except:
        wec_info+="We Don\'t Have any Upcoming Events..\nStay Tuned as we will be back wih more events\n"
    wec_info+="Follow the WEC Insta page for Latest Updates on WEC events : https://www.instagram.com/wecnitk/"

    await ctx.respond(wec_info)

@bot.command()
@lightbulb.command('algorithms','Information about The Algorithms SIG')
@lightbulb.implements(lightbulb.SlashCommand)
async def events(ctx):
    """A command to display information about club events from MongoDB."""
    wec_data = collection.find({"$and":[{"sig":"Algorithms"},{"date":{"$gt": current_date}}]}).sort('date',pymongo.ASCENDING)  # Customize the query as per your data structure

    wec_info = "About Us : We are a group of coding enthusiasts whose aim is to promote Competitive Programming culture at NITK. As part of this mission, we conduct many workshops and contests related to CP. We also conduct sessions like Codebuddy as a bridge between junior-senior. This year we are starting a new mentorship program as part of the SIG to help students in the field of coding skills required to crack interviews for internships and placements\n"
    try:
        next(wec_data)
        wec_data.rewind()
        wec_info+="Some of Our Upcoming Events are...\n"
        for i in wec_data:
            wec_info += f"{i['Name']}: {i['date']}\n"
    except:
        wec_info+="We Don\'t Have any Upcoming Events..\nStay Tuned as we will be back wih more events\n"
    wec_info+="Follow the WEC Insta page for Latest Updates on WEC events : https://www.instagram.com/wecnitk/"

    await ctx.respond(wec_info)

@bot.command()
@lightbulb.command('systems','Information about The Systems SIG')
@lightbulb.implements(lightbulb.SlashCommand)
async def events(ctx):
    """A command to display information about club events from MongoDB."""
    wec_data = collection.find({"$and":[{"sig":"Systems"},{"date":{"$gt": current_date}}]}).sort('date',pymongo.ASCENDING)  # Customize the query as per your data structure

    wec_info = "About Us : We are group of motivated, passionate students who are interested in exploring the various avenues of computer systems . The Systems and Security SIG deals with a broad range of domains including Networks and Distributed Systems, Blockchains, Security, OS, DBMS and Architecture. We are enthusiastic about exploring large open source projects like the Linux kernel. Whether you're interested in Capture the Flag (CTF) security challenges or understanding how large systems like Netflix work, Systems and Security SIG is your go-to group at NITK\n"
    try:
        next(wec_data)
        wec_data.rewind()
        wec_info+="Some of Our Upcoming Events are...\n"
        for i in wec_data:
            wec_info += f"{i['Name']}: {i['date']}\n"
    except:
        wec_info+="We Don\'t Have any Upcoming Events..\nStay Tuned as we will be back wih more events\n"
    wec_info+="Follow the WEC Insta page for Latest Updates on WEC events : https://www.instagram.com/wecnitk/"

    await ctx.respond(wec_info)
bot.run()
mongo_client.close()
