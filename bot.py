/// Delete this "//" since this might distract you

import praw
import random
from discord.ext import commands

bot = commands.Bot(description="test", command_prefix="!")

reddit = praw.Reddit(client_id='CLIENT_ID HERE', // Replace this for Client ID
                     client_secret='CLIENT_SECRET HERE', // Replace for client secret
                     user_agent='USER_AGENT HERE') // replace the USer Agent

@bot.command()
async def meme():
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await bot.say(submission.url)

bot.run('TOKEN')
