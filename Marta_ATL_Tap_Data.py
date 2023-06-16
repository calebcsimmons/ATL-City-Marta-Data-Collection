#This dataset is massive: over 200,000 individual rides are recorded.
#Each line of the marta_file contains six items, separated by commas:
#
# - the transit day, in MM/DD/YYYY format.
# - the transit time, in HH:MM:SS format.
# - the device ID, an identifer of the gate at which the rider entered.
# - the station ID, a numeric identifier the station.
# - the use type, whether the rider was entering, exiting, etc.
# - a serial number, the unique identifier of the rider's Breeze Card.
#
#Your goal is to use this file to answer three questions:
#
# - What is the average number of Breeze Card taps per station?
# - What is the station ID of the station whose traffic is the closest
#   to that average?
# - What station has the least overall amount of traffic?

filename = 'sample.txt'

total_taps = 0
tap_count = {}
average_taps = 0
closest_station = ""
least_traffic_station = ""

with open(filename, 'r') as marta_file: # Opening marta_file data and cleaning data
    for line in marta_file:
        station = line.strip().split(",")[3]
        if station not in tap_count: #Populating a dictionary 
            tap_count[station] = 0
        tap_count[station] += 1
        total_taps += 1

tap_values = list(tap_count.values()) #creating list of all taps
average_taps = total_taps / len(tap_count)
tap_values.sort() #sorting list to determine smallest 

closest_num = min(tap_values, key=lambda x: abs(x - average_taps)) #Determining closest tap to overall average

for station, taps in tap_count.items(): #Determining key based on specified values
    if taps == closest_num:
        closest_station = station
    if taps == tap_values[0]:
        least_traffic_station = station

print("The average number of taps per station is: " + str(average_taps))
print("The station whose traffic is closest to the average is: " + str(closest_station))
print("The station with the least amount of traffic is: " + str(least_traffic_station))








