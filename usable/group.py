import discord
import json

from data import datamanager

class Group:

    def __init__(self, client, name = 'text_channel'):
        self.client = client
        self.members = []
        self.guild = client.get_guild(datamanager.getConfig('covert_server')) # insert guild ID
        self.name = name
        self.channel = None

    async def instantiate_channel(self):
        category = self.guild.get_channel(685952096981221442)
        overwrites = {
            self.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            self.guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        self.channel = await self.guild.create_text_channel(self.name, overwrites=overwrites, category = category)

    def add_user(self, user_id):
        user = self.client.get_user(user_id)
        self.members.append(user)

    def remove_user(self, user_id):
        user = self.client.get_user(user_id)
        self.members.remove(user)

    async def refresh_members(self):
        for user in self.channel.members:
            print("Debug: Removed " + user.name + " from secret channel")
            await self.channel.set_permissions(user, overwrite = None)
        for user in self.members:
            print ("Debug: Added " + user.name + " to secret channel")
            await self.channel.set_permissions(user, read_messages = True, send_messages = True)

    async def delete_channel(self):
        await self.channel.delete()

    def get_id(self):
        return self.channel.id
