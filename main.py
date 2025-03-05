import discord
from discord.ext import commands
from discord.ui import View, Button, Select
import io
import asyncio
from datetime import datetime

TOKEN = "MTM0NjQ2MTMxNTc0MDIwNTE0Nw.GZ8r6s.zGjsjwu6ck4a1U3ri3dkfqTQHGzswjCBUeZecQ"

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

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
        self.pwn_generated = False  # Prevents auto-export before editing

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
        preview = f"**Text:** {self.text}\n**Position:** ({self.x}, {self.y})\n**Font Size:** {self.font_size}"
        embed = discord.Embed(title="V H TextDraw Editor 🛠️ Preview", description=preview, color=discord.Color.blue())

        if self.image_url:
            embed.set_image(url=self.image_url)

        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="⬆️ Up", style=discord.ButtonStyle.primary)
    async def move_up(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id == self.user_id:
            self.y -= 5
            self.pwn_generated = True
            await self.update_message(interaction)

    @discord.ui.button(label="⬅️ Left", style=discord.ButtonStyle.primary)
    async def move_left(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id == self.user_id:
            self.x -= 5
            self.pwn_generated = True
            await self.update_message(interaction)

    @discord.ui.button(label="➡️ Right", style=discord.ButtonStyle.primary)
    async def move_right(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id == self.user_id:
            self.x += 5
            self.pwn_generated = True
            await self.update_message(interaction)

    @discord.ui.button(label="⬇️ Down", style=discord.ButtonStyle.primary)
    async def move_down(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id == self.user_id:
            self.y += 5
            self.pwn_generated = True
            await self.update_message(interaction)

    @discord.ui.button(label="Export as .pwn", style=discord.ButtonStyle.success)
    async def export_pwn(self, interaction: discord.Interaction, button: Button):
        if interaction.user.id == self.user_id:
            if not self.pwn_generated:
                await interaction.response.send_message("⚠️ You must edit your textdraw before exporting!", ephemeral=True)
                return

            pawn_code = self.generate_pawn_code()
            file = discord.File(io.BytesIO(pawn_code.encode()), filename="vhop.pwn")
            await interaction.user.send("📜 Here is your exported `.pwn` file:", file=file)
            await interaction.response.send_message("✅ Exported and sent to your DM!", ephemeral=True)

@bot.command()
async def start(ctx):
    if ctx.guild is None:
        return await ctx.send("❌ This command can only be used in a server!")

    view = TextDrawEditor(ctx.author.id, ctx.channel.id)
    embed = discord.Embed(title="TextDraw Editor", description="Use the buttons to adjust your textdraw.", color=discord.Color.blue())
    await ctx.send(embed=embed, view=view)

@bot.command()
async def settext(ctx, *, new_text: str):
    if ctx.guild is None:
        return await ctx.send("❌ This command can only be used in a server!")

    view = TextDrawEditor(ctx.author.id, ctx.channel.id)
    view.text = new_text
    view.pwn_generated = True  # Mark changes made
    embed = discord.Embed(title="Text Updated", description=f"New text: `{new_text}`", color=discord.Color.green())
    await ctx.send(embed=embed, view=view)

@bot.command()
async def upload(ctx):
    if ctx.guild is None:
        return await ctx.send("❌ This command can only be used in a server!")

    await ctx.send("📸 Upload a **PNG** image to use as a textdraw in this channel.")

@bot.event
async def on_message(message):
    if message.guild is None:
        return  # Ignore DMs

    if message.attachments:
        attachment = message.attachments[0]
        if not attachment.filename.lower().endswith(".png"):
            await message.channel.send("❌ Please upload a valid **PNG** file!")
            return

        view = TextDrawEditor(message.author.id, message.channel.id)
        view.image_url = attachment.url
        view.pwn_generated = True  # Mark changes made
        embed = discord.Embed(title="TextDraw Image Set", description="✅ Your uploaded image is now the textdraw.", color=discord.Color.blue())
        embed.set_image(url=attachment.url)
        await message.channel.send(embed=embed, view=view)

    await bot.process_commands(message)

@bot.command(name="help_menu")
async def help_menu(ctx):
    if ctx.guild is None:
        return await ctx.send("❌ This command can only be used in a server!")

    def get_time():
        return datetime.now().strftime("[%H:%M:%S]")

    msg = await ctx.send(f"```{get_time()} SA-MP Server Starting...```")
    await asyncio.sleep(0.5)

    fake_loading = [
        "Initializing...",
        "Loading assets...",
        "Applying configurations...",
        "Setting up modules...",
        "Almost done..."
    ]

    for line in fake_loading:
        await asyncio.sleep(0.5)
        await msg.edit(content=f"```{msg.content.strip('```')}\n{get_time()} {line}```")

    await asyncio.sleep(0.5)
    await msg.edit(content=f"```{get_time()} Welcome to V H Codes```")
    await asyncio.sleep(1)

    embed = discord.Embed(title="<:VH_OP:935801670368129075> V H TextDraw Editor Help Menu <:VH_OP:935801670368129075>", description="Select an option below:", color=discord.Color.blue())
    view = View()

    select = Select(placeholder="Choose an option...", options=[
        discord.SelectOption(label="Start Editor", description="Start the textdraw editor", value="start"),
        discord.SelectOption(label="Set Text", description="Change the textdraw text", value="settext"),
        discord.SelectOption(label="Upload Image", description="Upload a PNG image for the textdraw", value="upload"),
        discord.SelectOption(label="Export", description="Export the textdraw as .pwn", value="export")
    ])

    async def callback(interaction: discord.Interaction):
        if interaction.user != ctx.author:
            await interaction.response.send_message("❌ You can't edit someone else's textdraw!", ephemeral=True)
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

    await ctx.send("**CODED BY<a:DEV_VH:926095137438838835>V H#5111 FOR DEVELOPERS CAFE**\nJOIN<:DCAFE:930896522722304060>THE [DCAFE](https://discord.gg/AeGuFxBAnc) FOR SUPPORT")

bot.run(TOKEN)
