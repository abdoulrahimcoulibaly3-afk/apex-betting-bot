import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.environ["BOT_TOKEN"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚽ Pronostics Gratuits", callback_data="free")],
        [InlineKeyboardButton("🎰 Casino", callback_data="casino")],
        [InlineKeyboardButton("💎 VIP", callback_data="vip")],
        [InlineKeyboardButton("🎁 Bonus", callback_data="bonus")],
        [InlineKeyboardButton("📊 Résultats", callback_data="resultats")],
        [InlineKeyboardButton("📞 Support", callback_data="contact")],
    ]

    await update.message.reply_text(
        "🏆 Bienvenue sur APEX BETTING\n\nChoisissez une option :",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "free": "⚽ Pronostics gratuits disponibles prochainement.",
        "casino": "🎰 Découvrez nos jeux de casino partenaires.",
        "vip": "💎 Rejoignez notre offre VIP.",
        "bonus": "🎁 Consultez les bonus disponibles.",
        "resultats": "📊 Résultats publiés régulièrement.",
        "contact": "📞 Support : @ApexBettingSupport",
    }

    await query.edit_message_text(messages.get(query.data, "Option inconnue."))


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("Bot lancé...")

app.run_polling()
