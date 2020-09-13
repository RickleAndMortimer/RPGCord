from discord.ext import commands
import discord
import asyncio
    
@commands.command()
async def beginnerCampaign(ctx):
    description = "The kingdom had begun to fail. The towers were crumbling little by little, the castle had lost its regal glow, and the royal guard’s numbers had begun to drop rapidly. "
                #+"Because of this, the royal family took it upon themselves to go to the village that they’d ruled, and find those worthy to help repair what had begun to become known as “The Broken Kingdom.”
                    #  +"The king has disguised himself and seems no more than but a simple villager, but he seeks blacksmiths, archers, mages, and swordsmen.")
    await ctx.channel.send(description)
    #PART ONE
    event_text = "The king, with his you all by his side, embarks onto the Forgotten Kingdom. You traverse a forest and find a small shack housing an old hermit. The hermit leaps forward to the party asking for some Bitcoin. "
    decision_text = "Will your party donate? 1. Yes 2. No"
    poll = await makeDecision(event_text, decision_text, ctx)
    #returns the index of the highest number in the poll
    #in other words, it chooses the most voted decision
    if poll.index(max(poll)) == 0:
        await ctx.channel.send("The old man says thank you, but one of your party members finds themselves feeling ill. -15 HP to ")
    else:
        await ctx.channel.send("The old man quietly respects your choice, and scurries away into the bushes.")

    event_text = "As you traverse the forest, you encounter a goblin encampment blocking your route. The goblins inhabiting the area are small, skinny creatures armed with wooden sticks\n"
    decision_text = "How will your party approach the encampment?\n 1. Beat up the goblins 2. Attempt diplomacy 3. Sneak around the encampment\n"

    poll = makeDecision(event_text, decision_text, ctx)

    if poll.index(max(poll)) == 0:
        await ctx.channel.send("You and your party fight the goblins. The battle wasn't very hard, but it was a valiant effort from the goblin's side as they did -5 damage to your whole party")
    elif  poll.index(max(poll)) == 1:
        await ctx.channel.send("You approach the goblins and, surprisingly, they weren't aggressive. In fact, they were very civil and fluent in their languages. Your party asks the goblins for a shortcut to the Forgotten Kingdom, and they respond by giving you a map")
    else:
        await ctx.channel.send("The old man quietly respects your choice, and scurries away into the bushes.")
    
#FUNCTIONS
async def makeDecision(event, decision, ctx):
    #sends the decision and event text to the users
    await ctx.channel.send(event)
    message = await ctx.channel.send(decision)
    #prepares a poll by adding the reactions 1 2 3 and 👍 nnnn ==orodooer 
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')
    await message.add_reaction('4️⃣')
    poll = []
    #waits 10 seconds, then counts up the reactions
    await asyncio.sleep(10)
    print("im working :)")
    reactions = message.reactions
    for reaction in reactions:
        poll.append(reaction.count) 
    return poll
