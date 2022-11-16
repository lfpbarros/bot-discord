import lightbulb
# Biblioteca para criar o bot

bot = lightbulb.BotApp(token = open('tokens/token_ds.txt', 'r').read(), default_enabled_guilds=(int(open('tokens/ds_channel_id.txt', 'r').read())))
# Instanciando o bot na variável, daí passamos o token como parâmetro, também passamos o id do servidor do discord no outro parâmetro, precisou ser convertido para inteiro

# Saudação
@bot.command
# Decorador do bot, setamos um comando
@lightbulb.command('msg_asmv', 'Saudação Asimov Academy')
# Setados o comando e retorno
@lightbulb.implements(lightbulb.SlashCommand)
# Setamos o que vai ser feito
async def hello(ctx):
    # Esse contexto ctx identifica o que vai estar dentro do comando
    await ctx.respond('*Olá, comunidade Asimov Academy!*')

# Piada
import random

p1 = "O que o pato disse para a pata? \nR.: Vem Quá!"
p2 = "Por que o menino estava falando ao telefone deitado? \nR.: Para não cair a ligação."
p3 = "Qual é a fórmula da água benta? \nR.: H Deus O!"
p4 = "Qual a cidade brasileira que não tem táxi? \nR.: Uberlândia"
p5 = "Qual é a fruta que anda de trem? \nR.: O kiwiiiiiiii."
p6 = "O que é um pontinho preto no avião? \nR.: Uma aeromosca."
p7 = "Como o Batman faz para entrar na Bat-caverna? \nR.: Ele bat-palma"
p8 = "Por que o pão não entende a batata? \nR.: Porque o pão é francês e a batata é inglesa"
p9 = "O que o zero disse para o oito? \nR.: Belo cinto!"
p10 = "Por que os elétrons nunca são convidados para as festas? \nR.: Porque eles são muito negativos."

piadas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

@bot.command
@lightbulb.command('piada', 'Receba uma piada')
@lightbulb.implements(lightbulb.SlashCommand)
async def joke(ctx):
    n = random.randint(1, 10)
    await ctx.respond(f'*{piadas[n]}*')

# Esse tipo de função pode retornar qualquer coisa em texto, pode ser útil para retornar senhas, por exemplo.


# Calculadora
@bot.command
@lightbulb.command('calculadora', 'Calculadora')
@lightbulb.implements(lightbulb.SlashCommandGroup)
# Nesse caso, ao invés de um comando só, temos um grupo de comandos, um comando principal e daí, vem outros comandos, diferente das outras funções que fizemos apenas um comando /  
async def my_calculator(ctx):
    pass
# O comando calculadora só, não nos serve precisamos saber da operação, assim essa função só precisa do pass. Ela só precisa ser registrada.
@my_calculator.child
# As próximas funções são oriundas da my_calculator
@lightbulb.option('n2', 'Segundo número', type=float)
# O segundo número é lido primeiro
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('soma', 'Operação de Adição')
@lightbulb.implements(lightbulb.SlashSubCommand)
# É um subcomando da calculadora
async def soma(ctx):
    r = ctx.options.n1 + ctx.options.n2
    await ctx.respond(f'*O resultado é **{r}***')

# -- Subtração
@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('subtração', 'Operação de Subtração')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subracao(ctx):
    r = ctx.options.n1 - ctx.options.n2
    await ctx.respond(f'*O resultado é **{r}***')

# -- Multiplicação
@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('multiplicação', 'Operação de Multiplicação')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def multiplicacao(ctx):
    r = ctx.options.n1 * ctx.options.n2
    await ctx.respond(f'*O resultado é **{r}***')

# -- Divisão
@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('divisão', 'Operação de Divisão')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def divisao(ctx):
    r = ctx.options.n1 / ctx.options.n2
    await ctx.respond(f'*O resultado é **{r}***')

# Aqui é possível interagir com o usuário, isso traz mais funcionalidades.

# API
# Temperatura

import requests
import string

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('tokens/api_weather_key.txt', 'r').read()

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius
# Conversor para celsius

@bot.command
@lightbulb.option('pais', 'País', type=str)
@lightbulb.option('cidade', 'Cidade', type=str)
@lightbulb.command('temperatura', 'Informe uma cidade e seu país para saber as condições climáticas atuais:')
@lightbulb.implements(lightbulb.SlashCommand)

async def temperatura(ctx):
    country = ctx.options.pais
    # Essa variável serve para tratar o dado já que as API, para fornecer o que precisamos, torna-se necessário enviar os parâmetros segundo o que elas pedem.
    CITY = string.capwords(ctx.options.cidade) + ',' + country[0:2].lower()
    # Tratamento de dados, a cidade começa com iniciais maiúsculas, o país são as primeiras duas letras em minúsculo
    url = BASE_URL + 'q=' + CITY + '&APPID=' + API_KEY
    # Montando o link exato da requisição
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    umidade = response['main']['humidity']
    vento = response['wind']['speed']
    # Fatiando o json para as informações que precisamos

    temp_celsius = str(round(kelvin_to_celsius(temp_kelvin)))
    # Converte de Kelvin para celsius e depois arredonda

    await ctx.respond(f'```A temperatura atual em {string.capwords(ctx.options.cidade)} é de {temp_celsius}ºC \numidade do ar: {umidade}% \nvento: {vento}m/s```')

    # Projeto para depois: acrescentar função do analytics

bot.run()
# Roda o bot

