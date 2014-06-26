'''Import of other modules'''
import math
import random

'''Execution of other scripts'''
exec(open('C:/IIER/PROJECT_Crop_nutrients/Python_model_implementation/Climate_data_v1.py').read())

'''Parameter initialization
lw1 layer 1 width in meters
lw2 layer 2 width in meters
lw3 layer 3 width in meters
lw4 layer 4 width in meters
ld1 layer 1 depth in meters
ld2 layer 2 depth in meters
ld3 layer 3 depth in meters
td total depth from lowest layer to surface (m)
wp1 pressure on soil in kPa layer 1
wp2 pressure on soil in kPa layer 2
wp3 pressure on soil in kPa layer 3

cl1 clay percentage layer 1
cl2 clay percentage layer 2
cl3 clay percentage layer 3

sl1 silt percentage layer 1
sl2 silt percentage layer 2
sl3 silt percentage layer 3

oc1 organic carbon percentage layer 1
oc2 organic carbon percentage layer 2
oc3 organic carbon percentage layer 3
sa1 sand percentage layer 1
sa2 sand percentage layer 2
sa3 sand percentage layer 3
pH1 pH measured by H2O for layer 1
pH2 pH measured by H2O for layer 2
pH3 pH measured by H2O for layer 3
cn1 carbo nitrogen ratio organic layer 1
cn2 carbo nitrogen ratio organic layer 2
cn3 carbo nitrogen ratio organic layer 3

ni1 nitrogen in kg NH4+ + NO3 - per hectare layer 1
ni2 nitrogen in kg NH4+ + NO3 - per hectare layer 2
ni3 nitrogen in kg NH4+ + NO3 - per hectare layer 3

no1 kg organic nitrogen per hectare layer 1
no2 kg organic nitrogen per hectare layer 2
no3 kg organic nitrogen per hectare layer 3

kora kor residue decomposition parameter 1
korb kor residue decomposition parameter 2
korc kor residue decomposition parameter 3

bdi1 initial bulk density in gram per cm3 layer 1
bdi2 initial bulk density in gram per cm3 layer 2
bdi3 initial bulk density in gram per cm3 layer 3
mbd1 mineral bulk density layer 1
mbd2  mineral bulk density layer 2
mbd3  mineral bulk density layer 3

obd organic bulk density 
bdt total bulk density of all three layers

somi percentage initial soil organic matter layer 1
somi1 percentage initial soil organic matter layer 1
somi2 percentage initial soil organic matter layer 2
somi3 percentage initial soil organic matter layer 3

woi1 is initial water content in m3 per m3  at 33 kPa in layer 1
woi2 is initial water content in m3 per m3  at 33 kPa in layer 2
woi3 is initial water content in m3 per m3  at 33 kPa in layer 3

wcf water content factor in m3 per m3 (strange unit? volume?)
rd regression coefficient D
re regression coefficient E
bs base saturation in percentage
cc cation exchange capacity in meq + per 100 grams
ca CaCo3 percentage in soil
la LAG factor

so1 stable organic carbon percentage in soil layer 1
so2 stable organic carbon percentage in soil layer 2
so3 stable organic carbon percentage in soil layer 3
cf coarse fragments in soil in percentage

soilt soil type in name
'''

kora = 0.2
korb = 0.05
korc = 0.0095

lw1 = 0.3
lw2 = 0.3
lw3 = 0.4
lw4 = 0.5

ld1 = lw1
ld2 = lw1 + lw2
ld3 = lw1 + lw2 + lw3

td = 1.5


wp1 = 0.165
wp2 = 0.14
wp3 = 0.14

cl1 = 35
cl2 = 22
cl3 = 32

sl1 = 59
sl2 = 49
sl3 = 56

oc1 = 2.85
oc2 = 1.2
oc3 = 0.2

sa1 = 6
sa2 = 29
sa3 = 13

pH1 = 5.7
pH2 = 6.8
pH3 = 7.2

cn1 = 10
cn2 = 10
cn3 = 9

bdi1 = 1.2
bdi2 = 1.6
bdi3 = 1.8

ni1 = lw1 * bdi1 * 100
ni2 = lw2 * bdi2 * 100
ni3 = lw3 * bdi3 * 100

no1 = (1 / cn1) * 10000000 * lw1 * bdi1 * ( oc1 / 100)
no2 = (1 / cn2) * 10000000 * lw2 * bdi2 * ( oc2 / 100)
no3 = (1 / cn3) * 10000000 * lw3 * bdi3 * ( oc3 / 100)

obd = 0.224


somi1 = oc1 * 1.724
somi2 = oc2 * 1.724
somi3 = oc3 * 1.724

mbd1 = ( 100 - somi1 ) / (( 100 / bdi1 ) - ( somi1 / obd ))
mbd2 = ( 100 - somi2 ) / (( 100 / bdi2 ) - ( somi2 / obd ))
mbd3 = ( 100 - somi3 ) / (( 100 / bdi3 ) - ( somi3 / obd ))

bdt = 1.56

woi1 = 0.27
woi2 = 0.3
woi3 = 0.3

wcf = 0.25
rd = 0.002208
re = -0.1434
bs = 100
cc = 30
ca = 0.18
la = 0.2

so1 = 0.015 * (cl1 + sl1 ) + 0.069 
so2 = 0.015 * (cl2 + sl2 ) + 0.069
so3 = 0.015 * (cl3 + sl3 ) + 0.069
cf = 50

soilt = []
if ca > 0.15:
    soilt.extend(['calcareous'])
elif (cc / cl1 / 100 ) > 100:
    soilt.extend(['slightly weathered'])
else:
    soilt.extend(['highly weathered'])

    '''Description of variables and parameters
Kos ?
Kor
fcnl1 ?
fcpl1 ?
fotl1 ?
pmom microbrial P concentration in kilogram per phosphorus per kg of organic matter?
orgi initial organic residue in kilogram per hectare
porg organic phosphorus in mg phosphorus per kilogram
porgi initial organic phosphorus in mg phosphorus per kilogram
org organic residue in kilogram per hectare
resi initial residue in kilogram phosphorus per hectare
res residue in kilogram phosphorus per hectare
resd residue decomposition in kilogram per hectare
stp stable Po in kilogram phosphorus per hectare
stpp Stable Po in percentage

plabi1 initial phosphorus labile in soil layer 1
plabi2 initial phosphorus labile in soil layer 2
plabi3 initial phosphorus labile in soil layer 3

rpr gross P mineralization rate from organic residue in kg P per pectare per day
rpo gross P mineralization rate from active organic P in kg P per hectare per day
rip gross P immobilization rate in kilogram phosphorus per hectare
pos active organic matter phosphorus in kilogram phosphorus per hectare
totp total soil organic phosphorus in kilogram phosphorus per hectare
totpi initial total soil organic phosphorus in kilogram phosphorus per hectare
'''

Kos = 0.0003
fcnl1 = 1
fcnl = 1
fcpl1 = 1
fcpl = 1

orgi1 = 3500
orgi2 = 0.01
orgi3 = 0.01

resi1 = orgi1 * 0.0025
resi2 = orgi2 * 0.0025
resi3 = orgi3 * 0.0025

porgi1 = 900 * ( 1 - math.exp(-1.1 * oc1 * 10)) * math.exp(-1.5 * ((pH1 - 10)/12)**2)
porgi2 = 900 * ( 1 - math.exp(-1.1 * oc2 * 10)) * math.exp(-1.5 * ((pH2 - 10)/12)**2)
porgi3 = 900 * ( 1 - math.exp(-1.1 * oc3 * 10)) * math.exp(-1.5 * ((pH3 - 10)/12)**2)

totpi1 = porgi1 * 10000 * 1000 * 0.3 * bdi1 / 10 ** 6
totpi2 = porgi2 * 10000 * 1000 * 0.3 * bdi2 / 10 ** 6
totpi3 = porgi3 * 10000 * 1000 * 0.3 * bdi3 / 10 ** 6

stp1 = so1 / oc1 * totpi1
stp2 = so2 / oc2 * totpi2
stp3 = so3 / (oc3 + 1.5) * totpi3

stpp1 = stp1 / (0.3 * 10000 * 1000 * 1.2)
stpp2 = stp2 / (0.3 * 10000 * 1000 * 1.2)
stpp3 = stp3 / (0.3 * 10000 * 1000 * 1.2)

plabi1 = 21.33
plabi2 = 0.1
plabi3 = 0.05

'''Calculation of surface temperature and dp maximum daping depth'''

st = []
k = 0
for i in list(range(0,365)):
    if i == Dmc:
        k = k + 1
    if Rf[i] > 0:
        st.extend([Tdmin[i] + 0.1 * (Tdmax[i] - Tdmin[i])])
    else:
        st.extend([((Tdmin[i] + Tdmax[i])/2  - Rd[k] / Dm[k] * (Tdmin[i] + 0.1 * (Tdmax[i] - Tdmin[i] ))) / (1 - ( Rd[k] / Dm[k] ))])


dp = 1 + (2.5 * bdt) / (bdt + math.exp(6.53 - 5.63 * bdt))

'''Integrated alculation of org, resd and Kor'''
'''bulk density calculations
bd bulk density after addition of residue in g per cm3
bdd change in bulk density between periods in g per cm3
wod 03 in m3 per m3 at 33 kPa
wc water content factor in m3 per m3 (strange unit? volume?)
wdwo water content factor ?????
'''

'''Parameter/Variable calculations single value at present
dp maximum damping depth in meters
sc scaling parameter
dd damping depth in meters
zd depth factor
dwl1 depth weighting factor layer 1'''

'''soil temperature final calculations
sti soil temperature inside soil in celsius
Ta long term average annual temperature in celsius'''

org1 = []
org2 = []
org3 = []
resd1 = []
resd2 = []
resd3 =[]
Kor1 = []
Kor2 = []
Kor3 = []
somd1 = []
somd2 = []
somd3 = []
som1 = []
som2 = []
som3 = []
bd1 = []
bd2 = []
bd3 = []
bdd1 = []
bdd2 = []
bdd3 = []
wc1 = []
wc2 = []
wc3 = []
wod1 = []
wod2 = []
wod3 = []
wdwo1 = []
wdwo2 = []
wdwo3 = []
sc = []
dd = []
zd1 = []
zd2 = []
zd3 = []
dwl1 = []
dwl2 = []
dwl3 = []
sti1 = []
sti2 = []
sti3 = []
fotl1 = []
fotl2 = []
fotl3 = []
for i in list(range(0,365)):
    if i == 0:
        wc1.extend([woi1])
        wc2.extend([woi2])
        wc3.extend([woi3])
        if (wcf / wc1[i]) > 1:
            wdwo1.extend([1])
        else:
            wdwo1.extend([wcf / wc1[i]])
        if (wcf / wc2[i]) > 1:
            wdwo2.extend([1])
        else:
            wdwo2.extend([wcf / wc2[i]])
        if (wcf / wc3[i]) > 1:
            wdwo3.extend([1])
        else:
            wdwo3.extend([wcf / wc3[i]])
        sc.extend([wc1[i] / ((0.356 - 0.144 * bdt) * td)])
        dd.extend([ dp * math.exp(math.log(0.5 / dp) * ((1 - sc[i]) / ( 1 + sc[i])) ** 2 ) ] )
        zd1.extend([   (2 * ld1 + lw2) / dd[i] * 2])
        zd2.extend([   (2 * ld2 + lw3) / dd[i] * 2])
        zd3.extend([   (2 * ld3 + lw4) / dd[i] * 2])
        dwl1.extend([ zd1[i] / (zd1[i] + math.exp( -0.867 - 2.08 * zd1[i]))])
        dwl2.extend([ zd2[i] / (zd2[i] + math.exp( -0.867 - 2.08 * zd2[i]))])
        dwl3.extend([ zd3[i] / (zd3[i] + math.exp( -0.867 - 2.08 * zd3[i]))])
        sti1.extend( [ (1 - la) * ( dwl1[i] * (Ta - st[i]) + st[i] ) ] )
        sti2.extend( [ (1 - la) * ( dwl2[i] * (Ta - st[i]) + st[i] ) ] )
        sti3.extend( [ (1 - la) * ( dwl3[i] * (Ta - st[i]) + st[i] ) ] )
        if ( 0.9 * sti1[i] / ( sti1[i] + math.exp(7.63 - 0.312 * sti1[i])) + 0.1 ) >= 1:
            fotl1.extend([1])
        else:
            fotl1.extend([0.9 * sti1[i] / ( sti1[i] + math.exp(7.63 - 0.312 * sti1[i])) + 0.1])
        if ( 0.9 * sti2[i] / ( sti2[i] + math.exp(7.63 - 0.312 * sti2[i])) + 0.1 ) >= 1:
            fotl2.extend([1])
        else:
            fotl2.extend([0.9 * sti2[i] / ( sti2[i] + math.exp(7.63 - 0.312 * sti2[i])) + 0.1])
        if ( 0.9 * sti3[i] / ( sti3[i] + math.exp(7.63 - 0.312 * sti3[i])) + 0.1 ) >= 1:
            fotl3.extend([1])
        else:
            fotl3.extend([0.9 * sti3[i] / ( sti3[i] + math.exp(7.63 - 0.312 * sti3[i])) + 0.1])
        org1.extend([orgi1])
        org2.extend([orgi2])
        org3.extend([orgi3])
        if org1[i] / orgi1 >= 0.8:
            Kor1.extend([kora])
        elif 0.1 < ( org1[i] / orgi1 ) < 0.8:
            Kor1.extend([korb])
        elif org1[i] / orgi1 <= 0.1:
            Kor1.extend([korc])
            
        if org2[i] / orgi2 >= 0.8:
            Kor2.extend([kora])
        elif 0.1 < ( org2[i] / orgi2 ) < 0.8:
            Kor2.extend([korb])
        elif org2[i] / orgi2 <= 0.1:
            Kor2.extend([korc])
            
        if org3[i] / orgi3 >= 0.8:
            Kor3.extend([kora])
        elif 0.1 < ( org3[i] / orgi3 ) < 0.8:
            Kor3.extend([korb])
        elif org3[i] / orgi3 <= 0.1:
            Kor3.extend([korc])
            
        resd1.extend([ Kor1[i] * org1[i] * (wdwo1[i] * fotl1[i]) ** 0.5 * min(fcnl,fcpl)])
        resd2.extend([ Kor2[i] * org2[i] * (wdwo2[i] * fotl2[i]) ** 0.5 * min(fcnl,fcpl)])
        resd3.extend([ Kor3[i] * org3[i] * (wdwo3[i] * fotl3[i]) ** 0.5 * min(fcnl,fcpl)])
        somd1.extend([ (((( orgi1 + (bdi1 * lw1 * 1000 * 10000 * (somi1 / 100)))) / (bdi1 * lw1 * 1000 * 10000 + orgi1)) - somi1 / 100 ) * 100 ])
        somd2.extend([ (((( orgi2 + (bdi2 * lw2 * 1000 * 10000 * (somi2 / 100)))) / (bdi2 * lw2 * 1000 * 10000 + orgi2)) - somi2 / 100 ) * 100 ])
        somd3.extend([ (((( orgi3 + (bdi3 * lw3 * 1000 * 10000 * (somi3 / 100)))) / (bdi3 * lw3 * 1000 * 10000 + orgi3)) - somi3 / 100 ) * 100 ])
        som1.extend([somi1 + somd1[i]])
        som2.extend([somi2 + somd2[i]])
        som3.extend([somi3 + somd3[i]])
        bd1.extend([ 100 / ((som1[i] / obd) + ((100 - som1[i]) / mbd1))])
        bd2.extend([ 100 / ((som2[i] / obd) + ((100 - som2[i]) / mbd2))])
        bd3.extend([ 100 / ((som3[i] / obd) + ((100 - som3[i]) / mbd3))])
        bdd1.extend([bd1[i] - bdi1])
        bdd2.extend([bd2[i] - bdi2])
        bdd3.extend([bd3[i] - bdi3])
        wod1.extend([rd * bdd1[i] + re * somd1[i]])
        wod2.extend([rd * bdd2[i] + re * somd2[i]])
        wod3.extend([rd * bdd3[i] + re * somd3[i]])

        
       
    if i > 0:
        wc1.extend([wc1[i-1] + wod1[i-1]])
        wc2.extend([wc2[i-1] + wod2[i-1]])
        wc3.extend([wc3[i-1] + wod3[i-1]])
        if (wcf / wc1[i]) > 1:
            wdwo1.extend([1])
        else:
            wdwo1.extend([wcf / wc1[i]])
        if (wcf / wc2[i]) > 1:
            wdwo2.extend([1])
        else:
            wdwo2.extend([wcf / wc2[i]])
        if (wcf / wc3[i]) > 1:
            wdwo3.extend([1])
        else:
            wdwo3.extend([wcf / wc3[i]])
        sc.extend([wc1[i] / ((0.356 - 0.144 * bdt) * td)])
        dd.extend([ dp * math.exp(math.log(0.5 / dp) * ((1 - sc[i]) / ( 1 + sc[i])) ** 2 ) ] )
        zd1.extend([   (2 * ld1 + lw2) / (dd[i] * 2)])
        zd2.extend([   (2 * ld2 + lw3) / (dd[i] * 2)])
        zd3.extend([   (2 * ld3 + lw4) / (dd[i] * 2)])
        dwl1.extend([ zd1[i] / (zd1[i] + math.exp( -0.867 - 2.08 * zd1[i]))])
        dwl2.extend([ zd2[i] / (zd2[i] + math.exp( -0.867 - 2.08 * zd2[i]))])
        dwl3.extend([ zd3[i] / (zd3[i] + math.exp( -0.867 - 2.08 * zd3[i]))])
        sti1.extend( [ sti1[i-1] * la + (1 - la) * ( dwl1[i] * (Ta - st[i]) + st[i] ) ] )
        sti2.extend( [ sti2[i-1] * la + (1 - la) * ( dwl2[i] * (Ta - st[i]) + st[i] ) ] )
        sti3.extend( [ sti3[i-1] * la + (1 - la) * ( dwl3[i] * (Ta - st[i]) + st[i] ) ] )
        if ( 0.9 * sti1[i] / ( sti1[i] + math.exp(7.63 - 0.312 * sti1[i])) + 0.1 ) >= 1:
            fotl1.extend([1])
        else:
            fotl1.extend([0.9 * sti1[i] / ( sti1[i] + math.exp(7.63 - 0.312 * sti1[i])) + 0.1])
        if ( 0.9 * sti2[i] / ( sti2[i] + math.exp(7.63 - 0.312 * sti2[i])) + 0.1 ) >= 1:
            fotl2.extend([1])
        else:
            fotl2.extend([0.9 * sti2[i] / ( sti2[i] + math.exp(7.63 - 0.312 * sti2[i])) + 0.1])
        if ( 0.9 * sti3[i] / ( sti3[i] + math.exp(7.63 - 0.312 * sti3[i])) + 0.1 ) >= 1:
            fotl3.extend([1])
        else:
            fotl3.extend([0.9 * sti3[i] / ( sti3[i] + math.exp(7.63 - 0.312 * sti3[i])) + 0.1])
            
        org1.extend([ org1[i-1] - resd1[i-1] ])
        org2.extend([ org2[i-1] - resd2[i-1] ])
        org3.extend([ org3[i-1] - resd3[i-1] ])
        if org1[i] / orgi1 >= 0.8:
            Kor1.extend([kora])
        elif 0.1 < (org1[i] / orgi1) < 0.8:
            Kor1.extend([korb])
        elif org1[i] / orgi1 <= 0.1:
            Kor1.extend([korc])

        if org2[i] / orgi2 >= 0.8:
            Kor2.extend([kora])
        elif 0.1 < (org2[i] / orgi2) < 0.8:
            Kor2.extend([korb])
        elif org2[i] / orgi2 <= 0.1:
            Kor2.extend([korc])

        if org3[i] / orgi3 >= 0.8:
            Kor3.extend([kora])
        elif 0.1 < (org3[i] / orgi3) < 0.8:
            Kor3.extend([korb])
        elif org3[i] / orgi3 <= 0.1:
            Kor3.extend([korc])
            
        resd1.extend([ Kor1[i] * org1[i] * (wdwo1[i] * fotl1[i]) ** 0.5 * min(fcnl,fcpl)])
        resd2.extend([ Kor2[i] * org2[i] * (wdwo2[i] * fotl2[i]) ** 0.5 * min(fcnl,fcpl)])
        resd3.extend([ Kor3[i] * org3[i] * (wdwo3[i] * fotl3[i]) ** 0.5 * min(fcnl,fcpl)])
        somd1.extend([ ((( (org1[i] - org1[i-1]) + (bd1[i-1] * 0.3 * 1000 * 10000 * (som1[i-1] / 100)))) / ((org1[i] - org1[i-1]) + 1000 * 10000 * 0.3 * bd1[i-1]) * 100 ) - som1[i-1]])
        somd2.extend([ ((( (org2[i] - org2[i-1]) + (bd2[i-1] * 0.3 * 1000 * 10000 * (som2[i-1] / 100)))) / ((org2[i] - org2[i-1]) + 1000 * 10000 * 0.3 * bd2[i-1]) * 100 ) - som2[i-1]])
        somd3.extend([ ((( (org3[i] - org3[i-1]) + (bd3[i-1] * 0.3 * 1000 * 10000 * (som3[i-1] / 100)))) / ((org3[i] - org3[i-1]) + 1000 * 10000 * 0.3 * bd3[i-1]) * 100 ) - som3[i-1]])
        som1.extend([som1[i-1] + somd1[i]])
        som2.extend([som2[i-1] + somd2[i]])
        som3.extend([som3[i-1] + somd3[i]])
        bd1.extend([ 100 / ((som1[i] / obd) + ((100 - som1[i]) / mbd1))])
        bd2.extend([ 100 / ((som2[i] / obd) + ((100 - som2[i]) / mbd2))])
        bd3.extend([ 100 / ((som3[i] / obd) + ((100 - som3[i]) / mbd3))])
        bdd1.extend([bd1[i] - bd1[i-1]])
        bdd2.extend([bd2[i] - bd2[i-1]])
        bdd3.extend([bd3[i] - bd3[i-1]])
        wod1.extend([rd * bdd1[i] + re * somd1[i]])
        wod2.extend([rd * bdd2[i] + re * somd2[i]])
        wod3.extend([rd * bdd3[i] + re * somd3[i]])     

        

'''Calculation of pmom'''

if plabi1 >= 10:
    pmom1 = 0.02
elif plabi1 < 10:
    pmom1 = 0.01 + 0.001 * plabi1

if plabi2 >= 10:
    pmom2 = 0.02
elif plabi2 < 10:
    pmom2 = 0.01 + 0.001 * plabi2

if plabi3 >= 10:
    pmom3 = 0.02
elif plabi3 < 10:
    pmom3 = 0.01 + 0.001 * plabi3

        


'''rip calculation'''

rip1 = [i * pmom1 * 0.16 for i in resd1]
rip2 = [i * pmom2 * 0.16 for i in resd2]
rip3 = [i * pmom3 * 0.16 for i in resd3]


'''Calculation of Porg and rpo and rpr and res
pos active organic matter phosphorus in kilogram phosphorus per hectare'''

rpo1 = []
rpr1 = []
porg1 = []
res1 = []
pos1 = []
totp1 = []
for i in list(range(0,365)):
    if i == 0:
        porg1.extend([porgi1])
        totp1.extend([totpi1])
        res1.extend([resi1])
        rpr1.extend([Kor1[i] * res1[i] * ((fotl1[i] * wdwo1[i]) ** 0.5) * min(fcnl,fcpl)])
        pos1.extend([ (totp1[i] - stp1) * 0.95])
        rpo1.extend([Kos * pos1[i] * min(wdwo1[i], fotl1[i])])
    elif i > 0:
        porg1.extend([ porg1[i-1] + ((( - rpo1[i-1] + 0.2 * rpr1[i-1]) / (0.3 * 10000 * 1000 * bd1[i-1])) ** 10 ** 6) ] )
        totp1.extend([totp1[i-1] - rpo1[i-1] + 0.2 * rpr1[i-1]])
        res1.extend([res1[i-1] - rpr1[i-1] + rip1[i-1]])
        rpr1.extend([Kor1[i] * res1[i] * ((fotl1[i] * wdwo1[i]) ** 0.5) * min(fcnl,fcpl)])
        pos1.extend( [ pos1[i-1] - rpo1[i-1] + 0.2 * rpr1[i-1] ] )
        rpo1.extend([Kos * pos1[i] * min(wdwo1[i], fotl1[i])])

rpo2 = []
rpr2 = []
porg2 = []
res2 = []
pos2 = []
totp2 = []
for i in list(range(0,365)):
    if i == 0:
        porg2.extend([porgi2])
        totp2.extend([totpi2])
        res2.extend([resi2])
        rpr2.extend([Kor2[i] * res2[i] * ((fotl2[i] * wdwo2[i]) ** 0.5) * min(fcnl,fcpl)])
        pos2.extend([ (totp2[i] - stp2) * 0.95])
        rpo2.extend([Kos * pos2[i] * min(wdwo2[i], fotl2[i])])
    elif i > 0:
        porg2.extend([ porg2[i-1] + ((( - rpo2[i-1] + 0.2 * rpr2[i-1]) / (0.3 * 10000 * 1000 * bd2[i-1])) ** 10 ** 6) ] )
        totp2.extend([totp2[i-1] - rpo2[i-1] + 0.2 * rpr2[i-1]])
        res2.extend([res2[i-1] - rpr2[i-1] + rip2[i-1]])
        rpr2.extend([Kor2[i] * res2[i] * ((fotl2[i] * wdwo2[i]) ** 0.5) * min(fcnl,fcpl)])
        pos2.extend( [ pos2[i-1] - rpo2[i-1] + 0.2 * rpr2[i-1] ] )
        rpo2.extend([Kos * pos2[i] * min(wdwo2[i], fotl2[i])])

rpo3 = []
rpr3 = []
porg3 = []
res3 = []
pos3 = []
totp3 = []
for i in list(range(0,365)):
    if i == 0:
        porg3.extend([porgi3])
        totp3.extend([totpi3])
        res3.extend([resi3])
        rpr3.extend([Kor3[i] * res3[i] * ((fotl3[i] * wdwo3[i]) ** 0.5) * min(fcnl,fcpl)])
        pos3.extend([ (totp3[i] - stp3) * 0.95])
        rpo3.extend([Kos * pos3[i] * min(wdwo3[i], fotl3[i])])
    elif i > 0:
        porg3.extend([ porg3[i-1] + ((( - rpo3[i-1] + 0.2 * rpr3[i-1]) / (0.3 * 10000 * 1000 * bd3[i-1])) ** 10 ** 6) ] )
        totp3.extend([totp3[i-1] - rpo3[i-1] + 0.2 * rpr3[i-1]])
        res3.extend([res3[i-1] - rpr3[i-1] + rip3[i-1]])
        rpr3.extend([Kor3[i] * res3[i] * ((fotl3[i] * wdwo3[i]) ** 0.5) * min(fcnl,fcpl)])
        pos3.extend( [ pos3[i-1] - rpo3[i-1] + 0.2 * rpr3[i-1] ] )
        rpo3.extend([Kos * pos3[i] * min(wdwo3[i], fotl3[i])])

'''calculation of cr
cr carbon content of oranic matter in kilogram  per hectare
'''
cr1 = [i * 0.4 for i in org1]
cr2 = [i * 0.4 for i in org2]
cr3 = [i * 0.4 for i in org3]

'''calculation of rpm
rpm net mineralization in kilogram phosphorus per hectare
'''

rpm1 = []
for i in list(range(0,365)):
    rpm1.extend([ 0.8 * rpr1[i] + rpo1[i] - rip1[i] ] )

rpm2 = []
for i in list(range(0,365)):
    rpm2.extend([ 0.8 * rpr2[i] + rpo2[i] - rip2[i] ] )

rpm3 = []
for i in list(range(0,365)):
    rpm3.extend([ 0.8 * rpr3[i] + rpo3[i] - rip3[i] ] )
        
