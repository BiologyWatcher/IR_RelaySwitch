from time import sleep
import RPi.GPIO as GPIO

RelayPin = 11
IrPin = 18

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(IrPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(RelayPin,GPIO.OUT)
	GPIO.output(RelayPin,GPIO.LOW)

def loop():
	GPIO.add_event_detect(IrPin, GPIO.FALLING, bouncetime=2000, callback=cnt)  
        while True:
            pass

def cnt(ev=None):
                status = GPIO.input(RelayPin)
                if status == 1:
                    relayoff()
                elif status == 0:
                    relayon()

def relayoff():
    GPIO.output(RelayPin,GPIO.LOW)
    sleep(1)

def relayon():
    GPIO.output(RelayPin,GPIO.HIGH)
    sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':  
        setup()
        try:
                loop()
        except KeyboardInterrupt: 
                destroy()
