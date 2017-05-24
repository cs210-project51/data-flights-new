import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

incomeDict = {'AA': 2.676, 
              'AS': 0.251, 
              'B6': 0.759,  
              'DL': 4.373, 
              'HA': 0.244, 
              'UA': 2.263, 
              'WN': 2.2, 
              '9E': 0.0419, 
              'OO': 0.103, 
              'XE': 0.048, 
              'DH': 0.0961, 
              'US': 2.2,
              'F9': 0.0109}

avgDelay = {'AA': 6380905.22222222, 
            'AS': 1486018.55555556, 
            'B6': 1505594, 
            'DL': 4777007, 
            'HA': -23497.6666666667, 
            'UA': 5866346.44444444, 
            'WN': 10061853.3333333,
            
            '9E': 2006297.5, 
            'OO': 3627632.83333333, 
            'XE': 3235739, 
            'DH': 2149613.66666667, 
            'US': 3626777.55555556,
            'F9': 510897}


plt.scatter(avgDelay['AA'], incomeDict['AA'], label='AA')
plt.scatter(avgDelay['AS'], incomeDict['AS'], label='AS')
plt.scatter(avgDelay['B6'], incomeDict['B6'], label='B6')
plt.scatter(avgDelay['DL'], incomeDict['DL'], label='DL')
plt.scatter(avgDelay['HA'], incomeDict['HA'], label='HA')
plt.scatter(avgDelay['UA'], incomeDict['UA'], label='UA')
plt.scatter(avgDelay['WN'], incomeDict['WN'], label='WN')

plt.scatter(avgDelay['9E'], incomeDict['9E'], label='9E')
plt.scatter(avgDelay['OO'], incomeDict['OO'], label='OO')
plt.scatter(avgDelay['XE'], incomeDict['XE'], label='XE')
plt.scatter(avgDelay['DH'], incomeDict['DH'], label='DH')
plt.scatter(avgDelay['US'], incomeDict['US'], label='US')
plt.scatter(avgDelay['F9'], incomeDict['F9'], label='F9')

plt.xlabel('avg delay per year (min)')
plt.ylabel('income($billion)')
plt.xlim(-1000000, 15000000)
plt.ylim(0, 5)
plt.title('avarage delay per year \nvs \nincome')
plt.show()