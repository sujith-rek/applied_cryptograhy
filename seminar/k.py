import random 
cho = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

ar = []

for i in range(4):
    arr = []
    for j in range(4):
        ch = random.choice(cho)
        arr.append(ch)
        cho.remove(ch)
    
    ar.append(arr)

print(ar)