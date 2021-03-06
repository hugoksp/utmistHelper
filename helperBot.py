import discord
import hashlib

# import the token
with open('token') as tokenFile:
	token = tokenFile.readlines()[0].rstrip()

# boiler plate code
client = discord.Client()

# parse message contents
def commands(message):
	content = message.split()	

	if len(content) == 1:
		return 'Not enough args, check with `h! help`'
	
	if content[1] == 'hash':
		if len(content) != 3:
			return 'not enough or too many args'
		hashVal = hashlib.sha256(content[2].encode()).hexdigest()
		return 'Hashed value is: ' + str(hashVal)
	
	if content[1] == 'help':
		with open('manPage') as helpText:
			return ''.join(helpText.readlines())
	
	return 'Unknown command, check with `h! help`'


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(status=discord.Status.invisible)

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('h!'):
		response = commands(message.content)
		await message.channel.send(response)

client.run(token)


