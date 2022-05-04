from datetime import datetime as dt

# variable initialization
file = open("pnl_history.csv", 'r')
dailyPnl = 0
dailyWins = 0
dailyLoss = 0
dailyTotal = 0
monthlyPnl = 0
monthlyWins = 0
monthlyLoss = 0
monthlyTotal = 0
totalPnl = 0
totalWins = 0
totalLoss = 0
totalTrades = 0
quoteSkip = 0


file.readline()
lines = file.readlines()
lines = list(map(lambda x: x.rstrip(), lines)) # remove new line from lines in file
i = 0
while(i < len(lines)-1):
    # parse line
    quoteLine = lines[i]
    coinLine = lines[i+1]
    pnlLine = lines[i+2]
    dateLine = lines[i+3].split('"')[0]
    date = dt.strptime(dateLine, '%Y/%m/%d %H:%M:%S') 
    currentDate = dt.today() 
    i += 5 # jump to the next set 

    if('&lt;' in pnlLine): # weird edge case
        totalPnl += 0.01
        dailyPnl += 0.01
        monthlyPnl += 0.01
        totalWins += 1
        dailyWins += 1
        monthlyWins += 1
        continue

    # pnl calculations
    pnl = float(pnlLine.split('USDT')[0])
    if(date.month == currentDate.month and date.day == currentDate.day): # daily pnl calculation
        dailyPnl += pnl
        if(pnl >= 0):
            dailyWins += 1
        else:
            dailyLoss += 1
    if(date.month == currentDate.month): # monthly pnl calculation
        monthlyPnl += pnl
        if(pnl >= 0):
            monthlyWins += 1
        else:
            monthlyLoss += 1
    # total pnl calculation 
    totalPnl += pnl
    if(pnl >= 0):
        totalWins += 1
    else:
        totalLoss += 1

dailyTotal = dailyWins + dailyLoss
if(dailyTotal != 0):
    print("Daily Statistics")
    print("Total Trades: {}".format(dailyTotal))
    print("Win/Loss Ratio: {}%".format((dailyWins  / dailyTotal) * 100))
    print("Total PNL: {}".format(dailyPnl))
else:
    print("No trades today")
print()

monthlyTotal = monthlyWins + monthlyLoss
if(monthlyTotal != 0):
    print("Monthly Statistics")
    print("Total Trades: {}".format(monthlyTotal))
    print("Win/Loss Ratio: {}%".format((monthlyWins  / monthlyTotal) * 100))
    print("Total PNL: {}".format(monthlyPnl))
else:
    print("No trades this month")
print()

totalTrades = totalWins + totalLoss
if(totalTrades != 0):
    print("Total Statistics")
    print("Total Trades: {}".format(totalTrades))
    print("Win/Loss Ratio: {}%".format((totalWins  / totalTrades) * 100))
    print("Total PNL: {}".format(totalPnl))
else:
    print("No trades to date")

file.close()
