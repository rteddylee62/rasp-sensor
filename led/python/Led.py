# class for handling PIR functionality

import RPi.GPIO as GPIO
import sys
import time

class Led:

	def __init__( self, gpio, pin ):

		# initialize class variables
		self.gpio = gpio
		self.led = pin

	def setup( self ):

		# set up sensor for input
		self.gpio.setup( self.led, GPIO.OUT )
		self.off()

	def on( self ):

		# read the PIR sensor
		reading = self.gpio.output( self.led, GPIO.HIGH )

	def off( self ):

		# read the PIR sensor
		reading = self.gpio.output( self.led, GPIO.LOW )

# Test case
class LedTest:

	def __init__( self, gpio, pin ):

		# initialize class variables
		self.gpio = gpio
		self.led = pin


	def runTest( self ):

		sensor = Led( self.gpio, self.led )
		sensor.setup()

		try:
			while True:
				# turn LED off
				i = self.gpio.output( self.led, GPIO.LOW )
				time.sleep( 1.0 )

				# turn LED on
				i = self.gpio.output( self.led, GPIO.HIGH )
				time.sleep( 1.0 )

		except KeyboardInterrupt:  
			# here you put any code you want to run before the program   
			# exits when you press CTRL+C
			print "Keyboard interrupt"
			self.gpio.output( self.led, GPIO.LOW )

		except:  
			# this catches ALL other exceptions including errors.  
			# You won't get any error messages for debugging  
			# so only use it once your code is working  
			print "exception raised"
			self.gpio.output( self.led, GPIO.LOW )

		finally:
			print "gpio cleanup"
			self.gpio.cleanup() # this ensures a clean exit  


#//////////////////////////////////////////////////////////////////////////////
#// main()
#//////////////////////////////////////////////////////////////////////////////

def main( args ):
	print "in main"

	if len( args ) == 1:
		print "no pin for LED in command line"
		return

	# setup gpio
	print "set up gpio"
	GPIO.setwarnings( False )
	GPIO.setmode( GPIO.BCM )

	test = LedTest( GPIO, int( args[1] ) )

	print "runTest"
	test.runTest()
	

if __name__ == '__main__':
	print "calling main"

	main( sys.argv )

