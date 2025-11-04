import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Get bot token from environment variable (set this in Render)
BOT_TOKEN = os.environ.get('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /start command - send image with join link
    """
    # Your new image URL and join link
    image_url = "https://freeimage.host/i/KQbXdoF"
    join_link = "https://t.me/+eabn_K2wO6kwNjQ9"
    
    # Create caption with the join link
    caption = (
        "Welcome! 🎉\n\n"
        "Join our community here:\n"
        f"{join_link}"
    )
    
    # Send the image with caption
    await update.message.reply_photo(
        photo=image_url,
        caption=caption
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command"""
    help_text = (
        "Available commands:\n"
        "/start - Start the bot and get welcome message\n"
        "/help - Show this help message\n"
        "/join - Get the join link"
    )
    await update.message.reply_text(help_text)

async def join_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /join command"""
    join_link = "https://t.me/+eabn_K2wO6kwNjQ9"
    await update.message.reply_text(f"Join our community: {join_link}")

def main():
    """Start the bot"""
    # Create Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("join", join_command))
    
    # Start polling
    print("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
