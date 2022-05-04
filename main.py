from datetime import datetime as dt

# variable initialization
file = open("pnl_history.csv", 'r')
dailyPnl = 0
dailyWins = 0
dailyLoss = 0
monthlyPnl = 0
monthlyWins = 0
monthlyLoss = 0
totalPnl = 0
totalWins = 0
totalLoss = 0
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

    if(pnlLine in '&lt;' or pnlLine == '- &lt; 0.01USDT≈ 0.01USD","'): # weird edge case
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

print("Daily Statistics")
print("Total Trades: {}".format(dailyWins + dailyLoss))
print("Win/Loss Ratio: {}%".format(dailyWins  / (dailyWins + dailyLoss) * 100))
print("Total PNL: {}".format(dailyPnl))
print()

print("Monthly Statistics")
print("Total Trades: {}".format(monthlyWins + monthlyLoss))
print("Win/Loss Ratio: {}%".format(monthlyWins  / (monthlyWins + monthlyLoss) * 100))
print("Total PNL: {}".format(monthlyPnl))
print()

print("Total Statistics")
print("Total Trades: {}".format(totalWins + totalLoss))
print("Win/Loss Ratio: {}%".format(totalWins  / (totalWins + totalLoss) * 100))
print("Total PNL: {}".format(totalPnl))

file.close()
