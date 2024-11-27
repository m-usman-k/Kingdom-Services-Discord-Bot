import discord, os, json
from discord.ext import commands

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
    

@bot.tree.command(name="h1" , description="Show ID For H1")
async def h1(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h1')}**")


@bot.tree.command(name="h2" , description="Show ID For H2")
async def h2(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h2')}**")


@bot.tree.command(name="h3" , description="Show ID For H3")
async def h3(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h3')}**")


@bot.tree.command(name="h4" , description="Show ID For H4")
async def h4(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h4')}**")


@bot.tree.command(name="h5" , description="Show ID For H5")
async def h5(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h5')}**")


@bot.tree.command(name="h6" , description="Show ID For H6")
async def h6(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h6')}**")


@bot.tree.command(name="h7" , description="Show ID For H7")
async def h7(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h7')}**")


@bot.tree.command(name="h8" , description="Show ID For H8")
async def h8(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h8')}**")


@bot.tree.command(name="h9" , description="Show ID For H9")
async def h9(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h9')}**")


@bot.tree.command(name="h10" , description="Show ID For H10")
async def h10(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h10')}**")


@bot.tree.command(name="h11" , description="Show ID For H11")
async def h11(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h11')}**")


@bot.tree.command(name="h12" , description="Show ID For H12")
async def h12(interaction: discord.Interaction):    
    return await interaction.response.send_message(content=f"# **Please Add Activision ID - {get_id('h12')}**")



# Running bot:
bot.run(BOT_TOKEN)