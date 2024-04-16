import random

# data = []
# file = open("data.txt", "w")

# for i in range(1000):
#     m = random.randint(0,18446744073709551616)
#     # convert to bytes
#     data.append(m.to_bytes(8, byteorder='big'))

# file.write(str(data))
# file.close()
choice = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# st = ""
# for i in range(16):
#     st += random.choice(choice)

# print(st)

file = open("input100.txt", "w")
for i in range(1000):
    for j in range(100):
        file.write(random.choice(choice))

file.close()

