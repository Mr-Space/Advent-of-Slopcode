from pprint import pprint

data = [[]]
array = []
while True:
    
    putin = input('enter data')
    if putin == 'end':
            break
    if putin == '':
        array.append(putin)
    else:
        array.append(int(putin, 10))

    
    
for i in array:
    if i == '':
        data.append([])
    else:
        data[-1].append(i)
    
summed = [sum(sub_list) for sub_list in data]

letsago = summed.index(max(summed)) + 1
top3 = sum(sorted(summed, reverse=True)[:3])

##pprint(letsago)
##pprint(max(summed))
pprint(top3)
