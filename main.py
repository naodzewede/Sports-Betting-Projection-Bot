import discord
from discord.ext import commands
import csv
import requests

# url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

# querystring = {"id":"236","season":"2023"}

# headers = {
# 	"X-RapidAPI-Key": "a3f1d5fe9dmshd4b70a31327ee50p1c7078jsn3d9753af9eb2",
# 	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

with open("prizepickProjections.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    next(csvreader)

client = commands.Bot(command_prefix= '!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is ready!")
    print("---------------------")

@client.command()
async def instructions(ctx, *args):
    strInstructions = str("_name_ Points | _name_ Rebounds | _name_ PTS+REB+AST\n_name_ Assists | _name_ Fantasy Score | _name_ Defensive Rebounds\n" +
                       "_name_ Offensive Rebounds | _name_ 3PT Made | _name_ FT Made\n_name_ FG Attempted | _name_ PTS+REB | _name_ Blocks\n" +
                       "_name_ Steals | _name_ REB+AST | _name_ BLK+STL\n_name_ Turnovers | _name_ 3PT Attempts")
    embed = discord.Embed(title="Instructions")
    embed.add_field(name="Use these commands", value = strInstructions)
    await ctx.send(embed = embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    with open("prizepickProjections.csv", 'r') as file:
        csvreader = csv.DictReader(file)
        next(csvreader)

        for row in csvreader:
            entry = row["Player"] + " " + row["Market Name"]
            if message.content.startswith(entry):
                intPredication = float(row["Prediction"])
                if(intPredication < 5 or intPredication > -5):
                    print (row["Prediction"])
                    lean = "_Very Risky_"
                if(5 < intPredication <= 25 or -5 >= intPredication > -25):
                    lean = "_Slight Risk_"
                if(25 < intPredication <= 50 or -25 >= intPredication > -50):
                    lean = "_Good Chance_"
                if(50 < intPredication <= 100 or -50 >= intPredication >= -100):
                    lean = "_Strong Chance_"
                await message.channel.send(row["Date"] + " " + row["Time"] + " ⏰" + " \n_Based on the average of all projection factors_ 🧮, \n" + row["Player"] +
                                            " ⛹️ will be " +  "**" + row["Lean"] + "**" + " in " + row["Market Name"] + " (" + lean + ")")
                strBreakdown = ("**RotoWire Projection Factor:** " + row["RotoWire Projection Factor"] + "\n" +
                                "**Sportsbooks Factor:** " + row["Sportsbooks Factor"] + "\n" + 
                                 "**DFS Pick'em Sites Factor:** " + row["DFS Pick'em Sites Factor"] + "\n" + 
                                 "**Hit Rate Factor is:** " + row["Hit Rate Factor"] + "\n")
                embed = discord.Embed(title="Breakdown 🧑🏽‍🏫")
                embed.add_field(name="", value = strBreakdown)
                await message.channel.send(embed = embed)
                # await message.channel.send("**Breakdown** 🧑🏽‍🏫 : \n**RotoWire Projection Factor:** " + row["RotoWire Projection Factor"] + "\n" +
                #                                         "**Sportsbooks Factor:** " + row["Sportsbooks Factor"] + "\n" + 
                #                                         "**DFS Pick'em Sites Factor:** " + row["DFS Pick'em Sites Factor"] + "\n" + 
                #                                         "**Hit Rate Factor is:** " + row["Hit Rate Factor"] + "\n")

client.run('MTE4MzMzNTc3MzA5Nzk1NTM4OA.GP8K1F.Tc0CiaDiU-9hK6VCh74RsLnGlgJPd1YKZZkLoE')