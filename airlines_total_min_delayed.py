
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

# These airlines operates today... We did not include the airlines which do not oparate in present.

AAdelays = [7865606,6181171,3770725,3459811,6196410,6307716,6776914,9066828,7802966]
ASdelays = [1899553,1652522,1144349,916855,1468593,2106401,1473647,1691897,1020350]
B6delays = [0,0,0,378292,556397,1139506,1751381,2767110,2440878]
COdelays = [3289400,2029647,821796,1171639,1775949,2323384,3393126,3774557,3886953]
DLdelays = [8287197,6018513,4011043,2973962,5193312,5218108,4039668,3686443,3564817]
HAdelays = [0,0,0,8062,-10680,-53692,-63173,-49390,27887]
UAdelays = [12895873,7399741,2720805,2512578,3978918,4612759,5831704,6648458,6196282]
WNdelays = [11470445,8230629,8447603,6360097,9955591,10423665,11224333,12094777,12349540]
delays9E = [0,0,0,0,0,0,0,2285792,1726803]

OOdelays = [0,0,0,2125532,2982997,2941282,4729541,4848850,4137595]
XEdelays = [0,0,0,1332807,1921948,2698243,4271628,5035103,4154705]
DHdelays = [0,0,0,2638536,2932459,877846,0,0,0]
USdelays = [6586411,3870767,1860425,1693836,2830401,3515474,3939983,5787520,2556181]
F9delays = [0,0,0,0,0,303223,453707,721561,565097]



years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008']

plt.scatter(years, AAdelays, label='AA')
plt.scatter(years, ASdelays, label='AS')
plt.scatter(years, B6delays, label='B6')
plt.scatter(years, COdelays, label='CO')
plt.scatter(years, DLdelays, label='DL')
plt.scatter(years, HAdelays, label='HA')
plt.scatter(years, UAdelays, label='UA')
plt.scatter(years, WNdelays, label='WN',marker='^')
plt.scatter(years, delays9E, label='9E',marker='^')
plt.scatter(years, OOdelays, label='OO',marker='^')
plt.scatter(years, XEdelays, label='XE',marker='^')
plt.scatter(years, DHdelays, label='DH',marker='^')
plt.scatter(years, USdelays, label='US',marker='^')
plt.scatter(years, F9delays, label='F9',marker='^')





plt.xlabel('years')
plt.ylabel('total min delayed')
plt.title('Airlines Total Min Delayed per Year')
plt.ylim(-1000000,15000000)
plt.legend()
plt.show()
