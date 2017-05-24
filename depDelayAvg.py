from matplotlib import pyplot as plt
import numpy as np

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

avgMinuteDelayed = [6380905.22222222,
48473.4,
1486018.55555556,
1505594,
2496272.33333333,
4777007,
3704775.66666667,
510897,
2145183.66666667,
-23497.6666666667,
4378475.375,
2814536.77777778,
2638735.2,
3627632.83333333,
286200,
5866346.44444444,
3626777.55555556,
10061853.3333333,
3235739,
3548808.33333333,
2006297.5,
2149613.66666667,
1699556.33333333]

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

for i in range(0, len(avgMinuteDelayed)):
	avgMinuteDelayed[i] = (avgMinuteDelayed[i] / 60)/(10**5)


x = plt.bar(xs, avgMinuteDelayed)

plt.ylabel("Avarage Hours Delayed per Year (x10^5)")
plt.xlabel("Unique Carrier Codes of Airlines")
plt.grid(linestyle=':', linewidth=0.5)
plt.xticks([i + 0.1 for i, _ in enumerate(uniqueCarriers)], uniqueCarriers)

plt.show()