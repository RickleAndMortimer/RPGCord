import discord
from discord.ext import commands
import campaigns

#a dictionary of users who in turn have a dictionary of character attributes
userChar = {}

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
bot = commands.Bot(command_prefix= '!')

bot.remove_command('help')
@bot.command()
async def help(ctx):
    await ctx.send("create - Creates a character for the user {create [name][profession(0-4)])\n"
                   "rename - renames your character {rename [name]}\n"
                   "rest - restores your character to full health {rest}\n"
                   "join - allows your character to join a certain profession {join [0-4]}\n"
                             "0 - No profession\n"
                             "1 - Alchemist\n"
                             "2 - Archer\n"
                             "3 - Mage\n"
                             "4 - Swordsman\n"
                   "leave - Resets progress on your character and leaves your current occupation\n"
                   "startCampaign - Begins a tutorial campaign\n"
                   "joinAdventure - Allows your character to join Campaigns\n")

#creates a character for the user
@bot.command()
async def create(ctx, name: str, prof: int):
        if ctx.author.name in userChar:
            await ctx.send("You already have a character!")
        else:
            if checkProfession(prof):

                profession = checkProfession(prof)
                userChar[ctx.author.name] = {
                    "name": name,
                    "profession": profession,
                    "level": 0,
                    "health": 100,
                    "inventory": "",
                    "married": False,
                    "inCombat": False
                }
                await ctx.send(f"Successfully created {name}, the {profession}!")

            else:
                await ctx.send("Your profession must be a number from 0-4:\n" 
                             "0 - No profession\n"
                             "1 - Alchemist\n"
                             "2 - Archer\n"
                             "3 - Mage\n"
                             "4 - Swordsman\n"
                             )


#renames the character
@bot.command()
async def rename(ctx, newName: str):
    if ctx.author.name in userChar:
        character = userChar[ctx.author.name]
        character["name"] = newName
        await ctx.send(f"Changed character's name to {newName}!")
    else:
        await ctx.send("You haven't made a character yet\n "
                       "Use the command !create [name] [profession (0-4)] to create one")


#rests the character back to full health
@bot.command()
async def rest(ctx):
    if ctx.author.name in userChar:
        character = userChar[ctx.author.name]
        if character["profession"] == "No profession":
            await ctx.send("")
        else:
            await ctx.channel.send(file=discord.File('Images/House.jpg'))
            character["health"] = 100
            await ctx.send(f"{character['name']} is fully rested!")
    else:
        await ctx.send("You haven't made a character yet\n "
                       "Use the command !create [name] [profession (0-4)] to create one")


#gives the character a new profession
@bot.command()
async def join(ctx, prof: int):
    if ctx.author.name in userChar:
        character = userChar[ctx.author.name]
        if character["profession"] == "No Profession":
            character["profession"] = checkProfession(prof)
            await ctx.send(f"Congratulations, {character['name']} is now a level {character['level']} {character['profession']}!")
        else:
            await ctx.send("You have to leave your current profession before joining a new one!")
    else:
        await ctx.send("You haven't made a character yet\n "
                       "Use the command !create [name] [profession (0-4)] to create one")


#allows the user to leave their profession and resets their level
@bot.command()
async def leave(ctx):
    if ctx.author.name in userChar:
        character = userChar[ctx.author.name]
        if character["profession"] == "No Profession":
            await ctx.send("Silly goose; you don't have a profession to leave!")

        else:
            await ctx.send(f"You are about to abandon your {character['profession']} profession. This will reset your level to 0. Are you sure (!yes/!no)?")
            @bot.command()
            async def yes(ctx):
                await ctx.channel.send(file=discord.File('Images/Satchel.jpg'))
                await ctx.send(f"You have left the ways of the {character['profession']}")
                character["profession"] = "No Profession"
            @bot.command()
            async def no(ctx):
                await ctx.send("A wise choice.")

    else:
        await ctx.send("You haven't made a character yet\n "
                       "Use the command !create [name] [profession (0-4)] to create one")

##CAMPAIGNS
adventurers = []

@bot.command()
async def startCampaign(ctx):
    await campaigns.beginnerCampaign(ctx)

def checkProfession(prof: int):
    if prof == 0:
        return "No Profession"
    if prof == 1:
        return "Alchemist"
    elif prof == 2:
        return "Archer"
    elif prof == 3:
        return "Mage"
    elif prof == 4:
        return "Swordsman"

##CAMPAIGNS
adventurers = []

async def injure(ctx, name, damage: int):
    character = userChar[name]
    character["health"] -= damage
    ctx.send(f"{character['name']} took {damage} damage!")
    if character["health"] >= 0:
        ctx.send(f"Aw shucks! {character['name']} died!")
        character["level"] = 0


@bot.command()
async def joinAdventure(ctx):
    global userChar
    if str(ctx.author.name) in userChar:
        global adventurers
        adventurers.append(ctx.author.name)
        await ctx.send("You've joined the adventure!")
    else:
        await ctx.send("You haven't made a character yet\n "
                       "Use the command !create [name] [profession (0-4)] to create one")


bot.run(token)
