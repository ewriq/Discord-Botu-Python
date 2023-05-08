import os # os modülünü yükler
from flask import Flask
from discord.ext import commands 
from dotenv import load_dotenv

load_dotenv() # .env yi yükler

app = Flask(__name__)

token = os.environ.get("token") # .env dosyasından token değerini alır

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} Botunuz açıldı.")

@app.route("/")
def home(): #web sunucusunu çalıştırır
    return "Web Sitesi çalışıyor."

if __name__ == "__main__":
    bot.run(token) #token ile projeyi açar
    app.run()
