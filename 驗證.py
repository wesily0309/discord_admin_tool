import discord
from discord.ext import commands
#import log
#import Popups
from discord_webhook import DiscordWebhook
import datetime
#import notify
import threading
import asyncio
intents = discord.Intents.all()#啟用所有
bot = commands.Bot(command_prefix='!', intents=intents)
pd="12345678"
inpcfg='Admin'

@bot.command(name="grant_admin")
@commands.has_role('Admin')
async def grant_admin(ctx, password):
    try:
        if password==pd:
            admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
            permissions = discord.Permissions(administrator=True)
            await admin_role.edit(permissions=permissions)
            await ctx.send("已開啟管理員權限")
        elif password!=pd:
            await ctx.send("密碼錯誤")
    except:
        print("指令語法錯誤 正確語法:!grant_admin <password>")
        await ctx.send("指令語法錯誤 正確語法:!grant_admin<password>")

@bot.command(name='revoke_admin')
@commands.has_role('Admin')
async def revoke_admin(ctx, password):
    try:
        if password==pd:
            admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
            permissions = discord.Permissions(administrator=False)
            await admin_role.edit(permissions=permissions)
            await ctx.send("已開啟管理員權限")
        elif password!=pd:
            await ctx.send("密碼錯誤")
    except:
        print("指令語法錯誤 正確語法:!revoke_admin <password>")
        await ctx.send("指令語法錯誤 正確語法:!revoke_admin <password>")
@bot.command()
async def ping(ctx):
    """測試機器人是否在線上"""
    await ctx.send('Pong! Latency: {}ms'.format(round(bot.latency * 1000)))
"""
@bot.command(name="help")
@commands.has_role('Admin')
async def help(cxt):
    await cxt.send("開啟權限:!grant_admin <password>")
    await cxt.send("關閉權限:!revoke_admin <password>")
bot.run("MTA5MjE1MDc1OTMxNzA1MzU3MQ.G2J0oo.RMqemxcpGBXaSTq3v3JESqjVT_eRQ_uMfT0BCc") 
"""
bot.run("MTA5MjE1MDc1OTMxNzA1MzU3MQ.G2J0oo.RMqemxcpGBXaSTq3v3JESqjVT_eRQ_uMfT0BCc") 