import webiopi
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
#lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec
#lcd.clear()
#lcd.message("Casetta al lago")
webiopi.sleep(1)

# Helper for LOW/HIGH values
GPIO = webiopi.GPIO

# *** MyLake test relay passo passo
# *** OUT
RelayLuceSala = 15
RelayLuceCamera = 14
# *** IN
LuceSala = 0 # *** Effettiva Accensione Luce
LuceCamera =1

# *** AUTOMAZIONE IRRIGAZIONE
AUTO = False
print ("Script MyLake is working")
# setup function is automatically called at WebIOPi startup
def setup():
    tmp = webiopi.deviceInstance("temp0") # retrieve the device named "tmp" in th
    mcp = webiopi.deviceInstance("mcp0") # retrieve the device named "mcp0" in the configuration 
    mcpLCD = webiopi.deviceInstance("mcp1")
    mcp.setFunction(RelayLuceSala, GPIO.OUT)
    mcp.setFunction(LuceSala, GPIO.IN)
	

# loop function is repeatedly called by WebIOPi 
def loop():
    webiopi.sleep(1)
    if (AUTO):
        celsius = tmp.getCelsius() # retrieve current temperature
        mcp.digitalWrite(RelayLuceSala, GPIO.HIGH)
        webiopi.sleep(1)
        mcp.digitalWrite(RelayLuceSala, GPIO.LOW)
        webiopi.sleep(30)

# destroy function is called at WebIOPi shutdown
def destroy():
    mcp = webiopi.deviceInstance("mcp0") # retrieve the device named "mcp" in the configuration 
    mcpLCD = webiopi.deviceInstance("mcp1") # retrieve the device named "mcp" in the configuration 
    mcp.digitalWrite(RelayLuceSala, GPIO.LOW) # turn off to avoid over heating
    mcp.digitalWrite(RelayLuceCamera, GPIO.LOW)
    mcp.digitalWrite(LuceSala, GPIO.IN)
    mcp.digitalWrite(LuceCamera, GPIO.IN)

# a simple macro to return heater mode
@webiopi.macro
def getMode():
    if (AUTO):
        return "auto"
    return "manual"

# simple macro to set and return heater mode
@webiopi.macro
def setMode(mode):
    global AUTO
    if (mode == "auto"):
        AUTO = True
    elif (mode == "manual"):
        AUTO = False
    return getMode()
