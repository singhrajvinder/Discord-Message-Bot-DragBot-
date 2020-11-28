import discord
from discord.ext import commands
from webserver import keep_alive
import os

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self,member):
        '''someoen joined the selver'''
        say = member.name + ' has joined the server. \nPlease ping a deputy or leader to be assigned a role. \nRead rules in <#688158261714747520> channel.'
        await member.guild.text_channels[0].send(say)

    async def on_member_remove(self,member):
        '''someone left the server'''
        say = member.name + ' has left the server.'
        await member.guild.text_channels[0].send(say)

    async def on_message(self, message):
        '''the commands hehehe'''
        if message.author == client.user:
            return

        if message.content.startswith(':ping'):
            say = f'pong! {round(self.latency * 1000)}ms' + ' {0.author.mention}'
            await message.channel.send(say.format(message))

        if message.content.startswith(':clear'):
            word = message.content.strip(':clear ')
            amount = int(word) + 1
            await message.channel.purge(limit=amount)


keep_alive()
client = MyClient()
Token = os.environ.get("Discord_Bot_Secret")
client.run(Token)