from matplotlib import pyplot as plt
import numpy

times = []
with open('sunsets.txt', 'r') as sunFile:
    days = 0
    for line in sunFile:
        days += 1
        minute = int(line[30: 32])
        hour = int(line[26: 29])
        if hour > 12:
            hour = hour - 12
        time = int(str(hour) + str(minute))
        times.append(time)
        
print(days)
print(times)
plt.plot(range(days), times)
plt.show()
