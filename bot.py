import os
import telebot
from keep_alive import keep_alive

# ទាញយក Token ពី Environment Variable ដើម្បីសុវត្ថិភាព
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'id'])
def send_user_id(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    user_tag = f"@{username}" if username else "មិនមាន"

    reply_text = (
        f"សួស្តី **{first_name}**! 👋\n\n"
        f"🆔 **User ID របស់អ្នកគឺ៖** `{user_id}`\n"
        f"👤 **Username:** {user_tag}"
    )
    bot.reply_to(message, reply_text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.forward_from:
        fwd_id = message.forward_from.id
        fwd_name = message.forward_from.first_name
        bot.reply_to(
            message, 
            f"📩 **ព័ត៌មានអ្នកផ្ញើដើម (Forwarded):**\n"
            f"ឈ្មោះ៖ {fwd_name}\n"
            f"🆔 User ID៖ `{fwd_id}`", 
            parse_mode="Markdown"
        )
    else:
        user_id = message.from_user.id
        bot.reply_to(message, f"🆔 User ID របស់អ្នកគឺ៖ `{user_id}`", parse_mode="Markdown")

keep_alive()
print("Bot កំពុងដំណើរការ...")
bot.infinity_polling()
