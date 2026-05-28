import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8957268369:AAH9l6bAilO_K76F9Zx5s0BwTkVWOKEXMjc"

def prendi_menu():

    url = "https://www.ristoranteperche.com/menu-del-giorno-pranzo"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    testo = soup.get_text("\n")

    righe = [
        r.strip()
        for r in testo.split("\n")
        if len(r.strip()) > 3
    ]

    menu = "\n".join(righe[:25])

    return menu


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    testo_menu = prendi_menu()

    messaggio = f"🍝 MENU DEL GIORNO\n\n{testo_menu}"

    await update.message.reply_text(messaggio)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("menu", menu))

print("BOT AVVIATO")

app.run_polling()
