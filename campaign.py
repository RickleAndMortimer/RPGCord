from discord.ext import commands
import discord
import asyncio
import random

timer = 60
campaign_running = False

@commands.command()
async def beginnerCampaign(ctx):
    await ctx.channel.send(f"{timer} SECONDS TO JOIN THE ADVENTURE\n"
                           f"JOIN USING !joinAdventure")
    campaign_running = True
    await asyncio.sleep(timer)
    campaign_running = False
    description = "The kingdom had begun to fail. The towers were crumbling little by little, the castle had lost its regal glow, and the royal guard’s numbers had begun to drop rapidly. "
    # "Because of this, the royal family took it upon themselves to go to the village that they’d ruled, and find those worthy to help repair what had begun to become known as “The Forgotten Kingdom.”
    # "The king has disguised himself and seems no more than but a simple villager, but he seeks blacksmiths, archers, mages, and swordsmen.")
    await ctx.channel.send(description)
    await asyncio.sleep(10)
    # PART ONE

    # returns the index of the highest number in the poll
    # in other words, it chooses the most voted decision
    skip = False
    event_text = "The king, with you all by his side, embarks into the Lost Kingdom. " \
                 "You traverse a forest and find a small shack housing an old hermit. The hermit leaps forward to the party asking for some coin. "
    decision_text = "Will your party donate?\n" \
                    " 1. Yes 2. No"
    max = await makeDecision(event_text, decision_text, 2, ctx)
    # returns the index of the highest number in the poll
    # in other words, it chooses the most voted decision
    if max == 0:
        await ctx.channel.send(
            "The old man says thank you, but one of your party members finds themselves feeling ill.")
    else:
        await ctx.channel.send("The old man quietly respects your choice, and scurries away into the bushes.")

    await asyncio.sleep(10)
    await ctx.channel.send(file=discord.File('Images/Forest.jpg'))
    event_text = "As you traverse the forest, you encounter a goblin encampment blocking your route. " \
                 "The goblins inhabiting the area are small, skinny creatures armed with wooden sticks\n"
    decision_text = "How will your party approach the encampment?\n 1. Beat up the goblins " \
                    "2. Attempt diplomacy 3. Sneak around the encampment\n"

    max = await makeDecision(event_text, decision_text, 3, ctx)

    if max == 0:
        await ctx.channel.send(
            "Your party fought the goblins. The battle wasn't very hard, but it was a valiant effort "
            "from the goblin's side as they landed a few punches on everyone in the party.")
    elif max == 1:
        event_text = "Your party approached the goblins and, surprisingly, they weren't aggressive. In fact, " \
                     "they were very civil and fluent in their languages. Your party asks the goblins for a " \
                     "shortcut to the Forgotten Kingdom, and they respond by giving you a map."
        decision_text = "Does your party wish to follow the map?\n" \
                        "1. Yes 2. No"
        max = await makeDecision(event_text, decision_text, 2, ctx)
        if max == 0:
            await ctx.channel.send(file=discord.File('Images/Map.jpg'))
            await ctx.channel.send(f"Your party follows the map. The map tells them to go through a graveyard. "
                             f"Surprisingly, no danger was there.")
            skip = True
        else:
            await ctx.channel.send("Your party does not use the map")
    else:
        await ctx.channel.send("You snuck around the goblins successfully.")

    if (skip == False):
        await asyncio.sleep(10)
        await ctx.channel.send(file=discord.File('Images/Witch.jpg'))
        event_text = "Going straight forward, you enter a swamp. The area is grimy and full of muck. A witch flies into your locations. Aggression can be felt from her presence"
        decision_text = "What will the party do? 1. Fight the witch 2. Try to escape"
        max = await makeDecision(event_text, decision_text, 2, ctx)
        if max == 0:
            await ctx.channel.send(
                "Your party fights the witch. It was not an easy fight, but the witch succumbed to your combined strength. -30 HP for the whole party")
        elif max == 1:
            await ctx.channel.send(
                "Your party manages to flee, but the witch casta a spell right before you elude her vision. Everyone gets randomized HP")

    await asyncio.sleep(timer)
    event_text = "Your party makes it to the Lost Kingdom! An impoverished but quaintly dressed figure approaches you. 'It is me, the king of the Lost Kingdom!' he exclaims. "
    decision_text = "What will the party do? 1. Fight the man 2. Ask for coin 3. Ask him to leave"
    max = await makeDecision(event_text, decision_text, 3, ctx)
    if max == 0:
        await ctx.channel.send("With one swift blow, you take out the king of the Lost Kingdom. It is done.")
    elif max == 1:
        await ctx.channel.send(
            "Seeing that the party has no coin, the king of the Lost Kingdom donates 500 coin to your party. As your party returns home, the king accepts the end of his monarchy. The End.")
    elif max == 2:
        await ctx.channel.send(
            "The king of the Lost Kingdom at first vehemently refuses. However, after explaining that the monarchy is suffering because of his actions,"
            " the king of the Lost Kingdom leaves. No one dies and every lives a happy ending. The end")


# FUNCTIONS
async def makeDecision(event, decision, num: int, ctx):
    # sends the decision and event text to the users
    await ctx.channel.send(event)
    message = await ctx.channel.send(decision)
    poll = []
    emoji = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
    eIndex = 0
    while num > 0:
        await message.add_reaction(emoji[eIndex])
        eIndex += 1
        num -= 1

    # waits 60 seconds, then counts up the reactions
    await asyncio.sleep(timer)
    cacheMessage = await ctx.channel.fetch_message(message.id)
    reactions = cacheMessage.reactions
    for reaction in reactions:
        print(f"reaction count:{reaction.count}")
        poll.append(reaction.count)
    index = 0
    maxIndex = 0
    max = 0
    print(len(poll))
    while index < len(poll):
        if poll[index] > max:
            maxIndex = index
            max = poll[index]
        index += 1
    print(maxIndex)
    return maxIndex
