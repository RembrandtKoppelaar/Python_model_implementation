'''Import of other modules'''
import math

'''Execution of other scripts'''
exec(open('C:/IIER/PROJECT_crop_nutrients/Python_model_implementation/Climate_data').read())

'''Parameter initialization
si soil erodability index in t/ha
rh ridge height value in mm
ri ridge interval value in mm
rr ridge roughness in mm
rrf ridge roughness factor as a factor
fl field length value in meters
fw field width value in meters
fsb factor standing biomass value as factor
fsr factor standign residue value as factor
ffr factor flat residue value as factor
aws average annual wind speed in m/s
mes minimal erosive wind speed in m/s
ftw fraction of time wind speed occurs in fraction from jan to dec
mws maximum wind speed in meters per second from jan to dec
ftw2 fraction of time wind speed occurs as second fraction from jan to dec
'''


si = 160
rh = 50
ri =500
fl = 4000
fw = 2000
fsb = 0.2
fsr = 0.4
ffr = 0.4
aws = 4.2
mes = 8
mws = [20,15,12,10,10,9,9,9,12,15,20,20]
ftw = [0.15,0.12,0.1,0.06,0.06,0.06,0.07,0.075,0.15,0.2,0.2,0.2]
ftw2 = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
rr = 4*rh**2 / ri

rrf = 0
if rr < 2.27:
    rrf = rrf + 1
if rr >= 2.27 and rr < 89:
    rrf = rrf + 1.125 - 0.153 * math.log(rr)
if rr >= 89:
    rrf = rrf + 0.336 * math.exp(0.00324 * rr)


    
'''Calculation of subclimatic factor based on rainfall values
Cfs climatic factor sub-parameter in ...? as a factor
Cf is climate factor parameter in ... as a factor
Tmmin is average minimum monthly temperature in Celsius from Jan to Dec
Rfma is average rainfall per day in a month in mm according to the model
Rfmf is the fake rainfall per month to test values
'''

Cfs = []
Rfmf = [10.16,10.16,10.16,10.16,10.16,10.16,10.16,10.16,10.16,10.16,10.16,10.16]
for i in list(range(0,12)):
        if Tmmin[i] >= -1.7:
            Cfs.extend([ 115*((Rfmf[i]/25.4)/(1.8*Tmmin[i]+22))**(10/9) ])
        else:
            Cfs.extend([ 115*((Rfmf[i]/25.4)/(1.8*-1.7+22))**(10/9)  ])

Cf = (386 * (aws**3)) / (( sum(Cfs))**2)

'''Calculation of E2, E3,E4, WL0, WF parameter value
E2 is ?
E3 is ?
E4 is ?
WL0 is ?
WF is ?
'''

E2 = rrf * si
E3 = rrf * si * Cf
WL0 = 1.56 * 10**6 * E2**-1.26 * math.exp(-0.00156 * E2)
WF = E2 * (1 - 0.1218 * ((fl / WL0) ** -0.3829 ) * math.exp( -3.33 * fl / WL0 ) )
E4 = (WF**0.3484 + E3**0.3484 - E2**0.3484 )**2.87


'''Biomass calculation?
Standing biomass in kg /ha
Vegetative cover equivalent factor as factor 
Flat residue kg per ha'''

'''Calculation for Lambda1, Lambda2 and E5'''

'''Calculation wind energy
Ams average monthly wind speed from Jan to Dec in meters per second
Dwe daily wind energy in kwh per m2
Dwea daily wind energy average per month in kwh per m2
Dmc is the cumulative number of days from Jan to Dec per month
V1 wind speed factor one
V2 wind speed factor two
Mwe is monthly wind energy in kwh per m2 from jan to dec
Awe is annual wind energy on average in kWh per m2
'''

Ams = [5,5,6,6,4,4,4,4,4,4,4,5]

V1 = []
V2 = []
k = 0
for i in list(range(0,365)):
        if i < Dmc[k]:
            V1.extend(([Ams[k] - 30]))
            V2.extend(([Ams[k] + 1]))
        else:
            k = (k + 1)
            V1.extend(([Ams[k] - 30 ]))
            V2.extend(([Ams[k] + 1 ]))

Dwe = []
for i in list(range(0,365)):
        Dwe.extend([193 * math.exp( 1.103 * V1[i] / V2[i])])

Dwea = []
for i in list(range(0,12)):
    Dwea.extend([sum(Dwe[Dmca[i]:Dmca[i+1]]) / Dm[i]])

Mwe = []
for i in list(range(0,12)):
    Mwe.extend([(Dwea[i] * ftw2[i] * mws[i] - mes * ftw[i] * Dwea[i] ) /  ( ( ftw2[i] * mws[i] ) - ( ftw[i] * mes ) ) ] )

Awe = 30.4 * sum(Mwe)



