# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 13:29:01 2022

@author: Charl
"""

import csv
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

'''
Opens and plots dam data given as date in first column (%Y-%m-%d) and measured
amount of flow in ft^3/sec in the column. Also calculates total amount of water
flow over the duration of the data given.
'''

# Create necessary variables for reading data and caculating flow
x = []; y = []
pval = 0; pday = 0; wsum = 0

# Open and iterate through csv file by line
with open('dam_data.csv', newline='') as csvfile:
    dreader = csv.reader(csvfile, delimiter=',', quotechar='-')
    
    for row in dreader:
        if (len(row[1])>0): # Check to see if there is a measured flow value
            x.append(dt.datetime.strptime(row[0],'%Y-%m-%d').date()) # store date
            y.append(float(row[1])) # store flow value
            cday = dt.datetime.strptime(row[0],'%Y-%m-%d').date() # store current day
            cval = float(row[1])    # store current flow value
            # Bypass trapezoidal area calc if the previous flow was 0 (day 1)
            if (pval>0): #### potential for dropping days where flow was actually 0?
                h=cday-pday # get width of interval
                # add product of width of interval and current and previous flow values
                wsum += h.days*cval*pval
            pday=cday # make current day the previous day
            pval=cval # make current value of flow the previous value of flow

days = max(x)-min(x) # calculate # of days covered by data
#### why does .seconds not work?
scnds = days.days*24*60*60 # convert # of days to seconds 
voltot = .5*wsum*scnds # Adjust sum by 1/2 in accordance with trapezoidal rule
print("Total volume of water in the last year was ", voltot, "ft^3")
            
        
# Create plot of data points
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(x, y, color = 'xkcd:lightish blue', linestyle ='dashed', marker='^')
plt.xticks(rotation=25)
plt.ylabel('Daily Discharge (ft^3/sec)')
plt.title('Muddy River Dam, Overton NV')
vert=[10, 100, 200, 300, 400]
ylab=['10','100','200', '300','400']
plt.yticks(vert, ylab)
plt.legend()
plt.show()

    


