from dotenv import load_dotenv
load_dotenv()
import os
from pyrogram import Client, filters
import yt_dlp
from dotenv import load_dotenv

# Load env
load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

print("API_ID:", api_id)
print("API_HASH:", api_hash)
print("BOT_TOKEN:", bot_token)

app = Client("downloader_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "ketik atau klik ini /help jika ingin langsung menggunakan bot ini.\n"
        "Perkenalkan saya adalah @Moonarck developer dari bot @Cloudiva.\n"
        "Bot ini bisa apa? coba tekan di bawah ini /help\n"
        "-\n"
        "Dev: @Moonarck\n"
        "Project : Bot Telegram / @Cloudiva\n"
        "Awal Pembuatan: 10 March 2025."
    )

@app.on_message(filters.text & filters.private)
async def download_video(client, message):
    url = message.text

    if "youtube.com" in url or "youtu.be" in url or "tiktok.com" in url:
        await message.reply_text("Sabar suki, lagi download...")

        ydl_opts = {
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "format": "best",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await client.send_video(message.chat.id, filename, caption="Nih videonya, :).")
        os.remove(filename)
    else:
        await message.reply_text("Ajg, kirim link YouTube atau TikTok yang bener!")

        print("Bot started...")

app.run()
