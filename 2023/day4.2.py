total = 0
scoretest = 0
score = 0
winner = []
yougot = []
howmany = []
gameid= 0
while True:
    data = input("enter data")
    if data == "end":
        break
    splitdata = data.split("|")
    winnersplit = splitdata[0].split(" ")
    del winnersplit[-1]
    gameid = int((winnersplit[1].split(":"))[0])
    del winnersplit[0:2]
    while '' in winnersplit: winnersplit.remove('')
    winner = winnersplit
    yougotsplit = splitdata[1].split(" ")
    while '' in yougotsplit: yougotsplit.remove('')
    yougot = yougotsplit
    for x in winner:
        if x in yougot:
            scoretest += 1
    howmany.append(scoretest)
    print(gameid)
    scoretest = 0
    
print(howmany)
