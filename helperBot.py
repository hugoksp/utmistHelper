import discord

# import the token
tokenFile = "token"
token = tokenFile.readlines()[0].rstrip()

# boiler plate code
client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

client.run(token)