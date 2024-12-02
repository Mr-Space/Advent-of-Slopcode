score = 0

rock = ["A"]
paper = ["B"]
scissors = ["C"]
while True:
    x, y = input("enter data").split()
    if x == 'end':
            break
    if y == "Y":
        score += 3
        if x in rock:
            score += 1
        elif x in paper:
            score += 2
        elif x in scissors:
            score += 3
    elif y == "Z":
        score += 6
        if x in rock:
            score += 2
        elif x in paper:
            score += 3
        elif x in scissors:
            score += 1
    elif y == "X":
        if x in rock:
            score += 3
        elif x in paper:
            score += 1
        elif x in scissors:
            score += 2
      
print(score)
