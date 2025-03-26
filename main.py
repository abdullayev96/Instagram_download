from TikTokAPI import TikTokAPI
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters



tik = TikTokAPI(language='en', region='IN', cookie=None)
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, bot
from telegram.ext import *
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def getvid(link):
    try:
        link = link.split("/video/")[1].split("?")[0]
    except:
        return False
    tik.downloadVideoById(link, "new/1.mp4")
    return True

# try to download before bot start .. no problems
getvid("https://www.tiktok.com/@2r_9a/video/7059793616004238593?is_copy_url=1&is_from_webapp=v1")


def msghandler(update: Update, context: CallbackContext) -> None:

    text = str(update.message.text).lower()
    if getvid(str(text)):
        update.message.reply_text("Sending video")
    else:
        update.message.reply_text("Wrong Link")


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me Tiktok link')


def main() -> None:
    updater = Updater("5154205801:AAGHjmTYxCyhEsLhdH9PulGFTrCvIrUCpM4")
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, msghandler))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()



########  no work
import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "6895917982:AAGJl8FZPiaUTPsP2eyJdiUtf_9QdwLU87g"

# Configure logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


async def start(update: Update, context):
    print(update.message.reply_text("hello"))
    await update.message.reply_text("Send me a TikTok video link, and I'll download it for you!")




async def download_tiktok(update: Update, context):
    url = update.message.text.strip()

    if "tiktok.com" not in url:
        await update.message.reply_text("Please send a valid TikTok URL.")
        return

    await update.message.reply_text("Downloading video, please wait...")

    try:
        # Using TikWM API (a better alternative)
        api_url = f"https://www.tikwm.com/api/?url={url}"
        response = requests.get(api_url)
        data = response.json()

        if data.get("data") and data["data"].get("play"):
            video_url = data["data"]["play"]

            # Send the video to the user
            await context.bot.send_video(chat_id=update.effective_chat.id, video=video_url,
                                         caption="Here is your TikTok video!")
        else:
            await update.message.reply_text("Failed to download the video. Try another link.")
    except Exception as e:
        logging.error(e)
        await update.message.reply_text("An error occurred. Please try again later.")


def main():
    print("Bot is starting...")

    app = Application.builder().token(TOKEN).build()
    print(app, "yes")

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_tiktok))

    print("Bot is running...")  # Confirm the bot is running
    app.run_polling()


if __name__ == "__main__":
    main()



# import logging
# import requests
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters
#
#
# TOKEN = "6895917982:AAGJl8FZPiaUTPsP2eyJdiUtf_9QdwLU87g"
#
# # Configure logging
# logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
#
#
# async def start(update: Update, context):
#     print("hello bot ")
#     await update.message.reply_text("Send me a TikTok video link, and I'll download it for you!")
#
#
# async def download_tiktok(update: Update, context):
#     url = update.message.text.strip()
#
#     if "tiktok.com" not in url:
#         await update.message.reply_text("Please send a valid TikTok URL.")
#         return
#
#     await update.message.reply_text("Downloading video, please wait...")
#
#     # Using SnapTik API (or any other service)
#     try:
#         response = requests.get(f"https://api.tikmate.app/api/lookup?url={url}")
#         data = response.json()
#
#         if "videoUrl" in data:
#             video_url = data["videoUrl"]
#
#             # Send the video to the user
#             await context.bot.send_video(chat_id=update.message.chat_id, video=video_url,
#                                          caption="Here is your TikTok video!")
#         else:
#             await update.message.reply_text("Failed to download the video. Try another link.")
#     except Exception as e:
#         logging.error(e)
#         await update.message.reply_text("An error occurred. Please try again later.")
#
#
# def main():
#     app = Application.builder().token(TOKEN).build()
#
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_tiktok))
#
#     print("Bot is running...")
#     app.run_polling()
#
#
# if __name__ == "__main__":
#     main()
