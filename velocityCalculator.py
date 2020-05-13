time = 0.22
positions = [209.8, 213.2, 215.4,220.3,220.6,222.8,232.3,250.7,253.0,255.5,256.8,258.7,259.6,260.1,264.5,
             267.6,267.8,262.8,269.3,274.2]

sum = 0
for x in positions:
    sum += round((x / time), 2)

average = sum / 20
print (average)