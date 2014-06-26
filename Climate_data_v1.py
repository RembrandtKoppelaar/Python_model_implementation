import random
import itertools

'''Temperature data initialization
Tmmax is average maximum monthly temperature in Celsius from Jan to Dec
Tmmin is average minimum monthly temperature in Celsius from Jan to Dec
Ta is annual average temperature in celsius
Rae monthly average daily solar ratiation in MJ per m2 from Jan to Dec
Ral monthly average daily solar radiation in Langley (one langley equals 0.04187 MJ per m2 per day) from Jan to Dec
'''

Tmmax = [-7.78, -2.22, 1.67, 15.56, 22.22, 27.22, 29.44, 27.78, 23.89, 16.67, 7.22, -0.56]
Tmmin = [-13.34, -10.56, -4.44, 1.67, 7.78, 13.89, 16.11, 15.00, 3.33, 2.22, -4.44, -11.11]
Ta = sum(Tmmax + Tmmin) / 24
Rae = [10,12,15,18,20,23,26,24,18,15,10,8]
Ral = [x/0.04187 for x in Rae]

'''Rainfall data initialization
Rfd is rainfall per month in mm from Jan to Dec from the data source
Rd is average monthly rainy days from Jan to Dec
Dm is the number of days in a month from Jan to Dec
Pr is the probability that it will rain on a day in a month from Jan to Dec
Pd is the probability that it will be dry on a day in a month from Jan to Dec
Rfr is the amount of rain that will fall on a rainy day in mm for each month according to the model
'''

Rfd = [10.16, 32.00, 56.90, 38.10, 119.89, 124.97, 113.03, 103.89, 76.96, 67.06, 55.12, 35.05]
Rd = [7,7,9,9,11,11,9,9,8,7,8,8]
Dm = [31,28,31,30,31,30,31,31,30,31,30,31]
l = list(range(0,len(Rd))) 
Pr = [Rd[j]/Dm[j] for j in l]
Pd = [1 - Pr[j] for j in l]
Rfr = [Rfd[j]/Rd[j] for j in l]

'''Rainfall calculation per day
Rf is the rainfall per day in mm according to the model
Dmc is the cumulative number of days from Jan to Dec per month


Steps:
1) Create a cumulative list of the number of days from Jan to Dec
2) go through the list comparing the number of days from 0 to 365 with the cumulative
list indicating the month. If within the month select the appropriate rainfall
under a probability from the variables Pr and Rfr
'''

Dmc = list(itertools.accumulate(Dm))
Prd = []
Rf = []
k = 0
for i in list(range(0,365)): 
    if i < Dmc[k]:
        if random.random() < Pr[k]:
            Rf.extend([Rfr[k]])
        else:
            Rf.extend([0])
    else:
        k = (k + 1)
        if random.random() < Pr[k]:
            Rf.extend([Rfr[k]])
        else:
            Rf.extend([0])

'''for i in list(range(0,365)):
    if i < Dmc[k]:
        if random.random() <6'''
        
'''Temperature extremes calulation per day
Tdmax is the average daily maximum temperature in celsius
Tdmin is the average daily minimum temperature in celsius

Steps
1) compare the list of the number of days from 0 to 365 with the cumulative monthly list
Dmc and compare it with the min and max values per month Tmmax and Tmmin
'''

Tdmax = []
Tdmin = []
k = 0
for i in list(range(0,365)): 
    if i < Dmc[k]:
       Tdmax.extend([Tmmax[k]])
       Tdmin.extend([Tmmin[k]])
   
    else:
        k = (k + 1)
        Tdmax.extend([Tmmax[k]])
        Tdmin.extend([Tmmin[k]])

'''Calculation of average rainfall per day in a month
Rf is the rainfall per day in mm according to the model
Rfma is average rainfall per day in a month in mm according to the model
Dmca is the adjusted cumulative number of days from Jan to Dec per month
Dm is the number of days in a month from Jan to Dec '''

Dmca = [0] + Dmc
Rfma = []
for i in list(range(0,len(Rd))):
    Rfma.extend([sum(Rf[Dmca[i]:Dmca[i+1]]) / Dm[i]])

   
                  
