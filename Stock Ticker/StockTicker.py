import random
import os
 
#Clears screen to make it easier to follow.
def clearScreen():
    os.system('cls') #uncomment for Windows system
    #os.system('clear') #uncomment for Linux system
    
#Starting message displayed at beginning of game
def welcomeMsg():
    welcome = """
                     STOCK TICKER
 
    The object of the game is to buy and sell stocks,
    and by doing so, accumulate a greater amount of
    money than the other players by the end of the game.
    """
    print(welcome)
 
# Choose how many players are in game as well as choose names
def createPlayers():
    turnCount = 0
    playerStats = {'Name': 'player', 'Money': 5000, '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0}

    ask = True
    while ask is True:
        numPlayers = input("Please choose between 2 and 8 players.\n")
        ask = False if numPlayers.isdigit() and 2 <= int(numPlayers) <= 8 else True
    for _ in range(int(numPlayers)):
        players.append(playerStats.copy())
    while turnCount < len(players):
        players[turnCount]["Name"] = input("What is player {}'s name?\n".format(turnCount+1))
        if players[turnCount]["Name"] == "":
            print("Name cannot be left blank")
        else:
            turnCount += 1
 
#Players can choose how many rounds game lasts
def chooseRounds():
    ask = True
    print("\nHow many rounds would you like to play?")
    while ask is True:
        Rounds = input("Please choose a number between 1 - 100\n")
        ask = False if Rounds.isdigit() and 1 <= int(Rounds) <= 100 else True
    return int(Rounds)
 
# Function to select random dice roll
def rollDice():
    outcomeStock = random.choice([0, 1, 2, 3, 4, 5]) # Relates to global StockValue variable index
    outcomeAction = random.choice(["Up", "Down", "Dividend"])
    outcomeAmount = random.choice([5, 10, 20])
 
    stockChange(outcomeStock, outcomeAction, outcomeAmount)
    print("----------")
    if outcomeStock == 0:
        print("Gold", outcomeAction, outcomeAmount)
    elif outcomeStock == 1:
        print("Silver", outcomeAction, outcomeAmount)
    elif outcomeStock == 2:
        print("Oil", outcomeAction, outcomeAmount)
    elif outcomeStock == 3:
        print("Bonds", outcomeAction, outcomeAmount)
    elif outcomeStock == 4:
        print("Grain", outcomeAction, outcomeAmount)
    elif outcomeStock == 5:
        print("Industrial", outcomeAction, outcomeAmount)
    print("----------\n")
 
# Takes results of rollDice() and applies it to the Stock value
def stockChange(rolledStock, rolledAction, rolledAmount):
    turnCounts = 0
    numPlayers = len(players)
    stockNames = optionStockName(rolledStock)
    
    if rolledAction == "Up":
        StockValue[int(rolledStock)] = StockValue[int(rolledStock)] + rolledAmount
        if StockValue[int(rolledStock)] >= 200:
            while turnCounts < numPlayers:
                if players[turnCounts][str(rolledStock)] == 0:
                    turnCounts += 1
                elif players[turnCounts][str(rolledStock)] > 0:
                    oldValue = players[turnCounts][str(rolledStock)]
                    players[turnCounts][str(rolledStock)] = players[turnCounts][str(rolledStock)] * 2
                    newValue = players[turnCounts][str(rolledStock)]
                    print("{} just doubled their {} stock from {} to {}".format(players[turnCounts]["Name"], stockNames, oldValue, newValue))
                    turnCounts += 1
            StockValue[int(rolledStock)] = 100
    elif rolledAction == "Down":
        StockValue[int(rolledStock)] = StockValue[int(rolledStock)] - rolledAmount
        if StockValue[int(rolledStock)] <= 0:
            while turnCounts < numPlayers:
                if players[turnCounts][str(rolledStock)] == 0:
                    turnCounts += 1
                elif players[turnCounts][str(rolledStock)] > 0:
                    players[turnCounts][str(rolledStock)] = players[turnCounts][str(rolledStock)] * 0
                    newValue = players[turnCounts][str(rolledStock)] * 0
                    print("{} got unlucky and lost all of their {} stock".format(players[turnCounts]["Name"], stockNames))
                    turnCounts += 1
            StockValue[int(rolledStock)] = 100
    elif rolledAction == "Dividend":
        if StockValue[int(rolledStock)] >= 100:
            while turnCounts < numPlayers:
                if players[turnCounts][str(rolledStock)] == 0:
                    turnCounts += 1
                elif players[turnCounts][str(rolledStock)] > 0:
                    players[turnCounts]["Money"] += (StockValue[int(rolledStock)] * int(rolledAmount))
                    newValue = StockValue[int(rolledStock)] * int(rolledAmount)
                    print("\n{} just got ${} from {}\n".format(players[turnCounts]["Name"], newValue, stockNames))
                    turnCounts += 1
    return StockValue[rolledStock]
    
def optionStockName(stockOption):
    if stockOption == "gold" or stockOption == 0:
        stockName = "Gold"
    elif stockOption == "silver" or stockOption == 1:
        stockName = "Silver"
    elif stockOption == "oil" or stockOption == 2:
        stockName = "Oil"
    elif stockOption == "bonds" or stockOption == 3:
        stockName = "Bonds"
    elif stockOption == "grain" or stockOption == 4:
        stockName = "Grain"
    elif stockOption == "industrial" or stockOption == 5:
        stockName = "Industrial"
    return stockName
    
def optionStockNumber(stockOption):
    if stockOption == "gold":
        stockNumber = 0
    elif stockOption == "silver":
        stockNumber = 1
    elif stockOption == "oil":
        stockNumber = 2
    elif stockOption == "bonds":
        stockNumber = 3
    elif stockOption == "grain":
        stockNumber = 4
    elif stockOption == "industrial":
        stockNumber = 5
    return stockNumber
    
def curPlayerInfo(turnCount):
    print("----------It is {}'s turn----------\n".format(players[turnCount]["Name"]))
    print("Money:      {}".format(players[turnCount]["Money"]))
    print("Gold:       {}".format(players[turnCount]["0"]))
    print("Silver:     {}".format(players[turnCount]["1"]))
    print("Oil:        {}".format(players[turnCount]["2"]))
    print("Bonds:      {}".format(players[turnCount]["3"]))
    print("Grain:      {}".format(players[turnCount]["4"]))
    print("Industrial: {}\n".format(players[turnCount]["5"]))
 
#Players can purchase stocks before game begins
def firstPurchase():
    turnCount = 0
    numPlayers = len(players)
    canBuy = min(StockValue)
    
    while turnCount < numPlayers:
        print("""
            STOCK TICKER
    """)
        print("""
    Before the game starts, each player gets the
    choice of purchasing any stocks they want.
        """)
        curPlayerInfo(turnCount)
        currentPrices()
        valueChange = input("Buy, Sell or Done?\n")
        valueChange = valueChange.lower()
        if valueChange != "buy" and valueChange != "sell" and valueChange != "done" and valueChange != "":
            clearScreen()
            print("Please choose a correct action.\n")
        if valueChange == "done" or valueChange == "":
            clearScreen()
            turnCount += 1
        elif valueChange == "buy":
            if int(int(players[turnCount]["Money"])) < int(canBuy):
                print("You can't afford any stocks.\n")
            else:
                stockBuy = input("Which stock would you like to buy?\n")
                stockBuy = stockBuy.lower()
                if stockBuy != "gold" and stockBuy != "silver" and stockBuy != "oil" and stockBuy != "bonds" and stockBuy != "grain" and stockBuy != "industrial":
                    clearScreen()
                    print("Please choose a valid stock.\n")
                else:
                    ask = True
                    while ask is True:
                        buyNumber = input("How many shares of {} would you like to buy?\n".format(optionStockName(stockBuy)))
                        ask = False if buyNumber.isdigit() else True
                    if int(players[turnCount]["Money"]) < (StockValue[optionStockNumber(stockBuy)] * int(buyNumber)):
                        clearScreen()
                        print("You can't afford {} {} stock(s).\n".format(buyNumber, optionStockName(stockBuy)))
                    elif int(players[turnCount]["Money"]) >= (StockValue[optionStockNumber(stockBuy)] * int(buyNumber)):
                        players[turnCount]["Money"] = players[turnCount]["Money"] - int(StockValue[optionStockNumber(stockBuy)] * int(buyNumber))
                        players[turnCount][str(optionStockNumber(stockBuy))] += int(buyNumber)
                        clearScreen()
                        print("You bought {} {} stock(s).\n".format(buyNumber, optionStockName(stockBuy)))
        elif valueChange == "sell":
            stockSell = input("Which stock would you like to sell?\n")
            stockSell = stockSell.lower()
            if stockSell != "gold" and stockSell != "silver" and stockSell != "oil" and stockSell != "bonds" and stockSell != "grain" and stockSell != "industrial":
                clearScreen()
                print("Please choose a valid stock.\n")
            else:
                ask = True
                while ask is True:
                    sellNumber = input("How many shares of {} would you like to sell?\n".format(optionStockName(stockSell)))
                    ask = False if sellNumber.isdigit() else True
                if int(players[turnCount][str(optionStockNumber(stockSell))]) < int(sellNumber):
                    clearScreen()
                    print("You don't have that much.\n")
                elif int(players[turnCount][str(optionStockNumber(stockSell))]) >= int(sellNumber):
                    players[turnCount]["Money"] = players[turnCount]["Money"] + int(StockValue[optionStockNumber(stockSell)] * int(sellNumber))
                    players[turnCount][str(optionStockNumber(stockSell))] -= int(sellNumber)
                    clearScreen()
                    print("You sold {} {} stock(s).\n".format(sellNumber, optionStockName(stockSell)))
    clearScreen()
    print("         \nThe game has begun!\n")
    rollDice()
 
#Main gameplay mechanics
def turnCount():
    turnCount = 0
    rounds = 0
    numPlayers = len(players)
    maxRounds = int(maxRound)
    canBuy = min(StockValue)
 
    while rounds < maxRounds:
        if turnCount < numPlayers:
            print("Round:", rounds+1, "/", maxRounds, "\n")
            curPlayerInfo(turnCount)
            currentPrices()
            valueChange = input("Buy, Sell, or Done?\n")
            valueChange = valueChange.lower()
            if valueChange != "buy" and valueChange != "sell" and valueChange != "done" and valueChange != "":
                clearScreen()
                print("Please choose a correct action.\n")
            if valueChange == "done" or valueChange == "":
                turnCount += 1
                clearScreen()
                if rounds+1 == maxRounds and turnCount == numPlayers:
                    endGame()
                else:
                    rollDice()
            elif valueChange == "buy":
                if int(int(players[turnCount]["Money"])) < int(canBuy):
                    clearScreen()
                    print("You can't afford any stocks.\n")
                else:
                    stockBuy = input("Which stock would you like to buy?\n")
                    stockBuy = stockBuy.lower()
                    if stockBuy != "gold" and stockBuy != "silver" and stockBuy != "oil" and stockBuy != "bonds" and stockBuy != "grain" and stockBuy != "industrial":
                        clearScreen()
                        print("Please choose a valid stock.\n")
                    else:
                        ask = True
                        while ask is True:
                            buyNumber = input("How many shares of {} would you like to buy?\n".format(optionStockName(stockBuy)))
                            ask = False if buyNumber.isdigit() else True
                        if int(players[turnCount]["Money"]) < (StockValue[optionStockNumber(stockBuy)] * int(buyNumber)):
                            clearScreen()
                            print("You can't afford {} stocks of {}.\n".format(buyNumber, optionStockName(stockBuy)))
                        elif int(players[turnCount]["Money"]) >= (StockValue[optionStockNumber(stockBuy)] * int(buyNumber)):
                            players[turnCount]["Money"] = players[turnCount]["Money"] - int(StockValue[optionStockNumber(stockBuy)] * int(buyNumber))
                            players[turnCount][str(optionStockNumber(stockBuy))] += int(buyNumber)
                            clearScreen()
                            print("You bought {} {} stock(s).\n".format(buyNumber, optionStockName(stockBuy)))
            elif valueChange == "sell":
                stockSell = input("Which stock would you like to sell?\n")
                stockSell = stockSell.lower()
                if stockSell != "gold" and stockSell != "silver" and stockSell != "oil" and stockSell != "bonds" and stockSell != "grain" and stockSell != "industrial":
                    clearScreen()
                    print("Please choose a valid stock.\n")
                else:
                    ask = True
                    while ask is True:
                        sellNumber = input("How many shares of {} would you like to sell?\n".format(optionStockName(stockSell)))
                        ask = False if sellNumber.isdigit() else True
                    if int(players[turnCount][str(optionStockNumber(stockSell))]) < int(sellNumber):
                        clearScreen()
                        print("You don't have that much.\n")
                    elif int(players[turnCount][str(optionStockNumber(stockSell))]) >= int(sellNumber):
                        players[turnCount]["Money"] = players[turnCount]["Money"] + int(StockValue[optionStockNumber(stockSell)] * int(sellNumber))
                        players[turnCount][str(optionStockNumber(stockSell))] -= int(sellNumber)
                        clearScreen()
                        print("You sold {} {} stock(s).\n".format(sellNumber, optionStockName(stockSell)))
        elif turnCount == numPlayers:
            turnCount = 0
            rounds += 1
 
#Displays current price based on results of rollDice()
def currentPrices():
    print("Stock Prices:")
    print("-----")
    print("Gold:      ", StockValue[0])
    print("Silver:    ", StockValue[1])
    print("Oil:       ", StockValue[2])
    print("Bonds:     ", StockValue[3])
    print("Grain:     ", StockValue[4])
    print("Industrial:", StockValue[5])
    print("-----")
    print("")
 
#When result of chooseRounds() is met, display all players total money
def endGame():
    turnCounted = 0
    numPlayers = len(players)
    while turnCounted < numPlayers:
        stockNumbered = 0
        numStocks = len(StockValue)
        while stockNumbered < numStocks:
            players[turnCounted]["Money"] += players[turnCounted][str(stockNumbered)] * StockValue[stockNumbered]
            stockNumbered += 1
        print("{} has ${}".format(players[turnCounted]["Name"], players[turnCounted]["Money"]))
        turnCounted += 1
        stockNumbered = 0
    input('Press ENTER to exit')
    
##########################################
#               Begin game               #
##########################################

StockValue = [100, 100, 100, 100, 100, 100] #0-Gold, 1-Silver, 2-Oil, 3-Bonds, 4-Grain, 5-Industrial
players = [] # Empty list to store player data generated by createPlayers()
numPlayers = len(players)

welcomeMsg()
createPlayers()
maxRound = chooseRounds()
clearScreen()
firstPurchase()
turnCount()

#TODO:
#package for Windows local
#refactor with classes?
#add save option
#add networking
#add client/server
#add GUI
#package for Windows multiplayer