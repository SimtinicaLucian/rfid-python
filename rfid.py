import pymongo
import RPi.GPIO as GPIO 
import MFRC522 
import signal 
import time
import json
from datetime import date 
import datetime

GPIO.setwarnings(False);
continue_reading = True
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["accessDB"]
mylog = mydb["log"]
myuser = mydb["user"]


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
pwm=GPIO.PWM(3, 50)
pwm.start(1)


# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print("Looking for cards")
print("Press Ctrl-C to stop.")

# This loop checks for chips. If one is near it will get the UID
try:
  
  while True:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

      # Print UID
        myquery = { "uid": str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3]) }
        doc = myuser.find(myquery)
        x = {"uid": str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3])}
        y = json.dumps(x); # parsare JSON
        
        result = False;
        for w in doc:
            if(result != ''):
                result = True;
                
        if result:
            print("Acces OK!")
            
            x = datetime.datetime.now()
            uidQuery = { "uid": str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3]), "name" : w["name"], "data" : x.strftime("%d.%m %H:%M") }
            mylog.insert_one(uidQuery)

            pwm.ChangeDutyCycle(6)
            time.sleep(5)
            pwm.ChangeDutyCycle(1)
        else:
            print("Denid Access!")
            GPIO.output(7, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(7, GPIO.LOW)



            
    

except KeyboardInterrupt:
  GPIO.cleanup()