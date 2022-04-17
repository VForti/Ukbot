import discord
from discord import utils
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from time import sleep


bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

bot.remove_command('help')



@bot.event
async def on_ready():
    print('I am connected!')

    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game('Verify'))


@bot.command(aliases = ['print'])
async def __print(ctx):
	member = ctx.author
	emb = discord.Embed(title = 'Успішно!',colour = discord.Colour.green())
	emb.add_field(name = 'Щоби веревікуватися запустіть команду ".verify"',value = f'Команду запустив {member.mention}')

	await ctx.send(embed = emb)


@bot.command(aliases=['verify'])


async def __verify(ctx):
	
	member = ctx.author
	
	emb = discord.Embed(title = 'Що таке паляниця?!',colour = discord.Colour.orange())
	
	emb.add_field(name = 'Варіанти - 1).Вулиця 2).Хліб 3).назва_заводу',value = f'Писати з крапкою!Викликав команду - {member.mention}')
	
	await ctx.send(embed = emb)


@bot.command(aliases = ['Хліб','хліб'],pass_context = True)

async def __yes(ctx):
	member = ctx.author
	emb = discord.Embed(title = "Успішно!",colour = discord.Colour.green())
	emb.add_field(name = f'УВАГА! УВАГА! ЩОБ ПОЛУЧИТИ РОЛЬ ТРЕБА НАПИСАТИ КОМАНДУ ".give @Верефікований"!',value = f'Дав правильну відповідь - {member.mention}')

	await ctx.send(embed = emb)


@bot.command(aliases = ['Вулиця','вулиця'])
async def __no(ctx):
		
	member = ctx.author
	emb = discord.Embed(title = "Погано!",colour = discord.Colour.red())

			
	emb.add_field(name = f'Ви не Українець!',value = f'НЕ УКРАЇНЕЦЬ - {member.mention}')

	await ctx.send(embed = emb)
	sleep(5)

	await ctx.author.kick(reason=f'')
	

@bot.command(aliases = ['назва_заводу','Назва_заводу','НАЗВА_ЗАВОДУ','назва_Заводу','НазваЗаводу'])
async def __noo(ctx):
	member = ctx.author



	emb = discord.Embed(title = "Погано!",colour = discord.Colour.red())
	emb.add_field(name = f'Ви не Українець!',value = f'НЕ УКРАЇНЕЦЬ - {member.mention}')
	await ctx.send(embed = emb)
	sleep(5)
	

	await ctx.author.kick(reason=f'')


@bot.command(aliases = ['give'])
async def __give(ctx,role : discord.Role = None):
	if  role  is None:
		await ctx.send(f'**{ctx.author},вкажіт роль - (@Верефікований),щоби получити доступ до чатів!**')
	else:
		await ctx.author.add_roles(role)
		emb = discord.Embed(title = 'Молодець!',colour = discord.Colour.green())
		emb.add_field(name = 'Ви получили роль і тепер вам віддкрито чати!',value = f'{member.mention} пройшов верефікацію!')

		await ctx.send(embed = emb)
		await ctx.message.add_reaction('✅')
		


	
bot.run("TOKEN")

