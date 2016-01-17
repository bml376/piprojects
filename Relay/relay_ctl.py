#!/bin/python

import RPi.GPIO as GPIO
import time
import argparse

class Relay():

    """
    Python script to test a 4-channel relay connected to a Raspberry Pi 2
    model B v 1.1.
    
    """

    def __init__(self):

        self.channels = [4, 17, 27, 22]

        GPIO.setmode(GPIO.BCM)

        for channel in self.channels:
            GPIO.setup(channel, GPIO.OUT)
            GPIO.output(channel, GPIO.HIGH)

    def sanityTest(self):

        for channel in self.channels:
            GPIO.output(channel, GPIO.LOW)
            print "Relay at GPIO: %s" % (str(channel))
            time.sleep(2)

        GPIO.cleanup()
        print "Good bye"

def main():

    parser = argparse.ArgumentParser(description="Relay Test Program")
    parser.add_argument("--mode", dest="mode",
                        help="Test mode",
                        default="sanity-test"
                       )

    args = parser.parse_args()
    mode = args.mode  

    relay = Relay()

    if mode == "sanity-test":
        relay.sanityTest()

if __name__ == "__main__":

    main()
