from matplotlib import pyplot as plt
import numpy as np
#asdada
#afs
uniqueCarriers = ['AA',
'AQ',
'AS',
'B6',
'CO',
'DL',
'EV',
'F9',
'FL',
'HA',
'MQ',
'NW',
'OH',
'OO',
'TZ',
'UA',
'US',
'WN',
'XE',
'YV',
'9E',
'DH',
'HP']

median = [6307716,
17268,
1473647,
1445443.5,
2323384,
4039668,
3561209,
509402,
2378713.5,
-30035,
4343978,
2989737,
2544892,
3560296,
288165.5,
5831704,
3515474,
10423665,
3426474,
3489825,
2006297.5,
2638536,
1426245]
xs = [i + 0.1 for i, _ in enumerate(uniqueCarriers)]

for i in range(0, len(median)):
	median[i] = (median[i] / 60)/(10**5)


plt.bar(xs, median)

plt.ylabel("Median of 2000-2008 Total Delay per Year (x10^5)")
plt.xlabel("Unique Carrier Codes of Airlines")
plt.grid(linestyle=':', linewidth=0.5)
plt.xticks([i + 0.1 for i, _ in enumerate(uniqueCarriers)], uniqueCarriers)

plt.show()