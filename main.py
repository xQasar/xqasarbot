import discord
from discord.ext import commands
import asyncio
import time
from asyncio import sleep
import aiohttp
import random
print('\033[2;32;40m LOADING...')


bot = commands.Bot(command_prefix=('q-'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="q-help"))
    print('\033[2;32;40m QUASAR BOT ONLINE')
	

@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ответ...")
    end = time.perf_counter()
    
    duration = (end - start) * 1000
    
    await message.edit(content=f"**Веб сокет:** {round(bot.latency * 1000)}ms\n**Общий пинг:** {duration:.0f}ms")

    
@bot.command()
@commands.has_permissions(administrator = True)
async def kletka(ctx, member: discord.Member, *,reason="не указана"):
    role = discord.utils.get(ctx.guild.roles, id=967517782465986660)
    await member.add_roles(role, reason=reason)
    message: discord.Message = await ctx.send(f"Ебаклак {member} был посажен в клетку по причине: {reason}")


@bot.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, reason="не указана"):
    await member.kick(reason=reason)
    await ctx.send(f"Ебаклак {member} кикнут с сервера по причине")

    
    
@bot.command()
async def help(ctx):
    embed1 = discord.Embed(title="Помощь", description="Для корректной работы бота, поставьте его роль выше остальных", color=discord.Color.green())
    embed1.add_field(name="kick '@пользователь' 'причина' ", value="Выгнать ебаклака с сервера")
    embed1.add_field(name="clear", value="очищает 100 сообщений")
    embed1.add_field(name="ping", value="проверка отклика бота")
    embed1.add_field(name="author", value="информация об авторе бота")
    await ctx.send(embed=embed1)
    
    
@bot.command()
async def author(ctx):
    embed2 = discord.Embed(title="Автор", description="Автор бота Quasar#2240", color=discord.Color.green())
    embed2.add_field(name="YouTube", value="https://youtube.com/channel/UCULXkYNkx7Rca6h1rPevXDw")
    embed2.add_field(name="Telegram", value="@ItzQasar")
    embed2.add_field(name="VK", value="@xqasar")
    await ctx.send(embed=embed2)
    
    
@bot.command()
async def clear(ctx, count=100):
	await ctx.channel.purge(limit=count)


@bot.event
async def on_message(message):
   if 'https://' in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention}, не рассылайте ссылки!")
   else:
      await bot.process_commands(message)
	

bot.run('OTY2NzQ1OTMxNjExNTI1MTYy.YmGOTw.7jSHyWTQn_U3ew5w0oqZiIGLfEo')