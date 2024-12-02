lastbox = []

s1 = ['B','S','V','Z','G','P','W']
s2 = ['J','V','B','C','Z','F']
s3 = ['V','L','M','H','N','Z','D','C']
s4 = ['L','D','M','Z','P','F','J','B']
s5 = ['V','F','C','G','J','B','Q','H']
s6 = ['G','F','Q','T','S','L','B']
s7 = ['L','G','C','Z','V']
s8 = ['N','L','G']   
s9 = ['J','F','H','C']

buffer = []
while True:
    listolist = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
    data = input("enter data").split()
    if data == []:
        break
    howmny = data[1]
    froms = data[3]
    tos = data[5]
    buffer = (listolist[int(froms) - 1])[(-int(howmny)):]
    buffer.reverse()
    del (listolist[int(froms) - 1])[(-int(howmny)):]
    (listolist[int(tos) - 1]).extend(buffer)


lastbox.extend(s1[-1:])
lastbox.extend(s2[-1:])
lastbox.extend(s3[-1:])
lastbox.extend(s4[-1:])
lastbox.extend(s5[-1:])
lastbox.extend(s6[-1:])
lastbox.extend(s7[-1:])
lastbox.extend(s8[-1:])
lastbox.extend(s9[-1:])
    

print(lastbox)