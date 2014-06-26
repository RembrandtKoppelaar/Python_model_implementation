'''Import of other modules'''
import math
import random

'''Execution of other scripts'''
exec(open('C:/IIER/PROJECT_Crop_nutrients/Python_model_implementation/Climate_data_v1.py').read())
exec(open('C:/IIER/PROJECT_Crop_nutrients/Python_model_implementation/Soil_data_organic_transformations_v1.py').read())

'''Description of initial parameters
cv1 curve number 1 dry
cv2 curve number 2 (5% slope)
cv2a urve adjusted for other slope
cv3 curve number 3 wet
slo slope in meter/meter
sig slope dependent parmaeter
cmf crop management factor ce
rtc amount of rainfull during time of concentration (mm)
pee erosion control practice factor
ami a min ???
re1 retention parameter for cn1
re2 retention parameter for cn2
re3 retention parameter for cn3
ffc fraction of field capacity
spw1 shape paremeter w1
spw2 shape paremeter w2
sfa s factor?
tct time of concentration (h)
tcc time of concentration of channel flow (h)
tcs time of concentration of surface flow (h)
dra drainage area in hectare
lcl channel length from most distant point to watershed outlet in kilometer
lsl slope length and steepness factor
acs average channel slope in meter per meter
slm slope length in meters
mcnc manning coefficient n for channel surface
mcnl manning coefficient n for land surface
kef soil erodibility factor
sa1 salt percentage in layer 1
sn1 ?
rokf ?
'''

cv2 = 89
slo = 0.05
cmf = 0.2
rtc = 0
pee = 7
sig = 0.3 * slo / (slo + math.exp(-1.47 - 61.09 * slo)) + 0.2
cv3 = cv2 * math.exp(0.00673 * (100 - cv2))
cv2a = (1/3) * (cv3 - cv2) * (1 - 2 * math.exp(-13.86 * slo)) + cv2
cv1 = cv2 - ((20 * (100 - cv2)) / (100 - cv2 + math.exp(2.533 - 0.0636 * (100 - cv2))))
sn1 = 1 - sa1/100
rokf = math.exp(-0.03 * cf)
kef = (0.2 + 0.3 * math.exp(-0.0256 * sa1 * (( 1 - sl1) / 100 )))    *  (( sl1 / (cl1 + sl1)) ** 0.3)    *   (1 - ((0.25 * oc1) / (oc1 + math.exp(3.72 - 2.95 * oc1 ))))   *    (1 - (0.7 * sn1) / ( sn1 + math.exp(-5.51 + 22.9 * sn1)))

re1 = 254 * ((100 / cv1) - 1 )
re2 = 254 * ((100 / cv2) - 1 )
re3 = 254 * ((100 / cv3) - 1 )
ffc = ( wcf - wp1 ) / ( woi1 - wp1 )
spw2 = 2 * ( math.log((0.5)/ (1 - (re2 / re1))) - 0.5 - math.log((1 / ( 1 - (re3 / re1))) - 1 ))
spw1 = math.log((1 / (1 - (re3 / re1) ) ) - 1 ) + spw2
sfa = re1 * (1 - (ffc / (ffc + math.exp(spw1 - spw2 * ffc))))

dra = 30
lcl = 2.5
acs = 0.05
slm = 50
mcnc = 0.01
mcnl = 0.005
lsl = ((slm / 22.1) ** sig) * (65.41 * (slo ** 2) + 4.56 * slo + 0.065)

tcc = (1.1 * lcl * mcnc ** 0.75) / (( dra ** 0.125) * (acs ** 0.375 ))
tcs = ((slm * mcnl) ** 0.6 ) / (18 * slo ** 0.3) 
tct = tcc + tcs
amin = tct / 23


'''Rainfall events calculation
yor years of record
tne total number of rainfall events
fre frequency of largest rainfall event
rfm mean monthly maximum 0.5 rainfall in mm
rfe mean amount of rainfall for each event in mm
mmr mean maximum 0.5h rainfall amount in mm
mme mean monthly rainfall for each evnt (mm)
a0h (0,5 h ) ?
'''

yor = 75
tne = [i * 75 for i in Rd]
fre = [1/(i * 2) for i in tne]
rfm = [19,16,20,24,28,16,19,22,29,0,20,15]
rfa = [a / b for a,b in zip(Rfd,Rd)]


mmr = []
for i in list(range(0,12)):
              mmr.extend([ rfm[i] /(-math.log(fre[i]))])

mme = [a / b for a,b in zip(Rfd,Rd)]

a0h = []
for i in list(range(0,12)):
        if i == 0:
            a0h.extend([0])
        elif mmr[i] / mme[i] > 1:
            a0h.extend([1])
        else:
            a0h.extend([mmr[i]/mme[i]])
              
    
'''rainfall variables calc
apro proprotion of total rainfall during tc
qrun q runoff value in mm
qrum q runoff value in m3
qpen q peak runoff rate in mm per h
qpem q peak runoff rate in m3 per s


'''

apro = []
for i in list(range(0,365)):
    apro.extend([random.random() * (1-amin) + amin])

qrun = []
for i in list(range(0,365)):
    if Rf[i] > (0.2 * re2):
        qrun.extend([ (( Rf[i] - 0.2 * re2) **2 ) / (Rf[i] + 0.8 * re2)])
    else:
        qrun.extend([0])

qrum = [i * 1000 for i in qrun]

qpem = []
for i in list(range(0,365)):
    qpem.extend([  (qrum[i] * apro[i] * dra)  / (  360  *   tct ) ] )

qpen = []
for i in list(range(0,365)):
    qpen.extend([  (qrun[i] * apro[i] * dra)  / (  360  *   tct ) ] )
    


'''rainfall estimates energy intensity etc.
r05 rainfall in 0.5 hours in mm
r0h rainfall in hours in mm per hour
pdr peak daily rainfall rate in mm per hour
dre daily ranfall energy in ?
rfe rainfall energy factor in ?

'''

r05 = []
k = 0 
for i in list(range(0,365)):
    if i <= Dmc[k]:
        r05.extend([Rf[i] * a0h[k]])
    elif i > Dmc[k]:
        k = k + 1
        r05.extend([Rf[i] * a0h[k]])
        
r0h = [i / 0.5 for i in r05]

pdr = []
k = 0
for i in list(range(0,365)):
    if i <= Dmc[k]:
        pdr.extend([ -2 * Rf[i] * math.log(1 - a0h[k])])
    elif i > Dmc[k]:
        k = k + 1
        pdr.extend([ -2 * Rf[i] * math.log(1 - a0h[k])])

dre = []
for i in list(range(0,365)):
    if pdr[i] > 0:
       dre.extend( [ Rf[i] * (12.1 + 8.9 * (math.log(pdr[i],10) - 0.434 ))])
    else:
       dre.extend([0])

rfe = []
for i in list(range(0,365)):
    if r0h[i] > 0:
        rfe.extend([dre[i] * r0h[i] / 1000 ])
    elif r0h[i] == 0:
        rfe.extend([0])
        

'''unknown variables calc + sediment  yield calc
xon x ONSTAD FOSTER
sdy sediment yield in ton per hectare'''

xon = []
for i in list(range(0,365)):
    xon.extend([ 0.646 * rfe[i] + 0.45 * (qrun[i] * qpem[i]) ** 0.33 ] )

sdy = []
for i in list(range(0,365)):
    sdy.extend([xon[i] * lsl * pee * kef * rokf * cmf])


'''rainfall calculations continued
dur rainfall duration in hours
fav average infilitration rate in mm per hour
rep peak rainfall excess rate in mm per hour
drr delivery ratio
csc sediment concentration in gram per m3
x2p x2 parameter
x1p x1 parameter
der enrichment ratio

'''

dur = []
for i in list(range(0,365)):
    if pdr[i] > 0:
        dur.extend([4.605 * Rf[i] / pdr[i]])
    else:
        dur.extend([0])

fav = []
for i in list(range(0,365)):
    if dur[i] > 0:
        fav.extend([ ( Rf[i] - qrun[i] ) / dur[i] ] )
    else:
        fav.extend([0])

rep = [a - b for a,b in zip(pdr,fav)]

drr = []
for i in list(range(0,365)):
    if rep[i] > 0:
        drr.extend([ (qpem[i] / rep[i])  ** 0.56 ] )
    else:
        drr.extend([0])

csc = []
for i in list(range(0,365)):
    if Rf[i] > 0:
        csc.extend([ ( sdy[i] / 10 ) * (1 / Rf[i]) * 10 ** 6 ])
    else:
        csc.extend([0])

x2p = []
for i in list(range(0,365)):
    if drr[i] > 0:
        x2p.extend([ - math.log((1 / drr[i]),10) / 2.699])
    else:
        x2p.extend([0])

x1p = []
for i in list(range(0,365)):
    if x2p[i] > 0:
        x1p.extend([ 1 / (( 0.25) ** x2p[i]) ])
    else:
        x1p.extend([0])

der = []
for i in list(range(0,365)):
    if csc[i] > 0:
        if x1p[i] > 0:
            der.extend([ x1p[i] * (csc[i] ** x2p[i])])
        else:
            der.extend([0])
    else:
        der.extend([0])



    
