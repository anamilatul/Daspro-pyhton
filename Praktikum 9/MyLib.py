from Globals import *

def CheckOnOff() :
    global g_onoff
    return g_onoff

def TurnOnOff() :
    global g_onoff
    if CheckOnOff() == True :
        g_onoff = False
    else :
        g_onoff = True

def TempUp() :
    global g_temp
    if CheckOnOff() == True :
        if g_temp < 30 :
            g_temp = g_temp+1

def TempDown() :
    global g_temp
    if CheckOnOff() == True :
        if g_temp > 18 :
            g_temp = g_temp-1

def FanSpeed() :
    global g_fanlevel
    if CheckOnOff() == True :
        if g_fanlevel < 4 :
            g_fanlevel = g_fanlevel+1
        else:
            g_fanlevel = 1

def PowerChill() :
    global g_temp
    global g_fanlevel
    if CheckOnOff() == True :
        g_temp = 18
        g_fanlevel = 4

def Display() :
    global g_temp
    global g_fanlevel
    if CheckOnOff() == True :
        print("Temperatur suhu : ", g_temp)
        print("Level Kipas : ",g_fanlevel)
