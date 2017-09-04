# class for handling PIR functionality

import Led
import RPi.GPIO as GPIO
import sys
import time

class PirSensor:

	def __init__( self, gpio, pin ):

		# initialize class variables
		self.gpio = gpio
		self.pir = pin

	def setup( self ):

		# set up sensor for input
		self.gpio.setup( self.pir, GPIO.IN )

	def read(self):

		try:
			# read the PIR sensor
			reading = self.gpio.input(self.pir)
	
		except:  
			# this catches ALL other exceptions including errors.  
			# You won't get any error messages for debugging  
			# so only use it once your code is working  
			reading = -1  

	        return reading

# Test case
class PirSensorTest:

	def __init__(self, gpio, pin, ledPin):

		# initialize class variables
		self.gpio = gpio
		self.pir = pin

		self.led = Led.Led( gpio, ledPin )
		self.led.setup()

	def runTest( self ):

		sensor = PirSensor( self.gpio, self.pir )
		print "created sensor, setting it up"
		sensor.setup()
		print "sensor setup, now reading"
		
		val = 0

		try:
			print "starting while loop"
			while val != -1:
				print "reading PIR sensor"

				val = sensor.read()
				print "val = %d" % val

				if val==0:                 #When output from motion sensor is LOW
					# turn LED off
					print "turn off LED"
					self.led.off()
					time.sleep(0.5)

				elif val==1:               #When output from motion sensor is HIGH
					# turn LED on
					print "turn on LED"
					self.led.on()
					time.sleep(0.5)

		except KeyboardInterrupt:  
			# here you put any code you want to run before the program   
			# exits when you press CTRL+C  
			self.led.off()

		except:  
			# this catches ALL other exceptions including errors.  
			# You won't get any error messages for debugging  
			# so only use it once your code is working  
			print "exception raised"
			self.led.off()

		finally:
			print "gpio cleanup"
			self.gpio.cleanup() # this ensures a clean exit  


#//////////////////////////////////////////////////////////////////////////////
#// main()
#//////////////////////////////////////////////////////////////////////////////

def main( args ):
	print "in main"

	if len( args ) == 1:
		print "no pin for PIR sensor in command line"
		return

	# setup gpio
	print "set up gpio"
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	test = PirSensorTest( GPIO, int( args[1] ), 2 )

	print "runTest"
	test.runTest()
	

if __name__ == '__main__':

	main( sys.argv )

