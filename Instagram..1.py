import requests
import time,random,os
import concurrent.futures,os,sys
from rich.panel import Panel
from rich import print
import telebot
g=0
b=0
bb=0

q = '\033[1;30m'
w = '\033[1;31m'
e = '\033[1;32m'
r = '\033[1;33m'
t = '\033[1;34m'
y = '\033[1;35m'
u = '\033[1;36m'
i = '\033[1;37m'
print ('𝑺𝑶𝑴𝑬 𝑯𝑨𝑪𝑲𝑬𝑹𝑺 𖠔 <|> ᏔᏫᏫᎠᎬ <|> V249V')
TOKEN=input(r+'TOKEN BOT :')
chat_id=input(r+'ID TELE :')
bot = telebot.TeleBot(TOKEN)
ti = '[i][bold green] @c249c[/bold green][/i]'
te = '''[green]Done

╭╮╭╮╭┳━━━┳━━━┳━━━┳━━━╮
\033[1;35m┃┃┃┃┃┃╭━╮┃╭━╮┣╮╭╮┃╭━━╯
\033[1;36m┃┃┃┃┃┃┃╱┃┃┃╱┃┃┃┃┃┃╰━━╮
\033[1;37m┃╰╯╰╯┃┃╱┃┃┃╱┃┃┃┃┃┃╭━━╯
\033[1;30m╰╮╭╮╭┫╰━╯┃╰━╯┣╯╰╯┃╰━━╮
\033[1;33m╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━╯
\033[1;32m𝑺𝑶𝑴𝑬 𝑯𝑨𝑪𝑲𝑬𝑹𝑺 𖠔
\033[1;33mᏔᏫᏫᎠᎬ | SUDAN
\033[1;37mادعـي لــي عـنـدي امـتـحانـات
        '''
print(Panel(te,title=ti))