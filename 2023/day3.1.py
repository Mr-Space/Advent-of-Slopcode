import numpy as np

indata = []
vibecheck = []
total = 0

while True:
    data = input("enter data")
    if data == "end":
        break
    for char in data:
        indata.append(char)
    
array = np.array(indata)
newarray = array.reshape(10,10)
checkarray = np.pad(newarray, pad_width=1, mode='constant', constant_values=".")

#for x in np.nditer(newarray):
    #if a and b == 0:
         
    #print(newarray[a])

print(checkarray)
#print(newarray)
#print(newarray.shape)
#print(newarray[0][1])

