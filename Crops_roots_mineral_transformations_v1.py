'''Import of other modules'''
import math
import random
import numpy
import matplotlib
import matplotlib.pyplot as plt

'''Execution of other scripts'''
exec(open('C:/IIER/PROJECT_Crop_nutrients/Python_model_implementation/Climate_data_v1.py').read())
exec(open('C:/IIER/PROJECT_Crop_nutrients/Python_model_implementation/Soil_data_organic_transformations_v1.py').read())
exec(open('C:/IIER/PROJECT_Crop_nutrients/Python_model_implementation/runoff_water_erosion_v1.py').read())

'''Description of initial parameters
pcs phosphorus concentration in seed in kilogram phosphorus per kg of organic matter
phu ?
sbm seed biomass in kilogram per hectare
tbm minimum temperature for crop growth in ? celsius ?
hic rop specific harvest index
tog optimum temperature for growth in celsius
bec biomass energy crop parameter in kilogram per MegaJoule
asa soil aldebo in ?
laii initial leaf area index max ?
tsi tassel initation ti ?
ssa senescenceall leafs tf
paa parameter a
pab parameter b
lat latitude of watershed in degrees
'''


pcs = 0.00576
phu = 1900
sbm = 41.2952381
tbm = 8
hic = 0.5
tog = 25
bec = 0.002
asa = 0.2
laii = 4.27
tsi = 647
ssa = 1657
paa = 0.0075 
pab = 0.012
lat = 60

'''Description of initial parameters
ssl1 soil stress factor layer 1
ssl2 soil stress factor layer 2
ssl3 soil stress fator layer 3
bt11 parameter 1 for stress factor layer 1
bt12 parameter 1 for stress factor layer 2
bt13 parameter 1 for stress factor layer 3
bt21 parameter 2 for stress factor layer 1
bt22 parameter 2 for stress factor layer 2
bt23 parameter 2 for stress factor layer 3
bdl1 lower stress boundary layer 1
bdl2 lower stress boundary layer 2
bdl3 lower stress boundary layer 3
bdu1 upper stress boundary layer 1
bdu2 upper stress boundary layer 2
bdu3 upper stress boundary layer 3
awu water use parameter
rdm maximum root depth
'''

bdl1 = 1.15 + 0.00445 * sa1
bdl2 = 1.15 + 0.00445 * sa2
bdl3 = 1.15 + 0.00445 * sa3
bdu1 = 1.5 + 0.005 * sa1
bdu2 = 1.5 + 0.005 * sa2
bdu3 = 1.5 + 0.005 * sa3
bt21 = (math.log(0.0112 * bdl1) - math.log(8 * bdu1)) / (bdl1 - bdu1)
bt22 = (math.log(0.0112 * bdl2) - math.log(8 * bdu2)) / (bdl2 - bdu2)
bt23 = (math.log(0.0112 * bdl3) - math.log(8 * bdu3)) / (bdl3 - bdu3)
bt11 = math.log(0.0112 * bdl1) - bt21 * bdl1
bt12 = math.log(0.0112 * bdl2) - bt22 * bdl2
bt13 = math.log(0.0112 * bdl3) - bt23 * bdl3
ssl1 = 0.1 + 0.9 * bd1[0] / ( bd1[0] + math.exp(bt11 + bt21 * bd1[0]))
ssl2 = 0.1 + 0.9 * bd2[0] / ( bd2[0] + math.exp(bt12 + bt22 * bd2[0]))
ssl3 = 0.1 + 0.9 * bd3[0] / ( bd3[0] + math.exp(bt13 + bt23 * bd3[0]))
awu = 10
rdm = 1

'''Calculation of root temp stress factor l1
rts1 root temperature stress factor l1
rts2 root temperature stress factor l2
rts3 root temperature stress factor l3
rgf1 root growth stress factor l1
rgf2 root growth stress factor l2
rgf3 root growth stress factor l3
ucl1 compensation factor l1
ucl2 compensation factor l2
ucl3 compensation factor l3
'''

rts1 = []
for i in list(range(0,365)):
    if math.sin(( math.pi / 2) * ( sti1[i] - tbm) / (tog - tbm)) < 0:
        rts1.extend([0])
    else:
        rts1.extend([  math.sin(( math.pi / 2) * ( sti1[i] - tbm) / (tog - tbm))])

rts2 = []
for i in list(range(0,365)):
    if math.sin(( math.pi / 2) * ( sti2[i] - tbm) / (tog - tbm)) < 0:
        rts2.extend([0])
    else:
        rts2.extend([  math.sin(( math.pi / 2) * ( sti2[i] - tbm) / (tog - tbm))])


rts3 = []
for i in list(range(0,365)):
    if math.sin(( math.pi / 2) * ( sti3[i] - tbm) / (tog - tbm)) < 0:
        rts3.extend([0])
    else:
        rts3.extend([  math.sin(( math.pi / 2) * ( sti3[i] - tbm) / (tog - tbm))])

                      
rgf1 = [min(ssl1,i) for i in rts1]
rgf2 = [min(ssl2,i) for i in rts2]
rgf3 = [min(ssl3,i) for i in rts3]

ucl1 = rgf1
ucl2 = [a * b for a,b in zip(rgf1,rgf2)]
ucl3 = [a * b * c for a,b,c in zip(rgf1,rgf2,rgf3)]

'''calculation of solar values used for?
sda declination angle of the sun
hrl day length in hours
hrld change in day length in hours

'''

sda = []
for i in list(range(0,365)):
     sda.extend([ 0.4102 * math.sin(( 2 * math.pi /365) * (i + 90) - 80.25)])

hrl = []
for i in list(range(0,365)):
        hrl.extend([ 7.64 * math.cos( - math.tan(((2 * math.pi )/ 365) * lat) * math.tan(sda[i])) ** - 1  ])

hrld = []
for i in list(range(0,365)):
     if i > 0:
        hrld.extend([hrl[i] - hrl[i-1]])
     if i == 0:
        hrld.extend([0])


'''calculation heat and plant matter
huk daily heat unit accumulation in
hui heat unit index
hufh heat unit factor harvest
lai leaf area index in ?
hia actual harvest index
par photosynthetic active radiation in mj per m2
avm average daily monthly temperature in celsius
avd average daily temperature in celsius
ssv slope of saturation vapor pressure curve in kPa per degree celsius
tss temperature stress factor
'''

huk = []
for i in list(range(0,365)):
    huk.extend([ (Tdmax[i] + Tdmin[i] ) / 2 - tbm ] )
    
hui = []
j = 0
for i in list(range(0,365)):
     if i == 0:
         hui.extend([0])
         j = j + 1
     elif huk[i] < 0:
          hui.extend([0 + hui[i-1]])
          j = j + 1
     elif huk[i] >= 0:
          hui.extend([ sum(huk[j:i]) / phu])

hufh = []
for i in list(range(0,365)):
     hufh.extend([ (100 * hui[i]) / (100 * hui[i] + math.exp(11.1 - 10 * hui[i]) ) ] )


hia = [i * hic for i in hufh]

lai = []
k = 0 
for i in list(range(0,365)):
    if huk[i] < 0:
        lai.extend([0])
        k = k + 1
    elif (laii * (1 / (1 + math.exp( - pab * ( sum(huk[k:i]) - tsi ))) - math.exp(paa * (sum (huk[k:i]) - ssa)))) > 0 :
        lai.extend([ (laii * (1 / (1 + math.exp( - pab * ( sum(huk[k:i]) - tsi ))) - math.exp(paa * (sum (huk[k:i]) - ssa))))])
    else:
        lai.extend([0])
        

par = []
k = 0
for i in list(range(0,365)):
    if i <= Dmc[k]:
        par.extend([ 0.5 * Rae[k] * (1 - math.exp(-0.65 * lai[i])) ])
    if i > Dmc[k]:
        k = k + 1
        par.extend([0.5 * Rae[k] * (1 - math.exp(-0.65 * lai[i])) ])
   

avm = [(a + b) /2 for a,b in zip(Tmmax,Tmmin)]

avd = []
k = 0
for i in list(range(0,365)):
    if i <= Dmc[k]:
        avd.extend([avm[k]])
    if i > Dmc[k]:
        k = k + 1
        avd.extend([avm[k]])

ssv = []
for i in list(range(0,365)):
    ssv.extend([ math.exp( 21.3 - 5304 / (avd[i] + 273 )) * (5304 / ( avd[i] + 273) ** 2 ) ] )


tss = []
for i in list(range(0,365)):
    tss.extend(  [ math.sin(( math.pi / 2 ) * (avd[i] - tbm) / (tog - tbm)) ]   )

    '''Calculation of fractions
rwt fraction of biomass to root
rod root depth in meters

'''

rwt = [0.4  - 0.2 * i for i in hui]

rod = []
for i in list(range(0,365)):
    rod.extend([ rdm * (0.5 + 0.5 * math.sin( 3.03 * hui[i] - 1.47 ) ) ] )



'''Plant variables
Pdr potential plant dry matter increase in kilogram per hectare
gst growth stage
ste days between growth stages in days
optp optimum phosphorus concentration in kilogram phosphorus per kg organic matter
'''

Pdr = [i * bec * 10000   for i in par]

gst = []
ste = [21,42,63,84,105,126,147,168,189,210]
k = 0
for i in list(range(0,365)):
     if i < 92:
          gst.extend([0])
     elif  92 <= i < 302:
           if i < (92 + ste[k]):
               gst.extend([k+1])
           else:
               k = k + 1
               gst.extend([k+1])
     else:
           gst.extend([0])

optp = []
for i in list(range(0,365)):
     if gst[i] == 0:
          optp.extend([0])
     elif gst[i] <= 4:
          optp.extend([ 0.00684 - 0.00108 * gst[i]])
     elif gst[i] > 4:
          optp.extend([ 0.00238 - 0.000056 * gst[i]])

'''Description of variables and parameters
pia phosphorus input in kg phosphorus per hectare per day
pis phophorus input in mg phosphorus per kilogram of soil
soilt soil typ in name defined in soil data sheet
plab labile phosphorus in soil in mg per kilogram of soil
kas K factor
afact in (t)?
bfact in (t)?
sorp sorption factor in ?
base
desorp
'''


'''calculations of phosphorus inputs'''

pia1 = []
for i in list(range(0,365)):
        if i < 90:
            pia1.extend([0])
        elif 90 < i < 92:
            pia1.extend([75])
        else:
            pia1.extend([0])

pia2 = [0] * 365
pia3 = [0] * 365


pis1 = [a / b for a,b in zip(  [i * 10**6 for i in pia1]   , [ 10000 * bdi1 * 1000 * lw1 ] * 365 ) ]
pis2 = [0] * 365
pis3 = [0] * 365


'''calculation of labile phosphorus including runoff'''

'''Final values for transport and lost phosphorus in transport
ysp soluble phosphorus lost in runoff in kilogram per hectare
ypp transport of phosphorus by sediment in kilogram per hectare
'''

'''labile phosphorus layer calculations
lpf1 labile phosphorus factor layer 1
lpf2 labile phosphorus factor layer 2
lpf3 labile phosphorus factor layer 3
rpu1 plant phosphorus uptake layer 1 in kilogram phosphorus per hectare per day
rpu2 plant phosphorus uptake layer 2 in kilogram phosphorus per hectare per day
rpu3 plant phosphorus uptake layer 3 in kilogram phosphorus per hectare per day

plant growth variables integrated
frb1 fraction of root biomass in layer 1
frb2 fraction of root biomass in layer 2
frb3 fraction of root biomass in layer 3

ppt plant tissue phosphorus in kilogram per hectare
pdm plant dry matter in kilogram per hectare per day
optt optimal phosphorus in plant tissue in kilogram phosphorus per hectare
fps scaling factor
fpp stress factor
apd actual plant dry matter increase in kilogram per hectare per day

rpu1 plant phosphorus uptake in layer 1 in kilogram phosphorus per hectare per day
rpu2 plant phosphorus uptake in layer 1 in kilogram phosphorus per hectare per day
rpu3 plant phosphorus uptake in layer 1 in kilogram phosphorus per hectare per day
Plant Matter total aboveground
apm aboveground plant matter
sab sum of aboveground biomass and crop residue in ton per hectare
eas soil cover index
abo albedo of field
hon net radiation in megajoule per m2
epv potential evaporation in mm
epp potential plant water evaporation in mm

calculation of root biomass change
rwtd daily change in root weight in kilogram per hectare

upl1 potential water uptake layer 1
upl2 potential water uptake layer 2
upl3 potential water uptake layer 3
asw1 actual soil water use layer 1
asw2 actual soil water uptake layer 2
asw3 actual soil water uptake layer 3

rwc1 root weight change in l layer 1 in ?
rwc2 root weight change in layer 2 in ?
rwc3 root weight change in layer 3 in ?

Root biomass final calculations
rbl1 root biomass layer 1
rbl2 root biomass layer 2
rbl3 root biomass layer 3
'''


    
plab1 = []
plab2 = []
plab3 = []
ysp = []
ypp = []
lpf1 = []
lpf2 = []
lpf3 = []
frb1 = []
frb2 = []
frb3 = []
ppt = []
pdm = []
optt = []
fps = []
fpp = []
apd = []
rpu1 = []
rpu2 = []
rpu3 = []
rwtd  = []
apm = []
sab = []
eas = []
abo = []
hon = []
epv = []
epp = []
upl1 = []
asw1 = []
upl2 = []
asw2 = []
upl3 = []
asw3 = []
rwc1 = []
rwc2 = []
rwc3 = []
rbl1 = []
rbl2 = []
rbl3 = []

k = 0
    
for i in list(range(0,365)):
        if i == 0:
                plab1.extend([ pis1[0]])
                plab2.extend([ pis2[0]])
                plab3.extend([ pis3[0]])
                ysp.extend([ 0.01 * plab1[i] * qrun[i] / 175 ] )
                ypp.extend([ 0.001 * plab1[i] * sdy[i] * der[i]])
                lpf1.extend([ 0.1 + (( 0.9 * plab1[i]) / (plab1[i] + 117 * math.exp(-0.283 * plab1[i])))])
                lpf2.extend([ 0.1 + (( 0.9 * plab2[i]) / (plab2[i] + 117 * math.exp(-0.283 * plab2[i])))])
                lpf3.extend([ 0.1 + (( 0.9 * plab3[i]) / (plab3[i] + 117 * math.exp(-0.283 * plab3[i])))])
                ppt.extend([pcs * sbm])
                pdm.extend([sbm])
                optt.extend([optp[i] * pdm[i]])
                if optt[i] <= 0:
                   fps.extend([0])
                elif ( 2 * ( 1 - ppt[i] / (optt[i]))) < 0:
                   fps.extend([0])
                elif ( 2 * ( 1 - ppt[i] / (optt[i]))) >= 0:
                   fps.extend([ 2 * (1 - ppt[i] / optt[i])])
                fpp.extend([ 1 - fps[i] / ((fps[i]+0.000001) + math.exp(3.38 - 10.9 * fps[i])) ])
                apd.extend([ Pdr[i] * min(fpp[i], tss[i])])
                rwtd.extend([ apd[i] * ( 0.4 - 0.2 * hui[i] ) ])
                apm.extend([ (1 - rwt[i]) * sum(apd[0:i])])
                sab.extend([ (apm[i] + org1[i]) / 1000])
                eas.extend([ math.exp(-0.1 * sab[i])])
                abo.extend([0.23 * (1 - eas[i]) + asa * eas[i]])
                if i < Dmc[k]:
                      hon.extend([(2 * math.pi / 365) * Rae[k] * (1 - abo[i]) ])
                if i == Dmc[k]:
                      k = k +1
                      hon.extend([(2 * math.pi / 365) * Rae[k] * (1 - abo[i]) ])
                epv.extend([30.6 * hon[i] * (ssv[i] / 0.68 + ssv[i])])
                if 0 < lai[i] < 3:
                    epp.extend([  epv[i] * lai[i] / 3 ])
                else:
                    epp.extend([ epv[i]])
                if ( epp[i] / (1 - math.exp( -awu)) * ( 1 - math.exp( - awu * ( ld1 / rod[i] )) - (1 - ucl1[i]) * (1 - math.exp( - awu * (0 / rod[i])))) ) >= 0:
                    upl1.extend([ epp[i] / (1 - math.exp( -awu)) * (1 - math.exp( - awu * ( ld1 / rod[i] )) - (1 - ucl1[i]) * (1 - math.exp( - awu * (0 / rod[i]))))])
                else:
                    upl1.extend([0])
                if wcf < (( wc1[i] - wp1) / 4 + wp1):
                    asw1.extend([ (upl1[i] * math.exp(5 * ((4 * wcf - wp1) / ( wc1[i] - wp1) - 1 ))) * rgf1[i] ])
                else:
                    asw1.extend([ upl1[i] * rgf1[i] ])
                if ( epp[i] / (1 - math.exp( -awu)) * ( 1 - math.exp( - awu * ( ld2 / rod[i] )) - (1 - ucl2[i]) * (1 - math.exp( - awu * (cf / rod[i])))) - ucl2[i] * asw1[i]) >= 0:
                    upl2.extend([ epp[i] / (1 - math.exp( -awu)) * (1 - math.exp( -awu * ( ld2 / rod[i] )) - (1 - ucl2[i]) * (1 - math.exp( - awu * (cf / rod[i])))) - ucl2[i] * asw1[i] ])
                else:
                    upl2.extend([0])
                    
                if wcf < (( wc2[i] - wp2) / 4 + wp2):
                    asw2.extend([ (upl2[i] * math.exp(5 * ((4 * wcf - wp2) / ( wc2[i] - wp2) - 1 ))) * rgf2[i] ])
                else:
                    asw2.extend([ upl2[i] * rgf2[i] ])
                if ( epp[i] / (1 - math.exp( -awu)) * ( 1 - math.exp( - awu * ( ld3 / rod[i] )) - (1 - ucl3[i]) * (1 - math.exp( - awu * (cf / rod[i])))) - ucl3[i] * (asw1[i] + asw2[i])) >= 0:
                    upl3.extend([ epp[i] / (1 - math.exp( -awu)) * (1 - math.exp( -awu * ( ld3 / rod[i] )) - (1 - ucl3[i]) * (1 - math.exp( - awu * (cf / rod[i])))) - ucl3[i] * (asw1[i] + asw2[i])])
                else:
                    upl3.extend([0])
                if wcf < (( wc3[i] - wp3) / 4 + wp3):
                    asw3.extend([ (upl3[i] * math.exp(5 * ((4 * wcf - wp3) / ( wc3[i] - wp3) - 1 ))) * rgf3[i] ])
                else:
                    asw3.extend([ upl3[i] * rgf3[i] ])
                if (asw1[i] + asw2[i] + asw3[i]) > 0:
                    rwc1.extend([ rwtd[i] * (asw1[i] / (asw1[i] + asw2[i] + asw3[i])) ])
                else:
                    rwc1.extend([0])
                if (asw1[i] + asw2[i] + asw3[i]) > 0:
                    rwc2.extend([ rwtd[i] * (asw2[i] / (asw1[i] + asw2[i] + asw3[i])) ])
                else:
                    rwc2.extend([0])
                if (asw1[i] + asw2[i] + asw3[i]) > 0:
                    rwc3.extend([ rwtd[i] * (asw3[i] / (asw1[i] + asw2[i] + asw3[i])) ])
                else:
                    rwc3.extend([0])
                rbl1.extend([ sum(rwc1[0:i])])
                rbl2.extend([ sum(rwc2[0:i])])
                rbl3.extend([ sum(rwc3[0:i])])
                if (rbl1[i] + rbl2[i] + rbl3[i]) > 0:
                    frb1.extend([ rbl1[i] / (rbl1[i] + rbl2[i] + rbl3[i])])
                else:
                    frb1.extend([0])
                if (rbl1[i] + rbl2[i] + rbl3[i]) > 0:
                    frb2.extend([ rbl2[i] / (rbl1[i] + rbl2[i] + rbl3[i])])
                else:
                    frb2.extend([0])
                if (rbl1[i] + rbl2[i] + rbl3[i]) > 0:
                    frb3.extend([ rbl3[i] / (rbl1[i] + rbl2[i] + rbl3[i])])
                else:
                    frb3.extend([0])
                rpu1.extend([ 1.5 * optp[i] * apd[i] * min(wdwo1[i], lpf1[i], frb1[i])])
                rpu2.extend([ 1.5 * optp[i] * apd[i] * min(wdwo2[i], lpf2[i], frb2[i])])
                rpu3.extend([ 1.5 * optp[i] * apd[i] * min(wdwo3[i], lpf3[i], frb3[i])])
                
        elif i > 0:
                plab1.extend([plab1[i-1] + pis1[i] - (rpu1[i-1] / (10000 * 1000 * 0.3 * bd1[i-1]) * 10 ** 6) + (rpm1[i] / (10000 * 1000 * 0.3 * bd1[i-1]) * 10 **6) - (ysp[i-1] + ypp[i-1])])
                plab2.extend([plab2[i-1] + pis2[i] - (rpu2[i-1] / (10000 * 1000 * 0.3 * bd2[i-1]) * 10 ** 6) + (rpm2[i] / (10000 * 1000 * 0.3 * bd2[i-1]) * 10 **6)])
                plab3.extend([plab3[i-1] + pis3[i] - (rpu3[i-1] / (10000 * 1000 * 0.3 * bd3[i-1]) * 10 ** 6) + (rpm3[i] / (10000 * 1000 * 0.3 * bd3[i-1]) * 10 **6)])
                ysp.extend([ 0.01 * plab1[i] * qrun[i] / 175 ] )
                ypp.extend([ 0.001 * plab1[i] * sdy[i] * der[i]])
                lpf1.extend([ 0.1 + (( 0.9 * plab1[i]) / (plab1[i] + 117 * math.exp(-0.283 * plab1[i])))])
                lpf2.extend([ 0.1 + (( 0.9 * plab2[i]) / (plab2[i] + 117 * math.exp(-0.283 * plab2[i])))])
                lpf3.extend([ 0.1 + (( 0.9 * plab3[i]) / (plab3[i] + 117 * math.exp(-0.283 * plab3[i])))])
                ppt.extend([ppt[i-1] + rpu1[i-1]])
                pdm.extend([pdm[i-1] + apd[i-1]])
                optt.extend([optp[i] * pdm[i]])
                if optt[i] <= 0:
                    fps.extend([0])
                elif ( 2 * ( 1 - ppt[i] / (optt[i]))) < 0:
                    fps.extend([0])
                elif ( 2 * ( 1 - ppt[i] / (optt[i]))) >= 0:
                    fps.extend([ 2 * (1 - ppt[i] / optt[i])])
                fpp.extend([ 1 - fps[i] / ((fps[i]+0.000001) + math.exp(3.38 - 10.9 * fps[i])) ])
                apd.extend([ Pdr[i] * min(fpp[i], tss[i])])
                rwtd.extend([ apd[i] * ( 0.4 - 0.2 * hui[i] ) ])
                apm.extend([ (1 - rwt[i]) * sum(apd[0:i])])
                sab.extend([ (apm[i] + org1[i]) / 1000])
                eas.extend([ math.exp(-0.1 * sab[i])])
                abo.extend([0.23 * (1 - eas[i]) + asa * eas[i]])
                if i < Dmc[k]:
                      hon.extend([(2 * math.pi / 365) * Rae[k] * (1 - abo[i]) ])
                if i == Dmc[k]:
                      k = k +1
                      hon.extend([(2 * math.pi / 365) * Rae[k] * (1 - abo[i]) ])
                epv.extend([30.6 * hon[i] * (ssv[i] / 0.68 + ssv[i])])
                if 0 < lai[i] < 3:
                    epp.extend([  epv[i] * lai[i] / 3 ])
                else:
                    epp.extend([ epv[i]])
                if ( epp[i] / (1 - math.exp( -awu)) * ( 1 - math.exp( - awu * ( ld1 / rod[i] )) - (1 - ucl1[i]) * (1 - math.exp( - awu * (0 / rod[i])))) ) >= 0:
                    upl1.extend([ epp[i] / (1 - math.exp( -awu)) * (1 - math.exp( - awu * ( ld1 / rod[i] )) - (1 - ucl1[i]) * (1 - math.exp( - awu * (0 / rod[i]))))])
                else:
                    upl1.extend([0])
                if wcf < (( wc1[i] - wp1) / 4 + wp1):
                    asw1.extend([ (upl1[i] * math.exp(5 * ((4 * wcf - wp1) / ( wc1[i] - wp1) - 1 ))) * rgf1[i] ])
                else:
                    asw1.extend([ upl1[i] * rgf1[i] ])
                    
                if ( epp[i] / (1 - math.exp( -awu)) * ( 1 - math.exp( - awu * ( ld2 / rod[i] )) - (1 - ucl2[i]) * (1 - math.exp( - awu * (cf / rod[i])))) - ucl2[i] * asw1[i]) >= 0:
                    upl2.extend([ epp[i] / (1 - math.exp( -awu)) * (1 - math.exp( -awu * ( ld2 / rod[i] )) - (1 - ucl2[i]) * (1 - math.exp( - awu * (cf / rod[i])))) - ucl2[i] * asw1[i]])
                else:
                    upl2.extend([0])
                    
                if wcf < (( wc2[i] - wp2) / 4 + wp2):
                    asw2.extend([ (upl2[i] * math.exp(5 * ((4 * wcf - wp2) / ( wc2[i] - wp2) - 1 ))) * rgf2[i] ])
                else:
                    asw2.extend([ upl2[i] * rgf2[i] ])
                    
                if ( epp[i] / (1 - math.exp( -awu)) * ( 1 - math.exp( - awu * ( ld3 / rod[i] )) - (1 - ucl3[i]) * (1 - math.exp( - awu * (cf / rod[i])))) - ucl3[i] * (asw1[i] + asw2[i])) >= 0:
                    upl3.extend([ epp[i] / (1 - math.exp( -awu)) * (1 - math.exp( -awu * ( ld3 / rod[i] )) - (1 - ucl3[i]) * (1 - math.exp( - awu * (cf / rod[i])))) - ucl3[i] * (asw1[i] + asw2[i])])
                else:
                    upl3.extend([0])
                if wcf < (( wc3[i] - wp3) / 4 + wp3):
                    asw3.extend([ (upl3[i] * math.exp(5 * ((4 * wcf - wp3) / ( wc3[i] - wp3) - 1 ))) * rgf3[i] ])
                else:
                    asw3.extend([ upl3[i] * rgf3[i] ])
                if (asw1[i] + asw2[i] + asw3[i]) > 0:
                    rwc1.extend([ rwtd[i] * (asw1[i] / (asw1[i] + asw2[i] + asw3[i])) ])
                else:
                    rwc1.extend([0])
                if (asw1[i] + asw2[i] + asw3[i]) > 0:
                    rwc2.extend([ rwtd[i] * (asw2[i] / (asw1[i] + asw2[i] + asw3[i])) ])
                else:
                    rwc2.extend([0])
                if (asw1[i] + asw2[i] + asw3[i]) > 0:
                    rwc3.extend([ rwtd[i] * (asw3[i] / (asw1[i] + asw2[i] + asw3[i])) ])
                else:
                    rwc3.extend([0])
                rbl1.extend([ sum(rwc1[0:i])])
                rbl2.extend([ sum(rwc2[0:i])])
                rbl3.extend([ sum(rwc3[0:i])])
                if (rbl1[i] + rbl2[i] + rbl3[i]) > 0:
                    frb1.extend([ rbl1[i] / (rbl1[i] + rbl2[i] + rbl3[i])])
                else:
                    frb1.extend([0])
                if (rbl1[i] + rbl2[i] + rbl3[i]) > 0:
                    frb2.extend([ rbl2[i] / (rbl1[i] + rbl2[i] + rbl3[i])])
                else:
                    frb2.extend([0])
                if (rbl1[i] + rbl2[i] + rbl3[i]) > 0:
                    frb3.extend([ rbl3[i] / (rbl1[i] + rbl2[i] + rbl3[i])])
                else:
                    frb3.extend([0])
                rpu1.extend([ 1.5 * optp[i] * apd[i] * min(wdwo1[i], lpf1[i], frb1[i])])
                rpu2.extend([ 1.5 * optp[i] * apd[i] * min(wdwo2[i], lpf2[i], frb2[i])])
                rpu3.extend([ 1.5 * optp[i] * apd[i] * min(wdwo3[i], lpf3[i], frb3[i])])


'''
fyh final yield in kilogram per hectare
'''

fyh = [a * b for a,b in zip(apm, hia)]
          

'''Calculation of psp factors and kas and afact, bfact, base, sorp, desorp '''

psp1 = []
psp2 = []
psp3 = []
for i in list(range(0,365)):
        if soilt == ['calcareous']:
                psp1.extend([ -0.053 * math.log(cl1) - 0.029 * oc1 + 0.42 + 0.001 * (plab1[i] - pis1[i])])
                psp2.extend([ -0.053 * math.log(cl2) - 0.029 * oc2 + 0.42 + 0.001 * (plab2[i] - pis2[i])])
                psp3.extend([ -0.053 * math.log(cl3) - 0.029 * oc3 + 0.42 + 0.001 * (plab3[i] - pis3[i])])
        elif soilt == ['highly weathered']:
                psp1.extend([ -0.053 * math.log(cl1) - 0.029 * oc1 + 0.42 + 0.001 * (plab1[i] - pis1[i])])
                psp2.extend([ -0.053 * math.log(cl2) - 0.029 * oc2 + 0.42 + 0.001 * (plab2[i] - pis2[i])])
                psp3.extend([ -0.053 * math.log(cl3) - 0.029 * oc3 + 0.42 + 0.001 * (plab3[i] - pis3[i])])
        elif soilt == ['slightly weathered']:
                psp1.extend([ 0.0043 * bs + 0.11 * pH1 - 0.7 + 0.0034 * (plab1[i] - pis1[i])])
                psp2.extend([ 0.0043 * bs + 0.11 * pH2 - 0.7 + 0.0034 * (plab2[i] - pis2[i])])
                psp3.extend([ 0.0043 * bs + 0.11 * pH3 - 0.7 + 0.0034 * (plab3[i] - pis3[i])])
        
if soilt == ['calcareous']:
    kas = [0.0076] * 365
else:
    kast = [a - b for a,b in zip([a * b for a,b in zip([-1.77] * 365, psp)], [-7.05] * 365)]
    kas = math.exp(i for i in kast) 

afact1 = [i * 0.918 for i in [math.exp(i) for i in [i * -4.603 for i in psp1]]]
afact2 = [i * 0.918 for i in [math.exp(i) for i in [i * -4.603 for i in psp2]]]
afact3 = [i * 0.918 for i in [math.exp(i) for i in [i * -4.603 for i in psp3]]]

bfact1 = [i * -0.238 - 1.126 for i in [math.log(i) for i in afact1]]
bfact2 = [i * -0.238 - 1.126 for i in [math.log(i) for i in afact2]]
bfact3 = [i * -0.238 - 1.126 for i in [math.log(i) for i in afact3]]

base1 = [i * -1.08 + 0.79 for i in psp1]
base2 = [i * -1.08 + 0.79 for i in psp2]
base3 = [i * -1.08 + 0.79 for i in psp3]

sorp1 = []
sorp2 = []
sorp3 = []
for i in list(range(0,365)):
    sorp1.extend([afact1[i] * (i + 1) ** bfact1[i]])
    sorp2.extend([afact2[i] * (i + 1) ** bfact2[i]])
    sorp3.extend([afact3[i] * (i + 1) ** bfact3[i]])

desorp1 = []
desorp2 = []
desorp3 = []
for i in list(range(0,365)):
    desorp1.extend([base1[i] * (i + 1) ** -0.29])
    desorp2.extend([base2[i] * (i + 1) ** -0.29])
    desorp3.extend([base3[i] * (i + 1) ** -0.29])

'''calculation of active and stable phosphorus
psp ?
pspc = 1 - psp
pact labile phosphorus in soil in mg per kilogram of soil
psta stabile phosphorus in soil in mg per kilogram of soil
pmas phosphorus moved from active to stabile
pmla phosphorus moved from labile to active
'''

pspc1 = [a - b for a,b in zip([1] * 365, psp1)]
pspc2 = [a - b for a,b in zip([1] * 365, psp2)]
pspc3 = [a - b for a,b in zip([1] * 365, psp3)]

pact1 = [a * b for a,b in zip(plab1, [a / b for a,b in zip(pspc1,psp1)] ) ]
pact2 = [a * b for a,b in zip(plab2, [a / b for a,b in zip(pspc2,psp2)] ) ]
pact3 = [a * b for a,b in zip(plab3, [a / b for a,b in zip(pspc3,psp3)] ) ]

psta1 = []
psta2 = []
psta3 = []
pmas1 = []
pmas2 = []
pmas3 = []
pmla1 = []
pmla2 = []
pmla3 = []
for i in list(range(0,365)):
    if i == 0:
        psta1.extend([4 * pact1[1]])
        psta2.extend([4 * pact2[1]])
        psta3.extend([4 * pact3[1]])
        if pact1[i] * 4 - psta1[i] > 0:
                pmas1.extend([kas[i] * (4 * pact1[i] - psta1[i])])
        elif pact1[i] * 4 - psta1[i] < 0:
                pmas1.extend([kas[i] * (4 * pact1[i] - psta1[i])])
        else:
                pmas1.extend([0])
        if pact2[i] * 4 - psta2[i] > 0:
                pmas2.extend([kas[i] * (4 * pact2[i] - psta2[i])])
        elif pact2[i] * 4 - psta2[i] < 0:
                pmas2.extend([kas[i] * (4 * pact2[i] - psta2[i])])
        else:
                pmas2.extend([0])
        if pact3[i] * 4 - psta3[i] > 0:
                pmas3.extend([kas[i] * (4 * pact3[i] - psta3[i])])
        elif pact2[i] * 4 - psta2[i] < 0:
                pmas3.extend([kas[i] * (4 * pact3[i] - psta3[i])])
        else:
                pmas3.extend([0])
        if (plab1[i] - pact1[i] * psp1[i] / (1 - psp1[i]) ) > 0:
                pmla1.extend( [sorp1[i] * ( plab1[i] - ( pact1[i] * psp1[i] ) / (1 - psp1[i]) ) ] )
        elif (plab1[i] - pact1[i] * psp1[i] / (1 - psp1[i]) ) < 0:
                pmla1.extend( [desorp1[i] * ( plab1[i] - ( pact1[i] * psp1[i] ) / (1 - psp1[i]) ) ] )
        else:
                pmla1.extend([0])
        if (plab2[i] - pact2[i] * psp2[i] / (1 - psp2[i]) ) > 0:
                pmla2.extend( [sorp2[i] * ( plab2[i] - ( pact2[i] * psp2[i] ) / (1 - psp2[i]) ) ] )
        elif (plab2[i] - pact2[i] * psp2[i] / (1 - psp2[i]) ) < 0:
                pmla2.extend( [desorp2[i] * ( plab2[i] - ( pact2[i] * psp2[i] ) / (1 - psp2[i]) ) ] )
        else:
                pmla2.extend([0])
        if (plab3[i] - pact3[i] * psp3[i] / (1 - psp3[i]) ) > 0:
                pmla3.extend( [sorp3[i] * ( plab3[i] - ( pact3[i] * psp3[i] ) / (1 - psp3[i]) ) ] )
        elif (plab3[i] - pact3[i] * psp3[i] / (1 - psp3[i]) ) < 0:
                pmla3.extend( [desorp3[i] * ( plab3[i] - ( pact3[i] * psp3[i] ) / (1 - psp3[i]) ) ] )
        else:
                pmla3.extend([0])
        
    if i > 0:
        psta1.extend([psta1[i-1] + pmas1[i-1]])
        psta2.extend([psta2[i-1] + pmas2[i-1]])
        psta3.extend([psta3[i-1] + pmas3[i-1]])
        if pact1[i] * 4 - psta1[i] > 0:
                pmas1.extend([kas[i] * (4 * pact1[i] - psta1[i])])
        elif pact1[i] * 4 - psta1[i] < 0:
                pmas1.extend([kas[i] * (4 * pact1[i] - psta1[i])])
        else:
                pmas1.extend([0])
        if pact2[i] * 4 - psta2[i] > 0:
                pmas2.extend([kas[i] * (4 * pact2[i] - psta2[i])])
        elif pact2[i] * 4 - psta2[i] < 0:
                pmas2.extend([kas[i] * (4 * pact2[i] - psta2[i])])
        else:
                pmas2.extend([0])
        if pact3[i] * 4 - psta3[i] > 0:
                pmas3.extend([kas[i] * (4 * pact3[i] - psta3[i])])
        elif pact2[i] * 4 - psta2[i] < 0:
                pmas3.extend([kas[i] * (4 * pact3[i] - psta3[i])])
        else:
                pmas3.extend([0])
        if (plab1[i] - pact1[i] * psp1[i] / (1 - psp1[i]) ) > 0:
                pmla1.extend( [sorp1[i] * ( plab1[i] - ( pact1[i] * psp1[i] ) / (1 - psp1[i]) ) ] )
        elif (plab1[i] - pact1[i] * psp1[i] / (1 - psp1[i]) ) < 0:
                pmla1.extend( [desorp1[i] * ( plab1[i] - ( pact1[i] * psp1[i] ) / (1 - psp1[i]) ) ] )
        else:
                pmla1.extend([0])
        if (plab2[i] - pact2[i] * psp2[i] / (1 - psp2[i]) ) > 0:
                pmla2.extend( [sorp2[i] * ( plab2[i] - ( pact2[i] * psp2[i] ) / (1 - psp2[i]) ) ] )
        elif (plab2[i] - pact2[i] * psp2[i] / (1 - psp2[i]) ) < 0:
                pmla2.extend( [desorp2[i] * ( plab2[i] - ( pact2[i] * psp2[i] ) / (1 - psp2[i]) ) ] )
        else:
                pmla2.extend([0])
        if (plab3[i] - pact3[i] * psp3[i] / (1 - psp3[i]) ) > 0:
                pmla3.extend( [sorp3[i] * ( plab3[i] - ( pact3[i] * psp3[i] ) / (1 - psp3[i]) ) ] )
        elif (plab3[i] - pact3[i] * psp3[i] / (1 - psp3[i]) ) < 0:
                pmla3.extend( [desorp3[i] * ( plab3[i] - ( pact3[i] * psp3[i] ) / (1 - psp3[i]) ) ] )
        else:
                pmla3.extend([0])


