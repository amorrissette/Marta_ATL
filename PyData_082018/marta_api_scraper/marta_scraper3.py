#!/usr/bin/python
#
#
#
#

import json
import requests
import datetime
import os

def main():
	rail_api_key = 'RAIL_API_KEY_GOES_HERE'
	bus_url = "http://developer.itsmarta.com/BRDRestService/RestBusRealTimeService/GetAllBus"
	rail_url = "http://developer.itsmarta.com/RealTimeTrain/RestServiceNextTrain/GetRealtimeArrivals?apiKey=" + rail_api_key

	time_total = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	
	filename_bus = 'marta_bus' + '_' + time_total + '.json'
	filename_rail= 'marta_rail'+ '_' + time_total + '.json'

	dir_name = datetime.datetime.now().strftime("%Y-%m-%d")
	bus_dir_path = '/home/pi/Desktop/marta_data/bus/' + dir_name + '/'
	rail_dir_path= '/home/pi/Desktop/marta_data/rail/' + dir_name + '/'

	if not os.path.exists(bus_dir_path):
		os.makedirs(bus_dir_path)
	if not os.path.exists(rail_dir_path):
		os.makedirs(rail_dir_path)

	r_bus  = requests.get(bus_url)
	with open(bus_dir_path  + filename_bus,  'w') as outfile:
		json.dump(r_bus.json(),  outfile)

	r_rail = requests.get(rail_url)
	with open(rail_dir_path + filename_rail, 'w') as outfile:
		json.dump(r_rail.json(), outfile)

if __name__ == '__main__':
	main()
