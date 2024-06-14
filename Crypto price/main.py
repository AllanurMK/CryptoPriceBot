from auth_data import token
import requests 
from datetime import datetime
import telebot
from telebot import types

def crypto_bahalar(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    jogaby = requests.get(url)
    data = jogaby.json()
    shu_gun_sene = datetime.now().strftime("%d.%m.%Y %H:%M")
    if crypto in data and "usd" in data[crypto]:
       return f"{crypto.capitalize()} bahasy: {data[crypto]['usd']}$\nSene: {shu_gun_sene}"
    else:
        return "Sorry! I coudn't to found a price of bitcoin"

'''price_of_bitcoin = crypto_bahalar("bitcoin")
print(price_of_bitcoin)'''

menin_botym =  telebot.TeleBot(token)

@menin_botym.message_handler(commands=["start"])
def start_knopka(message):
    klawiatura = types.InlineKeyboardMarkup( row_width=2)
    btc_knopka = types.InlineKeyboardButton("Bitcoin bahasy", callback_data="bitcoin")
    ltc_knopka = types.InlineKeyboardButton("Litecoin bahasy", callback_data="litcoin")
    eth_knopka = types.InlineKeyboardButton("Ethereum bahasy", callback_data="ethereum")
    klawiatura.add(btc_knopka, ltc_knopka, eth_knopka)

    menin_botym.send_message(message.chat.id, "Haýsy kriptowalýutaň bahasyny bilesiňiz gelyär?", reply_markup=klawiatura)

@menin_botym.callback_query_handler(func = lambda call:True)
def knopka_basylanda_jogap(callback):
    if callback.message:
        bahasy = crypto_bahalar(callback.data)
        menin_botym.send_message(callback.message.chat.id, bahasy)
        start_knopka(callback.message)

menin_botym.polling()
