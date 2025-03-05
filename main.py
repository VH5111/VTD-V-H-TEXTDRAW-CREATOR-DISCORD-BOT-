# =============================================================================
# CODE MADE BY V H CODES FOR DEVELOPERS CAFE
# LINK: https://discord.gg/AeGuFxBAnc
# GIVE CODE CREDITS TO V H OR OWNER WILL GET NOTIFY
#YOUR CODE WILL IRRUPTED
#This Is the Verison VTD v1.1
#Unauthorized copying, modification, distribution, or use without permission is strictly prohibited
#Join Our server for more updates and Enjoy The code!
# =============================================================================

import discord
from discord.ext import commands
from discord.ui import View, Button, Select
import io
import asyncio
from datetime import datetime

TOKEN = "YOUR DISCORD BOT TOKEN HERE"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("\n" + "="*30)
    print("LOADING V H CODES......")
    print("="*30)

    # Wait for 10 seconds before printing "V H OP"
    await asyncio.sleep(10)

    print("="*30)
    print("V H OP")
    print("="*30)
    print(f"{bot.user.name} BOT ADDED TO V H'S DATABASE ")
    print("="*30)

# Set bot status to "Streaming" with a YouTube link
    youtube_link = "https://youtube.com/@v_h_5111?si=JQTgK7korTylOqQE"  # Replace with your YouTube live link
    activity = discord.Streaming(name="DEVELOPER V H#5111", url=youtube_link)
    await bot.change_presence(activity=activity)

class TextDrawEditor(View):
    def __init__(self, user_id, channel_id):
        super().__init__(timeout=None)
        self.user_id = user_id
        self.channel_id = channel_id
        self.x = 320
        self.y = 240
        self.text = "Sample Text"
        self.font_size = 2
        self.image_url = None
        self.pwn_generated = False  

    def generate_pawn_code(self):
        return f"""
new Text:myTextDraw;

public OnGameModeInit()
{{
    myTextDraw = TextDrawCreate({self.x:.1f}, {self.y:.1f}, "{self.text}");
    TextDrawFont(myTextDraw, {self.font_size});
    TextDrawColor(myTextDraw, 0xFFFFFFAA);
    TextDrawSetOutline(myTextDraw, 1);
    TextDrawShowForAll(myTextDraw);
}}
"""

    async def update_message(self, interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message(
                "<a:wrong_monu:926092508260347905> You are not allowed to do this.", ephemeral=True
            )
            return

        preview = f"**Text:** {self.text}\n**Position:** ({self.x}, {self.y})\n**Font Size:** {self.font_size}"
        embed = discord.Embed(title="V H TextDraw Editor <:replit:926097723604762634> Preview", description=preview, color=discord.Color.blue())

        if self.image_url:
            embed.set_image(url=self.image_url)

        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="⬆️ Up", style=discord.ButtonStyle.primary)
    async def move_up(self, interaction: discord.Interaction, button: Button):
        await self.update_message(interaction)
        if interaction.user.id == self.user_id:
            self.y -= 5
            self.pwn_generated = True

    @discord.ui.button(label="⬅️ Left", style=discord.ButtonStyle.primary)
    async def move_left(self, interaction: discord.Interaction, button: Button):
        await self.update_message(interaction)
        if interaction.user.id == self.user_id:
            self.x -= 5
            self.pwn_generated = True

    @discord.ui.button(label="➡️ Right", style=discord.ButtonStyle.primary)
    async def move_right(self, interaction: discord.Interaction, button: Button):
        await self.update_message(interaction)
        if interaction.user.id == self.user_id:
            self.x += 5
            self.pwn_generated = True

    @discord.ui.button(label="⬇️ Down", style=discord.ButtonStyle.primary)
    async def move_down(self, interaction: discord.Interaction, button: Button):
        await self.update_message(interaction)
        if interaction.user.id == self.user_id:
            self.y += 5
            self.pwn_generated = True

    @discord.ui.button(label="Export as .pwn", style=discord.ButtonStyle.success)
    async def export_pwn(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message(
                "<a:wrong_monu:926092508260347905> You are not allowed to do this.", ephemeral=True
            )
            return

        if not self.pwn_generated:
            await interaction.response.send_message("⚠️ Edit your textdraw before exporting!", ephemeral=True)
            return

        pawn_code = self.generate_pawn_code()
        file = discord.File(io.BytesIO(pawn_code.encode()), filename="vhop.pwn")
        await interaction.user.send("<a:PINED_CAFE:926097736690962482> Here is your updated `.pwn` file:<:VH_OP:935801670368129075>", file=file)
        await interaction.response.send_message("<a:tick_monu:926097657972265010> Exported and sent to your DM!", ephemeral=True)

@bot.command()
async def start(ctx):
    if ctx.guild is None:
        return await ctx.send("<a:wrong_monu:926092508260347905> This command can only be used in a server!")

    bot.last_command_user = ctx.author.id  
    view = TextDrawEditor(ctx.author.id, ctx.channel.id)
    embed = discord.Embed(title="TextDraw Editor", description="Use the buttons to adjust your textdraw.", color=discord.Color.blue())
    await ctx.send(embed=embed, view=view)

@bot.command()
async def settext(ctx, *, new_text: str):
    if ctx.guild is None:
        return await ctx.send("<a:wrong_monu:926092508260347905> This command can only be used in a server!")

    if ctx.author.id != bot.last_command_user:
        return await ctx.send("<a:wrong_monu:926092508260347905> You are not allowed to do this.")

    view = TextDrawEditor(ctx.author.id, ctx.channel.id)
    view.text = new_text
    view.pwn_generated = True  
    embed = discord.Embed(title="Text Updated", description=f"New text: `{new_text}`", color=discord.Color.green())
    await ctx.send(embed=embed, view=view)

@bot.command()
async def upload(ctx):
    if ctx.guild is None:
        return await ctx.send("<a:wrong_monu:926092508260347905> This command can only be used in a server!")

    bot.last_upload_channel = ctx.channel.id
    bot.last_command_user = ctx.author.id  
    await ctx.send("📸 Upload a **PNG** image to use as a textdraw in this channel.<a:DCAFE_TIME:926098767030124544>")

@bot.event
async def on_message(message):
    if message.guild is None:
        return  

    if message.attachments:
        if not hasattr(bot, "last_upload_channel") or message.channel.id != bot.last_upload_channel:
            return  

        if message.author.id != bot.last_command_user:
            await message.channel.send("<a:wrong_monu:926092508260347905> You are not allowed to do this.")
            return

        attachment = message.attachments[0]
        if not attachment.filename.lower().endswith(".png"):
            await message.channel.send("<a:wrong_monu:926092508260347905> Please upload a valid **PNG** file!")
            return

        view = TextDrawEditor(message.author.id, message.channel.id)
        view.image_url = attachment.url
        view.pwn_generated = True
        embed = discord.Embed(title="TextDraw Image Set", description="<a:tick_monu:926097657972265010> Your uploaded image is now the textdraw.", color=discord.Color.blue())
        embed.set_image(url=attachment.url)
        await message.channel.send(embed=embed, view=view)

    await bot.process_commands(message)

from discord import SelectOption

@bot.command(name="help_menu")
async def help_menu(ctx):
    if ctx.guild is None:
        return await ctx.send("<a:wrong_monu:926092508260347905> This command can only be used in a server!")

    bot.last_command_user = ctx.author.id  

    msg = await ctx.send("```SA-MP Server Starting...```")
    await asyncio.sleep(1)

    loading_messages = [
        "[10:00:01] Loading plugins...",
        "[10:00:02] Initializing scripts...",
        "[10:00:03] Connecting to database...",
        "[10:00:04] Setting up game environment...",
        "[10:00:05] Almost ready..."
    ]

    for line in loading_messages:
        await asyncio.sleep(1)
        await msg.edit(content=f"```{line}```")

    await asyncio.sleep(1)
    await msg.edit(content="```WELCOME TO V H CODES```")

    # Animated emojis (replace with actual emoji names & IDs)
    start_emoji = "<a:SAMPDCAFE:926097698103394386>"
    settext_emoji = "<a:DCAFE_WELCOME:926098716820140062>"
    upload_emoji = "<a:LOADING_3:926098041637863484>"
    export_emoji = "<a:DCAFE_MUSICS:930083000740356096>"

    # Create Help Menu
    embed = discord.Embed(title="<a:IDIVETTU_DCAFE:926098186072891392> V H SA-MP TEXTDRAW EDITOR <a:IDIVETTU_DCAFE:926098186072891392>", description="Select an option below:", color=discord.Color.blue())
    view = View()

    select = Select(placeholder="Choose an option...", options=[
        SelectOption(label="Start Editor", description="Start the textdraw editor", value="start", emoji=start_emoji),
        SelectOption(label="Set Text", description="Change the textdraw text", value="settext", emoji=settext_emoji),
        SelectOption(label="Upload Image", description="Upload a PNG image for the textdraw", value="upload", emoji=upload_emoji),
        SelectOption(label="Export", description="Export the textdraw as .pwn", value="export", emoji=export_emoji)
    ])

    async def callback(interaction: discord.Interaction):
        if interaction.user.id != bot.last_command_user:
            await interaction.response.send_message("<a:wrong_monu:926092508260347905> You are not allowed to do this.", ephemeral=True)
            return

        command = select.values[0]
        if command == "start":
            await ctx.invoke(bot.get_command("start"))
        elif command == "settext":
            await ctx.send("Use `!settext <your text>` to change the text.")
        elif command == "upload":
            await ctx.invoke(bot.get_command("upload"))
        elif command == "export":
            await ctx.send("Use the **Export** button in the editor to save your textdraw.")
        await interaction.response.defer()

    select.callback = callback
    view.add_item(select)

    await msg.edit(content="", embed=embed, view=view)
    await ctx.send("**CODED BY<a:DEV_VH:926095137438838835>V H#5111 FOR DEVELOPERS CAFE**\nJOIN THE [DCAFE](https://discord.gg/AeGuFxBAnc) <:DCAFE:930896522722304060>FOR SUPPORT")

bot.run(TOKEN)
