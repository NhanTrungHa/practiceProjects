import math

time = 0.22
positions = [953.64,969.09,979.09,1001.4,1012.7,1055.9,1139.6,1150.0,1161.4, 1167.27,1175.9,1180.0,
             1182.3,1202.3,1216.36,1217.27,1194.5,1224.09,1246.36]

sum = 0
for x in positions:
    sum += round((x / time), 2)

average = sum / 20
print (average)

sum = 0
for x in positions:
    sum += (average - x) ** 2

sum = sum / 19
print(math.sqrt(sum))
