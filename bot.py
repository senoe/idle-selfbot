import discord, os

bot = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle)
    print(f"Logged in as {bot.user}!")

bot.run(os.environ.get("token"), bot=False, reconnect=True)
