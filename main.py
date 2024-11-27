from discord.ext import commands
import discord, os, json, asyncio

from dotenv import load_dotenv


# Globals and loading env:
load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Any useful functions:
def get_id(name: str) -> str:
    with open("./ids.json" , "r") as file:
        return json.load(file)[name]

# Initialization and commands:
bot = commands.Bot(command_prefix="!" , intents=discord.Intents().all())

@bot.event
async def on_ready():
    print("🟢 | Bot Loaded Successfully")

    await bot.tree.sync()
    
@commands.has_permissions(administrator=True)
@bot.tree.command(name="announce", description="Make an announcement")
async def announce(interaction: discord.Interaction, message: str, category: discord.CategoryChannel, delete_after: int):
    if interaction.user.guild_permissions.administrator == True:
        for channel in category.text_channels:
            if not channel.permissions_for(interaction.guild.me).send_messages:
                await interaction.response.send_message(f"I don't have permission to send messages in {channel.mention}.", ephemeral=True)
                return

        role_to_mention = interaction.guild.get_role(1311366704412098573)
        if not role_to_mention:
            await interaction.response.send_message(f"The role with ID {1311366704412098573} could not be found.", ephemeral=True)
            return

        embed = discord.Embed(
            title="📢 Announcement",
            description=message,
            color=discord.Color.blue(),
            timestamp=discord.utils.utcnow(),
        )
        embed.set_footer(text=f"Posted by {interaction.user.display_name}", icon_url=interaction.user.avatar.url)

        sent_messages = []
        for channel in category.text_channels:
            sent_message = await channel.send(content=role_to_mention.mention, embed=embed)
            sent_messages.append(sent_message)

        await interaction.response.send_message(f"Announcement posted in all channels of {category.name}.", ephemeral=True)

        if delete_after > 0:
            await asyncio.sleep(delete_after * 60)
            for sent_message in sent_messages:
                try:
                    await sent_message.delete()
                except discord.NotFound:
                    pass
    else:
        await interaction.response.send_message("Forbidden")
    
@commands.has_permissions(administrator=True)
@bot.tree.command(name="h1" , description="Show ID For H1")
async def h1(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h1')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h2" , description="Show ID For H2")
async def h2(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h2')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h3" , description="Show ID For H3")
async def h3(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h3')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h4" , description="Show ID For H4")
async def h4(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h4')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h5" , description="Show ID For H5")
async def h5(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h5')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h6" , description="Show ID For H6")
async def h6(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h6')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h7" , description="Show ID For H7")
async def h7(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h7')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h8" , description="Show ID For H8")
async def h8(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h8')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h9" , description="Show ID For H9")
async def h9(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h9')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h10" , description="Show ID For H10")
async def h10(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h10')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h11" , description="Show ID For H11")
async def h11(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h11')}**")
    else:
        await interaction.response.send_message("Forbidden")

@commands.has_permissions(administrator=True)
@bot.tree.command(name="h12" , description="Show ID For H12")
async def h12(interaction: discord.Interaction):    
    if interaction.user.guild_permissions.administrator == True:
        return await interaction.response.send_message(content=f"## **Please Add Activision ID - {get_id('h12')}**")
    else:
        await interaction.response.send_message("Forbidden")



# Running bot:
bot.run(BOT_TOKEN)