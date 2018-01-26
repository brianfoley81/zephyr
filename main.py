#!/usr/bin/python
from time import time, sleep
from numpy import median
import Adafruit_DHT
import logging

sleep_time = 5
items_per_avg = 20

c_data = []
h_data = []

c_median = 0
h_median = 0

logging.basicConfig(filename="/var/log/fans.log", level=logging.INFO)

logging.critical("Started up at " + str( int( time() ) ) )
logging.critical(str(sleep_time) +" second sleep, " + str(items_per_avg) +" items avg")

while True:
	sleep(sleep_time)
	hum, c_temp = Adafruit_DHT.read_retry(22, 4)
	#f_temp =  c_temp * (9/5) + 32

	c_data.append(c_temp)
	h_data.append(hum)

	if len(c_data) >= items_per_avg:
		c_median = median(c_data)
		h_median = median(h_data)

		logging.info( str(int(time())) + "||" +  ("%.2f" % c_median) + "||" + ("%.2f" % h_median) )

		c_data = []
		h_data = []
