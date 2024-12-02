total = 0
scoretest = 0
score = 0
winner = []
yougot = []

while True:
    data = input("enter data")
    if data == "end":
        break
    splitdata = data.split("|")
    winnersplit = splitdata[0].split(" ")
    del winnersplit[-1]
    del winnersplit[0:2]
    while '' in winnersplit: winnersplit.remove('')
    winner = winnersplit
    yougotsplit = splitdata[1].split(" ")
    while '' in yougotsplit: yougotsplit.remove('')
    yougot = yougotsplit
    for x in winner:
        if x in yougot:
            scoretest += 1
    if scoretest != 0:
        score = 2**(scoretest-1)
    else:
        score = 0
    total += score
    scoretest = 0
    
print(total)
