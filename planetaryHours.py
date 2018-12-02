'''
Created on Nov 22, 2018

@author: doktorbrown
'''


import time
import datetime
import ephem
# https://rhodesmill.org/pyephem/  pip install ephem
from astral import Astral
import Tkinter as tk

# https://github.com/sffjunkie/astral   pip install astral
# import swisseph as swe
# from Planetaries import Hours


city_name = 'choose from astral'

# print time.time()
# print time.time()+3600
yester= time.localtime(time.time()-86400)
# print time.localtime(time.time())
morrow= time.localtime(time.time()+86400)

localtime = time.asctime( time.localtime(time.time()) )
# print localtime

todayDate=datetime.date.today()
# print todayDate


dayOfWeek = todayDate.weekday()
yesterDayOfWeek = dayOfWeek -1
# print yesterDayOfWeek

if yesterDayOfWeek == 0:
    yesterDaysDay = "Monday       Moon"
elif yesterDayOfWeek == 1:
    yesterDaysDay = "Tuesday      Mars"
elif yesterDayOfWeek == 2:
    yesterDaysDay = "Wednesday    Mercury"
elif yesterDayOfWeek == 3:
    yesterDaysDay = "Thursday     Jupiter"
elif yesterDayOfWeek == 4:
    yesterDaysDay = "Friday       Venus"
elif yesterDayOfWeek == 5:
    yesterDaysDay = "Saturday     Saturn"
else:
    yesterDaysDay = "Sunday       Sun"
    
# print yesterDaysDay


# print dayOfWeek

if dayOfWeek == 0:
    todaysDay = "Monday       Moon"
elif dayOfWeek == 1:
    todaysDay = "Tuesday      Mars"
elif dayOfWeek == 2:
    todaysDay = "Wednesday    Mercury"
elif dayOfWeek == 3:
    todaysDay = "Thursday     Jupiter"
elif dayOfWeek == 4:
    todaysDay = "Friday       Venus"
elif dayOfWeek == 5:
    todaysDay = "Saturday     Saturn"
else:
    todaysDay = "Sunday       Sun"
    
# print todaysDay
    
dateE=str(todayDate)
# print dateE
# print todayDate + 1
# print todayDate - 1
dateSplit=dateE.split("-")
# print(dateSplit)
year = int(dateSplit[0])
# print(year)
month = int(dateSplit[1])
# print(month)
day = int(dateSplit[2])
# print(day)
# print(datetime.date.today())
# print(time.time()) 

m = ephem.Sun("2018")
sunConstellation = (ephem.constellation(m))



a = Astral()
a.solar_depression = 'civil'

city = a[city_name]

print('Information for %s/%s' % (city_name, city.region))
# Information for London/England

timezone = city.timezone
print('Timezone: %s' % timezone)
# Timezone: Europe/London

print('Latitude: %.02f; Longitude: %.02f' % (city.latitude, city.longitude))
# Latitude: 51.60; Longitude: 0.08
print "Local current time :", localtime
print "Sun is in",sunConstellation[1]
sun = city.sun(date=datetime.date(year, month, day), local=True)
# print('Dawn:    %s' % str(sun['dawn']))
# print('Sunrise: %s' % str(sun['sunrise']))
# print('Noon:    %s' % str(sun['noon']))
# print('Sunset:  %s' % str(sun['sunset']))
# print('Dusk:    %s' % str(sun['dusk']))

# print(sun)
sunRise = (sun['sunrise'])
# print sunRise, "sunRise"
sunSet = (sun['sunset'])
# print sunSet, "sunSet"
dayTime = sunSet - sunRise
# print dayTime, "dayTime"

sunTomorrow = city.sun(date=datetime.date(morrow[0],morrow[1],morrow[2]), local=True)
nextSunrise = sunTomorrow['sunrise']

sunYesterday = city.sun(date=datetime.date(yester[0],yester[1],yester[2]), local=True)
lastSunSet = sunYesterday['sunset']
lastSunrise = sunYesterday['sunrise']

# print lastSunrise, "lastSunrise"
# print lastSunset, "lastSunset"
lastDayTime = lastSunSet - lastSunrise
lastNightTime = sunRise - lastSunSet


# print nextSunrise, "nextSunrise"
nightTime = nextSunrise - sunSet

# print lastNightTime, "lastNightTime"
# print nightTime, "nightTime"

# print lastDayTime, "lastDayTime"
# print(dayTime), "daytime"

planetaryHourDayLength = (dayTime/12)

lastPlanetaryHourDayLength = (lastDayTime/12)
# print lastPlanetaryHourDayLength, "lastPlanetaryHourDayLength"

planetaryHourNightLength = (nightTime/12)
lastPlanetaryHourNightLength = (lastNightTime/12)



def moonCheck(a, year, month, day):
    moon_phase = a.moon_phase(date=datetime.date(year, month, day))
    moonPercent = moon_phase/29.53059
#     print(moon_phase), "Moon Phase", moonPercent
    return moon_phase, "Moon Phase", moonPercent

mc = ephem.Moon("2018")
moonConstellation = (ephem.constellation(mc))

print "Moon is in",moonConstellation[1]
print moonCheck(a, year, month, day)
# print yesterDaysDayTimeHoursLong(lastSunSet,lastPlanetaryHourNightLength,yesterDaysDay)
# print dayTimeHoursLong(sunRise,planetaryHourDayLength,todaysDay)
# print nightTimeHoursLong(sunSet, planetaryHourNightLength,todaysDay)

# print yesterDaysDayTimeHoursShort(lastSunrise,lastSunSet,lastPlanetaryHourNightLength,yesterDaysDay)
# print "Local current time :", localtime
# print rulingPlanet(sunRise)
# print dayTimeHoursShort(sunRise,planetaryHourDayLength,todaysDay)
# print "Local current time :", localtime, 
# print nightTimeHoursShort(sunRise,sunSet,planetaryHourNightLength,todaysDay)


# print str(sunRise.time())
# print sunRise.timetuple()[3:6]
# print sunRise.weekday()
# print sunRise.strftime("%H:%M")
# print sunRise.strftime("%W")
# print sunRise.strftime("%A")


class Hours:
        
    def __init__(self ):
        self.Hours = []
    
    def rulingPlanet(self,sunRise):
        chaldeanOrderDay=("Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn")
        if sunRise.strftime("%A") == "Sunday":
            ruler = chaldeanOrderDay[0]
        elif sunRise.strftime("%A") == "Monday":
            ruler = chaldeanOrderDay[1]
        elif sunRise.strftime("%A") == "Tuesday":
            ruler = chaldeanOrderDay[2]
        elif sunRise.strftime("%A") == "Wednesday":
            ruler = chaldeanOrderDay[3]
        elif sunRise.strftime("%A") == "Thursday":
            ruler = chaldeanOrderDay[4]
        elif sunRise.strftime("%A") == "Friday":
            ruler = chaldeanOrderDay[5]
        else: ruler = chaldeanOrderDay[6]
       
    
        return ruler
    
    def hourlyPlanet(self,rulingPlanet):
        chaldeanOrderDay=("Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn")
        chaldeanOrderHours=("Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter", "Mars")
        if rulingPlanet == "Sun":
            hourlyPlanetOUT = chaldeanOrderHours[0:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:3]
        elif rulingPlanet == "Moon":
            hourlyPlanetOUT = chaldeanOrderHours[3:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:6]
        elif rulingPlanet == "Mars":
            hourlyPlanetOUT = chaldeanOrderHours[6:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:2]
        elif rulingPlanet == "Mercury":
            hourlyPlanetOUT = chaldeanOrderHours[2:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:-2]
        elif rulingPlanet == "Jupiter":
            hourlyPlanetOUT = chaldeanOrderHours[5:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:1]
        elif rulingPlanet == "Venus":
            hourlyPlanetOUT = chaldeanOrderHours[1:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours[0:-3]
        else: hourlyPlanetOUT = chaldeanOrderHours[4:] + chaldeanOrderHours + chaldeanOrderHours + chaldeanOrderHours
        
        return hourlyPlanetOUT

            
    def hourOne(self,sunRise,planetaryHourDayLength,todaysDay,localtime):
        hourOne = sunRise + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= sunRise.strftime("%j:%H:%M") and tc <= hourOne.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""     
        return chaldean[0],chaldean[12],sunRise, hourOne, pHour, tcc
    
    def hourTwo(self, sunRise,planetaryHourDayLength,todaysDay,localtime):
        hourOne = self.hourOne(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourTwo = hourOne + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourOne.strftime("%j:%H:%M")[3] and tc <= hourTwo.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""     
        return chaldean[1],chaldean[13],hourOne, hourTwo, pHour, tcc
    
    def hourThree(self, sunRise,planetaryHourDayLength,todaysDay,localtime):
        hourTwo = self.hourTwo(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourThree = hourTwo + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourTwo.strftime("%j:%H:%M") and tc <= hourThree.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""         
        return chaldean[2],chaldean[14],hourTwo, hourThree, pHour, tcc
    
    def hourFour(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourThree = self.hourThree(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourFour = hourThree + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourThree.strftime("%j:%H:%M") and tc <= hourFour.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[3],chaldean[15],hourThree, hourFour, pHour, tcc
    

    def hourFive(self, sunRise,planetaryHourDayLength,todaysDay,localtime):
        hourFour = self.hourFour(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourFive = hourFour + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourFour.strftime("%j:%H:%M") and tc <= hourFive.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False 
            tcc = "" 
        return chaldean[4],chaldean[16],hourFour, hourFive, pHour, tcc
    
    def hourSix(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourFive = self.hourFive(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourSix = hourFive + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourFive.strftime("%j:%H:%M") and tc <= hourSix.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[5],chaldean[17],hourFive, hourSix, pHour, tcc
    
    def hourSeven(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourSix = self.hourSix(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourSeven = hourSix + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourSix.strftime("%j:%H:%M") and tc <= hourSeven.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[6],chaldean[18],hourSix, hourSeven, pHour, tcc
    
    def hourEight(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourSeven = self.hourSeven(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourEight = hourSeven + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourSeven.strftime("%j:%H:%M") and tc <= hourEight.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc 
        else:
            pHour = False
            tcc = ""   
        return chaldean[7],chaldean[19],hourSeven,hourEight, pHour, tcc
       
    def hourNine(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourEight = self.hourEight(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourNine = hourEight + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourEight.strftime("%j:%H:%M") and tc <= hourNine.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc 
        else:
            pHour = False
            tcc = ""   
        return chaldean[8],chaldean[20],hourEight, hourNine, pHour, tcc
    
    def hourTen(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourNine = self.hourNine(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourTen = hourNine + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourNine.strftime("%j:%H:%M") and tc <= hourTen.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[9],chaldean[21], hourNine, hourTen, pHour, tcc
    
    def hourEleven(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourTen = self.hourTen(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourEleven = hourTen + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourTen.strftime("%j:%H:%M") and tc <= hourEleven.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc
        else:
            pHour = False
            tcc = ""   
        return chaldean[10],chaldean[22],hourTen, hourEleven, pHour, tcc
    
    def hourTwelve(self, sunRise,planetaryHourDayLength,todaysDay, localtime):
        hourEleven = self.hourEleven(sunRise,planetaryHourDayLength,todaysDay,localtime)[3]
        hourTwelve = hourEleven + planetaryHourDayLength
        chaldean = self.hourlyPlanet(self.rulingPlanet(sunRise))
        tc = time.strftime("%j:%H:%M")
        if tc >= hourEleven.strftime("%j:%H:%M") and tc <= hourTwelve.strftime("%j:%H:%M"):
            pHour = True
            tcc = tc 
        else:
            pHour = False
            tcc = ""   
        return chaldean[11],chaldean[23],hourEleven, hourTwelve, pHour, tcc
 
h = Hours() 
# print h 

# Previous day so we can show from 00:00 to sunrise
pI = h.hourOne(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pII = h.hourTwo(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pIII = h.hourThree(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pIV = h.hourFour(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pV = h.hourFive(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pVI = h.hourSix(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pVII = h.hourSeven(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pVIII = h.hourEight(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pIX = h.hourNine(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pX = h.hourTen(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pXI = h.hourEleven(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
pXII = h.hourTwelve(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
print " "
print "lastPlanetaryHourNightLength:", lastPlanetaryHourNightLength, localtime
print " "
print pI[1],pI[2].strftime("%H:%M"),pI[3].strftime("%H:%M"),pI[4],pI[5]
print pII[1],pII[2].strftime("%H:%M"),pII[3].strftime("%H:%M"),pII[4],pII[5]
print pIII[1],pIII[2].strftime("%H:%M"),pIII[3].strftime("%H:%M"),pIII[4],pIII[5]
print pIV[1],pIV[2].strftime("%H:%M"),pIV[3].strftime("%H:%M"),pIV[4],pIV[5]
print pV[1],pV[2].strftime("%H:%M"),pV[3].strftime("%H:%M"),pV[4],pV[5]
print pVI[1],pVI[2].strftime("%H:%M"),pVI[3].strftime("%H:%M"),pVI[4],pVI[5]
print pVII[1],pVII[2].strftime("%H:%M"),pVII[3].strftime("%H:%M"),pVII[4],pVII[5]
print pVIII[1],pVIII[2].strftime("%H:%M"),pVIII[3].strftime("%H:%M"),pVIII[4],pVIII[5]
print pIX[1],pIX[2].strftime("%H:%M"),pIX[3].strftime("%H:%M"),pIX[4],pIX[5]
print pX[1],pX[2].strftime("%H:%M"),pX[3].strftime("%H:%M"),pX[4],pX[5]
print pXI[1],pXI[2].strftime("%H:%M"),pXI[3].strftime("%H:%M"),pXI[4],pXI[5]
print pXII[1],pXII[2].strftime("%H:%M"),pXII[3].strftime("%H:%M"),pXII[4],pXII[5]
print" "

dI = h.hourOne(sunRise, planetaryHourDayLength, todaysDay, localtime)
dII = h.hourTwo(sunRise, planetaryHourDayLength, todaysDay, localtime)
dIII = h.hourThree(sunRise, planetaryHourDayLength, todaysDay, localtime)
dIV = h.hourFour(sunRise, planetaryHourDayLength, todaysDay, localtime)
dV = h.hourFive(sunRise, planetaryHourDayLength, todaysDay, localtime)
dVI = h.hourSix(sunRise, planetaryHourDayLength, todaysDay, localtime)
dVII = h.hourSeven(sunRise, planetaryHourDayLength, todaysDay, localtime)
dVIII = h.hourEight(sunRise, planetaryHourDayLength, todaysDay, localtime)
dIX = h.hourNine(sunRise, planetaryHourDayLength, todaysDay, localtime)
dX = h.hourTen(sunRise, planetaryHourDayLength, todaysDay, localtime)
dXI = h.hourEleven(sunRise, planetaryHourDayLength, todaysDay, localtime)
dXII = h.hourTwelve(sunRise, planetaryHourDayLength, todaysDay, localtime)

print "planetaryHourDayLength:", planetaryHourDayLength, localtime
print " "
print dI[0],dI[2].strftime("%H:%M"),dI[3].strftime("%H:%M"),dI[4],dI[5]
print dII[0],dII[2].strftime("%H:%M"),dII[3].strftime("%H:%M"),dII[4],dII[5]
print dIII[0],dIII[2].strftime("%H:%M"),dIII[3].strftime("%H:%M"),dIII[4],dIII[5]
print dIV[0],dIV[2].strftime("%H:%M"),dIV[3].strftime("%H:%M"),dIV[4],dIV[5]
print dV[0],dV[2].strftime("%H:%M"),dV[3].strftime("%H:%M"),dV[4],dV[5]
print dVI[0],dVI[2].strftime("%H:%M"),dVI[3].strftime("%H:%M"),dVI[4],dVI[5]
print dVII[0],dVII[2].strftime("%H:%M"),dVII[3].strftime("%H:%M"),dVII[4],dVII[5]
print dVIII[0],dVIII[2].strftime("%H:%M"),dVIII[3].strftime("%H:%M"),dVIII[4],dVIII[5]
print dIX[0],dIX[2].strftime("%H:%M"),dIX[3].strftime("%H:%M"),dIX[4],dIX[5]
print dX[0],dX[2].strftime("%H:%M"),dX[3].strftime("%H:%M"),dX[4],dX[5]
print dXI[0],dXI[2].strftime("%H:%M"),dXI[3].strftime("%H:%M"),dXI[4],dXI[5]
print dXII[0],dXII[2].strftime("%H:%M"),dXII[3].strftime("%H:%M"),dXII[4],dXII[5]

print " "
  
I = h.hourOne(sunSet, planetaryHourNightLength, todaysDay, localtime)
II = h.hourTwo(sunSet, planetaryHourNightLength, todaysDay, localtime)
III = h.hourThree(sunSet, planetaryHourNightLength, todaysDay, localtime)
IV = h.hourFour(sunSet, planetaryHourNightLength, todaysDay, localtime)
V = h.hourFive(sunSet, planetaryHourNightLength, todaysDay, localtime)
VI = h.hourSix(sunSet, planetaryHourNightLength, todaysDay, localtime)
VII = h.hourSeven(sunSet, planetaryHourNightLength, todaysDay, localtime)
VIII = h.hourEight(sunSet, planetaryHourNightLength, todaysDay, localtime)
IX = h.hourNine(sunSet, planetaryHourNightLength, todaysDay, localtime)
X = h.hourTen(sunSet, planetaryHourNightLength, todaysDay, localtime)
XI = h.hourEleven(sunSet, planetaryHourNightLength, todaysDay, localtime)
XII = h.hourTwelve(sunSet, planetaryHourNightLength, todaysDay, localtime)

print "planetaryHourNightLength:", planetaryHourNightLength, localtime
print " "
print I[1],I[2].strftime("%H:%M"),I[3].strftime("%H:%M"),I[4],I[5]
print II[1],II[2].strftime("%H:%M"),II[3].strftime("%H:%M"),II[4],II[5]
print III[1],III[2].strftime("%H:%M"),III[3].strftime("%H:%M"),III[4],III[5]
print IV[1],IV[2].strftime("%H:%M"),IV[3].strftime("%H:%M"),IV[4],IV[5]
print V[1],V[2].strftime("%H:%M"),V[3].strftime("%H:%M"),V[4],V[5]
print VI[1],VI[2].strftime("%H:%M"),VI[3].strftime("%H:%M"),VI[4],VI[5]
print VII[1],VII[2].strftime("%H:%M"),VII[3].strftime("%H:%M"),VII[4],VII[5]
print VIII[1],VIII[2].strftime("%H:%M"),VIII[3].strftime("%H:%M"),VIII[4],VIII[5]
print IX[1],IX[2].strftime("%H:%M"),IX[3].strftime("%H:%M"),IX[4],IX[5]
print X[1],X[2].strftime("%H:%M"),X[3].strftime("%H:%M"),X[4],X[5]
print XI[1],XI[2].strftime("%H:%M"),XI[3].strftime("%H:%M"),XI[4],XI[5]
print XII[1],XII[2].strftime("%H:%M"),XII[3].strftime("%H:%M"),XII[4],XII[5]


def checkIt(chaldeanDay,chaldeanNight,hourStart, hourEnd, pHour, tcc):
    if pHour == True:
        j = (localtime)
        k=chaldeanDay,chaldeanNight,hourStart.strftime("%H:%M"), hourEnd.strftime("%H:%M")
    else:
        j=""
        k=""
    return j,k
  
# print V[4]    
# xx= checkIt(V[0],V[1],V[2],V[3],V[4], V[5])
# print xx
# xy = checkIt(VI[0],VI[1],VI[2],VI[3],VI[4], VI[5])
# print xy
  
# 
def update():
    lt = localtime

    pI = h.hourOne(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pII = h.hourTwo(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pIII = h.hourThree(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pIV = h.hourFour(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pV = h.hourFive(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pVI = h.hourSix(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pVII = h.hourSeven(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pVIII = h.hourEight(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pIX = h.hourNine(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pX = h.hourTen(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pXI = h.hourEleven(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)
    pXII = h.hourTwelve(lastSunSet, lastPlanetaryHourNightLength, yesterDaysDay, localtime)

    
    dI = h.hourOne(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dII = h.hourTwo(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dIII = h.hourThree(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dIV = h.hourFour(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dV = h.hourFive(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dVI = h.hourSix(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dVII = h.hourSeven(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dVIII = h.hourEight(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dIX = h.hourNine(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dX = h.hourTen(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dXI = h.hourEleven(sunRise, planetaryHourDayLength, todaysDay, localtime)
    dXII = h.hourTwelve(sunRise, planetaryHourDayLength, todaysDay, localtime)

    
    I = h.hourOne(sunSet, planetaryHourNightLength, todaysDay, localtime)
    II = h.hourTwo(sunSet, planetaryHourNightLength, todaysDay, localtime)
    III = h.hourThree(sunSet, planetaryHourNightLength, todaysDay, localtime)
    IV = h.hourFour(sunSet, planetaryHourNightLength, todaysDay, localtime)
    V = h.hourFive(sunSet, planetaryHourNightLength, todaysDay, localtime)
    VI = h.hourSix(sunSet, planetaryHourNightLength, todaysDay, localtime)
    VII = h.hourSeven(sunSet, planetaryHourNightLength, todaysDay, localtime)
    VIII = h.hourEight(sunSet, planetaryHourNightLength, todaysDay, localtime)
    IX = h.hourNine(sunSet, planetaryHourNightLength, todaysDay, localtime)
    X = h.hourTen(sunSet, planetaryHourNightLength, todaysDay, localtime)
    XI = h.hourEleven(sunSet, planetaryHourNightLength, todaysDay, localtime)
    XII = h.hourTwelve(sunSet, planetaryHourNightLength, todaysDay, localtime)
     
#     one.config(text= I[1],I[2].strftime("%H:%M"),I[3].strftime("%H:%M"),I[4],I[5])
#     two.config(text=II[1],II[2].strftime("%H:%M"),II[3].strftime("%H:%M"),II[4],II[5])
#     three.config(text=III[1],III[2].strftime("%H:%M"),III[3].strftime("%H:%M"),III[4],III[5])
#     four.config(text=IV[1],IV[2].strftime("%H:%M"),IV[3].strftime("%H:%M"),IV[4],IV[5])
#     five.config(text=V[1],V[2].strftime("%H:%M"),V[3].strftime("%H:%M"),V[4],V[5])
#     six.config(text=VI[1],VI[2].strftime("%H:%M"),VI[3].strftime("%H:%M"),VI[4],VI[5])
#     seven.config(text=VII[1],VII[2].strftime("%H:%M"),VII[3].strftime("%H:%M"),VII[4],VII[5])
#     eight.config(text=VIII[1],VIII[2].strftime("%H:%M"),VIII[3].strftime("%H:%M"),VIII[4],VIII[5])
#     nine.config(text=IX[1],IX[2].strftime("%H:%M"),IX[3].strftime("%H:%M"),IX[4],IX[5])
#     ten.config(text=X[1],X[2].strftime("%H:%M"),X[3].strftime("%H:%M"),X[4],X[5])
#     eleven.config(text=XI[1],XI[2].strftime("%H:%M"),XI[3].strftime("%H:%M"),XI[4],XI[5])
#     twelve.config(text=XII[1],XII[2].strftime("%H:%M"),XII[3].strftime("%H:%M"),XII[4],XII[5])
    ltt.config(text=lt)
    one.config(text= I[1])
    two.config(text=II[1])
    three.config(text=III[1])
    four.config(text=IV[1])
    five.config(text=V[1])
    six.config(text=VI[1])
    seven.config(text=VII[1])
    eight.config(text=VIII[1])
    nine.config(text=IX[1])
    ten.config(text=X[1])
    eleven.config(text=XI[1])
    twelve.config(text=XII[1])
 
    oneTwo.config(text= I[2].strftime("%H:%M"))
    twoTwo.config(text=II[2].strftime("%H:%M"))
#     threeThree.config(text=III[3])
#     fourThree.config(text=IV[3])
#     fiveThree.config(text=V[3])
#     sixThree.config(text=VI[3])
#     sevenThree.config(text=VII[3])
#     eightThree.config(text=VIII[3])
#     nineThree.config(text=IX[3])
#     tenThree.config(text=X[3])
#     elevenThree.config(text=XI[3])
#     twelveThree.config(text=XII[3])
#  
#     oneThree.config(text= I[3].strftime("%H:%M"))
#     twoThree.config(text=II[3].strftime("%H:%M"))
#        
#     root.after(100, update)  
#  
# root = tk.Tk()
# root.title("Planetary Hours")
# # root.toplevel(bg='green')  
#  
# ltt = tk.Label(text='TIME',padx=25)
# ltt.place(x=255, y=25)    
#  
# one = tk.Label(text='0',padx=25)    
# one.place(x=25, y=50)
#  
# oneTwo = tk.Label(text='0',padx=25)    
# oneTwo.place(x=100, y=50)  
#  
# oneThree = tk.Label(text='0',padx=25)    
# oneThree.place(x=175, y=50)  
#  
# two = tk.Label(text='0',padx=25)     
# two.place(x=25, y=75) 
#  
# twoTwo = tk.Label(text='0',padx=25)     
# twoTwo.place(x=100, y=75) 
#  
# twoThree = tk.Label(text='0',padx=25)     
# twoThree.place(x=175, y=75) 
#  
# three = tk.Label(text='0',padx=25)      
# three.place(x=25, y=100)
#  
# four = tk.Label(text='0',padx=25)     
# four.place(x=25, y=125)
#  
# five = tk.Label(text='0',padx=25)      
# five.place(x=25, y=150)
#  
# six = tk.Label(text='0',padx=25)     
# six.place(x=25, y=175)
#  
# seven = tk.Label(text='0',padx=25)     
# seven.place(x=25, y=200)
#  
# eight = tk.Label(text='0',padx=25) 
# eight.place(x=25, y=225)
#  
# nine = tk.Label(text='0',padx=25)      
# nine.place(x=25, y=250)
#  
# ten = tk.Label(text='0',padx=25)    
# ten.place(x=25, y=275)
#  
# eleven = tk.Label(text='0',padx=25)    
# eleven.place(x=25, y=300) 
#  
# twelve = tk.Label(text='0',padx=25)    
# twelve.place(x=25, y=325) 
#  
#   
# root.after(100, update)
# root.geometry("800x800+0+0") 
# root.mainloop() 



# def main():
#     m = ephem.Mars('1970')
#     print(ephem.constellation(m))
# 
# 
# 
# 
# 
# 
# if __name__ == '__main__':
#     pass
