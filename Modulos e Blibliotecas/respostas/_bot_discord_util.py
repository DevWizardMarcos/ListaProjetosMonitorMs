import discord
from discord.ext import commands
import requests
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')

@bot.command()
async def tempo(ctx, cidade):
    api_key = 'sua_chave_api_openweathermap'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br'
    resposta = requests.get(url).json()
    if resposta.get('cod') != 200:
        await ctx.send('Cidade não encontrada!')
    else:
        temp = resposta['main']['temp']
        await ctx.send(f'Temperatura em {cidade}: {temp}°C')

@bot.command()
async def piada(ctx):
    resposta = requests.get('https://v2.jokeapi.dev/joke/Any?lang=pt').json()
    if resposta['type'] == 'single':
        await ctx.send(resposta['joke'])
    else:
        await ctx.send(f"{resposta['setup']} - {resposta['delivery']}")

@bot.command()
async def dado(ctx):
    await ctx.send(f"Você rolou: {random.randint(1, 6)}")

# Inicie o bot
bot.run('sua_token_aqui')
