from discord import extentions.Commands
import discord

adventurers = list()

description = "The kingdom had begun to fail. The towers were crumbling little by little, the castle had lost its regal glow, and the royal guard’s numbers had begun to drop rapidly. "
                  +"Because of this, the royal family took it upon themselves to go to the village that they’d ruled, and find those worthy to help repair what had begun to become known as “The Broken Kingdom.”
                  +"The king has disguised himself and seems no more than but a simple villager, but he seeks blacksmiths, archers, mages, and swordsmen."


#PART ONE
event_text = "The king, with his you all by his side, embarks onto the Forgotten Kingdom. You traverse a forest and find a small shack housing an old hermit. The hermit leaps forward to the party asking for some Bitcoin. "
decision_text = "Will your party donate? 1. Yes 2. No"
poll = makeDecision("Will your party donate? 1. Yes 2. No")

if poll.index(max(poll)) == 0:
    adventurer = random.choice(adventurers)
    sendOutcome("The old man says thank you, but one of your party members finds themselves feeling ill. -15 HP to " + adventurer.name)
    adventurer.hp -= 15
else  poll.index(max(poll)) == 1:
    sendOutome("The old man quietly respects your choice, and scurries away in the bushes.")

event_text = "As you traverse the forest, you encounter a goblin encampment blocking your route. The goblins inhabiting the area are small, skinny creatures armed with wooden sticks\n" +
 + "How will your party approach the encampment\n" + 
decision_text = "1. Beat up the goblins 2. Attempt diplomacy 3. Sneak around the encampment\n"

poll = makeDecision(event_text, decision_text)


#PART TWO

#FUNCTIONS
async def makeDecision(event,decision):
#TODO: get reactions from discord
    await ctx.channel.send(decision)
    message = await ctx.channel.send(decision)
    vote_1 = get(message.reactions, emoji="one emoji").count
    vote_2 = get(message.reactions, emoji="two emoji").count
    vote_3 = get(message.reactions, emoji="three emoji").count
    vote_4 = get(message.reactions, emoji="four emoji").count
    return {vote_1, vote_2, vote_3, vote_4}

async def sendOutcome(message):
    await ctx.channel.send(message)
    
