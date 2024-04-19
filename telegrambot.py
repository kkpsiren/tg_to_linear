import os
from telegram import Update
from telegram.ext import (
    CommandHandler,
    filters,
    ContextTypes,
    Application,
)
import json
from dotenv import load_dotenv

load_dotenv()

from linear import create_issue
from queries import ALL_USERS

API_KEY = os.environ.get("TG_API_KEY")
BOT_NAME = os.environ.get("BOT_NAME")
# URL = os.environ.get("URL")
# ORB_ACCESS_TOKEN = os.environ.get("ORB_ACCESS_TOKEN")
# ORB_URL = os.environ.get("ORB_URL")
ALLOWED_USERS = [item["tgid"] for item in ALL_USERS]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    await update.message.reply_text(f"Hello @{username}, I'm {BOT_NAME}!")


async def create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    username = update.message.from_user.username
    user_id = update.message.from_user.id

    message_id = update.message.message_id
    chat_username = update.message.chat.username

    # Construct message URL for public groups and channels
    message_id = update.message.message_id
    chat_id = update.message.chat_id

    message_text = f'Please search for "message ID {message_id}" in this group to find the message.'

    if username not in ALLOWED_USERS:
        await update.message.reply_text(f"You're not allowed to create issues")
        return

    data = text.replace("  ", " ").split(" ", maxsplit=2)
    assignee = data[1]
    description = data[2]

    obj = {
        "assignee": assignee.split(",")[0],
        "users": assignee.split(","),
        "title": description[:42] + "...",
        "description": description + f"\n\n{message_text}",
        "priority": 0,
    }
    sent_message = await update.message.reply_text(f"creating issue... {message_text}")
    try:
        r = create_issue(**obj)
        if "errors" in r:
            await context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=sent_message.message_id,
                text=f"Failed to create issue: {json.dumps(r)}",
            )
        else:
            url = r["data"]["issueCreate"]["issue"]["url"]
            await context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=sent_message.message_id,
                text=f"✅ Issue created: {url}" + f"\n\n\n\n{message_text}",
            )
    except Exception as e:
        # Handle any exceptions and update the message
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=sent_message.message_id,
            text="An error occurred while creating the issue.",
        )


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update "{update}" caused error "{context.error}')


if __name__ == "__main__":
    print("starting...")
    app = Application.builder().token(API_KEY).build()

    # commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("create", create, filters=filters.TEXT))

    # message
    # app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # error
    app.add_error_handler(error)

    print("running...")
    app.run_polling(poll_interval=3)
