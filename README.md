# VTD Discord Bot Code Version 1.1  

![VTD Bot Banner](https://media.discordapp.net/attachments/1343165330046062595/1346924972249059348/InShot_20250306_002729171.jpg?ex=67c9f522&is=67c8a3a2&hm=aa5552a64e7fefad1ff344ac8e9701cd6f8001efa3a2b3dc1e11b0068a636226&)  

## 📌 About  
VTD Discord Bot is a **SA-MP TextDraw editor** that enables users to create, modify, and export TextDraws directly from a Discord channel. This bot provides real-time text and image adjustments, making TextDraw creation easier and faster.  

### ✨ Preview  
![TextDraw Example](https://media.discordapp.net/attachments/1343165330046062595/1346928132032172209/1741200529421.png?ex=67c9f813&is=67c8a693&hm=c7c4bbab9719f698dfadee5ed1245804f3edad3fe12fbf8b2533492f91c9fc83&)  

## 🚀 Features  
✅ **Interactive TextDraw Editor** – Move, resize, and edit TextDraws easily.  
✅ **Image Upload Support** – Upload PNG images to use as TextDraw backgrounds.  
✅ **Alignment & Formatting** – Change text size, color, and font.  
✅ **Live Previews** – See real-time updates in Discord.  
✅ **Export to PAWN** – Download TextDraws as `.pwn` files.  
✅ **Help Menu** – Easy-to-use interactive help command.  

## 🛠️ Installation  

### 1️⃣ Prerequisites  
- **Python 3.8+** installed  
- A **Discord bot token** from [Discord Developer Portal](https://discord.com/developers/applications)  
- **pip** (Python package manager)  

### 2️⃣ Setup Instructions  
1. **Clone the repository:**  
   ```sh
   git clone https://github.com/YOUR-GITHUB-USERNAME/VTD-DISCORD-BOT.git
   cd VTD-DISCORD-BOT
   ```  
2. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```  
3. **Configure environment variables:**  
   - Create a `.env` file in the root directory  
   - Add the following lines:  
     ```sh
     BOT_TOKEN=your-discord-bot-token
     ```  
4. **Run the bot:**  
   ```sh
   python bot.py
   ```  

## 🔧 Commands  
| Command | Description |  
|---------|------------|  
| `!start` | Start the TextDraw editor |  
| `!settext [text]` | Change TextDraw text |  
| `!upload` | Upload an image for TextDraw |  
| `!move [direction] [pixels]` | Move TextDraw position |  
| `!export` | Export the TextDraw as `.pwn` file |  
| `!help_menu` | Open the interactive help menu |  

### 🎮 Example Usage  
1. **Creating a TextDraw:**  
   ```sh
   !start
   !settext "Hello SA-MP!"
   !move right 10
   !export
   ```  

2. **Adding an Image:**  
   ```sh
   !upload (Attach an image)
   ```  

## 🖼️ Screenshots  
![Screenshot 1](your-image-url.png)  
![Screenshot 2](your-image-url.png)  

## 📜 License  
This project is licensed under the **MIT License**.  

## 📬 Contact  
Join our **Discord Server** for support: [Developers Café](https://discord.gg/AeGuFxBAnc)  

---
Made by **V H Codes** for **Developers Café**.  
