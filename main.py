import discord
from discord.ext import commands
import outputs
import random
import os

workout_plans = {
    "lose_weight": [
        outputs.cardioPlan1,
        outputs.cardioPlan2,
        outputs.cardioPlan3
    ],
    "strength": [
        outputs.strengthPlan1,
        outputs.strengthPlan2,
        outputs.strengthPlan3
    ]
}

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def workout(ctx, goal: str):
    if goal.lower() == 'lose_weight':
        workout = random.choice(workout_plans['lose_weight'])
        await ctx.send(f'For weight loss, your workout routine is:\n{workout}')
    elif goal.lower() == 'strength':
        workout = random.choice(workout_plans['strength'])
        await ctx.send(f'For strength, your workout routine is:\n{workout}')
    elif goal.lower() == 'hello':
        await ctx.send('Hello!')
    elif goal.lower() == 'coleman':
        await ctx.send('LIGHTWEIGHT')
    else:
        await ctx.send("Please specify either 'lose_weight' or 'strength' as your goal.")

bot.run('YourTokenHere')
